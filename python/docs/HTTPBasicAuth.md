# HTTPBasicAuth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**password** | **str** | The password for the user. The API returns null to hide this sensitive value. | 

## Example

```python
from opendatasoft_automation.models.http_basic_auth import HTTPBasicAuth

# TODO update the JSON string below
json = "{}"
# create an instance of HTTPBasicAuth from a JSON string
http_basic_auth_instance = HTTPBasicAuth.from_json(json)
# print the JSON string representation of the object
print(HTTPBasicAuth.to_json())

# convert the object into a dict
http_basic_auth_dict = http_basic_auth_instance.to_dict()
# create an instance of HTTPBasicAuth from a dict
http_basic_auth_form_dict = http_basic_auth.from_dict(http_basic_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


