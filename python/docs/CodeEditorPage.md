# CodeEditorPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** | Human-readable identifier used to generate the page URL | [optional] 
**title** | **Dict[str, str]** | Internationalized page title | [optional] 
**description** | **str** | Page description | [optional] 
**content** | [**CodeEditorPageContent**](CodeEditorPageContent.md) |  | 
**template** | **str** | The HTML template used by this page | [optional] 
**tags** | **List[str]** | List of strings used to classify and sort pages | [optional] 
**has_subdomain_copies** | **bool** | Inform if the page been distributed to any subdomain | [optional] [readonly] 
**is_pushed_by_parent** | **bool** | Inform if the page has been distributed by a parent domain | [optional] [readonly] 
**is_restricted** | **bool** | Defines if the page is visible to a few specific users, or every user who can explore the portal | [optional] 
**is_archived** | **bool** | Defines if the page is archived. An archived page isn&#39;t included in the license quota, but can&#39;t be edited and isn&#39;t available to users. | [optional] 
**created_by** | [**RelatedUserReadOnly**](RelatedUserReadOnly.md) |  | [optional] 
**updated_by** | [**RelatedUserReadOnly**](RelatedUserReadOnly.md) |  | [optional] 
**updated_at** | **datetime** | Date when the page was last edited | [optional] [readonly] 
**created_at** | **datetime** | Date when the page was created | [optional] [readonly] 

## Example

```python
from openapi_client.models.code_editor_page import CodeEditorPage

# TODO update the JSON string below
json = "{}"
# create an instance of CodeEditorPage from a JSON string
code_editor_page_instance = CodeEditorPage.from_json(json)
# print the JSON string representation of the object
print(CodeEditorPage.to_json())

# convert the object into a dict
code_editor_page_dict = code_editor_page_instance.to_dict()
# create an instance of CodeEditorPage from a dict
code_editor_page_form_dict = code_editor_page.from_dict(code_editor_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


