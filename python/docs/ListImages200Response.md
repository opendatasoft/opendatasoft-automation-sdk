# ListImages200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ListImages200ResponseAllOfResultsInner]**](ListImages200ResponseAllOfResultsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.list_images200_response import ListImages200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListImages200Response from a JSON string
list_images200_response_instance = ListImages200Response.from_json(json)
# print the JSON string representation of the object
print(ListImages200Response.to_json())

# convert the object into a dict
list_images200_response_dict = list_images200_response_instance.to_dict()
# create an instance of ListImages200Response from a dict
list_images200_response_form_dict = list_images200_response.from_dict(list_images200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


