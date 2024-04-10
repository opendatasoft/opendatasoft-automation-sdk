# GoogleDriveDatasource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** |  | 
**connection** | [**GoogleDriveDatasourceAllOfConnection**](GoogleDriveDatasourceAllOfConnection.md) |  | 

## Example

```python
from openapi_client.models.google_drive_datasource import GoogleDriveDatasource

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleDriveDatasource from a JSON string
google_drive_datasource_instance = GoogleDriveDatasource.from_json(json)
# print the JSON string representation of the object
print(GoogleDriveDatasource.to_json())

# convert the object into a dict
google_drive_datasource_dict = google_drive_datasource_instance.to_dict()
# create an instance of GoogleDriveDatasource from a dict
google_drive_datasource_form_dict = google_drive_datasource.from_dict(google_drive_datasource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


