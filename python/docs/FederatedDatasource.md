# FederatedDatasource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | [**FederatedDatasourceAllOfDomain**](FederatedDatasourceAllOfDomain.md) |  | 
**dataset** | [**FederatedDatasourceAllOfDataset**](FederatedDatasourceAllOfDataset.md) |  | 
**permissions_user** | [**RelatedUserReadOnly**](RelatedUserReadOnly.md) |  | [optional] 
**impersonate_permissions** | **bool** |  | 
**parameters** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.federated_datasource import FederatedDatasource

# TODO update the JSON string below
json = "{}"
# create an instance of FederatedDatasource from a JSON string
federated_datasource_instance = FederatedDatasource.from_json(json)
# print the JSON string representation of the object
print(FederatedDatasource.to_json())

# convert the object into a dict
federated_datasource_dict = federated_datasource_instance.to_dict()
# create an instance of FederatedDatasource from a dict
federated_datasource_form_dict = federated_datasource.from_dict(federated_datasource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


