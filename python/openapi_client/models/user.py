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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.explore_limits import ExploreLimits
from openapi_client.models.permission import Permission
from openapi_client.models.user_groups import UserGroups
from openapi_client.models.user_identity_providers_inner import UserIdentityProvidersInner
from typing import Optional, Set
from typing_extensions import Self

class User(BaseModel):
    """
    User
    """ # noqa: E501
    username: Optional[StrictStr] = Field(default=None, description="The user's username")
    display_name: Optional[StrictStr] = Field(default=None, description="Simplified version of the username")
    first_name: Optional[StrictStr] = Field(default=None, description="The user's first name")
    last_name: Optional[StrictStr] = Field(default=None, description="The user's last name")
    is_active: Optional[StrictBool] = Field(default=None, description="is `true` if the user can connect to their account")
    email: StrictStr = Field(description="The user's e-mail address")
    is_ods: Optional[StrictBool] = Field(default=None, description="is `true` if the user belongs to the Opendatasoft organization")
    account_type: Optional[StrictStr] = Field(default=None, description="The user's account type.")
    permissions: Optional[List[Permission]] = Field(default=None, description="A list of permissions granted to this user")
    joined_at: Optional[datetime] = Field(default=None, description="The date when the user joined the domain")
    last_seen_at: Optional[datetime] = Field(default=None, description="The date when the user used their account for the last time")
    last_login_at: Optional[datetime] = None
    expires_at: Optional[datetime] = None
    explore_limits: Optional[ExploreLimits] = None
    management_limits: Optional[Dict[str, Any]] = None
    gravatar_url: Optional[StrictStr] = None
    groups: Optional[UserGroups] = None
    identity_providers: Optional[List[UserIdentityProvidersInner]] = Field(default=None, description="The list of authentification providers type for this user.")
    __properties: ClassVar[List[str]] = ["username", "display_name", "first_name", "last_name", "is_active", "email", "is_ods", "account_type", "permissions", "joined_at", "last_seen_at", "last_login_at", "expires_at", "explore_limits", "management_limits", "gravatar_url", "groups", "identity_providers"]

    @field_validator('account_type')
    def account_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['global', 'linked', 'local']):
            raise ValueError("must be one of enum values ('global', 'linked', 'local')")
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
        """Create an instance of User from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "display_name",
            "is_active",
            "is_ods",
            "account_type",
            "joined_at",
            "last_seen_at",
            "last_login_at",
            "gravatar_url",
            "identity_providers",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of explore_limits
        if self.explore_limits:
            _dict['explore_limits'] = self.explore_limits.to_dict()
        # override the default output from pydantic by calling `to_dict()` of groups
        if self.groups:
            _dict['groups'] = self.groups.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in identity_providers (list)
        _items = []
        if self.identity_providers:
            for _item in self.identity_providers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['identity_providers'] = _items
        # set to None if expires_at (nullable) is None
        # and model_fields_set contains the field
        if self.expires_at is None and "expires_at" in self.model_fields_set:
            _dict['expires_at'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of User from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "username": obj.get("username"),
            "display_name": obj.get("display_name"),
            "first_name": obj.get("first_name"),
            "last_name": obj.get("last_name"),
            "is_active": obj.get("is_active"),
            "email": obj.get("email"),
            "is_ods": obj.get("is_ods"),
            "account_type": obj.get("account_type"),
            "permissions": obj.get("permissions"),
            "joined_at": obj.get("joined_at"),
            "last_seen_at": obj.get("last_seen_at"),
            "last_login_at": obj.get("last_login_at"),
            "expires_at": obj.get("expires_at"),
            "explore_limits": ExploreLimits.from_dict(obj["explore_limits"]) if obj.get("explore_limits") is not None else None,
            "management_limits": obj.get("management_limits"),
            "gravatar_url": obj.get("gravatar_url"),
            "groups": UserGroups.from_dict(obj["groups"]) if obj.get("groups") is not None else None,
            "identity_providers": [UserIdentityProvidersInner.from_dict(_item) for _item in obj["identity_providers"]] if obj.get("identity_providers") is not None else None
        })
        return _obj


