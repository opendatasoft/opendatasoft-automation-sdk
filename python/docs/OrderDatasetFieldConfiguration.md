# OrderDatasetFieldConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | **List[str]** | The ordered list of fields technical identifier | [optional] 

## Example

```python
from opendatasoft_automation.models.order_dataset_field_configuration import OrderDatasetFieldConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDatasetFieldConfiguration from a JSON string
order_dataset_field_configuration_instance = OrderDatasetFieldConfiguration.from_json(json)
# print the JSON string representation of the object
print(OrderDatasetFieldConfiguration.to_json())

# convert the object into a dict
order_dataset_field_configuration_dict = order_dataset_field_configuration_instance.to_dict()
# create an instance of OrderDatasetFieldConfiguration from a dict
order_dataset_field_configuration_from_dict = OrderDatasetFieldConfiguration.from_dict(order_dataset_field_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


