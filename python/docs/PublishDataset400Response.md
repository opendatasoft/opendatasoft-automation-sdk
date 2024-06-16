# PublishDataset400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  | [readonly] 
**message** | **str** |  | [readonly] 

## Example

```python
from opendatasoft_automation.models.publish_dataset400_response import PublishDataset400Response

# TODO update the JSON string below
json = "{}"
# create an instance of PublishDataset400Response from a JSON string
publish_dataset400_response_instance = PublishDataset400Response.from_json(json)
# print the JSON string representation of the object
print(PublishDataset400Response.to_json())

# convert the object into a dict
publish_dataset400_response_dict = publish_dataset400_response_instance.to_dict()
# create an instance of PublishDataset400Response from a dict
publish_dataset400_response_form_dict = publish_dataset400_response.from_dict(publish_dataset400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


