import argparse
from opendatasoft_automation import (
    ApiClient,
    Configuration,
    DatasetsApi,
    DatasetMetadataApi,
    DatasetMetadataValue
)

from urllib.parse import urlparse, parse_qs

def _parse_offset_limit(next_page):
    if not next_page:
        return {}

    query = parse_qs(urlparse(next_page).query)
    return {"limit": int(query["limit"][0]), "offset": int(query["offset"][0])}

def _list(conf, args):
    with ApiClient(conf) as client:
        next_page = None

        while True:

            datasets = DatasetsApi(client).list_datasets(**_parse_offset_limit(next_page))

            if not next_page:
                print(f"Total number of results: {datasets.total_count}")

            for dataset in datasets.results:
                print(f"{dataset.uid}: {dataset.dataset_id}")

            if not datasets.next:
                break

            next_page = datasets.next

def _get_metadata_default_title(conf, args):

    with ApiClient(conf) as client:

        metadata = DatasetMetadataApi(client).retrieve_template_field_dataset_metadata(
            dataset_uid=args.dataset_uid,
            template_name="default",
            template_field_name="title"
        )

        print(metadata.value)

def _set_metadata__default_title(conf, args):

    with ApiClient(conf) as client:

        metadata = DatasetMetadataApi(client).update_template_field_dataset_metadata(
            dataset_uid=args.dataset_uid,
            template_name="default",
            template_field_name="title",
            dataset_metadata_value=DatasetMetadataValue(value=args.value)
        )


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="List datasets on a given domain")

    parser.add_argument("-b", "--baseurl", action="store", required=True, help="API base URL")
    parser.add_argument("-k", "--apikey", action="store", required=False, help="API Key")

    subparsers = parser.add_subparsers(help="Sub commands")

    parser_list = subparsers.add_parser("list", help="List datasets")
    parser_list.set_defaults(func=_list)

    parser_get_metadata = subparsers.add_parser("metadata-get", help="Get dataset title")
    parser_get_metadata.set_defaults(func=_get_metadata_default_title)
    parser_get_metadata.add_argument("--dataset-uid", action="store", required=False, help="Dataset UID")

    parser_update_metadata = subparsers.add_parser("metadata-update", help="Update dataset title")
    parser_update_metadata.set_defaults(func=_set_metadata__default_title)
    parser_update_metadata.add_argument("--dataset-uid", action="store", required=False, help="Dataset UID")
    parser_update_metadata.add_argument("--value", action="store", required=False, help="Value")

    args = parser.parse_args()

    conf = Configuration(host=args.baseurl)
    conf.api_key["HeaderAPIKey"] = args.apikey
    conf.api_key_prefix['HeaderAPIKey'] = "ApiKey"

    args.func(conf, args)
