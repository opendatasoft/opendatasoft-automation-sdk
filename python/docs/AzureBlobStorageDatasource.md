# AzureBlobStorageDatasource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**headers** | [**List[HTTPDatasource1Headers]**](HTTPDatasource1Headers.md) |  | [optional] 
**connection** | [**AzureBlobStorageDatasourceAllOfConnection**](AzureBlobStorageDatasourceAllOfConnection.md) |  | 

## Example

```python
from opendatasoft_automation.models.azure_blob_storage_datasource import AzureBlobStorageDatasource

# TODO update the JSON string below
json = "{}"
# create an instance of AzureBlobStorageDatasource from a JSON string
azure_blob_storage_datasource_instance = AzureBlobStorageDatasource.from_json(json)
# print the JSON string representation of the object
print(AzureBlobStorageDatasource.to_json())

# convert the object into a dict
azure_blob_storage_datasource_dict = azure_blob_storage_datasource_instance.to_dict()
# create an instance of AzureBlobStorageDatasource from a dict
azure_blob_storage_datasource_from_dict = AzureBlobStorageDatasource.from_dict(azure_blob_storage_datasource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


