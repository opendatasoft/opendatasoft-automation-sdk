# AbortHarvester400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  | [readonly] 
**message** | **str** |  | [readonly] 

## Example

```python
from opendatasoft_automation.models.abort_harvester400_response import AbortHarvester400Response

# TODO update the JSON string below
json = "{}"
# create an instance of AbortHarvester400Response from a JSON string
abort_harvester400_response_instance = AbortHarvester400Response.from_json(json)
# print the JSON string representation of the object
print(AbortHarvester400Response.to_json())

# convert the object into a dict
abort_harvester400_response_dict = abort_harvester400_response_instance.to_dict()
# create an instance of AbortHarvester400Response from a dict
abort_harvester400_response_from_dict = AbortHarvester400Response.from_dict(abort_harvester400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


