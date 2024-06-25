# ListHarvesters200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Harvester]**](Harvester.md) |  | [optional] 

## Example

```python
from opendatasoft_automation.models.list_harvesters200_response import ListHarvesters200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListHarvesters200Response from a JSON string
list_harvesters200_response_instance = ListHarvesters200Response.from_json(json)
# print the JSON string representation of the object
print(ListHarvesters200Response.to_json())

# convert the object into a dict
list_harvesters200_response_dict = list_harvesters200_response_instance.to_dict()
# create an instance of ListHarvesters200Response from a dict
list_harvesters200_response_from_dict = ListHarvesters200Response.from_dict(list_harvesters200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


