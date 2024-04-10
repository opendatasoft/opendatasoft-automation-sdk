# Extractor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [readonly] 
**label** | **str** |  | [readonly] 
**parameters** | [**List[ExtractorParametersInner]**](ExtractorParametersInner.md) |  | [readonly] 

## Example

```python
from openapi_client.models.extractor import Extractor

# TODO update the JSON string below
json = "{}"
# create an instance of Extractor from a JSON string
extractor_instance = Extractor.from_json(json)
# print the JSON string representation of the object
print(Extractor.to_json())

# convert the object into a dict
extractor_dict = extractor_instance.to_dict()
# create an instance of Extractor from a dict
extractor_form_dict = extractor.from_dict(extractor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


