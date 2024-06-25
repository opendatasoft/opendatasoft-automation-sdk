# HTTPAuth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 

## Example

```python
from opendatasoft_automation.models.http_auth import HTTPAuth

# TODO update the JSON string below
json = "{}"
# create an instance of HTTPAuth from a JSON string
http_auth_instance = HTTPAuth.from_json(json)
# print the JSON string representation of the object
print(HTTPAuth.to_json())

# convert the object into a dict
http_auth_dict = http_auth_instance.to_dict()
# create an instance of HTTPAuth from a dict
http_auth_from_dict = HTTPAuth.from_dict(http_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


