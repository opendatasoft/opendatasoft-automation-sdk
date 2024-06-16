# FederatedDatasourceAllOfDataset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset_id** | **str** |  | 
**metas** | **object** |  | [optional] 
**fields** | **List[object]** |  | [optional] 

## Example

```python
from opendatasoft_automation.models.federated_datasource_all_of_dataset import FederatedDatasourceAllOfDataset

# TODO update the JSON string below
json = "{}"
# create an instance of FederatedDatasourceAllOfDataset from a JSON string
federated_datasource_all_of_dataset_instance = FederatedDatasourceAllOfDataset.from_json(json)
# print the JSON string representation of the object
print(FederatedDatasourceAllOfDataset.to_json())

# convert the object into a dict
federated_datasource_all_of_dataset_dict = federated_datasource_all_of_dataset_instance.to_dict()
# create an instance of FederatedDatasourceAllOfDataset from a dict
federated_datasource_all_of_dataset_form_dict = federated_datasource_all_of_dataset.from_dict(federated_datasource_all_of_dataset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


