# coding: utf-8

"""
    Pure Storage FlashBlade REST 1.6 Python SDK

    Pure Storage FlashBlade REST 1.6 Python SDK, developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/).

    OpenAPI spec version: 1.6
    Contact: info@purestorage.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Space(object):
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
        'virtual': 'int',
        'data_reduction': 'float',
        'unique': 'int',
        'snapshots': 'int',
        'total_physical': 'int'
    }

    attribute_map = {
        'virtual': 'virtual',
        'data_reduction': 'data_reduction',
        'unique': 'unique',
        'snapshots': 'snapshots',
        'total_physical': 'total_physical'
    }

    def __init__(self, virtual=None, data_reduction=None, unique=None, snapshots=None, total_physical=None):
        """
        Space - a model defined in Swagger
        """

        self._virtual = None
        self._data_reduction = None
        self._unique = None
        self._snapshots = None
        self._total_physical = None

        if virtual is not None:
          self.virtual = virtual
        if data_reduction is not None:
          self.data_reduction = data_reduction
        if unique is not None:
          self.unique = unique
        if snapshots is not None:
          self.snapshots = snapshots
        if total_physical is not None:
          self.total_physical = total_physical

    @property
    def virtual(self):
        """
        Gets the virtual of this Space.
        usage in bytes

        :return: The virtual of this Space.
        :rtype: int
        """
        return self._virtual

    @virtual.setter
    def virtual(self, virtual):
        """
        Sets the virtual of this Space.
        usage in bytes

        :param virtual: The virtual of this Space.
        :type: int
        """

        self._virtual = virtual

    @property
    def data_reduction(self):
        """
        Gets the data_reduction of this Space.
        reduction of data

        :return: The data_reduction of this Space.
        :rtype: float
        """
        return self._data_reduction

    @data_reduction.setter
    def data_reduction(self, data_reduction):
        """
        Sets the data_reduction of this Space.
        reduction of data

        :param data_reduction: The data_reduction of this Space.
        :type: float
        """

        self._data_reduction = data_reduction

    @property
    def unique(self):
        """
        Gets the unique of this Space.
        physical usage in bytes

        :return: The unique of this Space.
        :rtype: int
        """
        return self._unique

    @unique.setter
    def unique(self, unique):
        """
        Sets the unique of this Space.
        physical usage in bytes

        :param unique: The unique of this Space.
        :type: int
        """

        self._unique = unique

    @property
    def snapshots(self):
        """
        Gets the snapshots of this Space.
        physical usage by snapshots, other than unique in bytes

        :return: The snapshots of this Space.
        :rtype: int
        """
        return self._snapshots

    @snapshots.setter
    def snapshots(self, snapshots):
        """
        Sets the snapshots of this Space.
        physical usage by snapshots, other than unique in bytes

        :param snapshots: The snapshots of this Space.
        :type: int
        """

        self._snapshots = snapshots

    @property
    def total_physical(self):
        """
        Gets the total_physical of this Space.
        total physical usage (including snapshots) in bytes

        :return: The total_physical of this Space.
        :rtype: int
        """
        return self._total_physical

    @total_physical.setter
    def total_physical(self, total_physical):
        """
        Sets the total_physical of this Space.
        total physical usage (including snapshots) in bytes

        :param total_physical: The total_physical of this Space.
        :type: int
        """

        self._total_physical = total_physical

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
        if not isinstance(other, Space):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
