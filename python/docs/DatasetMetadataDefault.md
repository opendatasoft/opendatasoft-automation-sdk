# DatasetMetadataDefault

The standard set of metadata common to all Opendatasoft datasets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**description** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**keyword** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**modified** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**modified_updates_on_metadata_change** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**modified_updates_on_data_change** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**geographic_reference** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**geographic_reference_auto** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**language** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**timezone** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**publisher** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**references** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 
**attributions** | [**DatasetMetadataValue**](DatasetMetadataValue.md) |  | [optional] 

## Example

```python
from opendatasoft_automation.models.dataset_metadata_default import DatasetMetadataDefault

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetMetadataDefault from a JSON string
dataset_metadata_default_instance = DatasetMetadataDefault.from_json(json)
# print the JSON string representation of the object
print(DatasetMetadataDefault.to_json())

# convert the object into a dict
dataset_metadata_default_dict = dataset_metadata_default_instance.to_dict()
# create an instance of DatasetMetadataDefault from a dict
dataset_metadata_default_form_dict = dataset_metadata_default.from_dict(dataset_metadata_default_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


