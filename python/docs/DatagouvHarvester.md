# DatagouvHarvester


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** |  | 
**attachment** | **bool** |  | [optional] [default to False]
**filter_name** | **str** |  | [optional] [default to '']
**filter_value** | **str** |  | [optional] [default to '']
**download_resources** | **bool** | If you want to download resources instead of attaching them via URL. | [optional] [default to False]
**metadata_only** | **bool** | If you want to harvest the remote datasets metadata without their resources. | [optional] [default to False]

## Example

```python
from opendatasoft_automation.models.datagouv_harvester import DatagouvHarvester

# TODO update the JSON string below
json = "{}"
# create an instance of DatagouvHarvester from a JSON string
datagouv_harvester_instance = DatagouvHarvester.from_json(json)
# print the JSON string representation of the object
print(DatagouvHarvester.to_json())

# convert the object into a dict
datagouv_harvester_dict = datagouv_harvester_instance.to_dict()
# create an instance of DatagouvHarvester from a dict
datagouv_harvester_form_dict = datagouv_harvester.from_dict(datagouv_harvester_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


