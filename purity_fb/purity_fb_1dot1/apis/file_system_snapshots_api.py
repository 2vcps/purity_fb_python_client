# coding: utf-8

"""
    Pure Storage FlashBlade REST 1.1 Python SDK

    Pure Storage FlashBlade REST 1.1 Python SDK, developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/).

    OpenAPI spec version: 1.1
    Contact: info@purestorage.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class FileSystemSnapshotsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create_file_system_snapshots(self, sources, **kwargs):
        """
        Create snapshots for the specified source file systems
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_file_system_snapshots(sources, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] sources: A list of names of source file systems. (required)
        :param SnapshotSuffix suffix: the suffix of the snapshot
        :return: FileSystemSnapshotResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_file_system_snapshots_with_http_info(sources, **kwargs)
        else:
            (data) = self.create_file_system_snapshots_with_http_info(sources, **kwargs)
            return data

    def create_file_system_snapshots_with_http_info(self, sources, **kwargs):
        """
        Create snapshots for the specified source file systems
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_file_system_snapshots_with_http_info(sources, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] sources: A list of names of source file systems. (required)
        :param SnapshotSuffix suffix: the suffix of the snapshot
        :return: FileSystemSnapshotResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sources', 'suffix']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_file_system_snapshots" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sources' is set
        if ('sources' not in params) or (params['sources'] is None):
            raise ValueError("Missing the required parameter `sources` when calling `create_file_system_snapshots`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sources' in params:
            query_params.append(('sources', params['sources']))
            collection_formats['sources'] = 'csv'

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'suffix' in params:
            body_params = params['suffix']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['AuthTokenHeader']

        return self.api_client.call_api('/1.1/file-system-snapshots', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='FileSystemSnapshotResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_file_system_snapshots(self, name, **kwargs):
        """
        Delete a file system snapshot
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_file_system_snapshots(name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: name of the file system snapshot to be deleted (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_file_system_snapshots_with_http_info(name, **kwargs)
        else:
            (data) = self.delete_file_system_snapshots_with_http_info(name, **kwargs)
            return data

    def delete_file_system_snapshots_with_http_info(self, name, **kwargs):
        """
        Delete a file system snapshot
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_file_system_snapshots_with_http_info(name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: name of the file system snapshot to be deleted (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_file_system_snapshots" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `delete_file_system_snapshots`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in params:
            query_params.append(('name', params['name']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['AuthTokenHeader']

        return self.api_client.call_api('/1.1/file-system-snapshots', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def list_file_system_snapshots(self, **kwargs):
        """
        List file system snapshots
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_file_system_snapshots(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str filter: The filter to be used for query.
        :param str sort: The way to order the results.
        :param int start: start
        :param int limit: limit, should be >= 0
        :param str token: token
        :param bool total: Return a total object in addition to the other results.
        :param bool total_only: Return only the total object.
        :param list[str] names_or_sources: A comma-separated list of resource names. Either the name of the snapshot or the source.
        :return: FileSystemSnapshotResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_file_system_snapshots_with_http_info(**kwargs)
        else:
            (data) = self.list_file_system_snapshots_with_http_info(**kwargs)
            return data

    def list_file_system_snapshots_with_http_info(self, **kwargs):
        """
        List file system snapshots
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_file_system_snapshots_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str filter: The filter to be used for query.
        :param str sort: The way to order the results.
        :param int start: start
        :param int limit: limit, should be >= 0
        :param str token: token
        :param bool total: Return a total object in addition to the other results.
        :param bool total_only: Return only the total object.
        :param list[str] names_or_sources: A comma-separated list of resource names. Either the name of the snapshot or the source.
        :return: FileSystemSnapshotResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filter', 'sort', 'start', 'limit', 'token', 'total', 'total_only', 'names_or_sources']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_file_system_snapshots" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'filter' in params:
            query_params.append(('filter', params['filter']))
        if 'sort' in params:
            query_params.append(('sort', params['sort']))
        if 'start' in params:
            query_params.append(('start', params['start']))
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'token' in params:
            query_params.append(('token', params['token']))
        if 'total' in params:
            query_params.append(('total', params['total']))
        if 'total_only' in params:
            query_params.append(('total_only', params['total_only']))
        if 'names_or_sources' in params:
            query_params.append(('names_or_sources', params['names_or_sources']))
            collection_formats['names_or_sources'] = 'csv'

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['AuthTokenHeader']

        return self.api_client.call_api('/1.1/file-system-snapshots', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='FileSystemSnapshotResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_file_system_snapshots(self, attributes, **kwargs):
        """
        Update an existing file system snapshot
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_file_system_snapshots(attributes, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param SnapshotSuffix attributes: the new attributes, only modifiable fields could be used. (required)
        :param str name: The name of the file system or snapshot to be updated.
        :return: FileSystemSnapshotResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_file_system_snapshots_with_http_info(attributes, **kwargs)
        else:
            (data) = self.update_file_system_snapshots_with_http_info(attributes, **kwargs)
            return data

    def update_file_system_snapshots_with_http_info(self, attributes, **kwargs):
        """
        Update an existing file system snapshot
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_file_system_snapshots_with_http_info(attributes, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param SnapshotSuffix attributes: the new attributes, only modifiable fields could be used. (required)
        :param str name: The name of the file system or snapshot to be updated.
        :return: FileSystemSnapshotResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['attributes', 'name']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_file_system_snapshots" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'attributes' is set
        if ('attributes' not in params) or (params['attributes'] is None):
            raise ValueError("Missing the required parameter `attributes` when calling `update_file_system_snapshots`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in params:
            query_params.append(('name', params['name']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'attributes' in params:
            body_params = params['attributes']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['AuthTokenHeader']

        return self.api_client.call_api('/1.1/file-system-snapshots', 'PATCH',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='FileSystemSnapshotResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
