# SnowflakeODBCDatasource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection** | [**SnowflakeODBCDatasourceAllOfConnection**](SnowflakeODBCDatasourceAllOfConnection.md) |  | [optional] 
**query** | **str** |  | [optional] 
**preview_query** | **str** |  | [optional] 
**incremental_query** | **str** |  | [optional] 
**incremental_field** | **str** |  | [optional] 

## Example

```python
from opendatasoft_automation.models.snowflake_odbc_datasource import SnowflakeODBCDatasource

# TODO update the JSON string below
json = "{}"
# create an instance of SnowflakeODBCDatasource from a JSON string
snowflake_odbc_datasource_instance = SnowflakeODBCDatasource.from_json(json)
# print the JSON string representation of the object
print(SnowflakeODBCDatasource.to_json())

# convert the object into a dict
snowflake_odbc_datasource_dict = snowflake_odbc_datasource_instance.to_dict()
# create an instance of SnowflakeODBCDatasource from a dict
snowflake_odbc_datasource_from_dict = SnowflakeODBCDatasource.from_dict(snowflake_odbc_datasource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


