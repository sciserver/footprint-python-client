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

from footprint.models.footprint import Footprint  # noqa: F401,E501


class FootprintRequest(object):
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
        'footprint': 'Footprint',
        'selection': 'list[str]'
    }

    attribute_map = {
        'footprint': 'footprint',
        'selection': 'selection'
    }

    def __init__(self, footprint=None, selection=None):  # noqa: E501
        """FootprintRequest - a model defined in Swagger"""  # noqa: E501

        self._footprint = None
        self._selection = None
        self.discriminator = None

        if footprint is not None:
            self.footprint = footprint
        if selection is not None:
            self.selection = selection

    @property
    def footprint(self):
        """Gets the footprint of this FootprintRequest.  # noqa: E501


        :return: The footprint of this FootprintRequest.  # noqa: E501
        :rtype: Footprint
        """
        return self._footprint

    @footprint.setter
    def footprint(self, footprint):
        """Sets the footprint of this FootprintRequest.


        :param footprint: The footprint of this FootprintRequest.  # noqa: E501
        :type: Footprint
        """

        self._footprint = footprint

    @property
    def selection(self):
        """Gets the selection of this FootprintRequest.  # noqa: E501


        :return: The selection of this FootprintRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._selection

    @selection.setter
    def selection(self, selection):
        """Sets the selection of this FootprintRequest.


        :param selection: The selection of this FootprintRequest.  # noqa: E501
        :type: list[str]
        """

        self._selection = selection

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
        if not isinstance(other, FootprintRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
