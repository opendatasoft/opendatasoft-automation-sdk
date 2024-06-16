# HTTPDatasource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relative_url** | **str** |  | [optional] 
**headers** | [**List[HTTPDatasource1Headers]**](HTTPDatasource1Headers.md) |  | [optional] 
**connection** | [**HTTPDatasource1Connection**](HTTPDatasource1Connection.md) |  | 

## Example

```python
from opendatasoft_automation.models.http_datasource import HTTPDatasource

# TODO update the JSON string below
json = "{}"
# create an instance of HTTPDatasource from a JSON string
http_datasource_instance = HTTPDatasource.from_json(json)
# print the JSON string representation of the object
print(HTTPDatasource.to_json())

# convert the object into a dict
http_datasource_dict = http_datasource_instance.to_dict()
# create an instance of HTTPDatasource from a dict
http_datasource_form_dict = http_datasource.from_dict(http_datasource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


