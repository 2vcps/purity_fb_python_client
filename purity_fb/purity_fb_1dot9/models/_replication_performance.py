# coding: utf-8

"""
    Pure Storage FlashBlade REST 1.9 Python SDK

    Pure Storage FlashBlade REST 1.9 Python SDK, developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/).

    OpenAPI spec version: 1.9
    Contact: info@purestorage.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ReplicationPerformance(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'transmitted_bytes_per_sec': 'int',
        'received_bytes_per_sec': 'int'
    }

    attribute_map = {
        'transmitted_bytes_per_sec': 'transmitted_bytes_per_sec',
        'received_bytes_per_sec': 'received_bytes_per_sec'
    }

    def __init__(self, transmitted_bytes_per_sec=None, received_bytes_per_sec=None):
        """
        ReplicationPerformance - a model defined in Swagger
        """

        self._transmitted_bytes_per_sec = None
        self._received_bytes_per_sec = None

        if transmitted_bytes_per_sec is not None:
          self.transmitted_bytes_per_sec = transmitted_bytes_per_sec
        if received_bytes_per_sec is not None:
          self.received_bytes_per_sec = received_bytes_per_sec

    @property
    def transmitted_bytes_per_sec(self):
        """
        Gets the transmitted_bytes_per_sec of this ReplicationPerformance.
        Total bytes transmitted per second.

        :return: The transmitted_bytes_per_sec of this ReplicationPerformance.
        :rtype: int
        """
        return self._transmitted_bytes_per_sec

    @transmitted_bytes_per_sec.setter
    def transmitted_bytes_per_sec(self, transmitted_bytes_per_sec):
        """
        Sets the transmitted_bytes_per_sec of this ReplicationPerformance.
        Total bytes transmitted per second.

        :param transmitted_bytes_per_sec: The transmitted_bytes_per_sec of this ReplicationPerformance.
        :type: int
        """
        if transmitted_bytes_per_sec is not None and transmitted_bytes_per_sec < 0:
            raise ValueError("Invalid value for `transmitted_bytes_per_sec`, must be a value greater than or equal to `0`")

        self._transmitted_bytes_per_sec = transmitted_bytes_per_sec

    @property
    def received_bytes_per_sec(self):
        """
        Gets the received_bytes_per_sec of this ReplicationPerformance.
        Total bytes received per second.

        :return: The received_bytes_per_sec of this ReplicationPerformance.
        :rtype: int
        """
        return self._received_bytes_per_sec

    @received_bytes_per_sec.setter
    def received_bytes_per_sec(self, received_bytes_per_sec):
        """
        Sets the received_bytes_per_sec of this ReplicationPerformance.
        Total bytes received per second.

        :param received_bytes_per_sec: The received_bytes_per_sec of this ReplicationPerformance.
        :type: int
        """
        if received_bytes_per_sec is not None and received_bytes_per_sec < 0:
            raise ValueError("Invalid value for `received_bytes_per_sec`, must be a value greater than or equal to `0`")

        self._received_bytes_per_sec = received_bytes_per_sec

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ReplicationPerformance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
