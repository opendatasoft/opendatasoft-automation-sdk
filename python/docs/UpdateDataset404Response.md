# UpdateDataset404Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  | [readonly] 
**message** | **str** |  | 

## Example

```python
from opendatasoft_automation.models.update_dataset404_response import UpdateDataset404Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDataset404Response from a JSON string
update_dataset404_response_instance = UpdateDataset404Response.from_json(json)
# print the JSON string representation of the object
print(UpdateDataset404Response.to_json())

# convert the object into a dict
update_dataset404_response_dict = update_dataset404_response_instance.to_dict()
# create an instance of UpdateDataset404Response from a dict
update_dataset404_response_from_dict = UpdateDataset404Response.from_dict(update_dataset404_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


