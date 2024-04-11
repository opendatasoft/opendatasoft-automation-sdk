# MetadataTemplate

Metadata Template

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name (identifier) of the template | 
**title** | **str** | Title (description) of the template | 
**is_active** | **bool** | True if the template is (needs to be) activated. False otherwise. | 
**is_always_active** | **bool** | True if the template can&#39;t be deactivated. | [optional] [readonly] 
**is_system** | **bool** | True if the template is provided by the system. A system template cannot be modifiable nor removable. False for all other templates. | [optional] [readonly] 
**var_schema** | [**List[MetadataTemplateField]**](MetadataTemplateField.md) |  | 
**created_at** | **datetime** | Date when the template was created | [optional] [readonly] 
**created_by** | [**RelatedUserReadOnly**](RelatedUserReadOnly.md) |  | [optional] 
**updated_at** | **datetime** | Date when the template was last edited | [optional] [readonly] 
**updated_by** | [**RelatedUserReadOnly**](RelatedUserReadOnly.md) |  | [optional] 
**type** | **str** | The type of the template. Only templates with type &#x60;basic&#x60; or &#x60;admin&#x60; can be created. | 

## Example

```python
from openapi_client.models.metadata_template import MetadataTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataTemplate from a JSON string
metadata_template_instance = MetadataTemplate.from_json(json)
# print the JSON string representation of the object
print(MetadataTemplate.to_json())

# convert the object into a dict
metadata_template_dict = metadata_template_instance.to_dict()
# create an instance of MetadataTemplate from a dict
metadata_template_form_dict = metadata_template.from_dict(metadata_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

