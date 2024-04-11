# coding: utf-8

# flake8: noqa

"""
    Opendatasoft's Automation API Documentation

    Opendatasoft REST API to manage your portal and its catalog

    The version of the OpenAPI document: 1.0
    Contact: support@opendatasoft.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from openapi_client.api.api_keys_api import APIKeysApi
from openapi_client.api.assets_api import AssetsApi
from openapi_client.api.code_editor_pages_api import CodeEditorPagesApi
from openapi_client.api.code_editor_pages_security_api import CodeEditorPagesSecurityApi
from openapi_client.api.dataset_alternative_exports_api import DatasetAlternativeExportsApi
from openapi_client.api.dataset_attachments_api import DatasetAttachmentsApi
from openapi_client.api.dataset_feedbacks_api import DatasetFeedbacksApi
from openapi_client.api.dataset_fields_api import DatasetFieldsApi
from openapi_client.api.dataset_metadata_api import DatasetMetadataApi
from openapi_client.api.dataset_processors_api import DatasetProcessorsApi
from openapi_client.api.dataset_resources_api import DatasetResourcesApi
from openapi_client.api.dataset_schedules_api import DatasetSchedulesApi
from openapi_client.api.dataset_security_api import DatasetSecurityApi
from openapi_client.api.dataset_versions_api import DatasetVersionsApi
from openapi_client.api.datasets_api import DatasetsApi
from openapi_client.api.datasource_connection_security_api import DatasourceConnectionSecurityApi
from openapi_client.api.datasources_connections_api import DatasourcesConnectionsApi
from openapi_client.api.harvester_schedules_api import HarvesterSchedulesApi
from openapi_client.api.harvesters_api import HarvestersApi
from openapi_client.api.metadata_templates_api import MetadataTemplatesApi
from openapi_client.api.studio_pages_api import StudioPagesApi
from openapi_client.api.studio_pages_security_api import StudioPagesSecurityApi
from openapi_client.api.user_groups_api import UserGroupsApi
from openapi_client.api.users_api import UsersApi

# import ApiClient
from openapi_client.api_response import ApiResponse
from openapi_client.api_client import ApiClient
from openapi_client.configuration import Configuration
from openapi_client.exceptions import OpenApiException
from openapi_client.exceptions import ApiTypeError
from openapi_client.exceptions import ApiValueError
from openapi_client.exceptions import ApiKeyError
from openapi_client.exceptions import ApiAttributeError
from openapi_client.exceptions import ApiException

# import models into sdk package
from openapi_client.models.api_key import APIKey
from openapi_client.models.api_key_revocation_status import APIKeyRevocationStatus
from openapi_client.models.awsiam_role_auth import AWSIAMRoleAuth
from openapi_client.models.aws_signature_v4_auth import AWSSignatureV4Auth
from openapi_client.models.abort_harvester400_response import AbortHarvester400Response
from openapi_client.models.amazon_s3_awsiam_role_auth import AmazonS3AWSIAMRoleAuth
from openapi_client.models.amazon_s3_aws_signature_v4_auth import AmazonS3AWSSignatureV4Auth
from openapi_client.models.amazon_s3_auth import AmazonS3Auth
from openapi_client.models.amazon_s3_connection import AmazonS3Connection
from openapi_client.models.amazon_s3_datasource import AmazonS3Datasource
from openapi_client.models.amazon_s3_datasource_all_of_connection import AmazonS3DatasourceAllOfConnection
from openapi_client.models.annotate_dataset_field_configuration import AnnotateDatasetFieldConfiguration
from openapi_client.models.annotate_dataset_field_configuration1_args import AnnotateDatasetFieldConfiguration1Args
from openapi_client.models.arcgis_harvester import ArcgisHarvester
from openapi_client.models.arcgis_opendata_harvester import ArcgisOpendataHarvester
from openapi_client.models.azure_blob_storage_auth import AzureBlobStorageAuth
from openapi_client.models.azure_blob_storage_connection import AzureBlobStorageConnection
from openapi_client.models.azure_blob_storage_datasource import AzureBlobStorageDatasource
from openapi_client.models.azure_blob_storage_datasource_all_of_connection import AzureBlobStorageDatasourceAllOfConnection
from openapi_client.models.azure_blob_storage_shared_key_auth import AzureBlobStorageSharedKeyAuth
from openapi_client.models.base_metadata_template import BaseMetadataTemplate
from openapi_client.models.basic_auth import BasicAuth
from openapi_client.models.ckan_harvester import CKANHarvester
from openapi_client.models.csw_harvester import CSWHarvester
from openapi_client.models.code_editor_page import CodeEditorPage
from openapi_client.models.code_editor_page_content import CodeEditorPageContent
from openapi_client.models.connection import Connection
from openapi_client.models.creatable_or_editable_metadata_template import CreatableOrEditableMetadataTemplate
from openapi_client.models.create_dataset400_response import CreateDataset400Response
from openapi_client.models.datagouv_harvester import DatagouvHarvester
from openapi_client.models.datajson_harvester import DatajsonHarvester
from openapi_client.models.dataset import Dataset
from openapi_client.models.dataset_alternative_export import DatasetAlternativeExport
from openapi_client.models.dataset_attachment import DatasetAttachment
from openapi_client.models.dataset_feedback import DatasetFeedback
from openapi_client.models.dataset_feedback_values import DatasetFeedbackValues
from openapi_client.models.dataset_field_configuration import DatasetFieldConfiguration
from openapi_client.models.dataset_file import DatasetFile
from openapi_client.models.dataset_group_security import DatasetGroupSecurity
from openapi_client.models.dataset_group_security_group import DatasetGroupSecurityGroup
from openapi_client.models.dataset_metadata import DatasetMetadata
from openapi_client.models.dataset_metadata_default import DatasetMetadataDefault
from openapi_client.models.dataset_metadata_internal import DatasetMetadataInternal
from openapi_client.models.dataset_metadata_template import DatasetMetadataTemplate
from openapi_client.models.dataset_metadata_value import DatasetMetadataValue
from openapi_client.models.dataset_metadata_visualization import DatasetMetadataVisualization
from openapi_client.models.dataset_processor import DatasetProcessor
from openapi_client.models.dataset_schedule import DatasetSchedule
from openapi_client.models.dataset_security import DatasetSecurity
from openapi_client.models.dataset_security_api_calls_quota import DatasetSecurityApiCallsQuota
from openapi_client.models.dataset_user_security import DatasetUserSecurity
from openapi_client.models.dataset_version import DatasetVersion
from openapi_client.models.datasource import Datasource
from openapi_client.models.delete_dataset_field_configuration import DeleteDatasetFieldConfiguration
from openapi_client.models.description_dataset_field_configuration import DescriptionDatasetFieldConfiguration
from openapi_client.models.explore_limits import ExploreLimits
from openapi_client.models.explore_limits_api_calls import ExploreLimitsApiCalls
from openapi_client.models.extractor import Extractor
from openapi_client.models.extractor_parameters_inner import ExtractorParametersInner
from openapi_client.models.ftp_auth import FTPAuth
from openapi_client.models.ftp_basic_auth import FTPBasicAuth
from openapi_client.models.ftpcsv_harvester import FTPCSVHarvester
from openapi_client.models.ftp_connection import FTPConnection
from openapi_client.models.ftp_datasource import FTPDatasource
from openapi_client.models.ftp_datasource1_connection import FTPDatasource1Connection
from openapi_client.models.ftp_harvester import FTPHarvester
from openapi_client.models.ftp_with_meta_csv_harvester import FTPWithMetaCSVHarvester
from openapi_client.models.federated_dataset import FederatedDataset
from openapi_client.models.federated_datasource import FederatedDatasource
from openapi_client.models.federated_datasource_all_of_dataset import FederatedDatasourceAllOfDataset
from openapi_client.models.federated_datasource_all_of_dataset_one_of import FederatedDatasourceAllOfDatasetOneOf
from openapi_client.models.federated_datasource_all_of_domain import FederatedDatasourceAllOfDomain
from openapi_client.models.get_apikeys200_response import GetApikeys200Response
from openapi_client.models.get_dataset_status200_response import GetDatasetStatus200Response
from openapi_client.models.get_dataset_status200_response_records_errors_inner import GetDatasetStatus200ResponseRecordsErrorsInner
from openapi_client.models.get_metadata_fields_list200_response import GetMetadataFieldsList200Response
from openapi_client.models.get_users200_response import GetUsers200Response
from openapi_client.models.google_drive_auth import GoogleDriveAuth
from openapi_client.models.google_drive_connection import GoogleDriveConnection
from openapi_client.models.google_drive_datasource import GoogleDriveDatasource
from openapi_client.models.google_drive_datasource_all_of_connection import GoogleDriveDatasourceAllOfConnection
from openapi_client.models.google_drive_oidc_auth import GoogleDriveOIDCAuth
from openapi_client.models.group_security import GroupSecurity
from openapi_client.models.group_security2 import GroupSecurity2
from openapi_client.models.group_security3 import GroupSecurity3
from openapi_client.models.group_security_group import GroupSecurityGroup
from openapi_client.models.guess_unsaved_resource_extractor_params200_response import GuessUnsavedResourceExtractorParams200Response
from openapi_client.models.guess_unsaved_resource_extractor_params_request import GuessUnsavedResourceExtractorParamsRequest
from openapi_client.models.guess_unsaved_resource_extractors_request import GuessUnsavedResourceExtractorsRequest
from openapi_client.models.http_auth import HTTPAuth
from openapi_client.models.http_basic_auth import HTTPBasicAuth
from openapi_client.models.http_connection import HTTPConnection
from openapi_client.models.http_connection_all_of_headers import HTTPConnectionAllOfHeaders
from openapi_client.models.http_datasource import HTTPDatasource
from openapi_client.models.http_datasource1_connection import HTTPDatasource1Connection
from openapi_client.models.http_datasource1_connection_one_of import HTTPDatasource1ConnectionOneOf
from openapi_client.models.http_datasource1_headers import HTTPDatasource1Headers
from openapi_client.models.httpo_auth2_auth import HTTPOAuth2Auth
from openapi_client.models.httpoidc_auth import HTTPOIDCAuth
from openapi_client.models.harvester import Harvester
from openapi_client.models.harvester_list_errors200_response import HarvesterListErrors200Response
from openapi_client.models.harvester_preview_result import HarvesterPreviewResult
from openapi_client.models.harvester_preview_result_results_inner import HarvesterPreviewResultResultsInner
from openapi_client.models.harvester_schedule import HarvesterSchedule
from openapi_client.models.invite_users200_response_value import InviteUsers200ResponseValue
from openapi_client.models.junar_harvester import JunarHarvester
from openapi_client.models.list_code_editor_page_group_security200_response import ListCodeEditorPageGroupSecurity200Response
from openapi_client.models.list_code_editor_page_user_security200_response import ListCodeEditorPageUserSecurity200Response
from openapi_client.models.list_code_editor_pages200_response import ListCodeEditorPages200Response
from openapi_client.models.list_connections200_response import ListConnections200Response
from openapi_client.models.list_dataset_alternative_exports200_response import ListDatasetAlternativeExports200Response
from openapi_client.models.list_dataset_attachments200_response import ListDatasetAttachments200Response
from openapi_client.models.list_dataset_feedbacks200_response import ListDatasetFeedbacks200Response
from openapi_client.models.list_dataset_field_configurations200_response import ListDatasetFieldConfigurations200Response
from openapi_client.models.list_dataset_group_security200_response import ListDatasetGroupSecurity200Response
from openapi_client.models.list_dataset_processors200_response import ListDatasetProcessors200Response
from openapi_client.models.list_dataset_resources200_response import ListDatasetResources200Response
from openapi_client.models.list_dataset_schedules200_response import ListDatasetSchedules200Response
from openapi_client.models.list_dataset_user_security200_response import ListDatasetUserSecurity200Response
from openapi_client.models.list_dataset_versions200_response import ListDatasetVersions200Response
from openapi_client.models.list_datasets200_response import ListDatasets200Response
from openapi_client.models.list_datasets_default_response import ListDatasetsDefaultResponse
from openapi_client.models.list_datasource_connection_group_security200_response import ListDatasourceConnectionGroupSecurity200Response
from openapi_client.models.list_datasource_connection_user_security200_response import ListDatasourceConnectionUserSecurity200Response
from openapi_client.models.list_harvester_schedules200_response import ListHarvesterSchedules200Response
from openapi_client.models.list_harvesters200_response import ListHarvesters200Response
from openapi_client.models.list_images200_response import ListImages200Response
from openapi_client.models.list_images200_response_all_of_results_inner import ListImages200ResponseAllOfResultsInner
from openapi_client.models.list_metadata_templates200_response import ListMetadataTemplates200Response
from openapi_client.models.list_studio_page_group_security200_response import ListStudioPageGroupSecurity200Response
from openapi_client.models.list_studio_page_user_security200_response import ListStudioPageUserSecurity200Response
from openapi_client.models.list_studio_pages200_response import ListStudioPages200Response
from openapi_client.models.list_user_groups200_response import ListUserGroups200Response
from openapi_client.models.metadata_template import MetadataTemplate
from openapi_client.models.metadata_template_field import MetadataTemplateField
from openapi_client.models.metadata_template_field_suggestions import MetadataTemplateFieldSuggestions
from openapi_client.models.metadata_template_field_suggestions_exhaustive import MetadataTemplateFieldSuggestionsExhaustive
from openapi_client.models.o_auth2_auth import OAuth2Auth
from openapi_client.models.odsoidc_auth import ODSOIDCAuth
from openapi_client.models.oidc_auth import OIDCAuth
from openapi_client.models.omi_node_harvester import OMINodeHarvester
from openapi_client.models.opendatasoft_harvester import OpendatasoftHarvester
from openapi_client.models.order_dataset_field_configuration import OrderDatasetFieldConfiguration
from openapi_client.models.paginated_results import PaginatedResults
from openapi_client.models.permission import Permission
from openapi_client.models.permission_enum import PermissionEnum
from openapi_client.models.permission_enum2 import PermissionEnum2
from openapi_client.models.permission_enum3 import PermissionEnum3
from openapi_client.models.post_apikeys_apikey_uid_revoke_request import PostApikeysApikeyUidRevokeRequest
from openapi_client.models.provision_users_request import ProvisionUsersRequest
from openapi_client.models.provision_users_request_all_of_identity_provider import ProvisionUsersRequestAllOfIdentityProvider
from openapi_client.models.publish_dataset200_response import PublishDataset200Response
from openapi_client.models.publish_dataset400_response import PublishDataset400Response
from openapi_client.models.quandl_harvester import QuandlHarvester
from openapi_client.models.related_user import RelatedUser
from openapi_client.models.related_user_read_only import RelatedUserReadOnly
from openapi_client.models.rename_dataset_field_configuration import RenameDatasetFieldConfiguration
from openapi_client.models.resource import Resource
from openapi_client.models.resource_guess_extractor_params200_response import ResourceGuessExtractorParams200Response
from openapi_client.models.resource_unsaved_preview200_response import ResourceUnsavedPreview200Response
from openapi_client.models.resource_unsaved_preview200_response_fields_inner import ResourceUnsavedPreview200ResponseFieldsInner
from openapi_client.models.resource_unsaved_preview200_response_fields_inner_annotations_inner import ResourceUnsavedPreview200ResponseFieldsInnerAnnotationsInner
from openapi_client.models.resource_unsaved_preview_request import ResourceUnsavedPreviewRequest
from openapi_client.models.search_apikey200_response import SearchApikey200Response
from openapi_client.models.search_apikey_request import SearchApikeyRequest
from openapi_client.models.sharepoint_auth import SharepointAuth
from openapi_client.models.sharepoint_connection import SharepointConnection
from openapi_client.models.sharepoint_datasource import SharepointDatasource
from openapi_client.models.sharepoint_datasource1_connection import SharepointDatasource1Connection
from openapi_client.models.sharepoint_oidc_auth import SharepointOIDCAuth
from openapi_client.models.socrata_harvester import SocrataHarvester
from openapi_client.models.studio_page import StudioPage
from openapi_client.models.studio_page_contents_inner import StudioPageContentsInner
from openapi_client.models.type_dataset_field_configuration import TypeDatasetFieldConfiguration
from openapi_client.models.url_dataset_alternative_export import URLDatasetAlternativeExport
from openapi_client.models.update_dataset404_response import UpdateDataset404Response
from openapi_client.models.update_dataset_alternative_export_request import UpdateDatasetAlternativeExportRequest
from openapi_client.models.uploaded_file_dataset_alternative_export import UploadedFileDatasetAlternativeExport
from openapi_client.models.uploaded_file_datasource import UploadedFileDatasource
from openapi_client.models.uploaded_file_datasource1_file import UploadedFileDatasource1File
from openapi_client.models.uploaded_file_datasource1_file_one_of import UploadedFileDatasource1FileOneOf
from openapi_client.models.user import User
from openapi_client.models.user_group import UserGroup
from openapi_client.models.user_groups import UserGroups
from openapi_client.models.user_groups_one_of_inner import UserGroupsOneOfInner
from openapi_client.models.user_identity_providers_inner import UserIdentityProvidersInner
from openapi_client.models.user_security import UserSecurity
from openapi_client.models.user_security2 import UserSecurity2
from openapi_client.models.user_security3 import UserSecurity3
from openapi_client.models.wfs_harvester import WFSHarvester