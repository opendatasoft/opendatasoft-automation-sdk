import os
from pprint import pprint

import opendatasoft_automation
from opendatasoft_automation.rest import ApiException

def get_api_client(domain, apikey):
    """Initializes and returns an API client for the given domain and API key."""
    configuration = opendatasoft_automation.Configuration(
        host=f"https://{domain}/api/automation/v1.0"
    )
    configuration.api_key['QueryAPIKey'] = apikey
    return opendatasoft_automation.ApiClient(configuration)



if __name__ == "__main__":
    destination_client = get_api_client(os.environ.get("DOMAIN") ,
                                        os.environ.get("APIKEY"))

    destination_resources_api = opendatasoft_automation.DatasetResourcesApi(destination_client)

    connection = opendatasoft_automation.ConnectionUID(uid="co_03fnbt")

    ftp_datasource_connection = opendatasoft_automation.FTPDatasource1Connection(actual_instance=connection)

    datasource = opendatasoft_automation.FTPDatasource(type="ftp",
                                                       connection=ftp_datasource_connection,
                                                       relative_url="/dev/dataflows/exports/series/")

    resource = opendatasoft_automation.Resource(
        type="csvfile",
        title="Titre de la source",
        params={
            "doublequote": True,
            "encoding": "utf-8",
            "first_row_no": 1,
            "headers_first_row": True,
            "separator": ","
        },
        datasource=datasource
    )

    try:
        created_resource = destination_resources_api.create_dataset_resource("da_2z0obh", resource=resource)
        pprint(created_resource)
        print(f"- Successfully created resource '{resource.title}'.")
    except ApiException as e:
        print(
            f"  - WARNING: Could not create resource '{resource.title}'. Status: {e.status}, Reason: {e.reason}")
        pprint(e.body)
