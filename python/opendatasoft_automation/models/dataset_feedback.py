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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from opendatasoft_automation.models.dataset_feedback_values import DatasetFeedbackValues
from opendatasoft_automation.models.related_user import RelatedUser
from typing import Optional, Set
from typing_extensions import Self

class DatasetFeedback(BaseModel):
    """
    A feedback made on a dataset
    """ # noqa: E501
    uid: StrictStr = Field(description="Unique identifier for the feedback")
    record_id: StrictStr = Field(description="ID of the record on which the feedback was made")
    user: RelatedUser
    comment: StrictStr = Field(description="User comments")
    values: Optional[DatasetFeedbackValues] = None
    is_archived: Optional[StrictBool] = Field(default=None, description="True if the feedback was archived by an administrator, False otherwise")
    created_at: Optional[datetime] = Field(default=None, description="Timestamp at which the feedback was submitted")
    __properties: ClassVar[List[str]] = ["uid", "record_id", "user", "comment", "values", "is_archived", "created_at"]

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
        """Create an instance of DatasetFeedback from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "uid",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of values
        if self.values:
            _dict['values'] = self.values.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DatasetFeedback from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "uid": obj.get("uid"),
            "record_id": obj.get("record_id"),
            "user": RelatedUser.from_dict(obj["user"]) if obj.get("user") is not None else None,
            "comment": obj.get("comment"),
            "values": DatasetFeedbackValues.from_dict(obj["values"]) if obj.get("values") is not None else None,
            "is_archived": obj.get("is_archived"),
            "created_at": obj.get("created_at")
        })
        return _obj


