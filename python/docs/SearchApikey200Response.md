# SearchApikey200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**found** | **bool** |  | [optional] 
**result** | [**APIKey**](APIKey.md) |  | [optional] 

## Example

```python
from opendatasoft_automation.models.search_apikey200_response import SearchApikey200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SearchApikey200Response from a JSON string
search_apikey200_response_instance = SearchApikey200Response.from_json(json)
# print the JSON string representation of the object
print(SearchApikey200Response.to_json())

# convert the object into a dict
search_apikey200_response_dict = search_apikey200_response_instance.to_dict()
# create an instance of SearchApikey200Response from a dict
search_apikey200_response_form_dict = search_apikey200_response.from_dict(search_apikey200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


