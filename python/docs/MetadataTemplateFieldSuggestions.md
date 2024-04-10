# MetadataTemplateFieldSuggestions

Suggested values provided when calling the suggest_url with the appropriate parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hits** | **List[str]** |  | [optional] [readonly] 
**nb_hits** | **float** |  | [optional] [readonly] 
**page** | **float** |  | [optional] [readonly] 
**hits_per_page** | **float** |  | [optional] [readonly] 
**exhaustive_nb_hits** | **bool** |  | [optional] [readonly] 
**exhaustive_typo** | **bool** |  | [optional] [readonly] 
**exhaustive** | [**MetadataTemplateFieldSuggestionsOneOf1Exhaustive**](MetadataTemplateFieldSuggestionsOneOf1Exhaustive.md) |  | [optional] 
**query** | **str** |  | [optional] [readonly] 
**params** | **str** |  | [optional] [readonly] 
**processing_time_ms** | **float** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.metadata_template_field_suggestions import MetadataTemplateFieldSuggestions

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataTemplateFieldSuggestions from a JSON string
metadata_template_field_suggestions_instance = MetadataTemplateFieldSuggestions.from_json(json)
# print the JSON string representation of the object
print(MetadataTemplateFieldSuggestions.to_json())

# convert the object into a dict
metadata_template_field_suggestions_dict = metadata_template_field_suggestions_instance.to_dict()
# create an instance of MetadataTemplateFieldSuggestions from a dict
metadata_template_field_suggestions_form_dict = metadata_template_field_suggestions.from_dict(metadata_template_field_suggestions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


