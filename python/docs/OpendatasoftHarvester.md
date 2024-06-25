# OpendatasoftHarvester


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The ID or base URL of the domain you want to harvest. | 
**refines** | **str** |  | [optional] [default to '']
**api_key** | **str** | The API key for the remote portal. If it isn&#39;t blank, the API returns null to hide this sensitive value. The API key must be linked to a user which has the permissions to browse datasets on the remote portal, and the permissions to create, edit and publish datasets on the local portal. | [optional] [default to '']

## Example

```python
from opendatasoft_automation.models.opendatasoft_harvester import OpendatasoftHarvester

# TODO update the JSON string below
json = "{}"
# create an instance of OpendatasoftHarvester from a JSON string
opendatasoft_harvester_instance = OpendatasoftHarvester.from_json(json)
# print the JSON string representation of the object
print(OpendatasoftHarvester.to_json())

# convert the object into a dict
opendatasoft_harvester_dict = opendatasoft_harvester_instance.to_dict()
# create an instance of OpendatasoftHarvester from a dict
opendatasoft_harvester_from_dict = OpendatasoftHarvester.from_dict(opendatasoft_harvester_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


