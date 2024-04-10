# AzureBlobStorageSharedKeyAuth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_name** | **str** |  | 
**shared_key** | **str** | The account shared key. The API returns null to hide this sensitive value. | 

## Example

```python
from openapi_client.models.azure_blob_storage_shared_key_auth import AzureBlobStorageSharedKeyAuth

# TODO update the JSON string below
json = "{}"
# create an instance of AzureBlobStorageSharedKeyAuth from a JSON string
azure_blob_storage_shared_key_auth_instance = AzureBlobStorageSharedKeyAuth.from_json(json)
# print the JSON string representation of the object
print(AzureBlobStorageSharedKeyAuth.to_json())

# convert the object into a dict
azure_blob_storage_shared_key_auth_dict = azure_blob_storage_shared_key_auth_instance.to_dict()
# create an instance of AzureBlobStorageSharedKeyAuth from a dict
azure_blob_storage_shared_key_auth_form_dict = azure_blob_storage_shared_key_auth.from_dict(azure_blob_storage_shared_key_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


