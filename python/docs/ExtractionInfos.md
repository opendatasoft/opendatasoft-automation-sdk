# ExtractionInfos

Information about the kind of extraction configured for this resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | human readable label for the extraction type | [optional] [readonly] 
**type** | **str** | extractor type that should handle this resource | [optional] [readonly] 

## Example

```python
from opendatasoft_automation.models.extraction_infos import ExtractionInfos

# TODO update the JSON string below
json = "{}"
# create an instance of ExtractionInfos from a JSON string
extraction_infos_instance = ExtractionInfos.from_json(json)
# print the JSON string representation of the object
print(ExtractionInfos.to_json())

# convert the object into a dict
extraction_infos_dict = extraction_infos_instance.to_dict()
# create an instance of ExtractionInfos from a dict
extraction_infos_from_dict = ExtractionInfos.from_dict(extraction_infos_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


