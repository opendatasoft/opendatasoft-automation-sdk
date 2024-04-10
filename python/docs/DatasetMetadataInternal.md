# DatasetMetadataInternal

This set of metadata is used for dataset configuration and won't appear on your portal.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license_id** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**theme_id** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**draft** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 

## Example

```python
from openapi_client.models.dataset_metadata_internal import DatasetMetadataInternal

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetMetadataInternal from a JSON string
dataset_metadata_internal_instance = DatasetMetadataInternal.from_json(json)
# print the JSON string representation of the object
print(DatasetMetadataInternal.to_json())

# convert the object into a dict
dataset_metadata_internal_dict = dataset_metadata_internal_instance.to_dict()
# create an instance of DatasetMetadataInternal from a dict
dataset_metadata_internal_form_dict = dataset_metadata_internal.from_dict(dataset_metadata_internal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


