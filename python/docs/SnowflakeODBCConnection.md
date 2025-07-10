# SnowflakeODBCConnection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**connection_string** | **str** | Your snowflake connection string | 

## Example

```python
from opendatasoft_automation.models.snowflake_odbc_connection import SnowflakeODBCConnection

# TODO update the JSON string below
json = "{}"
# create an instance of SnowflakeODBCConnection from a JSON string
snowflake_odbc_connection_instance = SnowflakeODBCConnection.from_json(json)
# print the JSON string representation of the object
print(SnowflakeODBCConnection.to_json())

# convert the object into a dict
snowflake_odbc_connection_dict = snowflake_odbc_connection_instance.to_dict()
# create an instance of SnowflakeODBCConnection from a dict
snowflake_odbc_connection_from_dict = SnowflakeODBCConnection.from_dict(snowflake_odbc_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


