# ArcgisHarvester


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**download_resources** | **bool** | If you want to download resources instead of attaching them via URL. | [optional] [default to False]
**metadata_only** | **bool** | If you want to harvest the remote datasets metadata without their resources. | [optional] [default to False]

## Example

```python
from opendatasoft_automation.models.arcgis_harvester import ArcgisHarvester

# TODO update the JSON string below
json = "{}"
# create an instance of ArcgisHarvester from a JSON string
arcgis_harvester_instance = ArcgisHarvester.from_json(json)
# print the JSON string representation of the object
print(ArcgisHarvester.to_json())

# convert the object into a dict
arcgis_harvester_dict = arcgis_harvester_instance.to_dict()
# create an instance of ArcgisHarvester from a dict
arcgis_harvester_form_dict = arcgis_harvester.from_dict(arcgis_harvester_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


