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


class Question(object):
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
        'answers': 'list[Answer]',
        'category': 'str',
        'description': 'str',
        'document': 'str',
        'id': 'str',
        'image': 'str',
        'is_account': 'bool',
        'metadata': 'dict(str, str)',
        'order_index': 'str',
        'question_type': 'str',
        'questionnaire': 'Questionnaire',
        'questionnaire_id': 'str',
        'subcategory': 'str',
        'title': 'str',
        'tooltip': 'str',
        'weight': 'float'
    }

    attribute_map = {
        'answers': 'answers',
        'category': 'category',
        'description': 'description',
        'document': 'document',
        'id': 'id',
        'image': 'image',
        'is_account': 'is_account',
        'metadata': 'metadata',
        'order_index': 'order_index',
        'question_type': 'question_type',
        'questionnaire': 'questionnaire',
        'questionnaire_id': 'questionnaire_id',
        'subcategory': 'subcategory',
        'title': 'title',
        'tooltip': 'tooltip',
        'weight': 'weight'
    }

    def __init__(self, answers=None, category=None, description=None, document=None, id=None, image=None, is_account=None, metadata=None, order_index=None, question_type=None, questionnaire=None, questionnaire_id=None, subcategory=None, title=None, tooltip=None, weight=None):  # noqa: E501
        """Question - a model defined in Swagger"""  # noqa: E501

        self._answers = None
        self._category = None
        self._description = None
        self._document = None
        self._id = None
        self._image = None
        self._is_account = None
        self._metadata = None
        self._order_index = None
        self._question_type = None
        self._questionnaire = None
        self._questionnaire_id = None
        self._subcategory = None
        self._title = None
        self._tooltip = None
        self._weight = None
        self.discriminator = None

        if answers is not None:
            self.answers = answers
        if category is not None:
            self.category = category
        if description is not None:
            self.description = description
        if document is not None:
            self.document = document
        if id is not None:
            self.id = id
        if image is not None:
            self.image = image
        if is_account is not None:
            self.is_account = is_account
        if metadata is not None:
            self.metadata = metadata
        if order_index is not None:
            self.order_index = order_index
        if question_type is not None:
            self.question_type = question_type
        if questionnaire is not None:
            self.questionnaire = questionnaire
        if questionnaire_id is not None:
            self.questionnaire_id = questionnaire_id
        if subcategory is not None:
            self.subcategory = subcategory
        if title is not None:
            self.title = title
        if tooltip is not None:
            self.tooltip = tooltip
        if weight is not None:
            self.weight = weight

    @property
    def answers(self):
        """Gets the answers of this Question.  # noqa: E501


        :return: The answers of this Question.  # noqa: E501
        :rtype: list[Answer]
        """
        return self._answers

    @answers.setter
    def answers(self, answers):
        """Sets the answers of this Question.


        :param answers: The answers of this Question.  # noqa: E501
        :type: list[Answer]
        """

        self._answers = answers

    @property
    def category(self):
        """Gets the category of this Question.  # noqa: E501

        category  # noqa: E501

        :return: The category of this Question.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this Question.

        category  # noqa: E501

        :param category: The category of this Question.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def description(self):
        """Gets the description of this Question.  # noqa: E501

        description  # noqa: E501

        :return: The description of this Question.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Question.

        description  # noqa: E501

        :param description: The description of this Question.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def document(self):
        """Gets the document of this Question.  # noqa: E501

        document  # noqa: E501

        :return: The document of this Question.  # noqa: E501
        :rtype: str
        """
        return self._document

    @document.setter
    def document(self, document):
        """Sets the document of this Question.

        document  # noqa: E501

        :param document: The document of this Question.  # noqa: E501
        :type: str
        """

        self._document = document

    @property
    def id(self):
        """Gets the id of this Question.  # noqa: E501


        :return: The id of this Question.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Question.


        :param id: The id of this Question.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def image(self):
        """Gets the image of this Question.  # noqa: E501

        image  # noqa: E501

        :return: The image of this Question.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this Question.

        image  # noqa: E501

        :param image: The image of this Question.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def is_account(self):
        """Gets the is_account of this Question.  # noqa: E501

        is_account  # noqa: E501

        :return: The is_account of this Question.  # noqa: E501
        :rtype: bool
        """
        return self._is_account

    @is_account.setter
    def is_account(self, is_account):
        """Sets the is_account of this Question.

        is_account  # noqa: E501

        :param is_account: The is_account of this Question.  # noqa: E501
        :type: bool
        """

        self._is_account = is_account

    @property
    def metadata(self):
        """Gets the metadata of this Question.  # noqa: E501

        metadata  # noqa: E501

        :return: The metadata of this Question.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Question.

        metadata  # noqa: E501

        :param metadata: The metadata of this Question.  # noqa: E501
        :type: dict(str, str)
        """

        self._metadata = metadata

    @property
    def order_index(self):
        """Gets the order_index of this Question.  # noqa: E501

        order_index  # noqa: E501

        :return: The order_index of this Question.  # noqa: E501
        :rtype: str
        """
        return self._order_index

    @order_index.setter
    def order_index(self, order_index):
        """Sets the order_index of this Question.

        order_index  # noqa: E501

        :param order_index: The order_index of this Question.  # noqa: E501
        :type: str
        """

        self._order_index = order_index

    @property
    def question_type(self):
        """Gets the question_type of this Question.  # noqa: E501

        question_type  # noqa: E501

        :return: The question_type of this Question.  # noqa: E501
        :rtype: str
        """
        return self._question_type

    @question_type.setter
    def question_type(self, question_type):
        """Sets the question_type of this Question.

        question_type  # noqa: E501

        :param question_type: The question_type of this Question.  # noqa: E501
        :type: str
        """

        self._question_type = question_type

    @property
    def questionnaire(self):
        """Gets the questionnaire of this Question.  # noqa: E501


        :return: The questionnaire of this Question.  # noqa: E501
        :rtype: Questionnaire
        """
        return self._questionnaire

    @questionnaire.setter
    def questionnaire(self, questionnaire):
        """Sets the questionnaire of this Question.


        :param questionnaire: The questionnaire of this Question.  # noqa: E501
        :type: Questionnaire
        """

        self._questionnaire = questionnaire

    @property
    def questionnaire_id(self):
        """Gets the questionnaire_id of this Question.  # noqa: E501

        questionnaireId  # noqa: E501

        :return: The questionnaire_id of this Question.  # noqa: E501
        :rtype: str
        """
        return self._questionnaire_id

    @questionnaire_id.setter
    def questionnaire_id(self, questionnaire_id):
        """Sets the questionnaire_id of this Question.

        questionnaireId  # noqa: E501

        :param questionnaire_id: The questionnaire_id of this Question.  # noqa: E501
        :type: str
        """

        self._questionnaire_id = questionnaire_id

    @property
    def subcategory(self):
        """Gets the subcategory of this Question.  # noqa: E501

        subcategory  # noqa: E501

        :return: The subcategory of this Question.  # noqa: E501
        :rtype: str
        """
        return self._subcategory

    @subcategory.setter
    def subcategory(self, subcategory):
        """Sets the subcategory of this Question.

        subcategory  # noqa: E501

        :param subcategory: The subcategory of this Question.  # noqa: E501
        :type: str
        """

        self._subcategory = subcategory

    @property
    def title(self):
        """Gets the title of this Question.  # noqa: E501

        title  # noqa: E501

        :return: The title of this Question.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Question.

        title  # noqa: E501

        :param title: The title of this Question.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def tooltip(self):
        """Gets the tooltip of this Question.  # noqa: E501

        tooltip  # noqa: E501

        :return: The tooltip of this Question.  # noqa: E501
        :rtype: str
        """
        return self._tooltip

    @tooltip.setter
    def tooltip(self, tooltip):
        """Sets the tooltip of this Question.

        tooltip  # noqa: E501

        :param tooltip: The tooltip of this Question.  # noqa: E501
        :type: str
        """

        self._tooltip = tooltip

    @property
    def weight(self):
        """Gets the weight of this Question.  # noqa: E501

        weight  # noqa: E501

        :return: The weight of this Question.  # noqa: E501
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this Question.

        weight  # noqa: E501

        :param weight: The weight of this Question.  # noqa: E501
        :type: float
        """

        self._weight = weight

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
        if issubclass(Question, dict):
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
        if not isinstance(other, Question):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other