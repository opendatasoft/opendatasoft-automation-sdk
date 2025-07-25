# OriginInfos

Information about the origin of the resource (e.g. HTTP, FTP etc.)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Human readable label for the resource origin | [optional] [readonly] 
**type** | **str** | Type of the resource origin. The most relevant information is returned between the datasource type and the extraction type. For example a resource using an HTTP Feed, has a \&quot;feed\&quot; origin, not HTTP. | [optional] [readonly] 

## Example

```python
from opendatasoft_automation.models.origin_infos import OriginInfos

# TODO update the JSON string below
json = "{}"
# create an instance of OriginInfos from a JSON string
origin_infos_instance = OriginInfos.from_json(json)
# print the JSON string representation of the object
print(OriginInfos.to_json())

# convert the object into a dict
origin_infos_dict = origin_infos_instance.to_dict()
# create an instance of OriginInfos from a dict
origin_infos_from_dict = OriginInfos.from_dict(origin_infos_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


