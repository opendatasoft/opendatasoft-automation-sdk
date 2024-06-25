# SharepointConnection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth** | [**SharepointAuth**](SharepointAuth.md) |  | [optional] 

## Example

```python
from opendatasoft_automation.models.sharepoint_connection import SharepointConnection

# TODO update the JSON string below
json = "{}"
# create an instance of SharepointConnection from a JSON string
sharepoint_connection_instance = SharepointConnection.from_json(json)
# print the JSON string representation of the object
print(SharepointConnection.to_json())

# convert the object into a dict
sharepoint_connection_dict = sharepoint_connection_instance.to_dict()
# create an instance of SharepointConnection from a dict
sharepoint_connection_from_dict = SharepointConnection.from_dict(sharepoint_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


