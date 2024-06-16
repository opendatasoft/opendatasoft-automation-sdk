# coding: utf-8

"""
    Opendatasoft's Automation API Documentation

    Opendatasoft REST API to manage your portal and its catalog

    The version of the OpenAPI document: 1.0
    Contact: support@opendatasoft.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from opendatasoft_automation.models.dataset_metadata import DatasetMetadata

class TestDatasetMetadata(unittest.TestCase):
    """DatasetMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DatasetMetadata:
        """Test DatasetMetadata
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DatasetMetadata`
        """
        model = DatasetMetadata()
        if include_optional:
            return DatasetMetadata(
                default = {"title":{"value":"Counties -  United States of America","remote_value":"Counties -  United States of America","override_remote_value":false},"description":{"value":"This dataset is part of the Geographical repository maintained by Opendatasoft.  This dataset contains data for counties and equivalent entities in United States of America.","remote_value":"This dataset is part of the Geographical repository maintained by Opendatasoft.  This dataset contains data for counties and equivalent entities in United States of America.","override_remote_value":false},"keyword":{"value":["territory","geography","boundary","county","usa"],"remote_value":["territory","geography","boundary","county","usa"],"override_remote_value":false},"modified":{"value":"2023-01-01T00:00:00Z","remote_value":"2023-01-01T00:00:00Z","override_remote_value":false},"modified_updates_on_metadata_change":{"value":false,"remote_value":false,"override_remote_value":false},"modified_updates_on_data_change":{"value":false,"remote_value":false,"override_remote_value":false},"geographic_reference":{"value":["world_us"],"remote_value":["world_us"],"override_remote_value":false},"geographic_reference_auto":{"value":false,"remote_value":false,"override_remote_value":false},"language":{"value":"en","remote_value":"en","override_remote_value":false},"timezone":{"value":"US/Pacific","remote_value":"US/Pacific","override_remote_value":false},"publisher":{"value":"U.S. Department of Commerce, U.S. Census Bureau, Geography Division, Spatial Data Collection and Products Branch","remote_value":"U.S. Department of Commerce, U.S. Census Bureau, Geography Division, Spatial Data Collection and Products Branch","override_remote_value":false},"references":{"value":"https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html","remote_value":"https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html","override_remote_value":false},"attributions":{"value":["U.S. Census Bureau"],"remote_value":["U.S. Census Bureau"],"override_remote_value":false}},
                visualization = {},
                internal = {"license_id":{"value":"38js5ao","remote_value":"38js5ao","override_remote_value":false},"theme_id":{"value":["38js5ao"],"remote_value":["38js5ao"],"override_remote_value":false},"draft":{"value":false,"remote_value":false,"override_remote_value":false}},
                custom_template_name = {"field_name_1":{"value":"field_value_1"},"field_name_2":{"value":"field_value_2","override_remote_value":true}}
            )
        else:
            return DatasetMetadata(
                default = {"title":{"value":"Counties -  United States of America","remote_value":"Counties -  United States of America","override_remote_value":false},"description":{"value":"This dataset is part of the Geographical repository maintained by Opendatasoft.  This dataset contains data for counties and equivalent entities in United States of America.","remote_value":"This dataset is part of the Geographical repository maintained by Opendatasoft.  This dataset contains data for counties and equivalent entities in United States of America.","override_remote_value":false},"keyword":{"value":["territory","geography","boundary","county","usa"],"remote_value":["territory","geography","boundary","county","usa"],"override_remote_value":false},"modified":{"value":"2023-01-01T00:00:00Z","remote_value":"2023-01-01T00:00:00Z","override_remote_value":false},"modified_updates_on_metadata_change":{"value":false,"remote_value":false,"override_remote_value":false},"modified_updates_on_data_change":{"value":false,"remote_value":false,"override_remote_value":false},"geographic_reference":{"value":["world_us"],"remote_value":["world_us"],"override_remote_value":false},"geographic_reference_auto":{"value":false,"remote_value":false,"override_remote_value":false},"language":{"value":"en","remote_value":"en","override_remote_value":false},"timezone":{"value":"US/Pacific","remote_value":"US/Pacific","override_remote_value":false},"publisher":{"value":"U.S. Department of Commerce, U.S. Census Bureau, Geography Division, Spatial Data Collection and Products Branch","remote_value":"U.S. Department of Commerce, U.S. Census Bureau, Geography Division, Spatial Data Collection and Products Branch","override_remote_value":false},"references":{"value":"https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html","remote_value":"https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html","override_remote_value":false},"attributions":{"value":["U.S. Census Bureau"],"remote_value":["U.S. Census Bureau"],"override_remote_value":false}},
        )
        """

    def testDatasetMetadata(self):
        """Test DatasetMetadata"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
