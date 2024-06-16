# StudioPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** | Unique identifier of the page | [optional] [readonly] 
**slug** | **str** | Human-readable identifier used to generate the page URL | [optional] 
**public** | **bool** | Defines if the page is visible to a few specific users, or every user who can explore the portal | [optional] [default to False]
**contents** | [**List[StudioPageContentsInner]**](StudioPageContentsInner.md) |  | [optional] [readonly] 
**first_published_at** | **datetime** | Date when the page was first published | [optional] [readonly] 
**created_at** | **datetime** | Date when the page was created | [optional] [readonly] 
**updated_at** | **datetime** | Date when the page was last edited | [optional] [readonly] 
**created_by** | [**RelatedUserReadOnly**](RelatedUserReadOnly.md) |  | [optional] 

## Example

```python
from opendatasoft_automation.models.studio_page import StudioPage

# TODO update the JSON string below
json = "{}"
# create an instance of StudioPage from a JSON string
studio_page_instance = StudioPage.from_json(json)
# print the JSON string representation of the object
print(StudioPage.to_json())

# convert the object into a dict
studio_page_dict = studio_page_instance.to_dict()
# create an instance of StudioPage from a dict
studio_page_form_dict = studio_page.from_dict(studio_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


