# coding: utf-8

"""
    Molecule API Documentation

    The Hydrogen Molecule API  # noqa: E501

    OpenAPI spec version: 1.3.0
    Contact: info@hydrogenplatform.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import molecule_api
from molecule_api.api.token_supply_api import TokenSupplyApi  # noqa: E501
from molecule_api.rest import ApiException


class TestTokenSupplyApi(unittest.TestCase):
    """TokenSupplyApi unit test stubs"""

    def setUp(self):
        self.api = molecule_api.api.token_supply_api.TokenSupplyApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_token_supply_all_using_get(self):
        """Test case for get_token_supply_all_using_get

        Fetch Token Supply record list  # noqa: E501
        """
        pass

    def test_get_token_supply_using_get(self):
        """Test case for get_token_supply_using_get

        Fetch Token Supply details  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
