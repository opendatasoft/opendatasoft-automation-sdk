# DeleteDatasetFieldConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | The technical identifier of the field you want to delete | 

## Example

```python
from opendatasoft_automation.models.delete_dataset_field_configuration import DeleteDatasetFieldConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteDatasetFieldConfiguration from a JSON string
delete_dataset_field_configuration_instance = DeleteDatasetFieldConfiguration.from_json(json)
# print the JSON string representation of the object
print(DeleteDatasetFieldConfiguration.to_json())

# convert the object into a dict
delete_dataset_field_configuration_dict = delete_dataset_field_configuration_instance.to_dict()
# create an instance of DeleteDatasetFieldConfiguration from a dict
delete_dataset_field_configuration_from_dict = DeleteDatasetFieldConfiguration.from_dict(delete_dataset_field_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


