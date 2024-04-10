# DatasetFeedbackValues

New values suggested by the user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Value suggested by the user | [optional] 
**type** | **str** | Value type | [optional] 

## Example

```python
from openapi_client.models.dataset_feedback_values import DatasetFeedbackValues

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetFeedbackValues from a JSON string
dataset_feedback_values_instance = DatasetFeedbackValues.from_json(json)
# print the JSON string representation of the object
print(DatasetFeedbackValues.to_json())

# convert the object into a dict
dataset_feedback_values_dict = dataset_feedback_values_instance.to_dict()
# create an instance of DatasetFeedbackValues from a dict
dataset_feedback_values_form_dict = dataset_feedback_values.from_dict(dataset_feedback_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


