# Harvester


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** |  | [readonly] 
**type** | **str** |  | 
**name** | **str** |  | 
**status** | **str** |  | [readonly] 
**version** | **int** |  | [optional] [default to 1]
**restrict_datasets_visibility** | **bool** | If the harvested datasets should be configured as private. By default, it has the same value as the domain configuration \&quot;Restrict new datasets by default\&quot; | [optional] 
**delete_missing_datasets** | **bool** | If the source datasets are deleted on the harvested portal, delete them on this Opendatasoft portal too | [optional] [default to False]
**forced_metas** | **Dict[str, Dict[str, object]]** | Allow you to override some metadata in every harvested dataset | [optional] 
**remote_datasets_count** | **int** | How many datasets have been found on the remote catalog | [readonly] 
**harvested_datasets_count** | **int** | How many datasets have been harvested in the current or last run | [readonly] 
**published_datasets_count** | **int** | How many harvested datasets are published | [readonly] 
**attached_datasets_count** | **int** | How many datasets in your Opendatasoft portal have been created by this harvester | [readonly] 
**has_error** | **bool** | If the last harvesting resulted in a critical error | [readonly] 
**resource_errors_count** | **int** | How many datasets on the remote catalog led to an error and couldn&#39;t be harvested | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 
**updated_by** | [**RelatedUserReadOnly**](RelatedUserReadOnly.md) |  | 
**last_started_at** | **datetime** | The last time the harvester was started | [readonly] 
**last_success_at** | **datetime** | The last time the harvesting has been succcesful | [readonly] 

## Example

```python
from opendatasoft_automation.models.harvester import Harvester

# TODO update the JSON string below
json = "{}"
# create an instance of Harvester from a JSON string
harvester_instance = Harvester.from_json(json)
# print the JSON string representation of the object
print(Harvester.to_json())

# convert the object into a dict
harvester_dict = harvester_instance.to_dict()
# create an instance of Harvester from a dict
harvester_from_dict = Harvester.from_dict(harvester_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


