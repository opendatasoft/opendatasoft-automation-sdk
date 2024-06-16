# DatasetMetadata

The data describing the dataset itself.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | [**DatasetMetadataDefault**](DatasetMetadataDefault.md) |  | [optional] 
**visualization** | [**DatasetMetadataVisualization**](DatasetMetadataVisualization.md) |  | [optional] 
**internal** | [**DatasetMetadataInternal**](DatasetMetadataInternal.md) |  | [optional] 
**custom_template_name** | [**Dict[str, DatasetMetadataValue]**](DatasetMetadataValue.md) | Additional values for custom metadata templates you have configured on your portal. | [optional] 

## Example

```python
from opendatasoft_automation.models.dataset_metadata import DatasetMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetMetadata from a JSON string
dataset_metadata_instance = DatasetMetadata.from_json(json)
# print the JSON string representation of the object
print(DatasetMetadata.to_json())

# convert the object into a dict
dataset_metadata_dict = dataset_metadata_instance.to_dict()
# create an instance of DatasetMetadata from a dict
dataset_metadata_form_dict = dataset_metadata.from_dict(dataset_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


