# OMINodeHarvester


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**infoitems_limit** | **int** |  | [optional] 
**omi_node_version** | **str** |  | [optional] [default to '0.9.0']
**download_resources** | **bool** | If you want to download resources instead of attaching them via URL. | [optional] [default to False]
**metadata_only** | **bool** | If you want to harvest the remote datasets metadata without their resources. | [optional] [default to False]

## Example

```python
from opendatasoft_automation.models.omi_node_harvester import OMINodeHarvester

# TODO update the JSON string below
json = "{}"
# create an instance of OMINodeHarvester from a JSON string
omi_node_harvester_instance = OMINodeHarvester.from_json(json)
# print the JSON string representation of the object
print(OMINodeHarvester.to_json())

# convert the object into a dict
omi_node_harvester_dict = omi_node_harvester_instance.to_dict()
# create an instance of OMINodeHarvester from a dict
omi_node_harvester_from_dict = OMINodeHarvester.from_dict(omi_node_harvester_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


