# RelatedUserReadOnly

Short representation of a User with only its username

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional] [readonly] 

## Example

```python
from opendatasoft_automation.models.related_user_read_only import RelatedUserReadOnly

# TODO update the JSON string below
json = "{}"
# create an instance of RelatedUserReadOnly from a JSON string
related_user_read_only_instance = RelatedUserReadOnly.from_json(json)
# print the JSON string representation of the object
print(RelatedUserReadOnly.to_json())

# convert the object into a dict
related_user_read_only_dict = related_user_read_only_instance.to_dict()
# create an instance of RelatedUserReadOnly from a dict
related_user_read_only_from_dict = RelatedUserReadOnly.from_dict(related_user_read_only_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


