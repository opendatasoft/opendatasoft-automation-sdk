# SocrataHarvester


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**download_resources** | **bool** | If you want to download resources instead of attaching them via URL. | [optional] [default to False]
**metadata_only** | **bool** | If you want to harvest the remote datasets metadata without their resources. | [optional] [default to False]

## Example

```python
from opendatasoft_automation.models.socrata_harvester import SocrataHarvester

# TODO update the JSON string below
json = "{}"
# create an instance of SocrataHarvester from a JSON string
socrata_harvester_instance = SocrataHarvester.from_json(json)
# print the JSON string representation of the object
print(SocrataHarvester.to_json())

# convert the object into a dict
socrata_harvester_dict = socrata_harvester_instance.to_dict()
# create an instance of SocrataHarvester from a dict
socrata_harvester_from_dict = SocrataHarvester.from_dict(socrata_harvester_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


