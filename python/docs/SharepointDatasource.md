# SharepointDatasource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** |  | 
**drive_id** | **str** |  | 
**connection** | [**SharepointDatasource1Connection**](SharepointDatasource1Connection.md) |  | 

## Example

```python
from opendatasoft_automation.models.sharepoint_datasource import SharepointDatasource

# TODO update the JSON string below
json = "{}"
# create an instance of SharepointDatasource from a JSON string
sharepoint_datasource_instance = SharepointDatasource.from_json(json)
# print the JSON string representation of the object
print(SharepointDatasource.to_json())

# convert the object into a dict
sharepoint_datasource_dict = sharepoint_datasource_instance.to_dict()
# create an instance of SharepointDatasource from a dict
sharepoint_datasource_form_dict = sharepoint_datasource.from_dict(sharepoint_datasource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


