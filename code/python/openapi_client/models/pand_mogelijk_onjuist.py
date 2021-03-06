# coding: utf-8

"""
    Huidige bevragingen API

    Deze API levert actuele gegevens over adressen, adresseerbaar objecten en panden. Actueel betekent in deze API `zonder eindstatus`. De bron voor deze API is de basisregistratie adressen en gebouwen (BAG).  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: bag@kadaster.nl
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class PandMogelijkOnjuist(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'geometrie': 'bool',
        'oorspronkelijk_bouwjaar': 'bool',
        'status': 'bool',
        'toelichting': 'list[str]'
    }

    attribute_map = {
        'geometrie': 'geometrie',
        'oorspronkelijk_bouwjaar': 'oorspronkelijkBouwjaar',
        'status': 'status',
        'toelichting': 'toelichting'
    }

    def __init__(self, geometrie=None, oorspronkelijk_bouwjaar=None, status=None, toelichting=None, local_vars_configuration=None):  # noqa: E501
        """PandMogelijkOnjuist - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._geometrie = None
        self._oorspronkelijk_bouwjaar = None
        self._status = None
        self._toelichting = None
        self.discriminator = None

        if geometrie is not None:
            self.geometrie = geometrie
        if oorspronkelijk_bouwjaar is not None:
            self.oorspronkelijk_bouwjaar = oorspronkelijk_bouwjaar
        if status is not None:
            self.status = status
        if toelichting is not None:
            self.toelichting = toelichting

    @property
    def geometrie(self):
        """Gets the geometrie of this PandMogelijkOnjuist.  # noqa: E501


        :return: The geometrie of this PandMogelijkOnjuist.  # noqa: E501
        :rtype: bool
        """
        return self._geometrie

    @geometrie.setter
    def geometrie(self, geometrie):
        """Sets the geometrie of this PandMogelijkOnjuist.


        :param geometrie: The geometrie of this PandMogelijkOnjuist.  # noqa: E501
        :type: bool
        """

        self._geometrie = geometrie

    @property
    def oorspronkelijk_bouwjaar(self):
        """Gets the oorspronkelijk_bouwjaar of this PandMogelijkOnjuist.  # noqa: E501


        :return: The oorspronkelijk_bouwjaar of this PandMogelijkOnjuist.  # noqa: E501
        :rtype: bool
        """
        return self._oorspronkelijk_bouwjaar

    @oorspronkelijk_bouwjaar.setter
    def oorspronkelijk_bouwjaar(self, oorspronkelijk_bouwjaar):
        """Sets the oorspronkelijk_bouwjaar of this PandMogelijkOnjuist.


        :param oorspronkelijk_bouwjaar: The oorspronkelijk_bouwjaar of this PandMogelijkOnjuist.  # noqa: E501
        :type: bool
        """

        self._oorspronkelijk_bouwjaar = oorspronkelijk_bouwjaar

    @property
    def status(self):
        """Gets the status of this PandMogelijkOnjuist.  # noqa: E501


        :return: The status of this PandMogelijkOnjuist.  # noqa: E501
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PandMogelijkOnjuist.


        :param status: The status of this PandMogelijkOnjuist.  # noqa: E501
        :type: bool
        """

        self._status = status

    @property
    def toelichting(self):
        """Gets the toelichting of this PandMogelijkOnjuist.  # noqa: E501


        :return: The toelichting of this PandMogelijkOnjuist.  # noqa: E501
        :rtype: list[str]
        """
        return self._toelichting

    @toelichting.setter
    def toelichting(self, toelichting):
        """Sets the toelichting of this PandMogelijkOnjuist.


        :param toelichting: The toelichting of this PandMogelijkOnjuist.  # noqa: E501
        :type: list[str]
        """

        self._toelichting = toelichting

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, PandMogelijkOnjuist):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PandMogelijkOnjuist):
            return True

        return self.to_dict() != other.to_dict()
