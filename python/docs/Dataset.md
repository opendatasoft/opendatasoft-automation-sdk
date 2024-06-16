# Dataset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** | Unique identifier of the dataset that will never change through the lifetime of the dataset | [optional] [readonly] 
**dataset_id** | **str** | Human-readable identifier of the dataset that can be modified when the dataset is not published | [optional] 
**created_at** | **datetime** | Date when the dataset was created | [optional] [readonly] 
**updated_at** | **datetime** | Date when the dataset&#39;s configuration was last edited | [optional] [readonly] 
**is_published** | **bool** |  | [optional] [readonly] [default to False]
**is_restricted** | **bool** | Defines if the dataset is visible for anonymous visitors.  - If it is &#x60;false&#x60;, anyone having access to the domain will be able to see the dataset in the catalog. Users who have at least a ruleset declared for them (whether directly, through a group or both) will be able to see everything their rulesets grant access to. Users who do not have any ruleset declared for them (neither directly nor through a group) will be able to see what the default ruleset (&#x60;default_security&#x60; dataset property) grants access to. - If it is &#x60;true&#x60;, the dataset will only appear in the catalog for users who have a ruleset declared for them, either directly or through a group. Other users won&#39;t have any access to the dataset. The &#x60;default_security&#x60; ruleset has no effect for restricted datasets. | [optional] 
**metadata** | [**DatasetMetadata**](DatasetMetadata.md) |  | 
**default_security** | [**DatasetSecurity**](DatasetSecurity.md) |  | [optional] 

## Example

```python
from opendatasoft_automation.models.dataset import Dataset

# TODO update the JSON string below
json = "{}"
# create an instance of Dataset from a JSON string
dataset_instance = Dataset.from_json(json)
# print the JSON string representation of the object
print(Dataset.to_json())

# convert the object into a dict
dataset_dict = dataset_instance.to_dict()
# create an instance of Dataset from a dict
dataset_form_dict = dataset.from_dict(dataset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


