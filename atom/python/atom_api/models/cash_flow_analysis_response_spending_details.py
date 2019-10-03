# coding: utf-8

"""
    Hydrogen Atom API

    The Hydrogen Atom API  # noqa: E501

    OpenAPI spec version: 1.0.1
    Contact: info@hydrogenplatform.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from atom_api.models.cash_flow_analysis_response_spending_details_by_category import CashFlowAnalysisResponseSpendingDetailsByCategory  # noqa: F401,E501
from atom_api.models.cash_flow_analysis_response_spending_details_by_merchant import CashFlowAnalysisResponseSpendingDetailsByMerchant  # noqa: F401,E501
from atom_api.models.specific_aggregation_account_transaction_response import SpecificAggregationAccountTransactionResponse  # noqa: F401,E501


class CashFlowAnalysisResponseSpendingDetails(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'by_category': 'list[CashFlowAnalysisResponseSpendingDetailsByCategory]',
        'by_merchant': 'list[CashFlowAnalysisResponseSpendingDetailsByMerchant]',
        'outliers': 'list[SpecificAggregationAccountTransactionResponse]'
    }

    attribute_map = {
        'by_category': 'by_category',
        'by_merchant': 'by_merchant',
        'outliers': 'outliers'
    }

    def __init__(self, by_category=None, by_merchant=None, outliers=None):  # noqa: E501
        """CashFlowAnalysisResponseSpendingDetails - a model defined in Swagger"""  # noqa: E501

        self._by_category = None
        self._by_merchant = None
        self._outliers = None
        self.discriminator = None

        if by_category is not None:
            self.by_category = by_category
        if by_merchant is not None:
            self.by_merchant = by_merchant
        if outliers is not None:
            self.outliers = outliers

    @property
    def by_category(self):
        """Gets the by_category of this CashFlowAnalysisResponseSpendingDetails.  # noqa: E501

        Breakdown of spending by category  # noqa: E501

        :return: The by_category of this CashFlowAnalysisResponseSpendingDetails.  # noqa: E501
        :rtype: list[CashFlowAnalysisResponseSpendingDetailsByCategory]
        """
        return self._by_category

    @by_category.setter
    def by_category(self, by_category):
        """Sets the by_category of this CashFlowAnalysisResponseSpendingDetails.

        Breakdown of spending by category  # noqa: E501

        :param by_category: The by_category of this CashFlowAnalysisResponseSpendingDetails.  # noqa: E501
        :type: list[CashFlowAnalysisResponseSpendingDetailsByCategory]
        """

        self._by_category = by_category

    @property
    def by_merchant(self):
        """Gets the by_merchant of this CashFlowAnalysisResponseSpendingDetails.  # noqa: E501

        Breakdown of spending by merchant  # noqa: E501

        :return: The by_merchant of this CashFlowAnalysisResponseSpendingDetails.  # noqa: E501
        :rtype: list[CashFlowAnalysisResponseSpendingDetailsByMerchant]
        """
        return self._by_merchant

    @by_merchant.setter
    def by_merchant(self, by_merchant):
        """Sets the by_merchant of this CashFlowAnalysisResponseSpendingDetails.

        Breakdown of spending by merchant  # noqa: E501

        :param by_merchant: The by_merchant of this CashFlowAnalysisResponseSpendingDetails.  # noqa: E501
        :type: list[CashFlowAnalysisResponseSpendingDetailsByMerchant]
        """

        self._by_merchant = by_merchant

    @property
    def outliers(self):
        """Gets the outliers of this CashFlowAnalysisResponseSpendingDetails.  # noqa: E501

        Outlying spending transactions  # noqa: E501

        :return: The outliers of this CashFlowAnalysisResponseSpendingDetails.  # noqa: E501
        :rtype: list[SpecificAggregationAccountTransactionResponse]
        """
        return self._outliers

    @outliers.setter
    def outliers(self, outliers):
        """Sets the outliers of this CashFlowAnalysisResponseSpendingDetails.

        Outlying spending transactions  # noqa: E501

        :param outliers: The outliers of this CashFlowAnalysisResponseSpendingDetails.  # noqa: E501
        :type: list[SpecificAggregationAccountTransactionResponse]
        """

        self._outliers = outliers

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(CashFlowAnalysisResponseSpendingDetails, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CashFlowAnalysisResponseSpendingDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other