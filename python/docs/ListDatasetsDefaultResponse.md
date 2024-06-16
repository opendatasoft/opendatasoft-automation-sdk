# ListDatasetsDefaultResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  | [readonly] 
**message** | **str** |  | [readonly] 
**trace_id** | **str** |  | [optional] [readonly] 
**detail** | **object** | In some cases, contains additional information about the error. | [optional] [readonly] 

## Example

```python
from opendatasoft_automation.models.list_datasets_default_response import ListDatasetsDefaultResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListDatasetsDefaultResponse from a JSON string
list_datasets_default_response_instance = ListDatasetsDefaultResponse.from_json(json)
# print the JSON string representation of the object
print(ListDatasetsDefaultResponse.to_json())

# convert the object into a dict
list_datasets_default_response_dict = list_datasets_default_response_instance.to_dict()
# create an instance of ListDatasetsDefaultResponse from a dict
list_datasets_default_response_form_dict = list_datasets_default_response.from_dict(list_datasets_default_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


