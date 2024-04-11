# GetMetadataFieldsList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[MetadataTemplateField]**](MetadataTemplateField.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_metadata_fields_list200_response import GetMetadataFieldsList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetMetadataFieldsList200Response from a JSON string
get_metadata_fields_list200_response_instance = GetMetadataFieldsList200Response.from_json(json)
# print the JSON string representation of the object
print(GetMetadataFieldsList200Response.to_json())

# convert the object into a dict
get_metadata_fields_list200_response_dict = get_metadata_fields_list200_response_instance.to_dict()
# create an instance of GetMetadataFieldsList200Response from a dict
get_metadata_fields_list200_response_form_dict = get_metadata_fields_list200_response.from_dict(get_metadata_fields_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

