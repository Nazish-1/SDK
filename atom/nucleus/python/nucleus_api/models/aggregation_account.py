# coding: utf-8

"""
    Hydrogen Atom API

    The Hydrogen Atom API  # noqa: E501

    OpenAPI spec version: 1.7.0
    Contact: info@hydrogenplatform.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AggregationAccount(object):
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
        'account_holder': 'str',
        'account_name': 'str',
        'account_number': 'str',
        'bank_link_id': 'str',
        'category': 'str',
        'client_id': 'str',
        'create_date': 'datetime',
        'currency_code': 'str',
        'financial_offer_id': 'str',
        'id': 'str',
        'institution_name': 'str',
        'is_active': 'bool',
        'is_asset': 'bool',
        'is_business': 'bool',
        'is_investment': 'bool',
        'is_link_verified': 'bool',
        'mask': 'str',
        'metadata': 'dict(str, str)',
        'secondary_id': 'str',
        'subcategory': 'str',
        'update_date': 'datetime'
    }

    attribute_map = {
        'account_holder': 'account_holder',
        'account_name': 'account_name',
        'account_number': 'account_number',
        'bank_link_id': 'bank_link_id',
        'category': 'category',
        'client_id': 'client_id',
        'create_date': 'create_date',
        'currency_code': 'currency_code',
        'financial_offer_id': 'financial_offer_id',
        'id': 'id',
        'institution_name': 'institution_name',
        'is_active': 'is_active',
        'is_asset': 'is_asset',
        'is_business': 'is_business',
        'is_investment': 'is_investment',
        'is_link_verified': 'is_link_verified',
        'mask': 'mask',
        'metadata': 'metadata',
        'secondary_id': 'secondary_id',
        'subcategory': 'subcategory',
        'update_date': 'update_date'
    }

    def __init__(self, account_holder=None, account_name=None, account_number=None, bank_link_id=None, category=None, client_id=None, create_date=None, currency_code=None, financial_offer_id=None, id=None, institution_name=None, is_active=None, is_asset=None, is_business=None, is_investment=None, is_link_verified=None, mask=None, metadata=None, secondary_id=None, subcategory=None, update_date=None):  # noqa: E501
        """AggregationAccount - a model defined in Swagger"""  # noqa: E501

        self._account_holder = None
        self._account_name = None
        self._account_number = None
        self._bank_link_id = None
        self._category = None
        self._client_id = None
        self._create_date = None
        self._currency_code = None
        self._financial_offer_id = None
        self._id = None
        self._institution_name = None
        self._is_active = None
        self._is_asset = None
        self._is_business = None
        self._is_investment = None
        self._is_link_verified = None
        self._mask = None
        self._metadata = None
        self._secondary_id = None
        self._subcategory = None
        self._update_date = None
        self.discriminator = None

        if account_holder is not None:
            self.account_holder = account_holder
        self.account_name = account_name
        if account_number is not None:
            self.account_number = account_number
        if bank_link_id is not None:
            self.bank_link_id = bank_link_id
        self.category = category
        self.client_id = client_id
        if create_date is not None:
            self.create_date = create_date
        if currency_code is not None:
            self.currency_code = currency_code
        if financial_offer_id is not None:
            self.financial_offer_id = financial_offer_id
        if id is not None:
            self.id = id
        self.institution_name = institution_name
        if is_active is not None:
            self.is_active = is_active
        if is_asset is not None:
            self.is_asset = is_asset
        if is_business is not None:
            self.is_business = is_business
        if is_investment is not None:
            self.is_investment = is_investment
        if is_link_verified is not None:
            self.is_link_verified = is_link_verified
        if mask is not None:
            self.mask = mask
        if metadata is not None:
            self.metadata = metadata
        if secondary_id is not None:
            self.secondary_id = secondary_id
        if subcategory is not None:
            self.subcategory = subcategory
        if update_date is not None:
            self.update_date = update_date

    @property
    def account_holder(self):
        """Gets the account_holder of this AggregationAccount.  # noqa: E501

        accountHolder  # noqa: E501

        :return: The account_holder of this AggregationAccount.  # noqa: E501
        :rtype: str
        """
        return self._account_holder

    @account_holder.setter
    def account_holder(self, account_holder):
        """Sets the account_holder of this AggregationAccount.

        accountHolder  # noqa: E501

        :param account_holder: The account_holder of this AggregationAccount.  # noqa: E501
        :type: str
        """

        self._account_holder = account_holder

    @property
    def account_name(self):
        """Gets the account_name of this AggregationAccount.  # noqa: E501

        accountName  # noqa: E501

        :return: The account_name of this AggregationAccount.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this AggregationAccount.

        accountName  # noqa: E501

        :param account_name: The account_name of this AggregationAccount.  # noqa: E501
        :type: str
        """
        if account_name is None:
            raise ValueError("Invalid value for `account_name`, must not be `None`")  # noqa: E501

        self._account_name = account_name

    @property
    def account_number(self):
        """Gets the account_number of this AggregationAccount.  # noqa: E501

        accountNumber  # noqa: E501

        :return: The account_number of this AggregationAccount.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this AggregationAccount.

        accountNumber  # noqa: E501

        :param account_number: The account_number of this AggregationAccount.  # noqa: E501
        :type: str
        """

        self._account_number = account_number

    @property
    def bank_link_id(self):
        """Gets the bank_link_id of this AggregationAccount.  # noqa: E501

        bankLinkId  # noqa: E501

        :return: The bank_link_id of this AggregationAccount.  # noqa: E501
        :rtype: str
        """
        return self._bank_link_id

    @bank_link_id.setter
    def bank_link_id(self, bank_link_id):
        """Sets the bank_link_id of this AggregationAccount.

        bankLinkId  # noqa: E501

        :param bank_link_id: The bank_link_id of this AggregationAccount.  # noqa: E501
        :type: str
        """

        self._bank_link_id = bank_link_id

    @property
    def category(self):
        """Gets the category of this AggregationAccount.  # noqa: E501

        category  # noqa: E501

        :return: The category of this AggregationAccount.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this AggregationAccount.

        category  # noqa: E501

        :param category: The category of this AggregationAccount.  # noqa: E501
        :type: str
        """
        if category is None:
            raise ValueError("Invalid value for `category`, must not be `None`")  # noqa: E501

        self._category = category

    @property
    def client_id(self):
        """Gets the client_id of this AggregationAccount.  # noqa: E501

        clientId  # noqa: E501

        :return: The client_id of this AggregationAccount.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this AggregationAccount.

        clientId  # noqa: E501

        :param client_id: The client_id of this AggregationAccount.  # noqa: E501
        :type: str
        """
        if client_id is None:
            raise ValueError("Invalid value for `client_id`, must not be `None`")  # noqa: E501

        self._client_id = client_id

    @property
    def create_date(self):
        """Gets the create_date of this AggregationAccount.  # noqa: E501


        :return: The create_date of this AggregationAccount.  # noqa: E501
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this AggregationAccount.


        :param create_date: The create_date of this AggregationAccount.  # noqa: E501
        :type: datetime
        """

        self._create_date = create_date

    @property
    def currency_code(self):
        """Gets the currency_code of this AggregationAccount.  # noqa: E501

        currencyCode  # noqa: E501

        :return: The currency_code of this AggregationAccount.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this AggregationAccount.

        currencyCode  # noqa: E501

        :param currency_code: The currency_code of this AggregationAccount.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def financial_offer_id(self):
        """Gets the financial_offer_id of this AggregationAccount.  # noqa: E501

        financialOfferId  # noqa: E501

        :return: The financial_offer_id of this AggregationAccount.  # noqa: E501
        :rtype: str
        """
        return self._financial_offer_id

    @financial_offer_id.setter
    def financial_offer_id(self, financial_offer_id):
        """Sets the financial_offer_id of this AggregationAccount.

        financialOfferId  # noqa: E501

        :param financial_offer_id: The financial_offer_id of this AggregationAccount.  # noqa: E501
        :type: str
        """

        self._financial_offer_id = financial_offer_id

    @property
    def id(self):
        """Gets the id of this AggregationAccount.  # noqa: E501


        :return: The id of this AggregationAccount.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AggregationAccount.


        :param id: The id of this AggregationAccount.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def institution_name(self):
        """Gets the institution_name of this AggregationAccount.  # noqa: E501

        institutionName  # noqa: E501

        :return: The institution_name of this AggregationAccount.  # noqa: E501
        :rtype: str
        """
        return self._institution_name

    @institution_name.setter
    def institution_name(self, institution_name):
        """Sets the institution_name of this AggregationAccount.

        institutionName  # noqa: E501

        :param institution_name: The institution_name of this AggregationAccount.  # noqa: E501
        :type: str
        """
        if institution_name is None:
            raise ValueError("Invalid value for `institution_name`, must not be `None`")  # noqa: E501

        self._institution_name = institution_name

    @property
    def is_active(self):
        """Gets the is_active of this AggregationAccount.  # noqa: E501

        isActive  # noqa: E501

        :return: The is_active of this AggregationAccount.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this AggregationAccount.

        isActive  # noqa: E501

        :param is_active: The is_active of this AggregationAccount.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def is_asset(self):
        """Gets the is_asset of this AggregationAccount.  # noqa: E501

        isAsset  # noqa: E501

        :return: The is_asset of this AggregationAccount.  # noqa: E501
        :rtype: bool
        """
        return self._is_asset

    @is_asset.setter
    def is_asset(self, is_asset):
        """Sets the is_asset of this AggregationAccount.

        isAsset  # noqa: E501

        :param is_asset: The is_asset of this AggregationAccount.  # noqa: E501
        :type: bool
        """

        self._is_asset = is_asset

    @property
    def is_business(self):
        """Gets the is_business of this AggregationAccount.  # noqa: E501

        isBusiness  # noqa: E501

        :return: The is_business of this AggregationAccount.  # noqa: E501
        :rtype: bool
        """
        return self._is_business

    @is_business.setter
    def is_business(self, is_business):
        """Sets the is_business of this AggregationAccount.

        isBusiness  # noqa: E501

        :param is_business: The is_business of this AggregationAccount.  # noqa: E501
        :type: bool
        """

        self._is_business = is_business

    @property
    def is_investment(self):
        """Gets the is_investment of this AggregationAccount.  # noqa: E501

        isInvestment  # noqa: E501

        :return: The is_investment of this AggregationAccount.  # noqa: E501
        :rtype: bool
        """
        return self._is_investment

    @is_investment.setter
    def is_investment(self, is_investment):
        """Sets the is_investment of this AggregationAccount.

        isInvestment  # noqa: E501

        :param is_investment: The is_investment of this AggregationAccount.  # noqa: E501
        :type: bool
        """

        self._is_investment = is_investment

    @property
    def is_link_verified(self):
        """Gets the is_link_verified of this AggregationAccount.  # noqa: E501

        isLinkVerified  # noqa: E501

        :return: The is_link_verified of this AggregationAccount.  # noqa: E501
        :rtype: bool
        """
        return self._is_link_verified

    @is_link_verified.setter
    def is_link_verified(self, is_link_verified):
        """Sets the is_link_verified of this AggregationAccount.

        isLinkVerified  # noqa: E501

        :param is_link_verified: The is_link_verified of this AggregationAccount.  # noqa: E501
        :type: bool
        """

        self._is_link_verified = is_link_verified

    @property
    def mask(self):
        """Gets the mask of this AggregationAccount.  # noqa: E501

        mask  # noqa: E501

        :return: The mask of this AggregationAccount.  # noqa: E501
        :rtype: str
        """
        return self._mask

    @mask.setter
    def mask(self, mask):
        """Sets the mask of this AggregationAccount.

        mask  # noqa: E501

        :param mask: The mask of this AggregationAccount.  # noqa: E501
        :type: str
        """

        self._mask = mask

    @property
    def metadata(self):
        """Gets the metadata of this AggregationAccount.  # noqa: E501


        :return: The metadata of this AggregationAccount.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this AggregationAccount.


        :param metadata: The metadata of this AggregationAccount.  # noqa: E501
        :type: dict(str, str)
        """

        self._metadata = metadata

    @property
    def secondary_id(self):
        """Gets the secondary_id of this AggregationAccount.  # noqa: E501


        :return: The secondary_id of this AggregationAccount.  # noqa: E501
        :rtype: str
        """
        return self._secondary_id

    @secondary_id.setter
    def secondary_id(self, secondary_id):
        """Sets the secondary_id of this AggregationAccount.


        :param secondary_id: The secondary_id of this AggregationAccount.  # noqa: E501
        :type: str
        """

        self._secondary_id = secondary_id

    @property
    def subcategory(self):
        """Gets the subcategory of this AggregationAccount.  # noqa: E501

        subcategory  # noqa: E501

        :return: The subcategory of this AggregationAccount.  # noqa: E501
        :rtype: str
        """
        return self._subcategory

    @subcategory.setter
    def subcategory(self, subcategory):
        """Sets the subcategory of this AggregationAccount.

        subcategory  # noqa: E501

        :param subcategory: The subcategory of this AggregationAccount.  # noqa: E501
        :type: str
        """

        self._subcategory = subcategory

    @property
    def update_date(self):
        """Gets the update_date of this AggregationAccount.  # noqa: E501


        :return: The update_date of this AggregationAccount.  # noqa: E501
        :rtype: datetime
        """
        return self._update_date

    @update_date.setter
    def update_date(self, update_date):
        """Sets the update_date of this AggregationAccount.


        :param update_date: The update_date of this AggregationAccount.  # noqa: E501
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
        if issubclass(AggregationAccount, dict):
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
        if not isinstance(other, AggregationAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
