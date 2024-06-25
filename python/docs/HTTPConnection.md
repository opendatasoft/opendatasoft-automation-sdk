# HTTPConnection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**headers** | [**List[HTTPConnectionAllOfHeaders]**](HTTPConnectionAllOfHeaders.md) |  | [optional] 
**auth** | [**HTTPAuth**](HTTPAuth.md) |  | [optional] 

## Example

```python
from opendatasoft_automation.models.http_connection import HTTPConnection

# TODO update the JSON string below
json = "{}"
# create an instance of HTTPConnection from a JSON string
http_connection_instance = HTTPConnection.from_json(json)
# print the JSON string representation of the object
print(HTTPConnection.to_json())

# convert the object into a dict
http_connection_dict = http_connection_instance.to_dict()
# create an instance of HTTPConnection from a dict
http_connection_from_dict = HTTPConnection.from_dict(http_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


