# HTTPDatasource1Headers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from opendatasoft_automation.models.http_datasource1_headers import HTTPDatasource1Headers

# TODO update the JSON string below
json = "{}"
# create an instance of HTTPDatasource1Headers from a JSON string
http_datasource1_headers_instance = HTTPDatasource1Headers.from_json(json)
# print the JSON string representation of the object
print(HTTPDatasource1Headers.to_json())

# convert the object into a dict
http_datasource1_headers_dict = http_datasource1_headers_instance.to_dict()
# create an instance of HTTPDatasource1Headers from a dict
http_datasource1_headers_from_dict = HTTPDatasource1Headers.from_dict(http_datasource1_headers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


