# ListDatasets200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Dataset]**](Dataset.md) |  | [optional] 

## Example

```python
from opendatasoft_automation.models.list_datasets200_response import ListDatasets200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListDatasets200Response from a JSON string
list_datasets200_response_instance = ListDatasets200Response.from_json(json)
# print the JSON string representation of the object
print(ListDatasets200Response.to_json())

# convert the object into a dict
list_datasets200_response_dict = list_datasets200_response_instance.to_dict()
# create an instance of ListDatasets200Response from a dict
list_datasets200_response_from_dict = ListDatasets200Response.from_dict(list_datasets200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


