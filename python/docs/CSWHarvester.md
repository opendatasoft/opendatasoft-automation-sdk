# CSWHarvester


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**keywords_thesaurus** | **str** |  | [optional] [default to '']
**theme_thesaurus** | **str** |  | [optional] [default to '']
**insert_br_in_description** | **bool** |  | [optional] [default to False]
**constraint_language** | **bool** |  | [optional] [default to False]
**invert_coordinates** | **bool** |  | [optional] [default to False]
**themes_mapping** | **Dict[str, Dict[str, str]]** |  | [optional] 
**licenses_mapping** | **Dict[str, str]** |  | [optional] 
**metadata_only** | **bool** | If you want to harvest the remote datasets metadata without their resources. | [optional] [default to False]

## Example

```python
from opendatasoft_automation.models.csw_harvester import CSWHarvester

# TODO update the JSON string below
json = "{}"
# create an instance of CSWHarvester from a JSON string
csw_harvester_instance = CSWHarvester.from_json(json)
# print the JSON string representation of the object
print(CSWHarvester.to_json())

# convert the object into a dict
csw_harvester_dict = csw_harvester_instance.to_dict()
# create an instance of CSWHarvester from a dict
csw_harvester_from_dict = CSWHarvester.from_dict(csw_harvester_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


