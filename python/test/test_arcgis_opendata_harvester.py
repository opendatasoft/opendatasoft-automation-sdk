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

from openapi_client.models.arcgis_opendata_harvester import ArcgisOpendataHarvester

class TestArcgisOpendataHarvester(unittest.TestCase):
    """ArcgisOpendataHarvester unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ArcgisOpendataHarvester:
        """Test ArcgisOpendataHarvester
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ArcgisOpendataHarvester`
        """
        model = ArcgisOpendataHarvester()
        if include_optional:
            return ArcgisOpendataHarvester(
                url = 'http://cassini.apur.opendata.arcgis.com/',
                compute_geo_area = True,
                fetch_data = True,
                download_resources = True,
                metadata_only = True
            )
        else:
            return ArcgisOpendataHarvester(
                url = 'http://cassini.apur.opendata.arcgis.com/',
        )
        """

    def testArcgisOpendataHarvester(self):
        """Test ArcgisOpendataHarvester"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
