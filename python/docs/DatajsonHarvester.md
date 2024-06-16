# DatajsonHarvester


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**number_of_datasets** | **int** |  | [optional] 
**download_resources** | **bool** | If you want to download resources instead of attaching them via URL. | [optional] [default to False]
**metadata_only** | **bool** | If you want to harvest the remote datasets metadata without their resources. | [optional] [default to False]

## Example

```python
from opendatasoft_automation.models.datajson_harvester import DatajsonHarvester

# TODO update the JSON string below
json = "{}"
# create an instance of DatajsonHarvester from a JSON string
datajson_harvester_instance = DatajsonHarvester.from_json(json)
# print the JSON string representation of the object
print(DatajsonHarvester.to_json())

# convert the object into a dict
datajson_harvester_dict = datajson_harvester_instance.to_dict()
# create an instance of DatajsonHarvester from a dict
datajson_harvester_form_dict = datajson_harvester.from_dict(datajson_harvester_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


