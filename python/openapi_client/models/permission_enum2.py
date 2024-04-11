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
from enum import Enum
from typing_extensions import Self


class PermissionEnum2(str, Enum):
    """
    A user or user group permission:  * `edit_page` - Ability to edit the page  * `manage_page` - Ability to change the security of the page
    """

    """
    allowed enum values
    """
    EDIT_PAGE = 'edit_page'
    MANAGE_PAGE = 'manage_page'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of PermissionEnum2 from a JSON string"""
        return cls(json.loads(json_str))

