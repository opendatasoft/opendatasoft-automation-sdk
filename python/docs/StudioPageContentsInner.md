# StudioPageContentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version_name** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**updated_by** | [**RelatedUserReadOnly**](RelatedUserReadOnly.md) |  | [optional] 

## Example

```python
from opendatasoft_automation.models.studio_page_contents_inner import StudioPageContentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of StudioPageContentsInner from a JSON string
studio_page_contents_inner_instance = StudioPageContentsInner.from_json(json)
# print the JSON string representation of the object
print(StudioPageContentsInner.to_json())

# convert the object into a dict
studio_page_contents_inner_dict = studio_page_contents_inner_instance.to_dict()
# create an instance of StudioPageContentsInner from a dict
studio_page_contents_inner_form_dict = studio_page_contents_inner.from_dict(studio_page_contents_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


