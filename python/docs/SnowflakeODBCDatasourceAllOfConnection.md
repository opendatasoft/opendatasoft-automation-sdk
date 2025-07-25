# SnowflakeODBCDatasourceAllOfConnection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**connection_string** | **str** | Your snowflake connection string | 
**uid** | **str** | The UID of an existing connection to reuse. | 

## Example

```python
from opendatasoft_automation.models.snowflake_odbc_datasource_all_of_connection import SnowflakeODBCDatasourceAllOfConnection

# TODO update the JSON string below
json = "{}"
# create an instance of SnowflakeODBCDatasourceAllOfConnection from a JSON string
snowflake_odbc_datasource_all_of_connection_instance = SnowflakeODBCDatasourceAllOfConnection.from_json(json)
# print the JSON string representation of the object
print(SnowflakeODBCDatasourceAllOfConnection.to_json())

# convert the object into a dict
snowflake_odbc_datasource_all_of_connection_dict = snowflake_odbc_datasource_all_of_connection_instance.to_dict()
# create an instance of SnowflakeODBCDatasourceAllOfConnection from a dict
snowflake_odbc_datasource_all_of_connection_from_dict = SnowflakeODBCDatasourceAllOfConnection.from_dict(snowflake_odbc_datasource_all_of_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


