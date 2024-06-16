# DatasetFeedback

A feedback made on a dataset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** | Unique identifier for the feedback | [readonly] 
**record_id** | **str** | ID of the record on which the feedback was made | 
**user** | [**RelatedUser**](RelatedUser.md) |  | 
**comment** | **str** | User comments | 
**values** | [**DatasetFeedbackValues**](DatasetFeedbackValues.md) |  | [optional] 
**is_archived** | **bool** | True if the feedback was archived by an administrator, False otherwise | [optional] 
**created_at** | **datetime** | Timestamp at which the feedback was submitted | [optional] 

## Example

```python
from opendatasoft_automation.models.dataset_feedback import DatasetFeedback

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetFeedback from a JSON string
dataset_feedback_instance = DatasetFeedback.from_json(json)
# print the JSON string representation of the object
print(DatasetFeedback.to_json())

# convert the object into a dict
dataset_feedback_dict = dataset_feedback_instance.to_dict()
# create an instance of DatasetFeedback from a dict
dataset_feedback_form_dict = dataset_feedback.from_dict(dataset_feedback_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


