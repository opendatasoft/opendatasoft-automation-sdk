# ListMetadataTemplates200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[MetadataTemplate]**](MetadataTemplate.md) |  | [optional] 

## Example

```python
from opendatasoft_automation.models.list_metadata_templates200_response import ListMetadataTemplates200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListMetadataTemplates200Response from a JSON string
list_metadata_templates200_response_instance = ListMetadataTemplates200Response.from_json(json)
# print the JSON string representation of the object
print(ListMetadataTemplates200Response.to_json())

# convert the object into a dict
list_metadata_templates200_response_dict = list_metadata_templates200_response_instance.to_dict()
# create an instance of ListMetadataTemplates200Response from a dict
list_metadata_templates200_response_form_dict = list_metadata_templates200_response.from_dict(list_metadata_templates200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


