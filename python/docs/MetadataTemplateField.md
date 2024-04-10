# MetadataTemplateField

Metadata Template Field (part of the template's schema)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Metadata Template field name (identifier) | 
**type** | **str** | Type of the field | [optional] [default to 'text']
**label** | **str** | The label (short description) of this field. | [optional] 
**help_text** | **str** |  | [optional] 
**is_hidden** | **bool** | System property. | [optional] [readonly] [default to False]
**self_suggest** | **bool** | If True then it will build an URL for getting suggestion of already-filled values. (see suggest_url) | [optional] [default to False]
**is_filter** | **bool** | If True then this filed can be used a filter. | [optional] [default to False]
**i18n** | **bool** | If True then this field will be managed by our i18n system. | [optional] [default to False]
**suggest_url** | **str** |  | [optional] 
**choices** | **List[str]** |  | [optional] 
**labels** | **Dict[str, Dict[str, str]]** |  | [optional] 
**requirement_level** | **str** | The indicative requirement level associated to this field. | [optional] [default to 'optional']

## Example

```python
from openapi_client.models.metadata_template_field import MetadataTemplateField

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataTemplateField from a JSON string
metadata_template_field_instance = MetadataTemplateField.from_json(json)
# print the JSON string representation of the object
print(MetadataTemplateField.to_json())

# convert the object into a dict
metadata_template_field_dict = metadata_template_field_instance.to_dict()
# create an instance of MetadataTemplateField from a dict
metadata_template_field_form_dict = metadata_template_field.from_dict(metadata_template_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


