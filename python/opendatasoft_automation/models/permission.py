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


class Permission(str, Enum):
    """
    A user or user group permission:  * `edit_domain` - Ability to edit the properties of the domain, including user and group management  * `create_page` - Ability to create new pages  * `edit_page` - Ability to edit all pages  * `manage_page` - Ability to change the security of any page editable by this user  * `explore_restricted_page` - Ability to browse any page, even the restricted ones  * `create_dataset` - Ability to create new datasets  * `edit_dataset` - Ability to edit all datasets  * `publish_dataset` - Ability to publish datasets editable by this user  * `manage_dataset` - Ability to change the security of datasets editable by this user  * `explore_restricted_dataset` - Ability to browse any dataset, even the restricted ones  * `edit_reuse` - Ability to edit and manage existing reuses  * `manage_subdomains` - Ability to create and manage subdomains  * `explore_monitoring` - Ability to browse any monitoring dataset and access the analytics section of the back-office  * `edit_theme` - Ability to manage the domain's theme (edit and make live)  * `edit_form` - Ability to create new forms, edit and publish all forms  * `submit_private_form` - Ability to see all the forms, even the restricted ones
    """

    """
    allowed enum values
    """
    EDIT_DOMAIN = 'edit_domain'
    CREATE_PAGE = 'create_page'
    EDIT_PAGE = 'edit_page'
    MANAGE_PAGE = 'manage_page'
    EXPLORE_RESTRICTED_PAGE = 'explore_restricted_page'
    CREATE_DATASET = 'create_dataset'
    EDIT_DATASET = 'edit_dataset'
    PUBLISH_DATASET = 'publish_dataset'
    MANAGE_DATASET = 'manage_dataset'
    EXPLORE_RESTRICTED_DATASET = 'explore_restricted_dataset'
    EDIT_REUSE = 'edit_reuse'
    MANAGE_SUBDOMAINS = 'manage_subdomains'
    EXPLORE_MONITORING = 'explore_monitoring'
    EDIT_THEME = 'edit_theme'
    EDIT_FORM = 'edit_form'
    SUBMIT_PRIVATE_FORM = 'submit_private_form'
    CREATE_EXTERNAL_ASSET = 'create_external_asset'
    EDIT_EXTERNAL_ASSET = 'edit_external_asset'
    EXPLORE_RESTRICTED_EXTERNAL_ASSET = 'explore_restricted_external_asset'
    MANAGE_GLOSSARY = 'manage_glossary'
    MANAGE_SHOWCASE_REQUESTS = 'manage_showcase_requests'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Permission from a JSON string"""
        return cls(json.loads(json_str))


