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
import pprint
import re  # noqa: F401
import json

from pydantic import ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_client.models.connection import Connection
from openapi_client.models.http_auth import HTTPAuth
from openapi_client.models.http_connection_all_of_headers import HTTPConnectionAllOfHeaders
from typing import Optional, Set
from typing_extensions import Self

class HTTPConnection(Connection):
    """
    HTTPConnection
    """ # noqa: E501
    url: Annotated[str, Field(min_length=1, strict=True)]
    headers: Optional[List[HTTPConnectionAllOfHeaders]] = None
    auth: Optional[HTTPAuth] = None
    __properties: ClassVar[List[str]] = ["uid", "type", "is_reusable", "can_reuse", "can_manage", "dataset_count", "user_count", "group_count", "created_at", "updated_at", "url", "headers", "auth"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of HTTPConnection from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in headers (list)
        _items = []
        if self.headers:
            for _item in self.headers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['headers'] = _items
        # override the default output from pydantic by calling `to_dict()` of auth
        if self.auth:
            _dict['auth'] = self.auth.to_dict()
        # set to None if auth (nullable) is None
        # and model_fields_set contains the field
        if self.auth is None and "auth" in self.model_fields_set:
            _dict['auth'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HTTPConnection from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "uid": obj.get("uid"),
            "type": obj.get("type"),
            "is_reusable": obj.get("is_reusable"),
            "can_reuse": obj.get("can_reuse"),
            "can_manage": obj.get("can_manage"),
            "dataset_count": obj.get("dataset_count"),
            "user_count": obj.get("user_count"),
            "group_count": obj.get("group_count"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "url": obj.get("url"),
            "headers": [HTTPConnectionAllOfHeaders.from_dict(_item) for _item in obj["headers"]] if obj.get("headers") is not None else None,
            "auth": HTTPAuth.from_dict(obj["auth"]) if obj.get("auth") is not None else None
        })
        return _obj


