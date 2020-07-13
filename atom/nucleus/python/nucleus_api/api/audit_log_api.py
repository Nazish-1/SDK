# coding: utf-8

"""
    Hydrogen Atom API

    The Hydrogen Atom API  # noqa: E501

    OpenAPI spec version: 1.7.0
    Contact: info@hydrogenplatform.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from nucleus_api.api_client import ApiClient


class AuditLogApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_audit_log_using_post(self, audit_log, **kwargs):  # noqa: E501
        """Create a audit log  # noqa: E501

        Create a new audit log.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_audit_log_using_post(audit_log, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AuditLog audit_log: auditLog (required)
        :return: AuditLog
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_audit_log_using_post_with_http_info(audit_log, **kwargs)  # noqa: E501
        else:
            (data) = self.create_audit_log_using_post_with_http_info(audit_log, **kwargs)  # noqa: E501
            return data

    def create_audit_log_using_post_with_http_info(self, audit_log, **kwargs):  # noqa: E501
        """Create a audit log  # noqa: E501

        Create a new audit log.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_audit_log_using_post_with_http_info(audit_log, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AuditLog audit_log: auditLog (required)
        :return: AuditLog
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['audit_log']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_audit_log_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'audit_log' is set
        if ('audit_log' not in params or
                params['audit_log'] is None):
            raise ValueError("Missing the required parameter `audit_log` when calling `create_audit_log_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'audit_log' in params:
            body_params = params['audit_log']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/audit_log', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AuditLog',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_audit_log_all_using_get(self, **kwargs):  # noqa: E501
        """List all audit log  # noqa: E501

        Get details for all audit log.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_audit_log_all_using_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool ascending: ascending
        :param str filter: filter
        :param str order_by: order_by
        :param int page: page
        :param int size: size
        :return: PageAuditLog
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_audit_log_all_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_audit_log_all_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_audit_log_all_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """List all audit log  # noqa: E501

        Get details for all audit log.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_audit_log_all_using_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool ascending: ascending
        :param str filter: filter
        :param str order_by: order_by
        :param int page: page
        :param int size: size
        :return: PageAuditLog
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ascending', 'filter', 'order_by', 'page', 'size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_audit_log_all_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ascending' in params:
            query_params.append(('ascending', params['ascending']))  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('order_by', params['order_by']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'size' in params:
            query_params.append(('size', params['size']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/audit_log', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PageAuditLog',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_audit_log_using_get(self, audit_log_id, **kwargs):  # noqa: E501
        """Retrieve a audit log  # noqa: E501

        Retrieve the information for a audit log.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_audit_log_using_get(audit_log_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str audit_log_id: UUID audit_log_id (required)
        :return: AuditLog
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_audit_log_using_get_with_http_info(audit_log_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_audit_log_using_get_with_http_info(audit_log_id, **kwargs)  # noqa: E501
            return data

    def get_audit_log_using_get_with_http_info(self, audit_log_id, **kwargs):  # noqa: E501
        """Retrieve a audit log  # noqa: E501

        Retrieve the information for a audit log.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_audit_log_using_get_with_http_info(audit_log_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str audit_log_id: UUID audit_log_id (required)
        :return: AuditLog
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['audit_log_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_audit_log_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'audit_log_id' is set
        if ('audit_log_id' not in params or
                params['audit_log_id'] is None):
            raise ValueError("Missing the required parameter `audit_log_id` when calling `get_audit_log_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'audit_log_id' in params:
            path_params['audit_log_id'] = params['audit_log_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/audit_log/{audit_log_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AuditLog',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)