# GoogleDriveOIDCAuth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nonce** | **str** |  | 
**grant_type** | **str** |  | 
**code** | **str** |  | 
**claims** | **object** |  | [readonly] 
**application_id** | **str** |  | [readonly] 

## Example

```python
from opendatasoft_automation.models.google_drive_oidc_auth import GoogleDriveOIDCAuth

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleDriveOIDCAuth from a JSON string
google_drive_oidc_auth_instance = GoogleDriveOIDCAuth.from_json(json)
# print the JSON string representation of the object
print(GoogleDriveOIDCAuth.to_json())

# convert the object into a dict
google_drive_oidc_auth_dict = google_drive_oidc_auth_instance.to_dict()
# create an instance of GoogleDriveOIDCAuth from a dict
google_drive_oidc_auth_form_dict = google_drive_oidc_auth.from_dict(google_drive_oidc_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


