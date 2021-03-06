/*
 * Molecule API Documentation
 * The Hydrogen Molecule API
 *
 * OpenAPI spec version: 1.3.0
 * Contact: info@hydrogenplatform.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 *
 * Swagger Codegen version: 2.4.14
 *
 * Do not edit the class manually.
 *
 */

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD. Register as an anonymous module.
    define(['ApiClient', 'model/ErrorResponse', 'model/PageWebhookResponse', 'model/WebhookParams', 'model/WebhookResponse'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    module.exports = factory(require('../ApiClient'), require('../model/ErrorResponse'), require('../model/PageWebhookResponse'), require('../model/WebhookParams'), require('../model/WebhookResponse'));
  } else {
    // Browser globals (root is window)
    if (!root.MoleculeApiDocumentation) {
      root.MoleculeApiDocumentation = {};
    }
    root.MoleculeApiDocumentation.WebhookApi = factory(root.MoleculeApiDocumentation.ApiClient, root.MoleculeApiDocumentation.ErrorResponse, root.MoleculeApiDocumentation.PageWebhookResponse, root.MoleculeApiDocumentation.WebhookParams, root.MoleculeApiDocumentation.WebhookResponse);
  }
}(this, function(ApiClient, ErrorResponse, PageWebhookResponse, WebhookParams, WebhookResponse) {
  'use strict';

  /**
   * Webhook service.
   * @module api/WebhookApi
   * @version 1.3.0
   */

  /**
   * Constructs a new WebhookApi. 
   * @alias module:api/WebhookApi
   * @class
   * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
   * default to {@link module:ApiClient#instance} if unspecified.
   */
  var exports = function(apiClient) {
    this.apiClient = apiClient || ApiClient.instance;


    /**
     * Callback function to receive the result of the createWebhookUsingPost operation.
     * @callback module:api/WebhookApi~createWebhookUsingPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/WebhookResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Creates a new Webhook record
     * @param {module:model/WebhookParams} webhookParams It enables a user to create a Webhook record
     * @param {module:api/WebhookApi~createWebhookUsingPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/WebhookResponse}
     */
    this.createWebhookUsingPost = function(webhookParams, callback) {
      var postBody = webhookParams;

      // verify the required parameter 'webhookParams' is set
      if (webhookParams === undefined || webhookParams === null) {
        throw new Error("Missing the required parameter 'webhookParams' when calling createWebhookUsingPost");
      }


      var pathParams = {
      };
      var queryParams = {
      };
      var collectionQueryParams = {
      };
      var headerParams = {
      };
      var formParams = {
      };

      var authNames = ['oauth2'];
      var contentTypes = [];
      var accepts = ['application/json'];
      var returnType = WebhookResponse;

      return this.apiClient.callApi(
        '/webhook', 'POST',
        pathParams, queryParams, collectionQueryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteWebhookUsingDelete operation.
     * @callback module:api/WebhookApi~deleteWebhookUsingDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete Webhook
     * @param {String} webhookId Webhook ID
     * @param {module:api/WebhookApi~deleteWebhookUsingDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    this.deleteWebhookUsingDelete = function(webhookId, callback) {
      var postBody = null;

      // verify the required parameter 'webhookId' is set
      if (webhookId === undefined || webhookId === null) {
        throw new Error("Missing the required parameter 'webhookId' when calling deleteWebhookUsingDelete");
      }


      var pathParams = {
        'webhook_id': webhookId
      };
      var queryParams = {
      };
      var collectionQueryParams = {
      };
      var headerParams = {
      };
      var formParams = {
      };

      var authNames = ['oauth2'];
      var contentTypes = [];
      var accepts = ['application/json'];
      var returnType = null;

      return this.apiClient.callApi(
        '/webhook/{webhook_id}', 'DELETE',
        pathParams, queryParams, collectionQueryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the getWebhookAllUsingGet operation.
     * @callback module:api/WebhookApi~getWebhookAllUsingGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PageWebhookResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Fetch Webhook list
     * @param {Object} opts Optional parameters
     * @param {Number} opts.page To filter response webhook list by page number
     * @param {Number} opts.size Number of records per page
     * @param {String} opts.orderBy Field to sort record list
     * @param {Boolean} opts.ascending Sorting order
     * @param {Boolean} opts.getLatest To fetch latest (one) record
     * @param {module:api/WebhookApi~getWebhookAllUsingGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PageWebhookResponse}
     */
    this.getWebhookAllUsingGet = function(opts, callback) {
      opts = opts || {};
      var postBody = null;


      var pathParams = {
      };
      var queryParams = {
        'page': opts['page'],
        'size': opts['size'],
        'order_by': opts['orderBy'],
        'ascending': opts['ascending'],
        'get_latest': opts['getLatest'],
      };
      var collectionQueryParams = {
      };
      var headerParams = {
      };
      var formParams = {
      };

      var authNames = ['oauth2'];
      var contentTypes = [];
      var accepts = ['application/json'];
      var returnType = PageWebhookResponse;

      return this.apiClient.callApi(
        '/webhook', 'GET',
        pathParams, queryParams, collectionQueryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the getWebhookUsingGet operation.
     * @callback module:api/WebhookApi~getWebhookUsingGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/WebhookResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Fetch Webhook details
     * @param {String} webhookId Webhook ID
     * @param {module:api/WebhookApi~getWebhookUsingGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/WebhookResponse}
     */
    this.getWebhookUsingGet = function(webhookId, callback) {
      var postBody = null;

      // verify the required parameter 'webhookId' is set
      if (webhookId === undefined || webhookId === null) {
        throw new Error("Missing the required parameter 'webhookId' when calling getWebhookUsingGet");
      }


      var pathParams = {
        'webhook_id': webhookId
      };
      var queryParams = {
      };
      var collectionQueryParams = {
      };
      var headerParams = {
      };
      var formParams = {
      };

      var authNames = ['oauth2'];
      var contentTypes = [];
      var accepts = ['application/json'];
      var returnType = WebhookResponse;

      return this.apiClient.callApi(
        '/webhook/{webhook_id}', 'GET',
        pathParams, queryParams, collectionQueryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the updateWebhookUsingPut operation.
     * @callback module:api/WebhookApi~updateWebhookUsingPutCallback
     * @param {String} error Error message, if any.
     * @param {module:model/WebhookResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update Webhook details
     * @param {String} webhookId Webhook ID
     * @param {module:model/WebhookParams} webhookUpdateParams Webhook details to be updated
     * @param {module:api/WebhookApi~updateWebhookUsingPutCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/WebhookResponse}
     */
    this.updateWebhookUsingPut = function(webhookId, webhookUpdateParams, callback) {
      var postBody = webhookUpdateParams;

      // verify the required parameter 'webhookId' is set
      if (webhookId === undefined || webhookId === null) {
        throw new Error("Missing the required parameter 'webhookId' when calling updateWebhookUsingPut");
      }

      // verify the required parameter 'webhookUpdateParams' is set
      if (webhookUpdateParams === undefined || webhookUpdateParams === null) {
        throw new Error("Missing the required parameter 'webhookUpdateParams' when calling updateWebhookUsingPut");
      }


      var pathParams = {
        'webhook_id': webhookId
      };
      var queryParams = {
      };
      var collectionQueryParams = {
      };
      var headerParams = {
      };
      var formParams = {
      };

      var authNames = ['oauth2'];
      var contentTypes = [];
      var accepts = ['application/json'];
      var returnType = WebhookResponse;

      return this.apiClient.callApi(
        '/webhook/{webhook_id}', 'PUT',
        pathParams, queryParams, collectionQueryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }
  };

  return exports;
}));
