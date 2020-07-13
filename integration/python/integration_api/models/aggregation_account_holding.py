# coding: utf-8

"""
    Hydrogen Integration API

    The Hydrogen Integration API  # noqa: E501

    OpenAPI spec version: 1.2.1
    Contact: info@hydrogenplatform.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AggregationAccountHolding(object):
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
        'aggregation_account_id': 'str',
        'amount': 'float',
        'asset_class': 'str',
        'cost_basis': 'float',
        'create_date': 'datetime',
        'currency_code': 'str',
        'cusip': 'str',
        'exchange': 'str',
        'holding_date': 'datetime',
        'holding_type': 'str',
        'id': 'str',
        'is_active': 'bool',
        'isin': 'str',
        'metadata': 'dict(str, str)',
        'price': 'float',
        'secondary_id': 'str',
        'shares': 'float',
        'ticker': 'str',
        'ticker_name': 'str',
        'update_date': 'datetime'
    }

    attribute_map = {
        'aggregation_account_id': 'aggregation_account_id',
        'amount': 'amount',
        'asset_class': 'asset_class',
        'cost_basis': 'cost_basis',
        'create_date': 'create_date',
        'currency_code': 'currency_code',
        'cusip': 'cusip',
        'exchange': 'exchange',
        'holding_date': 'holding_date',
        'holding_type': 'holding_type',
        'id': 'id',
        'is_active': 'is_active',
        'isin': 'isin',
        'metadata': 'metadata',
        'price': 'price',
        'secondary_id': 'secondary_id',
        'shares': 'shares',
        'ticker': 'ticker',
        'ticker_name': 'ticker_name',
        'update_date': 'update_date'
    }

    def __init__(self, aggregation_account_id=None, amount=None, asset_class=None, cost_basis=None, create_date=None, currency_code=None, cusip=None, exchange=None, holding_date=None, holding_type=None, id=None, is_active=None, isin=None, metadata=None, price=None, secondary_id=None, shares=None, ticker=None, ticker_name=None, update_date=None):  # noqa: E501
        """AggregationAccountHolding - a model defined in Swagger"""  # noqa: E501

        self._aggregation_account_id = None
        self._amount = None
        self._asset_class = None
        self._cost_basis = None
        self._create_date = None
        self._currency_code = None
        self._cusip = None
        self._exchange = None
        self._holding_date = None
        self._holding_type = None
        self._id = None
        self._is_active = None
        self._isin = None
        self._metadata = None
        self._price = None
        self._secondary_id = None
        self._shares = None
        self._ticker = None
        self._ticker_name = None
        self._update_date = None
        self.discriminator = None

        if aggregation_account_id is not None:
            self.aggregation_account_id = aggregation_account_id
        if amount is not None:
            self.amount = amount
        if asset_class is not None:
            self.asset_class = asset_class
        if cost_basis is not None:
            self.cost_basis = cost_basis
        if create_date is not None:
            self.create_date = create_date
        if currency_code is not None:
            self.currency_code = currency_code
        if cusip is not None:
            self.cusip = cusip
        if exchange is not None:
            self.exchange = exchange
        if holding_date is not None:
            self.holding_date = holding_date
        if holding_type is not None:
            self.holding_type = holding_type
        if id is not None:
            self.id = id
        if is_active is not None:
            self.is_active = is_active
        if isin is not None:
            self.isin = isin
        if metadata is not None:
            self.metadata = metadata
        if price is not None:
            self.price = price
        if secondary_id is not None:
            self.secondary_id = secondary_id
        self.shares = shares
        self.ticker = ticker
        self.ticker_name = ticker_name
        if update_date is not None:
            self.update_date = update_date

    @property
    def aggregation_account_id(self):
        """Gets the aggregation_account_id of this AggregationAccountHolding.  # noqa: E501

        aggregationAccountId  # noqa: E501

        :return: The aggregation_account_id of this AggregationAccountHolding.  # noqa: E501
        :rtype: str
        """
        return self._aggregation_account_id

    @aggregation_account_id.setter
    def aggregation_account_id(self, aggregation_account_id):
        """Sets the aggregation_account_id of this AggregationAccountHolding.

        aggregationAccountId  # noqa: E501

        :param aggregation_account_id: The aggregation_account_id of this AggregationAccountHolding.  # noqa: E501
        :type: str
        """

        self._aggregation_account_id = aggregation_account_id

    @property
    def amount(self):
        """Gets the amount of this AggregationAccountHolding.  # noqa: E501


        :return: The amount of this AggregationAccountHolding.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this AggregationAccountHolding.


        :param amount: The amount of this AggregationAccountHolding.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def asset_class(self):
        """Gets the asset_class of this AggregationAccountHolding.  # noqa: E501


        :return: The asset_class of this AggregationAccountHolding.  # noqa: E501
        :rtype: str
        """
        return self._asset_class

    @asset_class.setter
    def asset_class(self, asset_class):
        """Sets the asset_class of this AggregationAccountHolding.


        :param asset_class: The asset_class of this AggregationAccountHolding.  # noqa: E501
        :type: str
        """

        self._asset_class = asset_class

    @property
    def cost_basis(self):
        """Gets the cost_basis of this AggregationAccountHolding.  # noqa: E501


        :return: The cost_basis of this AggregationAccountHolding.  # noqa: E501
        :rtype: float
        """
        return self._cost_basis

    @cost_basis.setter
    def cost_basis(self, cost_basis):
        """Sets the cost_basis of this AggregationAccountHolding.


        :param cost_basis: The cost_basis of this AggregationAccountHolding.  # noqa: E501
        :type: float
        """

        self._cost_basis = cost_basis

    @property
    def create_date(self):
        """Gets the create_date of this AggregationAccountHolding.  # noqa: E501

        createDate  # noqa: E501

        :return: The create_date of this AggregationAccountHolding.  # noqa: E501
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this AggregationAccountHolding.

        createDate  # noqa: E501

        :param create_date: The create_date of this AggregationAccountHolding.  # noqa: E501
        :type: datetime
        """

        self._create_date = create_date

    @property
    def currency_code(self):
        """Gets the currency_code of this AggregationAccountHolding.  # noqa: E501


        :return: The currency_code of this AggregationAccountHolding.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this AggregationAccountHolding.


        :param currency_code: The currency_code of this AggregationAccountHolding.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def cusip(self):
        """Gets the cusip of this AggregationAccountHolding.  # noqa: E501


        :return: The cusip of this AggregationAccountHolding.  # noqa: E501
        :rtype: str
        """
        return self._cusip

    @cusip.setter
    def cusip(self, cusip):
        """Sets the cusip of this AggregationAccountHolding.


        :param cusip: The cusip of this AggregationAccountHolding.  # noqa: E501
        :type: str
        """

        self._cusip = cusip

    @property
    def exchange(self):
        """Gets the exchange of this AggregationAccountHolding.  # noqa: E501


        :return: The exchange of this AggregationAccountHolding.  # noqa: E501
        :rtype: str
        """
        return self._exchange

    @exchange.setter
    def exchange(self, exchange):
        """Sets the exchange of this AggregationAccountHolding.


        :param exchange: The exchange of this AggregationAccountHolding.  # noqa: E501
        :type: str
        """

        self._exchange = exchange

    @property
    def holding_date(self):
        """Gets the holding_date of this AggregationAccountHolding.  # noqa: E501

        holding_date  # noqa: E501

        :return: The holding_date of this AggregationAccountHolding.  # noqa: E501
        :rtype: datetime
        """
        return self._holding_date

    @holding_date.setter
    def holding_date(self, holding_date):
        """Sets the holding_date of this AggregationAccountHolding.

        holding_date  # noqa: E501

        :param holding_date: The holding_date of this AggregationAccountHolding.  # noqa: E501
        :type: datetime
        """

        self._holding_date = holding_date

    @property
    def holding_type(self):
        """Gets the holding_type of this AggregationAccountHolding.  # noqa: E501


        :return: The holding_type of this AggregationAccountHolding.  # noqa: E501
        :rtype: str
        """
        return self._holding_type

    @holding_type.setter
    def holding_type(self, holding_type):
        """Sets the holding_type of this AggregationAccountHolding.


        :param holding_type: The holding_type of this AggregationAccountHolding.  # noqa: E501
        :type: str
        """

        self._holding_type = holding_type

    @property
    def id(self):
        """Gets the id of this AggregationAccountHolding.  # noqa: E501

        id  # noqa: E501

        :return: The id of this AggregationAccountHolding.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AggregationAccountHolding.

        id  # noqa: E501

        :param id: The id of this AggregationAccountHolding.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def is_active(self):
        """Gets the is_active of this AggregationAccountHolding.  # noqa: E501

        isActive  # noqa: E501

        :return: The is_active of this AggregationAccountHolding.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this AggregationAccountHolding.

        isActive  # noqa: E501

        :param is_active: The is_active of this AggregationAccountHolding.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def isin(self):
        """Gets the isin of this AggregationAccountHolding.  # noqa: E501

        isin  # noqa: E501

        :return: The isin of this AggregationAccountHolding.  # noqa: E501
        :rtype: str
        """
        return self._isin

    @isin.setter
    def isin(self, isin):
        """Sets the isin of this AggregationAccountHolding.

        isin  # noqa: E501

        :param isin: The isin of this AggregationAccountHolding.  # noqa: E501
        :type: str
        """

        self._isin = isin

    @property
    def metadata(self):
        """Gets the metadata of this AggregationAccountHolding.  # noqa: E501


        :return: The metadata of this AggregationAccountHolding.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this AggregationAccountHolding.


        :param metadata: The metadata of this AggregationAccountHolding.  # noqa: E501
        :type: dict(str, str)
        """

        self._metadata = metadata

    @property
    def price(self):
        """Gets the price of this AggregationAccountHolding.  # noqa: E501


        :return: The price of this AggregationAccountHolding.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this AggregationAccountHolding.


        :param price: The price of this AggregationAccountHolding.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def secondary_id(self):
        """Gets the secondary_id of this AggregationAccountHolding.  # noqa: E501


        :return: The secondary_id of this AggregationAccountHolding.  # noqa: E501
        :rtype: str
        """
        return self._secondary_id

    @secondary_id.setter
    def secondary_id(self, secondary_id):
        """Sets the secondary_id of this AggregationAccountHolding.


        :param secondary_id: The secondary_id of this AggregationAccountHolding.  # noqa: E501
        :type: str
        """

        self._secondary_id = secondary_id

    @property
    def shares(self):
        """Gets the shares of this AggregationAccountHolding.  # noqa: E501

        shares  # noqa: E501

        :return: The shares of this AggregationAccountHolding.  # noqa: E501
        :rtype: float
        """
        return self._shares

    @shares.setter
    def shares(self, shares):
        """Sets the shares of this AggregationAccountHolding.

        shares  # noqa: E501

        :param shares: The shares of this AggregationAccountHolding.  # noqa: E501
        :type: float
        """
        if shares is None:
            raise ValueError("Invalid value for `shares`, must not be `None`")  # noqa: E501

        self._shares = shares

    @property
    def ticker(self):
        """Gets the ticker of this AggregationAccountHolding.  # noqa: E501

        ticker  # noqa: E501

        :return: The ticker of this AggregationAccountHolding.  # noqa: E501
        :rtype: str
        """
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this AggregationAccountHolding.

        ticker  # noqa: E501

        :param ticker: The ticker of this AggregationAccountHolding.  # noqa: E501
        :type: str
        """
        if ticker is None:
            raise ValueError("Invalid value for `ticker`, must not be `None`")  # noqa: E501

        self._ticker = ticker

    @property
    def ticker_name(self):
        """Gets the ticker_name of this AggregationAccountHolding.  # noqa: E501

        tickerName  # noqa: E501

        :return: The ticker_name of this AggregationAccountHolding.  # noqa: E501
        :rtype: str
        """
        return self._ticker_name

    @ticker_name.setter
    def ticker_name(self, ticker_name):
        """Sets the ticker_name of this AggregationAccountHolding.

        tickerName  # noqa: E501

        :param ticker_name: The ticker_name of this AggregationAccountHolding.  # noqa: E501
        :type: str
        """
        if ticker_name is None:
            raise ValueError("Invalid value for `ticker_name`, must not be `None`")  # noqa: E501

        self._ticker_name = ticker_name

    @property
    def update_date(self):
        """Gets the update_date of this AggregationAccountHolding.  # noqa: E501

        updateDate  # noqa: E501

        :return: The update_date of this AggregationAccountHolding.  # noqa: E501
        :rtype: datetime
        """
        return self._update_date

    @update_date.setter
    def update_date(self, update_date):
        """Sets the update_date of this AggregationAccountHolding.

        updateDate  # noqa: E501

        :param update_date: The update_date of this AggregationAccountHolding.  # noqa: E501
        :type: datetime
        """

        self._update_date = update_date

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
        if issubclass(AggregationAccountHolding, dict):
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
        if not isinstance(other, AggregationAccountHolding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other