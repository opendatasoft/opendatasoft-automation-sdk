# DescriptionDatasetFieldConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | **str** | The technical identifier of the field you want to describe | 
**description** | **str** | The user friendly description | 

## Example

```python
from openapi_client.models.description_dataset_field_configuration import DescriptionDatasetFieldConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of DescriptionDatasetFieldConfiguration from a JSON string
description_dataset_field_configuration_instance = DescriptionDatasetFieldConfiguration.from_json(json)
# print the JSON string representation of the object
print(DescriptionDatasetFieldConfiguration.to_json())

# convert the object into a dict
description_dataset_field_configuration_dict = description_dataset_field_configuration_instance.to_dict()
# create an instance of DescriptionDatasetFieldConfiguration from a dict
description_dataset_field_configuration_form_dict = description_dataset_field_configuration.from_dict(description_dataset_field_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


