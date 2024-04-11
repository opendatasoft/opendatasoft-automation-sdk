# Resource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** | Unique identifier for the resource | [optional] [readonly] 
**type** | **str** | extractor type that should handle this resource | 
**title** | **str** | friendly title | 
**updated_at** | **datetime** |  | [optional] [readonly] 
**params** | **object** | parameters passed to the extractor | [optional] 
**datasource** | [**Datasource**](Datasource.md) |  | 

## Example

```python
from openapi_client.models.resource import Resource

# TODO update the JSON string below
json = "{}"
# create an instance of Resource from a JSON string
resource_instance = Resource.from_json(json)
# print the JSON string representation of the object
print(Resource.to_json())

# convert the object into a dict
resource_dict = resource_instance.to_dict()
# create an instance of Resource from a dict
resource_form_dict = resource.from_dict(resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

