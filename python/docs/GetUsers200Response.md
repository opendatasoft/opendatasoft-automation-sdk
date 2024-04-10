# GetUsers200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **str** | The total number of results that can be queried. | [optional] 
**next** | **str** | Link to the next page of results if any. | [optional] 
**previous** | **str** | Link to the previous page of results if any. | [optional] 
**results** | [**List[User]**](User.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_users200_response import GetUsers200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetUsers200Response from a JSON string
get_users200_response_instance = GetUsers200Response.from_json(json)
# print the JSON string representation of the object
print(GetUsers200Response.to_json())

# convert the object into a dict
get_users200_response_dict = get_users200_response_instance.to_dict()
# create an instance of GetUsers200Response from a dict
get_users200_response_form_dict = get_users200_response.from_dict(get_users200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


