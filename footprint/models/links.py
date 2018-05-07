# coding: utf-8

"""
    null

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: null
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Links(object):
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
        '_self': 'str',
        'parent': 'str',
        'prev': 'str',
        'next': 'str'
    }

    attribute_map = {
        '_self': 'self',
        'parent': 'parent',
        'prev': 'prev',
        'next': 'next'
    }

    def __init__(self, _self=None, parent=None, prev=None, next=None):  # noqa: E501
        """Links - a model defined in Swagger"""  # noqa: E501

        self.__self = None
        self._parent = None
        self._prev = None
        self._next = None
        self.discriminator = None

        if _self is not None:
            self._self = _self
        if parent is not None:
            self.parent = parent
        if prev is not None:
            self.prev = prev
        if next is not None:
            self.next = next

    @property
    def _self(self):
        """Gets the _self of this Links.  # noqa: E501


        :return: The _self of this Links.  # noqa: E501
        :rtype: str
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this Links.


        :param _self: The _self of this Links.  # noqa: E501
        :type: str
        """

        self.__self = _self

    @property
    def parent(self):
        """Gets the parent of this Links.  # noqa: E501


        :return: The parent of this Links.  # noqa: E501
        :rtype: str
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this Links.


        :param parent: The parent of this Links.  # noqa: E501
        :type: str
        """

        self._parent = parent

    @property
    def prev(self):
        """Gets the prev of this Links.  # noqa: E501


        :return: The prev of this Links.  # noqa: E501
        :rtype: str
        """
        return self._prev

    @prev.setter
    def prev(self, prev):
        """Sets the prev of this Links.


        :param prev: The prev of this Links.  # noqa: E501
        :type: str
        """

        self._prev = prev

    @property
    def next(self):
        """Gets the next of this Links.  # noqa: E501


        :return: The next of this Links.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this Links.


        :param next: The next of this Links.  # noqa: E501
        :type: str
        """

        self._next = next

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Links):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
