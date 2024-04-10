# DatasetVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** | Unique identifier for the version | [optional] 
**sections** | **List[str]** | Sections modified by this change | [optional] 
**created_by** | [**RelatedUserReadOnly**](RelatedUserReadOnly.md) |  | [optional] 
**can_restore** | **bool** |  | [optional] 
**created_at** | **datetime** | Date at which the change was made | [optional] [readonly] 

## Example

```python
from openapi_client.models.dataset_version import DatasetVersion

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetVersion from a JSON string
dataset_version_instance = DatasetVersion.from_json(json)
# print the JSON string representation of the object
print(DatasetVersion.to_json())

# convert the object into a dict
dataset_version_dict = dataset_version_instance.to_dict()
# create an instance of DatasetVersion from a dict
dataset_version_form_dict = dataset_version.from_dict(dataset_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


