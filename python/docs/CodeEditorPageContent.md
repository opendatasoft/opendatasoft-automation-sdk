# CodeEditorPageContent

Internationalized page content

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**html** | **Dict[str, str]** |  | [optional] 
**css** | **Dict[str, str]** |  | [optional] 

## Example

```python
from opendatasoft_automation.models.code_editor_page_content import CodeEditorPageContent

# TODO update the JSON string below
json = "{}"
# create an instance of CodeEditorPageContent from a JSON string
code_editor_page_content_instance = CodeEditorPageContent.from_json(json)
# print the JSON string representation of the object
print(CodeEditorPageContent.to_json())

# convert the object into a dict
code_editor_page_content_dict = code_editor_page_content_instance.to_dict()
# create an instance of CodeEditorPageContent from a dict
code_editor_page_content_from_dict = CodeEditorPageContent.from_dict(code_editor_page_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


