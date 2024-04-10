# AzureBlobStorageConnection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headers** | [**List[HTTPConnectionAllOfHeaders]**](HTTPConnectionAllOfHeaders.md) |  | [optional] 
**auth** | [**AzureBlobStorageAuth**](AzureBlobStorageAuth.md) |  | [optional] 

## Example

```python
from openapi_client.models.azure_blob_storage_connection import AzureBlobStorageConnection

# TODO update the JSON string below
json = "{}"
# create an instance of AzureBlobStorageConnection from a JSON string
azure_blob_storage_connection_instance = AzureBlobStorageConnection.from_json(json)
# print the JSON string representation of the object
print(AzureBlobStorageConnection.to_json())

# convert the object into a dict
azure_blob_storage_connection_dict = azure_blob_storage_connection_instance.to_dict()
# create an instance of AzureBlobStorageConnection from a dict
azure_blob_storage_connection_form_dict = azure_blob_storage_connection.from_dict(azure_blob_storage_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


