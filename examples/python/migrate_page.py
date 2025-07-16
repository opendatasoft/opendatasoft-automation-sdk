"""""""""
Page Migration Script for Opendatasoft

This script migrates a Studio or Code Editor page from a source Opendatasoft domain to a destination domain.

**Features:**
- Migrates a page's title, content, and slug.
- Supports both Studio Pages and Code Editor Pages.
- Can identify the source page by its UID or its slug.
- Allows specifying a different slug for the destination page.

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
"""
import argparse
import sys
import json
from pprint import pprint

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

def migrate_page(args):
    """Main function to orchestrate the page migration."""
    source_client = get_api_client(args.source_domain, args.source_apikey)
    destination_client = get_api_client(args.destination_domain, args.destination_apikey)

    source_page_uid = args.page_uid
    source_page_slug = args.page_slug
    page_type = args.page_type

    # ------------------
    # STUDIO PAGE
    # ------------------
    if page_type == 'studio':
        source_pages_api = opendatasoft_automation.StudioPagesApi(source_client)
        destination_pages_api = opendatasoft_automation.StudioPagesApi(destination_client)

        if not source_page_uid:
            source_page_uid = get_studio_page_uid_from_slug(source_page_slug, source_client, args.source_domain)
        
        if not source_page_uid:
            print(f"{bcolors.FAIL}Could not find the specified Studio Page on the source domain. Aborting.{bcolors.ENDC}")
            sys.exit(1)

        print(f"\nFetching Studio Page '{source_page_uid}' from source...")
        try:
            source_page = source_pages_api.retrieve_studio_page(page_uid=source_page_uid)
            print("- Fetched page content successfully.")
        except ApiException as e:
            print(f"{bcolors.FAIL}ERROR: Failed to retrieve source page. Status: {e.status}, Reason: {e.reason}{bcolors.ENDC}")
            pprint(e.body)
            sys.exit(1)

        destination_slug = args.destination_page_slug or source_page.slug

        source_content = None
        if source_page.contents:
            source_content = source_page.contents[0]

        new_page_payload = opendatasoft_automation.StudioPage(
            title=source_content.title if source_content else '',
            slug=destination_slug,
            contents=source_page.contents,
            is_published=False  # Create as draft first
        )

        print(f"\nCreating Studio Page on destination with slug '{destination_slug}'...")
        try:
            created_page = destination_pages_api.create_studio_page(studio_page=new_page_payload)
            print(f"{bcolors.OKGREEN}- Successfully created new Studio Page with UID: {created_page.uid}{bcolors.ENDC}")
            print(f"\nMigration process complete!")
            print(f"Check your new page at: https://{args.destination_domain}/studio/pages/{created_page.slug}/")

        except ApiException as e:
            print(f"{bcolors.FAIL}ERROR: Failed to create page on destination. Status: {e.status}, Reason: {e.reason}{bcolors.ENDC}")
            pprint(e.body)
            sys.exit(1)

    # ------------------
    # CODE EDITOR PAGE
    # ------------------
    elif page_type == 'code-editor':
        source_pages_api = opendatasoft_automation.CodeEditorPagesApi(source_client)
        destination_pages_api = opendatasoft_automation.CodeEditorPagesApi(destination_client)

        if not source_page_slug:
            print(f"{bcolors.FAIL}For Code Editor pages, you must provide the --page-slug. Aborting.{bcolors.ENDC}")
            sys.exit(1)

        print(f"\nFetching Code Editor Page with slug '{source_page_slug}' from source...")
        try:
            source_page = source_pages_api.retrieve_code_editor_page(page_slug=source_page_slug)
            print("- Fetched page content successfully.")
        except ApiException as e:
            if e.status == 404:
                print(f"{bcolors.FAIL}Could not find a Code Editor Page with slug '{source_page_slug}' on the source domain. Aborting.{bcolors.ENDC}")
            else:
                print(f"{bcolors.FAIL}ERROR: Failed to retrieve source page. Status: {e.status}, Reason: {e.reason}{bcolors.ENDC}")
                pprint(e.body)
            sys.exit(1)

        destination_slug = args.destination_page_slug or source_page.slug

        # Build a new page object containing only the fields required for creation.
        # This avoids sending read-only fields like created_by, updated_at, etc.
        print("- Building payload for new page...")
        new_page_payload = opendatasoft_automation.CodeEditorPage(
            title=source_page.title,
            slug=destination_slug,
            content=source_page.content,
            description=source_page.description,
            template=source_page.template,
            tags=source_page.tags,
            is_restricted=source_page.is_restricted,
            is_published=False  # Always create as a draft for safety
        )

        print(f"\nCreating Code Editor Page on destination with slug '{destination_slug}'...")
        try:
            created_page = destination_pages_api.create_code_editor_page(code_editor_page=new_page_payload)
            print(f"{bcolors.OKGREEN}- Successfully created new Code Editor Page with slug: {created_page.slug}{bcolors.ENDC}")
            print(f"\nMigration process complete!")
            print(f"Check your new page at: https://{args.destination_domain}/pages/{created_page.slug}/")

        except ApiException as e:
            print(f"{bcolors.FAIL}ERROR: Failed to create page on destination. Status: {e.status}, Reason: {e.reason}{bcolors.ENDC}")
            pprint(e.body)
            sys.exit(1)


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

    parsed_args = parser.parse_args()

    if not parsed_args.page_uid and not parsed_args.page_slug:
        parser.error("Either --page-uid or --page-slug must be provided.")

    migrate_page(parsed_args)
