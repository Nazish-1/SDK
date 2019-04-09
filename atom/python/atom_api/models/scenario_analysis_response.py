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

from atom_api.models.scenario_results import ScenarioResults  # noqa: F401,E501


class ScenarioAnalysisResponse(object):
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
        'portfolio_impact': 'float',
        'scenario_results': 'ScenarioResults'
    }

    attribute_map = {
        'portfolio_impact': 'portfolio_impact',
        'scenario_results': 'scenario_results'
    }

    def __init__(self, portfolio_impact=None, scenario_results=None):  # noqa: E501
        """ScenarioAnalysisResponse - a model defined in Swagger"""  # noqa: E501

        self._portfolio_impact = None
        self._scenario_results = None
        self.discriminator = None

        self.portfolio_impact = portfolio_impact
        self.scenario_results = scenario_results

    @property
    def portfolio_impact(self):
        """Gets the portfolio_impact of this ScenarioAnalysisResponse.  # noqa: E501

        Expected impact of scenario factors on the portfolio's return. The associated unit of time is the base unit indicated by frequency_interval (for example, week = 1 week).  # noqa: E501

        :return: The portfolio_impact of this ScenarioAnalysisResponse.  # noqa: E501
        :rtype: float
        """
        return self._portfolio_impact

    @portfolio_impact.setter
    def portfolio_impact(self, portfolio_impact):
        """Sets the portfolio_impact of this ScenarioAnalysisResponse.

        Expected impact of scenario factors on the portfolio's return. The associated unit of time is the base unit indicated by frequency_interval (for example, week = 1 week).  # noqa: E501

        :param portfolio_impact: The portfolio_impact of this ScenarioAnalysisResponse.  # noqa: E501
        :type: float
        """
        if portfolio_impact is None:
            raise ValueError("Invalid value for `portfolio_impact`, must not be `None`")  # noqa: E501

        self._portfolio_impact = portfolio_impact

    @property
    def scenario_results(self):
        """Gets the scenario_results of this ScenarioAnalysisResponse.  # noqa: E501


        :return: The scenario_results of this ScenarioAnalysisResponse.  # noqa: E501
        :rtype: ScenarioResults
        """
        return self._scenario_results

    @scenario_results.setter
    def scenario_results(self, scenario_results):
        """Sets the scenario_results of this ScenarioAnalysisResponse.


        :param scenario_results: The scenario_results of this ScenarioAnalysisResponse.  # noqa: E501
        :type: ScenarioResults
        """
        if scenario_results is None:
            raise ValueError("Invalid value for `scenario_results`, must not be `None`")  # noqa: E501

        self._scenario_results = scenario_results

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
        if issubclass(ScenarioAnalysisResponse, dict):
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
        if not isinstance(other, ScenarioAnalysisResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other