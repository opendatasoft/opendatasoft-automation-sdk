# CreateDataset400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  | [readonly] 
**message** | **str** |  | [readonly] 
**detail** | **object** |  | [readonly] 

## Example

```python
from opendatasoft_automation.models.create_dataset400_response import CreateDataset400Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDataset400Response from a JSON string
create_dataset400_response_instance = CreateDataset400Response.from_json(json)
# print the JSON string representation of the object
print(CreateDataset400Response.to_json())

# convert the object into a dict
create_dataset400_response_dict = create_dataset400_response_instance.to_dict()
# create an instance of CreateDataset400Response from a dict
create_dataset400_response_from_dict = CreateDataset400Response.from_dict(create_dataset400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


