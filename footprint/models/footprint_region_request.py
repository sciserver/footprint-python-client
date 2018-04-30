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

from footprint.models.definitionfootprint_region import DefinitionfootprintRegion  # noqa: F401,E501


class FootprintRegionRequest(object):
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
        'region': 'DefinitionfootprintRegion',
        'sources': 'list[str]'
    }

    attribute_map = {
        'region': 'region',
        'sources': 'sources'
    }

    def __init__(self, region=None, sources=None):  # noqa: E501
        """FootprintRegionRequest - a model defined in Swagger"""  # noqa: E501

        self._region = None
        self._sources = None
        self.discriminator = None

        if region is not None:
            self.region = region
        if sources is not None:
            self.sources = sources

    @property
    def region(self):
        """Gets the region of this FootprintRegionRequest.  # noqa: E501


        :return: The region of this FootprintRegionRequest.  # noqa: E501
        :rtype: DefinitionfootprintRegion
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this FootprintRegionRequest.


        :param region: The region of this FootprintRegionRequest.  # noqa: E501
        :type: DefinitionfootprintRegion
        """

        self._region = region

    @property
    def sources(self):
        """Gets the sources of this FootprintRegionRequest.  # noqa: E501


        :return: The sources of this FootprintRegionRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this FootprintRegionRequest.


        :param sources: The sources of this FootprintRegionRequest.  # noqa: E501
        :type: list[str]
        """

        self._sources = sources

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
        if not isinstance(other, FootprintRegionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
