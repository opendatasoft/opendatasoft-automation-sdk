# FederatedDataset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset_id** | **str** |  | [optional] 
**metas** | **object** |  | [optional] 
**fields** | **List[object]** |  | [optional] 

## Example

```python
from opendatasoft_automation.models.federated_dataset import FederatedDataset

# TODO update the JSON string below
json = "{}"
# create an instance of FederatedDataset from a JSON string
federated_dataset_instance = FederatedDataset.from_json(json)
# print the JSON string representation of the object
print(FederatedDataset.to_json())

# convert the object into a dict
federated_dataset_dict = federated_dataset_instance.to_dict()
# create an instance of FederatedDataset from a dict
federated_dataset_from_dict = FederatedDataset.from_dict(federated_dataset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


