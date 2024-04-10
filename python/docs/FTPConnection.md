# FTPConnection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**auth** | [**FTPAuth**](FTPAuth.md) |  | [optional] 

## Example

```python
from openapi_client.models.ftp_connection import FTPConnection

# TODO update the JSON string below
json = "{}"
# create an instance of FTPConnection from a JSON string
ftp_connection_instance = FTPConnection.from_json(json)
# print the JSON string representation of the object
print(FTPConnection.to_json())

# convert the object into a dict
ftp_connection_dict = ftp_connection_instance.to_dict()
# create an instance of FTPConnection from a dict
ftp_connection_form_dict = ftp_connection.from_dict(ftp_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


