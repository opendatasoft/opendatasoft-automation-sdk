# TypeDatasetFieldConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | The technical identifier of the field you want to type | 
**type_param** | **str** | The type to apply | 

## Example

```python
from opendatasoft_automation.models.type_dataset_field_configuration import TypeDatasetFieldConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of TypeDatasetFieldConfiguration from a JSON string
type_dataset_field_configuration_instance = TypeDatasetFieldConfiguration.from_json(json)
# print the JSON string representation of the object
print(TypeDatasetFieldConfiguration.to_json())

# convert the object into a dict
type_dataset_field_configuration_dict = type_dataset_field_configuration_instance.to_dict()
# create an instance of TypeDatasetFieldConfiguration from a dict
type_dataset_field_configuration_from_dict = TypeDatasetFieldConfiguration.from_dict(type_dataset_field_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


