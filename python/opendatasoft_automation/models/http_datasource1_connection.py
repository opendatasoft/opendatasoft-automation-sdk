# coding: utf-8

"""
    Opendatasoft's Automation API Documentation

    Opendatasoft REST API to manage your portal and its catalog

    The version of the OpenAPI document: 1.0
    Contact: support@opendatasoft.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from opendatasoft_automation.models.http_connection import HTTPConnection
from opendatasoft_automation.models.http_datasource1_connection_one_of import HTTPDatasource1ConnectionOneOf
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

HTTPDATASOURCE1CONNECTION_ONE_OF_SCHEMAS = ["HTTPConnection", "HTTPDatasource1ConnectionOneOf"]

class HTTPDatasource1Connection(BaseModel):
    """
    HTTPDatasource1Connection
    """
    # data type: HTTPDatasource1ConnectionOneOf
    oneof_schema_1_validator: Optional[HTTPDatasource1ConnectionOneOf] = None
    # data type: HTTPConnection
    oneof_schema_2_validator: Optional[HTTPConnection] = None
    actual_instance: Optional[Union[HTTPConnection, HTTPDatasource1ConnectionOneOf]] = None
    one_of_schemas: Set[str] = { "HTTPConnection", "HTTPDatasource1ConnectionOneOf" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = HTTPDatasource1Connection.model_construct()
        error_messages = []
        match = 0
        # validate data type: HTTPDatasource1ConnectionOneOf
        if not isinstance(v, HTTPDatasource1ConnectionOneOf):
            error_messages.append(f"Error! Input type `{type(v)}` is not `HTTPDatasource1ConnectionOneOf`")
        else:
            match += 1
        # validate data type: HTTPConnection
        if not isinstance(v, HTTPConnection):
            error_messages.append(f"Error! Input type `{type(v)}` is not `HTTPConnection`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in HTTPDatasource1Connection with oneOf schemas: HTTPConnection, HTTPDatasource1ConnectionOneOf. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in HTTPDatasource1Connection with oneOf schemas: HTTPConnection, HTTPDatasource1ConnectionOneOf. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into HTTPDatasource1ConnectionOneOf
        try:
            instance.actual_instance = HTTPDatasource1ConnectionOneOf.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into HTTPConnection
        try:
            instance.actual_instance = HTTPConnection.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into HTTPDatasource1Connection with oneOf schemas: HTTPConnection, HTTPDatasource1ConnectionOneOf. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into HTTPDatasource1Connection with oneOf schemas: HTTPConnection, HTTPDatasource1ConnectionOneOf. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], HTTPConnection, HTTPDatasource1ConnectionOneOf]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


