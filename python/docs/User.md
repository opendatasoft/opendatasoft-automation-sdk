# User


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | The user&#39;s username | [optional] 
**display_name** | **str** | Simplified version of the username | [optional] [readonly] 
**first_name** | **str** | The user&#39;s first name | [optional] 
**last_name** | **str** | The user&#39;s last name | [optional] 
**is_active** | **bool** | is &#x60;true&#x60; if the user can connect to their account | [optional] [readonly] 
**email** | **str** | The user&#39;s e-mail address | 
**is_ods** | **bool** | is &#x60;true&#x60; if the user belongs to the Opendatasoft organization | [optional] [readonly] 
**account_type** | **str** | The user&#39;s account type. | [optional] [readonly] 
**permissions** | [**List[Permission]**](Permission.md) | A list of permissions granted to this user | [optional] 
**joined_at** | **datetime** | The date when the user joined the domain | [optional] [readonly] 
**last_seen_at** | **datetime** | The date when the user used their account for the last time | [optional] [readonly] 
**last_login_at** | **datetime** |  | [optional] [readonly] 
**expires_at** | **datetime** |  | [optional] 
**explore_limits** | [**ExploreLimits**](ExploreLimits.md) |  | [optional] 
**management_limits** | **object** |  | [optional] 
**gravatar_url** | **str** |  | [optional] [readonly] 
**groups** | [**UserGroups**](UserGroups.md) |  | [optional] 
**identity_providers** | [**List[UserIdentityProvidersInner]**](UserIdentityProvidersInner.md) | The list of authentification providers type for this user. | [optional] [readonly] 

## Example

```python
from opendatasoft_automation.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_form_dict = user.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


