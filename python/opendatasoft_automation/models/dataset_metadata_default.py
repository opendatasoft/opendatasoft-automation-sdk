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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from opendatasoft_automation.models.dataset_metadata_value import DatasetMetadataValue
from typing import Optional, Set
from typing_extensions import Self

class DatasetMetadataDefault(BaseModel):
    """
    The standard set of metadata common to all Opendatasoft datasets.
    """ # noqa: E501
    title: Optional[DatasetMetadataValue] = None
    description: Optional[DatasetMetadataValue] = None
    keyword: Optional[DatasetMetadataValue] = None
    modified: Optional[DatasetMetadataValue] = None
    modified_updates_on_metadata_change: Optional[DatasetMetadataValue] = None
    modified_updates_on_data_change: Optional[DatasetMetadataValue] = None
    geographic_reference: Optional[DatasetMetadataValue] = None
    geographic_reference_auto: Optional[DatasetMetadataValue] = None
    language: Optional[DatasetMetadataValue] = None
    timezone: Optional[DatasetMetadataValue] = None
    publisher: Optional[DatasetMetadataValue] = None
    references: Optional[DatasetMetadataValue] = None
    attributions: Optional[DatasetMetadataValue] = None
    __properties: ClassVar[List[str]] = ["title", "description", "keyword", "modified", "modified_updates_on_metadata_change", "modified_updates_on_data_change", "geographic_reference", "geographic_reference_auto", "language", "timezone", "publisher", "references", "attributions"]

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
        """Create an instance of DatasetMetadataDefault from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of title
        if self.title:
            _dict['title'] = self.title.to_dict()
        # override the default output from pydantic by calling `to_dict()` of description
        if self.description:
            _dict['description'] = self.description.to_dict()
        # override the default output from pydantic by calling `to_dict()` of keyword
        if self.keyword:
            _dict['keyword'] = self.keyword.to_dict()
        # override the default output from pydantic by calling `to_dict()` of modified
        if self.modified:
            _dict['modified'] = self.modified.to_dict()
        # override the default output from pydantic by calling `to_dict()` of modified_updates_on_metadata_change
        if self.modified_updates_on_metadata_change:
            _dict['modified_updates_on_metadata_change'] = self.modified_updates_on_metadata_change.to_dict()
        # override the default output from pydantic by calling `to_dict()` of modified_updates_on_data_change
        if self.modified_updates_on_data_change:
            _dict['modified_updates_on_data_change'] = self.modified_updates_on_data_change.to_dict()
        # override the default output from pydantic by calling `to_dict()` of geographic_reference
        if self.geographic_reference:
            _dict['geographic_reference'] = self.geographic_reference.to_dict()
        # override the default output from pydantic by calling `to_dict()` of geographic_reference_auto
        if self.geographic_reference_auto:
            _dict['geographic_reference_auto'] = self.geographic_reference_auto.to_dict()
        # override the default output from pydantic by calling `to_dict()` of language
        if self.language:
            _dict['language'] = self.language.to_dict()
        # override the default output from pydantic by calling `to_dict()` of timezone
        if self.timezone:
            _dict['timezone'] = self.timezone.to_dict()
        # override the default output from pydantic by calling `to_dict()` of publisher
        if self.publisher:
            _dict['publisher'] = self.publisher.to_dict()
        # override the default output from pydantic by calling `to_dict()` of references
        if self.references:
            _dict['references'] = self.references.to_dict()
        # override the default output from pydantic by calling `to_dict()` of attributions
        if self.attributions:
            _dict['attributions'] = self.attributions.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DatasetMetadataDefault from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "title": DatasetMetadataValue.from_dict(obj["title"]) if obj.get("title") is not None else None,
            "description": DatasetMetadataValue.from_dict(obj["description"]) if obj.get("description") is not None else None,
            "keyword": DatasetMetadataValue.from_dict(obj["keyword"]) if obj.get("keyword") is not None else None,
            "modified": DatasetMetadataValue.from_dict(obj["modified"]) if obj.get("modified") is not None else None,
            "modified_updates_on_metadata_change": DatasetMetadataValue.from_dict(obj["modified_updates_on_metadata_change"]) if obj.get("modified_updates_on_metadata_change") is not None else None,
            "modified_updates_on_data_change": DatasetMetadataValue.from_dict(obj["modified_updates_on_data_change"]) if obj.get("modified_updates_on_data_change") is not None else None,
            "geographic_reference": DatasetMetadataValue.from_dict(obj["geographic_reference"]) if obj.get("geographic_reference") is not None else None,
            "geographic_reference_auto": DatasetMetadataValue.from_dict(obj["geographic_reference_auto"]) if obj.get("geographic_reference_auto") is not None else None,
            "language": DatasetMetadataValue.from_dict(obj["language"]) if obj.get("language") is not None else None,
            "timezone": DatasetMetadataValue.from_dict(obj["timezone"]) if obj.get("timezone") is not None else None,
            "publisher": DatasetMetadataValue.from_dict(obj["publisher"]) if obj.get("publisher") is not None else None,
            "references": DatasetMetadataValue.from_dict(obj["references"]) if obj.get("references") is not None else None,
            "attributions": DatasetMetadataValue.from_dict(obj["attributions"]) if obj.get("attributions") is not None else None
        })
        return _obj


