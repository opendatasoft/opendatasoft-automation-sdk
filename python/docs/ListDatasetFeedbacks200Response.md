# ListDatasetFeedbacks200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[DatasetFeedback]**](DatasetFeedback.md) |  | [optional] 

## Example

```python
from opendatasoft_automation.models.list_dataset_feedbacks200_response import ListDatasetFeedbacks200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListDatasetFeedbacks200Response from a JSON string
list_dataset_feedbacks200_response_instance = ListDatasetFeedbacks200Response.from_json(json)
# print the JSON string representation of the object
print(ListDatasetFeedbacks200Response.to_json())

# convert the object into a dict
list_dataset_feedbacks200_response_dict = list_dataset_feedbacks200_response_instance.to_dict()
# create an instance of ListDatasetFeedbacks200Response from a dict
list_dataset_feedbacks200_response_from_dict = ListDatasetFeedbacks200Response.from_dict(list_dataset_feedbacks200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


