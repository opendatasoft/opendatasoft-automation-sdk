# DatasetMetadataValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **object** | The effective metadata value. If the dataset is linked to a remote dataset and &#x60;override_remote_value&#x60;  is &#x60;false&#x60;, this value will be the same as &#x60;remote_value&#x60;. | 
**remote_value** | **object** | The metadata value on the remote dataset. This property is present only if the dataset is linked to a remote  dataset (a federated dataset for example). | [optional] [readonly] 
**override_remote_value** | **bool** | Defines if the remote value is overridden (&#x60;true&#x60;), or if it is kept in sync with the value on the remote  dataset. This property is present only if the dataset is linked to a remote  dataset (a federated dataset for example). | [optional] 

## Example

```python
from openapi_client.models.dataset_metadata_value import DatasetMetadataValue

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetMetadataValue from a JSON string
dataset_metadata_value_instance = DatasetMetadataValue.from_json(json)
# print the JSON string representation of the object
print(DatasetMetadataValue.to_json())

# convert the object into a dict
dataset_metadata_value_dict = dataset_metadata_value_instance.to_dict()
# create an instance of DatasetMetadataValue from a dict
dataset_metadata_value_form_dict = dataset_metadata_value.from_dict(dataset_metadata_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


