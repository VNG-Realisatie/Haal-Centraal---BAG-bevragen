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


class ZoekResultaat(object):
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
        'omschrijving': 'str',
        'identificatie': 'str'
    }

    attribute_map = {
        'omschrijving': 'omschrijving',
        'identificatie': 'identificatie'
    }

    def __init__(self, omschrijving=None, identificatie=None, local_vars_configuration=None):  # noqa: E501
        """ZoekResultaat - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._omschrijving = None
        self._identificatie = None
        self.discriminator = None

        if omschrijving is not None:
            self.omschrijving = omschrijving
        if identificatie is not None:
            self.identificatie = identificatie

    @property
    def omschrijving(self):
        """Gets the omschrijving of this ZoekResultaat.  # noqa: E501

        Omschrijving van het zoekresultaat  # noqa: E501

        :return: The omschrijving of this ZoekResultaat.  # noqa: E501
        :rtype: str
        """
        return self._omschrijving

    @omschrijving.setter
    def omschrijving(self, omschrijving):
        """Sets the omschrijving of this ZoekResultaat.

        Omschrijving van het zoekresultaat  # noqa: E501

        :param omschrijving: The omschrijving of this ZoekResultaat.  # noqa: E501
        :type: str
        """

        self._omschrijving = omschrijving

    @property
    def identificatie(self):
        """Gets the identificatie of this ZoekResultaat.  # noqa: E501

        Identificatie van het zoekresultaat  # noqa: E501

        :return: The identificatie of this ZoekResultaat.  # noqa: E501
        :rtype: str
        """
        return self._identificatie

    @identificatie.setter
    def identificatie(self, identificatie):
        """Sets the identificatie of this ZoekResultaat.

        Identificatie van het zoekresultaat  # noqa: E501

        :param identificatie: The identificatie of this ZoekResultaat.  # noqa: E501
        :type: str
        """

        self._identificatie = identificatie

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
        if not isinstance(other, ZoekResultaat):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ZoekResultaat):
            return True

        return self.to_dict() != other.to_dict()
