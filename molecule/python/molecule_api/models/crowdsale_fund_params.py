# coding: utf-8

"""
    Molecule API Documentation

    The Hydrogen Molecule API  # noqa: E501

    OpenAPI spec version: 1.3.0
    Contact: info@hydrogenplatform.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CrowdsaleFundParams(object):
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
        'token_id': 'str',
        'supply': 'str'
    }

    attribute_map = {
        'token_id': 'token_id',
        'supply': 'supply'
    }

    def __init__(self, token_id=None, supply=None):  # noqa: E501
        """CrowdsaleFundParams - a model defined in Swagger"""  # noqa: E501

        self._token_id = None
        self._supply = None
        self.discriminator = None

        self.token_id = token_id
        self.supply = supply

    @property
    def token_id(self):
        """Gets the token_id of this CrowdsaleFundParams.  # noqa: E501


        :return: The token_id of this CrowdsaleFundParams.  # noqa: E501
        :rtype: str
        """
        return self._token_id

    @token_id.setter
    def token_id(self, token_id):
        """Sets the token_id of this CrowdsaleFundParams.


        :param token_id: The token_id of this CrowdsaleFundParams.  # noqa: E501
        :type: str
        """
        if token_id is None:
            raise ValueError("Invalid value for `token_id`, must not be `None`")  # noqa: E501

        self._token_id = token_id

    @property
    def supply(self):
        """Gets the supply of this CrowdsaleFundParams.  # noqa: E501


        :return: The supply of this CrowdsaleFundParams.  # noqa: E501
        :rtype: str
        """
        return self._supply

    @supply.setter
    def supply(self, supply):
        """Sets the supply of this CrowdsaleFundParams.


        :param supply: The supply of this CrowdsaleFundParams.  # noqa: E501
        :type: str
        """
        if supply is None:
            raise ValueError("Invalid value for `supply`, must not be `None`")  # noqa: E501

        self._supply = supply

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
        if issubclass(CrowdsaleFundParams, dict):
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
        if not isinstance(other, CrowdsaleFundParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other