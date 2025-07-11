# Resource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** | Unique identifier for the resource | [optional] [readonly] 
**type** | **str** | Extractor type that should handle this resource | 
**title** | **str** | User defined title for identifying the resource | 
**display_name** | **str** | A name representing the resource. It is computed from the resource &#x60;title&#x60; and &#x60;datasource&#x60; depending on the type of resource | [optional] [readonly] 
**extraction_infos** | [**ExtractionInfos**](ExtractionInfos.md) |  | [optional] 
**origin** | [**OriginInfos**](OriginInfos.md) |  | [optional] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**params** | **object** | Parameters passed to the extractor | [optional] 
**datasource** | [**Datasource**](Datasource.md) |  | 

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


