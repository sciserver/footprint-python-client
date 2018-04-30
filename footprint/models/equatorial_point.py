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


class EquatorialPoint(object):
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
        'ra': 'float',
        'dec': 'float'
    }

    attribute_map = {
        'ra': 'RA',
        'dec': 'Dec'
    }

    def __init__(self, ra=None, dec=None):  # noqa: E501
        """EquatorialPoint - a model defined in Swagger"""  # noqa: E501

        self._ra = None
        self._dec = None
        self.discriminator = None

        if ra is not None:
            self.ra = ra
        if dec is not None:
            self.dec = dec

    @property
    def ra(self):
        """Gets the ra of this EquatorialPoint.  # noqa: E501


        :return: The ra of this EquatorialPoint.  # noqa: E501
        :rtype: float
        """
        return self._ra

    @ra.setter
    def ra(self, ra):
        """Sets the ra of this EquatorialPoint.


        :param ra: The ra of this EquatorialPoint.  # noqa: E501
        :type: float
        """

        self._ra = ra

    @property
    def dec(self):
        """Gets the dec of this EquatorialPoint.  # noqa: E501


        :return: The dec of this EquatorialPoint.  # noqa: E501
        :rtype: float
        """
        return self._dec

    @dec.setter
    def dec(self, dec):
        """Sets the dec of this EquatorialPoint.


        :param dec: The dec of this EquatorialPoint.  # noqa: E501
        :type: float
        """

        self._dec = dec

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
        if not isinstance(other, EquatorialPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
