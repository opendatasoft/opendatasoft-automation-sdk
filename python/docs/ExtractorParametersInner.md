# ExtractorParametersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**is_mandatory** | **bool** |  | 
**name** | **str** |  | 
**label** | **str** |  | [optional] 
**default** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**hidden** | **bool** |  | [optional] 
**trim** | **str** |  | [optional] 
**choices** | **List[str]** |  | [optional] 
**can_create_field** | **bool** |  | [optional] 
**impacts_guessed_parameters** | **bool** |  | [optional] 

## Example

```python
from opendatasoft_automation.models.extractor_parameters_inner import ExtractorParametersInner

# TODO update the JSON string below
json = "{}"
# create an instance of ExtractorParametersInner from a JSON string
extractor_parameters_inner_instance = ExtractorParametersInner.from_json(json)
# print the JSON string representation of the object
print(ExtractorParametersInner.to_json())

# convert the object into a dict
extractor_parameters_inner_dict = extractor_parameters_inner_instance.to_dict()
# create an instance of ExtractorParametersInner from a dict
extractor_parameters_inner_from_dict = ExtractorParametersInner.from_dict(extractor_parameters_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


