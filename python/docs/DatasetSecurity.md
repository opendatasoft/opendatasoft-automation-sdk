# DatasetSecurity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_data_visible** | **bool** | Flag indicating whether the target will have access to the records of the dataset or not. | [optional] 
**visible_fields** | **List[str]** | The target will only have access to the fields from this list. &#x60;null&#x60; means that the target has access to all fields. An empty list means that the target won&#39;t see any field (empty dataset schema). | [optional] 
**filter_query** | **str** | The target will only have access to the records matching this query. An empty query means that all records are accessible. | [optional] 
**api_calls_quota** | [**DatasetSecurityApiCallsQuota**](DatasetSecurityApiCallsQuota.md) |  | [optional] 

## Example

```python
from openapi_client.models.dataset_security import DatasetSecurity

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetSecurity from a JSON string
dataset_security_instance = DatasetSecurity.from_json(json)
# print the JSON string representation of the object
print(DatasetSecurity.to_json())

# convert the object into a dict
dataset_security_dict = dataset_security_instance.to_dict()
# create an instance of DatasetSecurity from a dict
dataset_security_form_dict = dataset_security.from_dict(dataset_security_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


