# ArcgisOpendataHarvester


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**compute_geo_area** | **bool** |  | [optional] [default to False]
**fetch_data** | **bool** |  | [optional] [default to False]
**download_resources** | **bool** | If you want to download resources instead of attaching them via URL. | [optional] [default to False]
**metadata_only** | **bool** | If you want to harvest the remote datasets metadata without their resources. | [optional] [default to False]

## Example

```python
from opendatasoft_automation.models.arcgis_opendata_harvester import ArcgisOpendataHarvester

# TODO update the JSON string below
json = "{}"
# create an instance of ArcgisOpendataHarvester from a JSON string
arcgis_opendata_harvester_instance = ArcgisOpendataHarvester.from_json(json)
# print the JSON string representation of the object
print(ArcgisOpendataHarvester.to_json())

# convert the object into a dict
arcgis_opendata_harvester_dict = arcgis_opendata_harvester_instance.to_dict()
# create an instance of ArcgisOpendataHarvester from a dict
arcgis_opendata_harvester_from_dict = ArcgisOpendataHarvester.from_dict(arcgis_opendata_harvester_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


