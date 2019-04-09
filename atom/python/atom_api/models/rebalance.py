# coding: utf-8

"""
    Hydrogen Atom API

    The Hydrogen Atom API  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: info@hydrogenplatform.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Rebalance(object):
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
        'model_id': 'str',
        'start_date': 'date',
        'end_date': 'date',
        'initial_weights': 'object'
    }

    attribute_map = {
        'model_id': 'model_id',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'initial_weights': 'initial_weights'
    }

    def __init__(self, model_id=None, start_date=None, end_date=None, initial_weights=None):  # noqa: E501
        """Rebalance - a model defined in Swagger"""  # noqa: E501

        self._model_id = None
        self._start_date = None
        self._end_date = None
        self._initial_weights = None
        self.discriminator = None

        self.model_id = model_id
        self.start_date = start_date
        self.end_date = end_date
        if initial_weights is not None:
            self.initial_weights = initial_weights

    @property
    def model_id(self):
        """Gets the model_id of this Rebalance.  # noqa: E501

        Identifier of the model to rebalance  # noqa: E501

        :return: The model_id of this Rebalance.  # noqa: E501
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        """Sets the model_id of this Rebalance.

        Identifier of the model to rebalance  # noqa: E501

        :param model_id: The model_id of this Rebalance.  # noqa: E501
        :type: str
        """
        if model_id is None:
            raise ValueError("Invalid value for `model_id`, must not be `None`")  # noqa: E501

        self._model_id = model_id

    @property
    def start_date(self):
        """Gets the start_date of this Rebalance.  # noqa: E501

        Start date for analysis  # noqa: E501

        :return: The start_date of this Rebalance.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this Rebalance.

        Start date for analysis  # noqa: E501

        :param start_date: The start_date of this Rebalance.  # noqa: E501
        :type: date
        """
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this Rebalance.  # noqa: E501

        End date for analysis  # noqa: E501

        :return: The end_date of this Rebalance.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this Rebalance.

        End date for analysis  # noqa: E501

        :param end_date: The end_date of this Rebalance.  # noqa: E501
        :type: date
        """
        if end_date is None:
            raise ValueError("Invalid value for `end_date`, must not be `None`")  # noqa: E501

        self._end_date = end_date

    @property
    def initial_weights(self):
        """Gets the initial_weights of this Rebalance.  # noqa: E501

        Initial weights for model holdings  # noqa: E501

        :return: The initial_weights of this Rebalance.  # noqa: E501
        :rtype: object
        """
        return self._initial_weights

    @initial_weights.setter
    def initial_weights(self, initial_weights):
        """Sets the initial_weights of this Rebalance.

        Initial weights for model holdings  # noqa: E501

        :param initial_weights: The initial_weights of this Rebalance.  # noqa: E501
        :type: object
        """

        self._initial_weights = initial_weights

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
        if issubclass(Rebalance, dict):
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
        if not isinstance(other, Rebalance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other