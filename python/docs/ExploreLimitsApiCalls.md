# ExploreLimitsApiCalls


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **float** |  | 
**unit** | **str** |  | 

## Example

```python
from opendatasoft_automation.models.explore_limits_api_calls import ExploreLimitsApiCalls

# TODO update the JSON string below
json = "{}"
# create an instance of ExploreLimitsApiCalls from a JSON string
explore_limits_api_calls_instance = ExploreLimitsApiCalls.from_json(json)
# print the JSON string representation of the object
print(ExploreLimitsApiCalls.to_json())

# convert the object into a dict
explore_limits_api_calls_dict = explore_limits_api_calls_instance.to_dict()
# create an instance of ExploreLimitsApiCalls from a dict
explore_limits_api_calls_from_dict = ExploreLimitsApiCalls.from_dict(explore_limits_api_calls_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


