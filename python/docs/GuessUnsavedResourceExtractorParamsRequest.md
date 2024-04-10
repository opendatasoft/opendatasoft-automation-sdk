# GuessUnsavedResourceExtractorParamsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datasource** | [**Datasource**](Datasource.md) |  | 
**type** | **str** |  | 

## Example

```python
from openapi_client.models.guess_unsaved_resource_extractor_params_request import GuessUnsavedResourceExtractorParamsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GuessUnsavedResourceExtractorParamsRequest from a JSON string
guess_unsaved_resource_extractor_params_request_instance = GuessUnsavedResourceExtractorParamsRequest.from_json(json)
# print the JSON string representation of the object
print(GuessUnsavedResourceExtractorParamsRequest.to_json())

# convert the object into a dict
guess_unsaved_resource_extractor_params_request_dict = guess_unsaved_resource_extractor_params_request_instance.to_dict()
# create an instance of GuessUnsavedResourceExtractorParamsRequest from a dict
guess_unsaved_resource_extractor_params_request_form_dict = guess_unsaved_resource_extractor_params_request.from_dict(guess_unsaved_resource_extractor_params_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


