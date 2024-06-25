# JunarHarvester


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**auth_key** | **str** | The Junar auth key. The API returns null to hide this sensitive value. | 
**query_string** | **str** |  | [optional] [default to '']
**categories** | **str** |  | [optional] [default to '']
**download_resources** | **bool** | If you want to download resources instead of attaching them via URL. | [optional] [default to False]
**metadata_only** | **bool** | If you want to harvest the remote datasets metadata without their resources. | [optional] [default to False]

## Example

```python
from opendatasoft_automation.models.junar_harvester import JunarHarvester

# TODO update the JSON string below
json = "{}"
# create an instance of JunarHarvester from a JSON string
junar_harvester_instance = JunarHarvester.from_json(json)
# print the JSON string representation of the object
print(JunarHarvester.to_json())

# convert the object into a dict
junar_harvester_dict = junar_harvester_instance.to_dict()
# create an instance of JunarHarvester from a dict
junar_harvester_from_dict = JunarHarvester.from_dict(junar_harvester_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


