# SharepointDatasource1Connection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** | The UID of an existing connection to reuse. | 

## Example

```python
from opendatasoft_automation.models.sharepoint_datasource1_connection import SharepointDatasource1Connection

# TODO update the JSON string below
json = "{}"
# create an instance of SharepointDatasource1Connection from a JSON string
sharepoint_datasource1_connection_instance = SharepointDatasource1Connection.from_json(json)
# print the JSON string representation of the object
print(SharepointDatasource1Connection.to_json())

# convert the object into a dict
sharepoint_datasource1_connection_dict = sharepoint_datasource1_connection_instance.to_dict()
# create an instance of SharepointDatasource1Connection from a dict
sharepoint_datasource1_connection_from_dict = SharepointDatasource1Connection.from_dict(sharepoint_datasource1_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


