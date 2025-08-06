"""
Page Migration Script for Opendatasoft

This script migrates a Studio or Code Editor page from a source Opendatasoft domain to a destination domain.

**Features:**
- Migrates a page's title, content, and slug.
- Supports both Studio Pages and Code Editor Pages.
- Can identify the source page by its UID or its slug.
- Allows specifying a different slug for the destination page.
- Includes a `--dry-run` mode to simulate migration without making any changes.
- Saves logs to a dedicated `migration_logs` directory, even if the script fails.

**Prerequisites:**
- The Opendatasoft Automation SDK must be installed (`pip install opendatasoft_automation`).
- You need API keys with sufficient permissions for both the source and destination domains.

**How to Run:**

1. Make sure you are in the `examples/python` directory or provide the full path to the script.
2. Execute the script from your terminal with the required arguments.

**Example: Migrate a Studio Page using its slug**
```bash
python migrate_page.py \
    --source-domain "my-source-domain.opendatasoft.com" \
    --source-apikey "YOUR_SOURCE_API_KEY" \
    --destination-domain "my-destination-domain.opendatasoft.com" \
    --destination-apikey "YOUR_DESTINATION_API_KEY" \
    --page-type studio \
    --page-slug "my-awesome-studio-page"
```

**Example: Migrate a Code Editor Page using its UID and changing its slug**
```bash
python migrate_page.py \
    --source-domain "my-source-domain.opendatasoft.com" \
    --source-apikey "YOUR_SOURCE_API_KEY" \
    --destination-domain "my-destination-domain.opendatasoft.com" \
    --destination-apikey "YOUR_DESTINATION_API_KEY" \
    --page-type code-editor \
    --page-uid "pg_abcdef123456" \
    --destination-page-slug "my-new-code-page-slug"
```

**Example: Simulate a migration**
```bash
python migrate_page.py \
    --source-domain "my-source-domain.opendatasoft.com" \
    --source-apikey "YOUR_SOURCE_API_KEY" \
    --destination-domain "my-destination-domain.opendatasoft.com" \
    --destination-apikey "YOUR_DESTINATION_API_KEY" \
    --page-type studio \
    --page-slug "my-awesome-studio-page" \
    --dry-run
```
"""
import argparse
import sys
import json
from pprint import pprint
import datetime
import getpass
import socket
import platform
import time
import os
import traceback

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

def get_studio_page_uid_from_slug(slug, client, domain):
    """Fetches the Studio Page UID for a given slug."""
    print(f"Searching for Studio Page with slug '{slug}' on domain '{domain}'...")
    pages_api = opendatasoft_automation.StudioPagesApi(client)
    try:
        pages = pages_api.list_studio_pages()
        for page in pages.results:
            if page.slug == slug:
                print(f"Found page UID: {page.uid}")
                return page.uid
        print(f"Page with slug '{slug}' not found on '{domain}'.")
        return None
    except ApiException as e:
        print(f"ERROR: Failed to list Studio Pages on '{domain}'. Status: {e.status}, Reason: {e.reason}")
        pprint(e.body)
        return None

def write_page_migration_log(source_domain, source_page_identifier, dest_domain, dest_page_slug, source_apikey, dest_apikey, duration, migration_type, exception_info=None):
    """Writes a log file with a summary of the page migration."""
    now = datetime.datetime.now()
    logs_dir = "migration_logs"
    os.makedirs(logs_dir, exist_ok=True)
    log_filename = os.path.join(logs_dir, f"page_migration_log_{now.strftime('%Y%m%d_%H%M%S')}.log")

    try:
        user = getpass.getuser()
        hostname = socket.gethostname()
        os_info = platform.platform()
        python_version = platform.python_version()
    except Exception:
        user = "N/A"
        hostname = "N/A"
        os_info = "N/A"
        python_version = "N/A"

    masked_source_apikey = f"*{source_apikey[-4:]}" if source_apikey and len(source_apikey) > 4 else "N/A"
    masked_dest_apikey = f"*{dest_apikey[-4:]}" if dest_apikey and len(dest_apikey) > 4 else "N/A"

    log_content = f"""
# Opendatasoft Page Migration Log

## Execution Summary
- **Date and Time**: {now.strftime('%Y-%m-%d %H:%M:%S')}
- **Execution Duration**: {duration:.2f} seconds
- **User**: {user}
- **Machine**: {hostname}
- **Operating System**: {os_info}
- **Python Version**: {python_version}

## Migration Details
- **Migration Type**: {migration_type}
- **Source Domain**: {source_domain}
- **Source Page (UID or Slug)**: {source_page_identifier}
- **Source API Key (masked)**: {masked_source_apikey}
- **Destination Domain**: {dest_domain}
- **Destination Page Slug**: {dest_page_slug}
- **Destination API Key (masked)**: {masked_dest_apikey}
"""
    if exception_info:
        log_content += f"""
## SCRIPT FAILED
- **Status**: The script terminated unexpectedly with an error.

### Error Details
```
{exception_info}
```
"""
    else:
        log_content += """
## Migration Summary
- The migration completed successfully.
"""

    try:
        with open(log_filename, 'w') as f:
            f.write(log_content.strip())
        print(f"\n{bcolors.OKGREEN}Log file saved to: {log_filename}{bcolors.ENDC}")
    except IOError as e:
        print(f"\n{bcolors.FAIL}ERROR: Could not write log file '{log_filename}'. Reason: {e}{bcolors.ENDC}")


def get_user_choice_on_existing_page(page_slug, domain):
    """Asks the user what to do when a page with the same slug already exists."""
    while True:
        choice = input(
            f"\n{bcolors.WARNING}A page with slug '{page_slug}' already exists on '{domain}'.\n"
            f"Do you want to (U)pdate the existing page or (C)reate a new one with slug '{page_slug}-0'?{bcolors.ENDC}\n"
            f"Enter your choice [U/C]: ").upper()
        if choice in ['U', 'C']:
            return choice
        print(f"\n{bcolors.FAIL}Invalid choice. Please enter 'U' to update or 'C' to create.{bcolors.ENDC}")

def migrate_page(args):
    """Main function to orchestrate the page migration."""
    start_time = time.time()
    if args.dry_run:
        print(f"{bcolors.HEADER}--- DRY RUN MODE ENABLED ---{bcolors.ENDC}")
        print("No changes will be made to the destination domain.")

    exception_info = None
    source_page_identifier = args.page_uid or args.page_slug
    destination_slug = None
    migration_type = "Unknown"

    try:
        source_client = get_api_client(args.source_domain, args.source_apikey)
        destination_client = get_api_client(args.destination_domain, args.destination_apikey)

        page_type = args.page_type

        # ------------------
        # STUDIO PAGE
        # ------------------
        if page_type == 'studio':
            source_pages_api = opendatasoft_automation.StudioPagesApi(source_client)
            destination_pages_api = opendatasoft_automation.StudioPagesApi(destination_client)

            source_page_uid = args.page_uid or get_studio_page_uid_from_slug(args.page_slug, source_client, args.source_domain)
            
            if not source_page_uid:
                raise ValueError("Could not find the specified Studio Page on the source domain.")

            print(f"\nFetching Studio Page '{source_page_uid}' from source...")
            source_page = source_pages_api.retrieve_studio_page(page_uid=source_page_uid)
            print("- Fetched page content successfully.")

            destination_slug = args.destination_page_slug or source_page.slug
            
            # If no destination slug is provided, check if the page exists and ask the user what to do
            if not args.destination_page_slug:
                existing_dest_page_uid = get_studio_page_uid_from_slug(destination_slug, destination_client, args.destination_domain)
                if existing_dest_page_uid:
                    user_choice = get_user_choice_on_existing_page(destination_slug, args.destination_domain)
                    if user_choice == 'C':
                        destination_slug = f"{destination_slug}-0"
            
            # Re-check existence for migration type after potential slug change
            existing_dest_page_uid = get_studio_page_uid_from_slug(destination_slug, destination_client, args.destination_domain)
            migration_type = "Page Update" if existing_dest_page_uid else "Page Creation"
            print(f"Migration Type: {migration_type}")

            source_content = source_page.contents[0] if source_page.contents else None
            page_title = source_content.title if source_content else ''

            if migration_type == "Page Creation":
                new_page_payload = opendatasoft_automation.StudioPage(
                    title=page_title,
                    slug=destination_slug,
                    contents=source_page.contents,
                    is_published=False
                )
                print(f"\nCreating Studio Page on destination with slug '{destination_slug}'...")
                if args.dry_run:
                    print(f"[DRY RUN] Would create new Studio Page with slug '{destination_slug}'.")
                else:
                    created_page = destination_pages_api.create_studio_page(studio_page=new_page_payload)
                    print(f"{bcolors.OKGREEN}- Successfully created new Studio Page with UID: {created_page.uid}{bcolors.ENDC}")
            
            else: # Page Update
                print(f"\nUpdating Studio Page on destination with slug '{destination_slug}'...")
                if args.dry_run:
                    print(f"[DRY RUN] Would update Studio Page content for page with slug '{destination_slug}'.")
                else:
                    # For Studio Pages, updating content is done via the `contents` field on the main page object
                    page_update_payload = opendatasoft_automation.StudioPage(
                        title=page_title,
                        contents=source_page.contents
                    )
                    updated_page = destination_pages_api.update_studio_page(page_uid=existing_dest_page_uid, studio_page=page_update_payload)
                    print(f"{bcolors.OKGREEN}- Successfully updated Studio Page with UID: {updated_page.uid}{bcolors.ENDC}")

        # ------------------
        # CODE EDITOR PAGE
        # ------------------
        elif page_type == 'code-editor':
            source_pages_api = opendatasoft_automation.CodeEditorPagesApi(source_client)
            destination_pages_api = opendatasoft_automation.CodeEditorPagesApi(destination_client)

            if not args.page_slug:
                raise ValueError("For Code Editor pages, you must provide the --page-slug.")

            print(f"\nFetching Code Editor Page with slug '{args.page_slug}' from source...")
            source_page = source_pages_api.retrieve_code_editor_page(page_slug=args.page_slug)
            print("- Fetched page content successfully.")

            destination_slug = args.destination_page_slug or source_page.slug

            # If no destination slug is provided, check if the page exists and ask the user what to do
            if not args.destination_page_slug:
                try:
                    destination_pages_api.retrieve_code_editor_page(page_slug=destination_slug)
                    page_exists = True
                except ApiException as e:
                    if e.status == 404:
                        page_exists = False
                    else:
                        raise
                
                if page_exists:
                    user_choice = get_user_choice_on_existing_page(destination_slug, args.destination_domain)
                    if user_choice == 'C':
                        destination_slug = f"{destination_slug}-0"

            # Re-check existence for migration type after potential slug change
            try:
                destination_pages_api.retrieve_code_editor_page(page_slug=destination_slug)
                migration_type = "Page Update"
            except ApiException as e:
                if e.status == 404:
                    migration_type = "Page Creation"
                else:
                    raise
            print(f"Migration Type: {migration_type}")

            page_payload = opendatasoft_automation.CodeEditorPage(
                title=source_page.title,
                slug=destination_slug,
                content=source_page.content,
                description=source_page.description,
                template=source_page.template,
                tags=source_page.tags,
                is_restricted=True,
                is_published=False
            )

            if migration_type == "Page Creation":
                print(f"\nCreating Code Editor Page on destination with slug '{destination_slug}'...")
                if args.dry_run:
                    print(f"[DRY RUN] Would create new Code Editor Page with slug '{destination_slug}'.")
                else:
                    created_page = destination_pages_api.create_code_editor_page(code_editor_page=page_payload)
                    print(f"{bcolors.OKGREEN}- Successfully created new Code Editor Page with slug: {created_page.slug}{bcolors.ENDC}")
            
            else: # Page Update
                print(f"\nUpdating Code Editor Page on destination with slug '{destination_slug}'...")
                if args.dry_run:
                    print(f"[DRY RUN] Would update Code Editor Page with slug '{destination_slug}'.")
                else:
                    updated_page = destination_pages_api.update_code_editor_page(page_slug=destination_slug, code_editor_page=page_payload)
                    print(f"{bcolors.OKGREEN}- Successfully updated Code Editor Page with slug: {updated_page.slug}{bcolors.ENDC}")

        print("\nMigration process complete!")
        if not args.dry_run:
            url_path = "studio/pages" if page_type == 'studio' else "pages"
            message = "Check your updated page at" if migration_type == "Page Update" else "Check your new page at"
            print(f"{message}: https://{args.destination_domain}/{url_path}/{destination_slug}/")

    except Exception as e:
        print(f"\n{bcolors.FAIL}--- SCRIPT FAILED ---{bcolors.ENDC}")
        print("An unexpected error occurred. A log file with details has been created.")
        exception_info = traceback.format_exc()
        raise

    finally:
        if not args.dry_run:
            end_time = time.time()
            duration = end_time - start_time
            write_page_migration_log(
                source_domain=args.source_domain,
                source_page_identifier=source_page_identifier,
                dest_domain=args.destination_domain,
                dest_page_slug=destination_slug,
                source_apikey=args.source_apikey,
                dest_apikey=args.destination_apikey,
                duration=duration,
                migration_type=migration_type,
                exception_info=exception_info
            )



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Migrate an Opendatasoft Studio or Code Editor page between domains.")

    # Source arguments
    parser.add_argument("--source-domain", required=True, help="Domain of the source ODS portal.")
    parser.add_argument("--source-apikey", required=True, help="API key for the source ODS portal.")
    
    # Destination arguments
    parser.add_argument("--destination-domain", required=True, help="Domain of the destination ODS portal.")
    parser.add_argument("--destination-apikey", required=True, help="API key for the destination ODS portal.")

    # Page arguments
    parser.add_argument("--page-type", required=True, choices=['studio', 'code-editor'], help="The type of page to migrate.")
    parser.add_argument("--page-uid", required=False, help="The UID of the Studio Page to migrate. Not applicable for Code Editor pages.")
    parser.add_argument("--page-slug", required=False, help="The slug of the page to migrate.")
    parser.add_argument("--destination-page-slug", required=False, help="Optional: new slug for the page on the destination.")
    parser.add_argument("--dry-run", action='store_true', help="If set, the script will simulate the migration without applying any changes.")

    parsed_args = parser.parse_args()

    if not parsed_args.page_uid and not parsed_args.page_slug:
        parser.error("Either --page-uid or --page-slug must be provided.")

    migrate_page(parsed_args)