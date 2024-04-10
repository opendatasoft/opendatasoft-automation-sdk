# RenameDatasetFieldConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_name** | **str** | The original technical identifier | 
**to_name** | **str** | The new technical identifier | 
**field_label** | **str** | A user friendly label for the field | 

## Example

```python
from openapi_client.models.rename_dataset_field_configuration import RenameDatasetFieldConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of RenameDatasetFieldConfiguration from a JSON string
rename_dataset_field_configuration_instance = RenameDatasetFieldConfiguration.from_json(json)
# print the JSON string representation of the object
print(RenameDatasetFieldConfiguration.to_json())

# convert the object into a dict
rename_dataset_field_configuration_dict = rename_dataset_field_configuration_instance.to_dict()
# create an instance of RenameDatasetFieldConfiguration from a dict
rename_dataset_field_configuration_form_dict = rename_dataset_field_configuration.from_dict(rename_dataset_field_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


