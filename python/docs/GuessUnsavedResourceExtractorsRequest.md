# GuessUnsavedResourceExtractorsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datasource** | [**Datasource**](Datasource.md) |  | 

## Example

```python
from opendatasoft_automation.models.guess_unsaved_resource_extractors_request import GuessUnsavedResourceExtractorsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GuessUnsavedResourceExtractorsRequest from a JSON string
guess_unsaved_resource_extractors_request_instance = GuessUnsavedResourceExtractorsRequest.from_json(json)
# print the JSON string representation of the object
print(GuessUnsavedResourceExtractorsRequest.to_json())

# convert the object into a dict
guess_unsaved_resource_extractors_request_dict = guess_unsaved_resource_extractors_request_instance.to_dict()
# create an instance of GuessUnsavedResourceExtractorsRequest from a dict
guess_unsaved_resource_extractors_request_form_dict = guess_unsaved_resource_extractors_request.from_dict(guess_unsaved_resource_extractors_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


