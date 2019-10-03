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

from atom_api.models.financial_picture_response_change_total_assets180_day import FinancialPictureResponseChangeTotalAssets180Day  # noqa: F401,E501
from atom_api.models.financial_picture_response_change_total_assets1_day import FinancialPictureResponseChangeTotalAssets1Day  # noqa: F401,E501
from atom_api.models.financial_picture_response_change_total_assets30_day import FinancialPictureResponseChangeTotalAssets30Day  # noqa: F401,E501
from atom_api.models.financial_picture_response_change_total_assets365_day import FinancialPictureResponseChangeTotalAssets365Day  # noqa: F401,E501
from atom_api.models.financial_picture_response_change_total_assets7_day import FinancialPictureResponseChangeTotalAssets7Day  # noqa: F401,E501
from atom_api.models.financial_picture_response_change_total_assets90_day import FinancialPictureResponseChangeTotalAssets90Day  # noqa: F401,E501
from atom_api.models.financial_picture_response_change_total_assets_total import FinancialPictureResponseChangeTotalAssetsTotal  # noqa: F401,E501


class FinancialPictureResponseChangeTotalAssets(object):
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
        '_1_day': 'FinancialPictureResponseChangeTotalAssets1Day',
        '_7_day': 'FinancialPictureResponseChangeTotalAssets7Day',
        '_30_day': 'FinancialPictureResponseChangeTotalAssets30Day',
        '_90_day': 'FinancialPictureResponseChangeTotalAssets90Day',
        '_180_day': 'FinancialPictureResponseChangeTotalAssets180Day',
        '_365_day': 'FinancialPictureResponseChangeTotalAssets365Day',
        'total': 'FinancialPictureResponseChangeTotalAssetsTotal'
    }

    attribute_map = {
        '_1_day': '1_day',
        '_7_day': '7_day',
        '_30_day': '30_day',
        '_90_day': '90_day',
        '_180_day': '180_day',
        '_365_day': '365_day',
        'total': 'total'
    }

    def __init__(self, _1_day=None, _7_day=None, _30_day=None, _90_day=None, _180_day=None, _365_day=None, total=None):  # noqa: E501
        """FinancialPictureResponseChangeTotalAssets - a model defined in Swagger"""  # noqa: E501

        self.__1_day = None
        self.__7_day = None
        self.__30_day = None
        self.__90_day = None
        self.__180_day = None
        self.__365_day = None
        self._total = None
        self.discriminator = None

        if _1_day is not None:
            self._1_day = _1_day
        if _7_day is not None:
            self._7_day = _7_day
        if _30_day is not None:
            self._30_day = _30_day
        if _90_day is not None:
            self._90_day = _90_day
        if _180_day is not None:
            self._180_day = _180_day
        if _365_day is not None:
            self._365_day = _365_day
        if total is not None:
            self.total = total

    @property
    def _1_day(self):
        """Gets the _1_day of this FinancialPictureResponseChangeTotalAssets.  # noqa: E501


        :return: The _1_day of this FinancialPictureResponseChangeTotalAssets.  # noqa: E501
        :rtype: FinancialPictureResponseChangeTotalAssets1Day
        """
        return self.__1_day

    @_1_day.setter
    def _1_day(self, _1_day):
        """Sets the _1_day of this FinancialPictureResponseChangeTotalAssets.


        :param _1_day: The _1_day of this FinancialPictureResponseChangeTotalAssets.  # noqa: E501
        :type: FinancialPictureResponseChangeTotalAssets1Day
        """

        self.__1_day = _1_day

    @property
    def _7_day(self):
        """Gets the _7_day of this FinancialPictureResponseChangeTotalAssets.  # noqa: E501


        :return: The _7_day of this FinancialPictureResponseChangeTotalAssets.  # noqa: E501
        :rtype: FinancialPictureResponseChangeTotalAssets7Day
        """
        return self.__7_day

    @_7_day.setter
    def _7_day(self, _7_day):
        """Sets the _7_day of this FinancialPictureResponseChangeTotalAssets.


        :param _7_day: The _7_day of this FinancialPictureResponseChangeTotalAssets.  # noqa: E501
        :type: FinancialPictureResponseChangeTotalAssets7Day
        """

        self.__7_day = _7_day

    @property
    def _30_day(self):
        """Gets the _30_day of this FinancialPictureResponseChangeTotalAssets.  # noqa: E501


        :return: The _30_day of this FinancialPictureResponseChangeTotalAssets.  # noqa: E501
        :rtype: FinancialPictureResponseChangeTotalAssets30Day
        """
        return self.__30_day

    @_30_day.setter
    def _30_day(self, _30_day):
        """Sets the _30_day of this FinancialPictureResponseChangeTotalAssets.


        :param _30_day: The _30_day of this FinancialPictureResponseChangeTotalAssets.  # noqa: E501
        :type: FinancialPictureResponseChangeTotalAssets30Day
        """

        self.__30_day = _30_day

    @property
    def _90_day(self):
        """Gets the _90_day of this FinancialPictureResponseChangeTotalAssets.  # noqa: E501


        :return: The _90_day of this FinancialPictureResponseChangeTotalAssets.  # noqa: E501
        :rtype: FinancialPictureResponseChangeTotalAssets90Day
        """
        return self.__90_day

    @_90_day.setter
    def _90_day(self, _90_day):
        """Sets the _90_day of this FinancialPictureResponseChangeTotalAssets.


        :param _90_day: The _90_day of this FinancialPictureResponseChangeTotalAssets.  # noqa: E501
        :type: FinancialPictureResponseChangeTotalAssets90Day
        """

        self.__90_day = _90_day

    @property
    def _180_day(self):
        """Gets the _180_day of this FinancialPictureResponseChangeTotalAssets.  # noqa: E501


        :return: The _180_day of this FinancialPictureResponseChangeTotalAssets.  # noqa: E501
        :rtype: FinancialPictureResponseChangeTotalAssets180Day
        """
        return self.__180_day

    @_180_day.setter
    def _180_day(self, _180_day):
        """Sets the _180_day of this FinancialPictureResponseChangeTotalAssets.


        :param _180_day: The _180_day of this FinancialPictureResponseChangeTotalAssets.  # noqa: E501
        :type: FinancialPictureResponseChangeTotalAssets180Day
        """

        self.__180_day = _180_day

    @property
    def _365_day(self):
        """Gets the _365_day of this FinancialPictureResponseChangeTotalAssets.  # noqa: E501


        :return: The _365_day of this FinancialPictureResponseChangeTotalAssets.  # noqa: E501
        :rtype: FinancialPictureResponseChangeTotalAssets365Day
        """
        return self.__365_day

    @_365_day.setter
    def _365_day(self, _365_day):
        """Sets the _365_day of this FinancialPictureResponseChangeTotalAssets.


        :param _365_day: The _365_day of this FinancialPictureResponseChangeTotalAssets.  # noqa: E501
        :type: FinancialPictureResponseChangeTotalAssets365Day
        """

        self.__365_day = _365_day

    @property
    def total(self):
        """Gets the total of this FinancialPictureResponseChangeTotalAssets.  # noqa: E501


        :return: The total of this FinancialPictureResponseChangeTotalAssets.  # noqa: E501
        :rtype: FinancialPictureResponseChangeTotalAssetsTotal
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this FinancialPictureResponseChangeTotalAssets.


        :param total: The total of this FinancialPictureResponseChangeTotalAssets.  # noqa: E501
        :type: FinancialPictureResponseChangeTotalAssetsTotal
        """

        self._total = total

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
        if issubclass(FinancialPictureResponseChangeTotalAssets, dict):
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
        if not isinstance(other, FinancialPictureResponseChangeTotalAssets):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other