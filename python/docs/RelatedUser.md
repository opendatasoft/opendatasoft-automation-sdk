# RelatedUser

Short representation of a User with only its username

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.related_user import RelatedUser

# TODO update the JSON string below
json = "{}"
# create an instance of RelatedUser from a JSON string
related_user_instance = RelatedUser.from_json(json)
# print the JSON string representation of the object
print(RelatedUser.to_json())

# convert the object into a dict
related_user_dict = related_user_instance.to_dict()
# create an instance of RelatedUser from a dict
related_user_form_dict = related_user.from_dict(related_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


