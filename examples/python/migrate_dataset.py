"""
Dataset Migration Script for Opendatasoft

This script migrates a dataset from a source Opendatasoft domain to a destination domain.
It handles the migration of the dataset's core information, resources (datasources),
processing pipeline, and metadata.

**Features:**
- Copies basic dataset information (title, description, etc.).
- Migrates all resources associated with the dataset.
- Replicates the entire processing chain (processors) in the correct order.
- Applies all metadata from the source dataset to the destination dataset.
- Can either create a new dataset on the destination or update an existing one.
- Optionally publishes the dataset on the destination after a successful migration.

**Prerequisites:**
- The Opendatasoft Automation SDK must be installed (`pip install opendatasoft_automation`).
- You need API keys with sufficient permissions for both the source and destination domains.

**How to Run:**

1. Make sure you are in the `examples/python` directory or provide the full path to the script.
2. Execute the script from your terminal with the required arguments.

**Example: Create a new dataset on the destination using dataset ID**
```bash
python migrate_dataset.py \
    --source-domain "my-source-domain.opendatasoft.com" \
    --source-apikey "YOUR_SOURCE_API_KEY" \
    --source-cookie "YOUR_SOURCE_COOKIE" \
    --source-dataset-id "source_dataset_identifier" \
    --destination-domain "my-destination-domain.opendatasoft.com" \
    --destination-apikey "YOUR_DESTINATION_API_KEY" \
    --destination-cookie "YOUR_DESTINATION_COOKIE" \
    --publish
```

**Example: Update an existing dataset on the destination using dataset UID**
```bash
python migrate_dataset.py \
    --source-domain "my-source-domain.opendatasoft.com" \
    --source-apikey "YOUR_SOURCE_API_KEY" \
    --source-cookie "YOUR_SOURCE_COOKIE" \
    --source-dataset-uid "source_dataset_uid" \
    --destination-domain "my-destination-domain.opendatasoft.com" \
    --destination-apikey "YOUR_DESTINATION_API_KEY" \
    --destination-cookie "YOUR_DESTINATION_COOKIE" \
    --destination-dataset-uid "existing_destination_dataset_uid"
```
"""
import argparse
import sys
from email.policy import default
from pprint import pprint
import requests
import json

import opendatasoft_automation
from opendatasoft_automation.rest import ApiException

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def get_api_client(domain, apikey):
    """Initializes and returns an API client for the given domain and API key."""
    configuration = opendatasoft_automation.Configuration(
        host=f"https://{domain}/api/automation/v1.0"
    )
    configuration.api_key['QueryAPIKey'] = apikey
    return opendatasoft_automation.ApiClient(configuration)


def get_dataset_uid_from_id(dataset_id, client, domain):
    """Fetches the dataset UID for a given dataset ID by paginating through datasets."""
    if not dataset_id:
        return None
    print(f"Searching for dataset with ID '{dataset_id}' on domain '{domain}'...")
    datasets_api = opendatasoft_automation.DatasetsApi(client)
    limit = 100
    offset = 0
    while True:
        try:
            response = datasets_api.list_datasets(limit=limit, offset=offset)
            if not response.results:
                print(f"Dataset with ID '{dataset_id}' not found on '{domain}'.")
                return None

            for dataset in response.results:
                if dataset.dataset_id == dataset_id:
                    print(f"Found dataset UID: {dataset.uid}")
                    return dataset.uid

            offset += limit
        except ApiException as e:
            print(f"ERROR: Failed to list datasets on '{domain}'. Status: {e.status}, Reason: {e.reason}")
            pprint(e.body)
            return None


def find_matching_connection(source_connection_details, destination_client):
    """Finds a matching connection on the destination domain."""
    print("  - Searching for a matching connection on the destination...")
    dest_connections_api = opendatasoft_automation.DatasourcesConnectionsApi(destination_client)

    try:
        dest_connections = dest_connections_api.list_connections()
        for dest_conn in dest_connections.results:
            dest_conn_details = dest_connections_api.retrieve_connection(dest_conn.uid)

            if source_connection_details.type == dest_conn_details.type:
                if source_connection_details.type in ['ftp', 'http']:
                    if (hasattr(source_connection_details, 'url') and hasattr(dest_conn_details, 'url') and\
                        source_connection_details.url == dest_conn_details.url and\
                        hasattr(source_connection_details, 'auth') and hasattr(dest_conn_details, 'auth') and\
                        source_connection_details.auth and dest_conn_details.auth and\
                        source_connection_details.auth.to_dict().get('username') == dest_conn_details.auth.to_dict().get('username')):
                        print(f"  - Found matching connection {dest_conn_details.uid}: {dest_conn_details.url} / {source_connection_details.auth.to_dict().get('username')}")
                        return dest_conn_details
                elif source_connection_details.type == 'google_drive':
                    if (hasattr(source_connection_details, 'auth') and hasattr(dest_conn_details, 'auth') and\
                        source_connection_details.auth and dest_conn_details.auth and\
                        hasattr(source_connection_details.auth, 'claims') and hasattr(dest_conn_details.auth, 'claims') and\
                        source_connection_details.auth.claims.get('email') == dest_conn_details.auth.claims.get('email')):
                        print(f"  - Found matching Google Drive connection for email: {source_connection_details.auth.claims.get('email')}")
                        return dest_conn_details

    except ApiException as e:
        print(f"  - ERROR: An error occurred while searching for connections on destination. Status: {e.status}, Reason: {e.reason}")
        pprint(e.body)

    print("  - No matching connection found on the destination domain.")
    return None


def fetch_source_data(source_client, source_dataset_uid):
    """Fetches all necessary data from the source dataset."""
    print(f"\nFetching data from source dataset '{source_dataset_uid}'...")
    source_datasets_api = opendatasoft_automation.DatasetsApi(source_client)
    source_resources_api = opendatasoft_automation.DatasetResourcesApi(source_client)
    source_processors_api = opendatasoft_automation.DatasetProcessorsApi(source_client)
    source_metadata_api = opendatasoft_automation.DatasetMetadataApi(source_client)

    try:
        source_dataset = source_datasets_api.retrieve_dataset(source_dataset_uid)
        print("- Fetched dataset object.")

        source_resources = source_resources_api.list_dataset_resources(source_dataset_uid)
        print(f"- Fetched {len(source_resources.results)} resources.")

        source_processors = source_processors_api.list_dataset_processors(source_dataset_uid)
        print(f"- Fetched {len(source_processors.results)} processors.")

        source_metadata = source_metadata_api.list_all_dataset_metadata(source_dataset_uid)
        print(f"- Fetched metadata.")

        return source_dataset, source_resources.results, source_processors.results, source_metadata

    except ApiException as e:
        print(f"ERROR: Failed to fetch data from source. Status: {e.status}, Reason: {e.reason}")
        pprint(e.body)
        return None, None, None, None

def get_domain_themes(domain, cookie):
    """Fetches the themes from the given domain using the provided cookie."""
    if not cookie:
        return None
    print(f"Fetching themes from domain '{domain}'...")
    headers = {'Cookie': cookie}
    url = f"https://{domain}/api/management/1.0/domain/"
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        domain_info = response.json()
        return domain_info.get('properties', {}).get('metadata.themes', [])
    except requests.exceptions.RequestException as e:
        print(f"ERROR: Failed to fetch themes from '{domain}'. Status: {e.response.status_code}, Reason: {e.response.reason}")
        try:
            pprint(e.response.json())
        except json.JSONDecodeError:
            pprint(e.response.text)
        return None

def get_theme_by_name(themes, theme_name):
    """Finds a theme by its name in the list of themes."""
    if not themes:
        return None
    for theme in themes:
        for lang, label in theme.get('labels', {}).items():
            if label.strip().lower() == theme_name.strip().lower():
                return theme
    return None

def get_theme_by_id(themes, theme_id):
    """Finds a theme by its id in the list of themes."""
    if not themes:
        return None
    for theme in themes:
        if theme.get('id') == theme_id:
            return theme
    return None

def migrate_dataset(args):
    """Main function to orchestrate the dataset migration."""
    source_client = get_api_client(args.source_domain, args.source_apikey)
    destination_client = get_api_client(args.destination_domain, args.destination_apikey)

    # Get source and destination themes
    source_themes = get_domain_themes(args.source_domain, args.source_cookie)
    destination_themes = get_domain_themes(args.destination_domain, args.destination_cookie)

    # Step 1: Determine source and destination UIDs
    source_dataset_uid = args.source_dataset_uid or get_dataset_uid_from_id(args.source_dataset_id, source_client, args.source_domain)
    if not source_dataset_uid:
        print("ERROR: Source dataset could not be found. Please provide a valid source_dataset_uid or source_dataset_id.")
        return

    destination_dataset_uid = args.destination_dataset_uid or get_dataset_uid_from_id(args.destination_dataset_id, destination_client, args.destination_domain)

    # Step 2: Fetch all data from the source
    source_dataset, source_resources, source_processors, source_metadata = fetch_source_data(
        source_client, source_dataset_uid
    )
    if not source_dataset:
        return

    destination_datasets_api = opendatasoft_automation.DatasetsApi(destination_client)

    # Step 3: Create or retrieve the destination dataset
    if not destination_dataset_uid:
        print(f"\nCreating new dataset on destination domain '{args.destination_domain}'...")
        new_dataset_metadata = opendatasoft_automation.DatasetMetadata(
            default=opendatasoft_automation.DatasetMetadataDefault(
                title=opendatasoft_automation.DatasetMetadataValue(value=f"{source_dataset.metadata.default.title.value}"),
                description=opendatasoft_automation.DatasetMetadataValue(value=source_dataset.metadata.default.description.value if source_dataset.metadata.default.description else ""),
                timezone=opendatasoft_automation.DatasetMetadataValue(value=source_dataset.metadata.default.timezone.value if source_dataset.metadata.default.timezone else "UTC"),
                modified=opendatasoft_automation.DatasetMetadataValue(value=source_dataset.metadata.default.modified.value if source_dataset.metadata.default.modified else None),
                language=opendatasoft_automation.DatasetMetadataValue(value=source_dataset.metadata.default.language.value if source_dataset.metadata.default.language else None),
            )
        )

        new_dataset_payload = opendatasoft_automation.Dataset(
            dataset_id=args.destination_dataset_id if args.destination_dataset_id else source_dataset.dataset_id,
            is_restricted=source_dataset.is_restricted,
            metadata=new_dataset_metadata
        )
        try:
            created_dataset = destination_datasets_api.create_dataset(dataset=new_dataset_payload)
            destination_dataset_uid = created_dataset.uid
            print(f"- Successfully created new dataset with UID: {destination_dataset_uid}")
        except ApiException as e:
            print(f"ERROR: Failed to create dataset on destination. Status: {e.status}, Reason: {e.reason}")
            pprint(e.body)
            return
    else:
        print(f"\nUsing existing destination dataset '{destination_dataset_uid}'.")
        try:
            destination_datasets_api.retrieve_dataset(destination_dataset_uid)
        except ApiException as e:
            print(f"ERROR: Could not retrieve destination dataset '{destination_dataset_uid}'. Status: {e.status}, Reason: {e.reason}")
            return

    # Step 4: Migrate Resources
    print("\nMigrating resources...")
    destination_resources_api = opendatasoft_automation.DatasetResourcesApi(destination_client)
    for resource in source_resources:
        print(f"- Migrating resource: {resource.title} ({resource.type})")
        new_datasource = None
        if resource.datasource:
            source_connections_api = opendatasoft_automation.DatasourcesConnectionsApi(source_client)
            source_connection_details = source_connections_api.retrieve_connection(resource.datasource.connection.to_dict().get('uid'))
            matching_connection = find_matching_connection(source_connection_details, destination_client)

            if matching_connection:
                if resource.datasource.type == 'ftp':
                    connection = opendatasoft_automation.ConnectionUID(uid=matching_connection.uid, type='ftp')
                    ftp_datasource_connection = opendatasoft_automation.FTPDatasource1Connection(actual_instance=connection)
                    new_datasource = opendatasoft_automation.FTPDatasource(
                        type='ftp',
                        connection=ftp_datasource_connection,
                        relative_url=resource.datasource.relative_url
                    )
                # Add other types here if needed
            else:
                print(f"{bcolors.FAIL}FATAL: Could not find a matching connection for resource '{resource.title}' on the destination domain.{bcolors.ENDC}")
                print("Please create a connection on the destination with the following properties:")
                if source_connection_details.type in ['ftp', 'http']:
                    print(f"  - Type: {bcolors.OKCYAN}{source_connection_details.type}{bcolors.ENDC}")
                    print(f"  - URL: {bcolors.OKCYAN}{source_connection_details.url}{bcolors.ENDC}")
                    if hasattr(source_connection_details, 'auth') and source_connection_details.auth:
                        print(f"  - Username: {bcolors.OKCYAN}{source_connection_details.auth.to_dict().get('username')}{bcolors.ENDC}")
                elif source_connection_details.type == 'google_drive':
                    print(f"  - Type: {bcolors.OKCYAN}google_drive{bcolors.ENDC}")
                    if hasattr(source_connection_details, 'auth') and source_connection_details.auth and hasattr(source_connection_details.auth, 'claims'):
                        print(f"  - Email: {bcolors.OKCYAN}{source_connection_details.auth.claims.get('email')}{bcolors.ENDC}")
                print("Then, rerun this script.")
                sys.exit(1)

        new_resource = opendatasoft_automation.Resource(
            type=resource.type,
            title=resource.title,
            params=resource.params,
            datasource=new_datasource
        )
        try:
            destination_resources_api.create_dataset_resource(destination_dataset_uid, resource=new_resource)
            print(f"- Successfully migrated resource '{resource.title}'.")
        except ApiException as e:
            print(f"  - WARNING: Could not migrate resource '{resource.title}'. Status: {e.status}, Reason: {e.reason}, Resource: {new_resource.datasource.connection}")
            pprint(e.body)

    # Step 5: Migrate Processors
    print("\nMigrating processors...")
    destination_processors_api = opendatasoft_automation.DatasetProcessorsApi(destination_client)
    for processor in source_processors:
        print(f"- Migrating processor: {processor.type}")
        new_processor = opendatasoft_automation.DatasetProcessor(
            type=processor.type,
            label=processor.label,
            additional_properties=processor.additional_properties
        )
        try:
            destination_processors_api.create_dataset_processor(destination_dataset_uid, dataset_processor=new_processor)
        except ApiException as e:
            print(f"  - WARNING: Could not migrate processor '{processor.type}'. Status: {e.status}, Reason: {e.reason}")
            pprint(e.body)

    # Step 6: Migrate Metadata
    print("\nMigrating metadata...")
    destination_metadata_api = opendatasoft_automation.DatasetMetadataApi(destination_client)
    if source_metadata:
        if source_metadata.default:
            default_metadata_dict = source_metadata.default.to_dict()
            # Handle themes
            if 'theme' in default_metadata_dict and default_metadata_dict['theme'] and default_metadata_dict['theme']['value']:
                source_themes_val = default_metadata_dict['theme']['value']
                destination_themes_list = []
                for source_theme_name in source_themes_val:
                    theme = get_theme_by_name(destination_themes, source_theme_name)
                    if theme:
                        destination_themes_list.append(theme['id'])
                default_metadata_dict['theme']['value'] = destination_themes_list

            destination_metadata_payload = opendatasoft_automation.DatasetMetadata(default=opendatasoft_automation.DatasetMetadataDefault.from_dict(default_metadata_dict))
            destination_metadata_payload.default.modified_updates_on_metadata_change = opendatasoft_automation.DatasetMetadataValue(value=False)
            destination_metadata_payload.default.modified_updates_on_data_change = opendatasoft_automation.DatasetMetadataValue(value=False)

        if source_metadata.visualization:
            destination_metadata_payload.visualization = source_metadata.visualization

        if source_metadata.asset_content_configuration:
            destination_metadata_payload.asset_content_configuration = source_metadata.asset_content_configuration

        if source_metadata.internal:
            internal_metadata_dict = source_metadata.internal.to_dict()
            if 'theme_id' in internal_metadata_dict and internal_metadata_dict['theme_id'] and internal_metadata_dict['theme_id']['value']:
                source_theme_ids = internal_metadata_dict['theme_id']['value']
                destination_theme_ids = []
                for source_theme_id in source_theme_ids:
                    source_theme = get_theme_by_id(source_themes, source_theme_id)
                    if source_theme:
                        source_theme_name = next(iter(source_theme.get('labels', {}).values()), None)
                        if source_theme_name:
                            destination_theme = get_theme_by_name(destination_themes, source_theme_name)
                            if destination_theme:
                                destination_theme_ids.append(destination_theme['id'])
                            else:
                                print(f"  - WARNING: Theme '{source_theme_name}' not found on destination. Skipping theme.")
                        else:
                            print(f"  - WARNING: Could not find English label for source theme ID '{source_theme_id}'. Skipping theme.")
                    else:
                        print(f"  - WARNING: Source theme with ID '{source_theme_id}' not found. Skipping theme.")
                internal_metadata_dict['theme_id']['value'] = destination_theme_ids
            destination_metadata_payload.internal = opendatasoft_automation.DatasetMetadataInternal.from_dict(internal_metadata_dict)

        if hasattr(source_metadata, 'custom_template_name') and source_metadata.custom_template_name:
            destination_metadata_payload.custom_template_name = source_metadata.custom_template_name

        try:
            destination_metadata_api.update_all_dataset_metadata(destination_dataset_uid, dataset_metadata=destination_metadata_payload)
            print("- Successfully migrated all metadata.")
        except ApiException as e:
            print(f"  - WARNING: Could not migrate metadata. Status: {e.status}, Reason: {e.reason}")
            pprint(e.body)

        try:
            destination_metadata_api.update_template_field_dataset_metadata(destination_dataset_uid,
                                                                            "default",
                                                                            "modified_updates_on_metadata_change",
                                                                            opendatasoft_automation.DatasetMetadataValue(value=True))
            destination_metadata_api.update_template_field_dataset_metadata(destination_dataset_uid,
                                                                            "default",
                                                                            "modified_updates_on_data_change",
                                                                            opendatasoft_automation.DatasetMetadataValue(value=True))
            print("- Successfully updated metadata modified_updates_on_(meta)data_change.")
        except ApiException as e:
            print(f"  - WARNING: Could not migrate metadata. Status: {e.status}, Reason: {e.reason}")
            pprint(e.body)
    else:
        print("- No metadata to migrate.")

    # Step 7: Publish the dataset if requested
    if args.publish:
        print(f"\nPublishing dataset '{destination_dataset_uid}'...")
        try:
            destination_datasets_api.publish_dataset(destination_dataset_uid)
            print("- Dataset published successfully.")
        except ApiException as e:
            print(f"ERROR: Failed to publish dataset. Status: {e.status}, Reason: {e.reason}")
            pprint(e.body)

    print("\nMigration process complete!")
    print(f"Check your new dataset at: https://{args.destination_domain}/explore/dataset/{destination_dataset_uid}/")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Migrate an Opendatasoft dataset between domains.")

    # Source arguments
    parser.add_argument("--source-domain", required=True, help="Domain of the source ODS portal.")
    parser.add_argument("--source-apikey", required=True, help="API key for the source ODS portal.")
    parser.add_argument("--source-cookie", required=False, help="Cookie for the source ODS portal.")
    parser.add_argument("--source-dataset-uid", required=False, help="The UID of the dataset to migrate.")
    parser.add_argument("--source-dataset-id", required=False, help="The ID of the dataset to migrate.")

    # Destination arguments
    parser.add_argument("--destination-domain", required=True, help="Domain of the destination ODS portal.")
    parser.add_argument("--destination-apikey", required=True, help="API key for the destination ODS portal.")
    parser.add_argument("--destination-cookie", required=False, help="Cookie for the destination ODS portal.")
    parser.add_argument("--destination-dataset-uid", required=False, default=None,
                        help="Optional: UID of an existing dataset on the destination to update.")
    parser.add_argument("--destination-dataset-id", required=False, default=None,
                        help="Optional: ID of an existing dataset on the destination to update. If not provided, a new dataset will be created using the source dataset ID.")

    # Action arguments
    parser.add_argument("--publish", action='store_true',
                        help="If set, the script will attempt to publish the dataset on the destination after migration.")

    parsed_args = parser.parse_args()

    if not parsed_args.source_dataset_uid and not parsed_args.source_dataset_id:
        parser.error("Either --source-dataset-uid or --source-dataset-id must be provided.")

    migrate_dataset(parsed_args)