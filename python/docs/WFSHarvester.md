# WFSHarvester


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**metadata_only** | **bool** | If you want to harvest the remote datasets metadata without their resources. | [optional] [default to False]

## Example

```python
from opendatasoft_automation.models.wfs_harvester import WFSHarvester

# TODO update the JSON string below
json = "{}"
# create an instance of WFSHarvester from a JSON string
wfs_harvester_instance = WFSHarvester.from_json(json)
# print the JSON string representation of the object
print(WFSHarvester.to_json())

# convert the object into a dict
wfs_harvester_dict = wfs_harvester_instance.to_dict()
# create an instance of WFSHarvester from a dict
wfs_harvester_form_dict = wfs_harvester.from_dict(wfs_harvester_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


