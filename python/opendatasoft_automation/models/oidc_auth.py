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

from pydantic import BaseModel, ConfigDict, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class OIDCAuth(BaseModel):
    """
    OIDCAuth
    """ # noqa: E501
    client_id: StrictStr
    client_secret: StrictStr
    scope: StrictStr
    token_endpoint: StrictStr
    grant_type: StrictStr
    code: Optional[StrictStr] = None
    claims: Optional[Dict[str, Any]] = None
    __properties: ClassVar[List[str]] = ["client_id", "client_secret", "scope", "token_endpoint", "grant_type", "code", "claims"]

    @field_validator('grant_type')
    def grant_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['authorization_code']):
            raise ValueError("must be one of enum values ('authorization_code')")
        return value

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
        """Create an instance of OIDCAuth from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OIDCAuth from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "client_id": obj.get("client_id"),
            "client_secret": obj.get("client_secret"),
            "scope": obj.get("scope"),
            "token_endpoint": obj.get("token_endpoint"),
            "grant_type": obj.get("grant_type"),
            "code": obj.get("code"),
            "claims": obj.get("claims")
        })
        return _obj

