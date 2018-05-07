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


class Rotation(object):
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
        'alpha': 'float',
        'beta': 'float',
        'gamma': 'float'
    }

    attribute_map = {
        'alpha': 'alpha',
        'beta': 'beta',
        'gamma': 'gamma'
    }

    def __init__(self, alpha=None, beta=None, gamma=None):  # noqa: E501
        """Rotation - a model defined in Swagger"""  # noqa: E501

        self._alpha = None
        self._beta = None
        self._gamma = None
        self.discriminator = None

        if alpha is not None:
            self.alpha = alpha
        if beta is not None:
            self.beta = beta
        if gamma is not None:
            self.gamma = gamma

    @property
    def alpha(self):
        """Gets the alpha of this Rotation.  # noqa: E501


        :return: The alpha of this Rotation.  # noqa: E501
        :rtype: float
        """
        return self._alpha

    @alpha.setter
    def alpha(self, alpha):
        """Sets the alpha of this Rotation.


        :param alpha: The alpha of this Rotation.  # noqa: E501
        :type: float
        """

        self._alpha = alpha

    @property
    def beta(self):
        """Gets the beta of this Rotation.  # noqa: E501


        :return: The beta of this Rotation.  # noqa: E501
        :rtype: float
        """
        return self._beta

    @beta.setter
    def beta(self, beta):
        """Sets the beta of this Rotation.


        :param beta: The beta of this Rotation.  # noqa: E501
        :type: float
        """

        self._beta = beta

    @property
    def gamma(self):
        """Gets the gamma of this Rotation.  # noqa: E501


        :return: The gamma of this Rotation.  # noqa: E501
        :rtype: float
        """
        return self._gamma

    @gamma.setter
    def gamma(self, gamma):
        """Sets the gamma of this Rotation.


        :param gamma: The gamma of this Rotation.  # noqa: E501
        :type: float
        """

        self._gamma = gamma

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
        if not isinstance(other, Rotation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other