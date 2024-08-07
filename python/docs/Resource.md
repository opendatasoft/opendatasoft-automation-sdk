# Resource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** | Unique identifier for the resource | [optional] [readonly] 
**type** | **str** | extractor type that should handle this resource | 
**url** | **str** | resource url | [optional] 
**title** | **str** | friendly title | 
**updated_at** | **datetime** |  | [optional] [readonly] 
**params** | **object** | parameters passed to the extractor | [optional] 
**datasource** | [**Datasource**](Datasource.md) |  | [optional] 

## Example

```python
from opendatasoft_automation.models.resource import Resource

# TODO update the JSON string below
json = "{}"
# create an instance of Resource from a JSON string
resource_instance = Resource.from_json(json)
# print the JSON string representation of the object
print(Resource.to_json())

# convert the object into a dict
resource_dict = resource_instance.to_dict()
# create an instance of Resource from a dict
resource_from_dict = Resource.from_dict(resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


