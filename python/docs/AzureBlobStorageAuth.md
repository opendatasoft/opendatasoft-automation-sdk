# AzureBlobStorageAuth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 

## Example

```python
from opendatasoft_automation.models.azure_blob_storage_auth import AzureBlobStorageAuth

# TODO update the JSON string below
json = "{}"
# create an instance of AzureBlobStorageAuth from a JSON string
azure_blob_storage_auth_instance = AzureBlobStorageAuth.from_json(json)
# print the JSON string representation of the object
print(AzureBlobStorageAuth.to_json())

# convert the object into a dict
azure_blob_storage_auth_dict = azure_blob_storage_auth_instance.to_dict()
# create an instance of AzureBlobStorageAuth from a dict
azure_blob_storage_auth_from_dict = AzureBlobStorageAuth.from_dict(azure_blob_storage_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


