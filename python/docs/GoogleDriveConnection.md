# GoogleDriveConnection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth** | [**GoogleDriveAuth**](GoogleDriveAuth.md) |  | [optional] 

## Example

```python
from opendatasoft_automation.models.google_drive_connection import GoogleDriveConnection

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleDriveConnection from a JSON string
google_drive_connection_instance = GoogleDriveConnection.from_json(json)
# print the JSON string representation of the object
print(GoogleDriveConnection.to_json())

# convert the object into a dict
google_drive_connection_dict = google_drive_connection_instance.to_dict()
# create an instance of GoogleDriveConnection from a dict
google_drive_connection_form_dict = google_drive_connection.from_dict(google_drive_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


