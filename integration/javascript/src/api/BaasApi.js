/*
 * Hydrogen Integration API
 * The Hydrogen Integration API
 *
 * OpenAPI spec version: 1.2.1
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
    define(['ApiClient', 'model/BaasAccountCO', 'model/BaasAccountVO', 'model/BaasBalanceVO', 'model/BaasClientCO', 'model/BaasClientVO', 'model/BaasStatementsVO', 'model/BaasSubAccountCO', 'model/BaasSubAccountVO', 'model/BaasTransactionsVO'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    module.exports = factory(require('../ApiClient'), require('../model/BaasAccountCO'), require('../model/BaasAccountVO'), require('../model/BaasBalanceVO'), require('../model/BaasClientCO'), require('../model/BaasClientVO'), require('../model/BaasStatementsVO'), require('../model/BaasSubAccountCO'), require('../model/BaasSubAccountVO'), require('../model/BaasTransactionsVO'));
  } else {
    // Browser globals (root is window)
    if (!root.HydrogenIntegrationApi) {
      root.HydrogenIntegrationApi = {};
    }
    root.HydrogenIntegrationApi.BaasApi = factory(root.HydrogenIntegrationApi.ApiClient, root.HydrogenIntegrationApi.BaasAccountCO, root.HydrogenIntegrationApi.BaasAccountVO, root.HydrogenIntegrationApi.BaasBalanceVO, root.HydrogenIntegrationApi.BaasClientCO, root.HydrogenIntegrationApi.BaasClientVO, root.HydrogenIntegrationApi.BaasStatementsVO, root.HydrogenIntegrationApi.BaasSubAccountCO, root.HydrogenIntegrationApi.BaasSubAccountVO, root.HydrogenIntegrationApi.BaasTransactionsVO);
  }
}(this, function(ApiClient, BaasAccountCO, BaasAccountVO, BaasBalanceVO, BaasClientCO, BaasClientVO, BaasStatementsVO, BaasSubAccountCO, BaasSubAccountVO, BaasTransactionsVO) {
  'use strict';

  /**
   * Baas service.
   * @module api/BaasApi
   * @version 1.2.1
   */

  /**
   * Constructs a new BaasApi. 
   * @alias module:api/BaasApi
   * @class
   * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
   * default to {@link module:ApiClient#instance} if unspecified.
   */
  var exports = function(apiClient) {
    this.apiClient = apiClient || ApiClient.instance;


    /**
     * Callback function to receive the result of the createBaasAccountUsingPost operation.
     * @callback module:api/BaasApi~createBaasAccountUsingPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/BaasAccountVO} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * create a Baas account
     * @param {module:model/BaasAccountCO} baasAccountCO baasAccountCO
     * @param {module:api/BaasApi~createBaasAccountUsingPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/BaasAccountVO}
     */
    this.createBaasAccountUsingPost = function(baasAccountCO, callback) {
      var postBody = baasAccountCO;

      // verify the required parameter 'baasAccountCO' is set
      if (baasAccountCO === undefined || baasAccountCO === null) {
        throw new Error("Missing the required parameter 'baasAccountCO' when calling createBaasAccountUsingPost");
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
      var contentTypes = ['application/json'];
      var accepts = ['*/*'];
      var returnType = BaasAccountVO;

      return this.apiClient.callApi(
        '/baas/account', 'POST',
        pathParams, queryParams, collectionQueryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the createBaasClientUsingPost operation.
     * @callback module:api/BaasApi~createBaasClientUsingPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/BaasClientVO} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a Baas Client
     * @param {module:model/BaasClientCO} baasClientCO baasClientCO
     * @param {module:api/BaasApi~createBaasClientUsingPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/BaasClientVO}
     */
    this.createBaasClientUsingPost = function(baasClientCO, callback) {
      var postBody = baasClientCO;

      // verify the required parameter 'baasClientCO' is set
      if (baasClientCO === undefined || baasClientCO === null) {
        throw new Error("Missing the required parameter 'baasClientCO' when calling createBaasClientUsingPost");
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
      var contentTypes = ['application/json'];
      var accepts = ['*/*'];
      var returnType = BaasClientVO;

      return this.apiClient.callApi(
        '/baas/client', 'POST',
        pathParams, queryParams, collectionQueryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the createBaasSubAccountUsingPost operation.
     * @callback module:api/BaasApi~createBaasSubAccountUsingPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/BaasSubAccountVO} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * create a Baas subaccount
     * @param {module:model/BaasSubAccountCO} baasSubAccountCO baasSubAccountCO
     * @param {module:api/BaasApi~createBaasSubAccountUsingPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/BaasSubAccountVO}
     */
    this.createBaasSubAccountUsingPost = function(baasSubAccountCO, callback) {
      var postBody = baasSubAccountCO;

      // verify the required parameter 'baasSubAccountCO' is set
      if (baasSubAccountCO === undefined || baasSubAccountCO === null) {
        throw new Error("Missing the required parameter 'baasSubAccountCO' when calling createBaasSubAccountUsingPost");
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
      var contentTypes = ['application/json'];
      var accepts = ['*/*'];
      var returnType = BaasSubAccountVO;

      return this.apiClient.callApi(
        '/baas/subaccount', 'POST',
        pathParams, queryParams, collectionQueryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the getBaasAccountStatementUsingGet operation.
     * @callback module:api/BaasApi~getBaasAccountStatementUsingGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/BaasStatementsVO} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a Baas account statement
     * @param {Date} endDate end_date
     * @param {String} nucleusAccountId nucleus_account_id
     * @param {Date} startDate start_date
     * @param {Object} opts Optional parameters
     * @param {String} opts.statementType statement_type
     * @param {module:api/BaasApi~getBaasAccountStatementUsingGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/BaasStatementsVO}
     */
    this.getBaasAccountStatementUsingGet = function(endDate, nucleusAccountId, startDate, opts, callback) {
      opts = opts || {};
      var postBody = null;

      // verify the required parameter 'endDate' is set
      if (endDate === undefined || endDate === null) {
        throw new Error("Missing the required parameter 'endDate' when calling getBaasAccountStatementUsingGet");
      }

      // verify the required parameter 'nucleusAccountId' is set
      if (nucleusAccountId === undefined || nucleusAccountId === null) {
        throw new Error("Missing the required parameter 'nucleusAccountId' when calling getBaasAccountStatementUsingGet");
      }

      // verify the required parameter 'startDate' is set
      if (startDate === undefined || startDate === null) {
        throw new Error("Missing the required parameter 'startDate' when calling getBaasAccountStatementUsingGet");
      }


      var pathParams = {
        'nucleus_account_id': nucleusAccountId
      };
      var queryParams = {
        'end_date': endDate,
        'start_date': startDate,
        'statement_type': opts['statementType'],
      };
      var collectionQueryParams = {
      };
      var headerParams = {
      };
      var formParams = {
      };

      var authNames = ['oauth2'];
      var contentTypes = [];
      var accepts = ['*/*'];
      var returnType = BaasStatementsVO;

      return this.apiClient.callApi(
        '/baas/statement/{nucleus_account_id}', 'GET',
        pathParams, queryParams, collectionQueryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the getBaasPortfolioBalanceUsingGet operation.
     * @callback module:api/BaasApi~getBaasPortfolioBalanceUsingGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/BaasBalanceVO} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a Baas portfolio balance
     * @param {String} nucleusPortfolioId nucleus_portfolio_id
     * @param {Object} opts Optional parameters
     * @param {Date} opts.endDate end_date
     * @param {Date} opts.startDate start_date
     * @param {module:api/BaasApi~getBaasPortfolioBalanceUsingGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/BaasBalanceVO}
     */
    this.getBaasPortfolioBalanceUsingGet = function(nucleusPortfolioId, opts, callback) {
      opts = opts || {};
      var postBody = null;

      // verify the required parameter 'nucleusPortfolioId' is set
      if (nucleusPortfolioId === undefined || nucleusPortfolioId === null) {
        throw new Error("Missing the required parameter 'nucleusPortfolioId' when calling getBaasPortfolioBalanceUsingGet");
      }


      var pathParams = {
        'nucleus_portfolio_id': nucleusPortfolioId
      };
      var queryParams = {
        'end_date': opts['endDate'],
        'start_date': opts['startDate'],
      };
      var collectionQueryParams = {
      };
      var headerParams = {
      };
      var formParams = {
      };

      var authNames = ['oauth2'];
      var contentTypes = [];
      var accepts = ['*/*'];
      var returnType = BaasBalanceVO;

      return this.apiClient.callApi(
        '/baas/balance/{nucleus_portfolio_id}', 'GET',
        pathParams, queryParams, collectionQueryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the getBaasPortfolioTransactionUsingGet operation.
     * @callback module:api/BaasApi~getBaasPortfolioTransactionUsingGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/BaasTransactionsVO} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a Baas portfolio transaction
     * @param {String} nucleusPortfolioId nucleus_portfolio_id
     * @param {Object} opts Optional parameters
     * @param {Date} opts.endDate end_date
     * @param {Date} opts.startDate start_date
     * @param {module:api/BaasApi~getBaasPortfolioTransactionUsingGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/BaasTransactionsVO}
     */
    this.getBaasPortfolioTransactionUsingGet = function(nucleusPortfolioId, opts, callback) {
      opts = opts || {};
      var postBody = null;

      // verify the required parameter 'nucleusPortfolioId' is set
      if (nucleusPortfolioId === undefined || nucleusPortfolioId === null) {
        throw new Error("Missing the required parameter 'nucleusPortfolioId' when calling getBaasPortfolioTransactionUsingGet");
      }


      var pathParams = {
        'nucleus_portfolio_id': nucleusPortfolioId
      };
      var queryParams = {
        'end_date': opts['endDate'],
        'start_date': opts['startDate'],
      };
      var collectionQueryParams = {
      };
      var headerParams = {
      };
      var formParams = {
      };

      var authNames = ['oauth2'];
      var contentTypes = [];
      var accepts = ['*/*'];
      var returnType = BaasTransactionsVO;

      return this.apiClient.callApi(
        '/baas/transaction/{nucleus_portfolio_id}', 'GET',
        pathParams, queryParams, collectionQueryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the updateBaasClientUsingPut operation.
     * @callback module:api/BaasApi~updateBaasClientUsingPutCallback
     * @param {String} error Error message, if any.
     * @param {module:model/BaasClientVO} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update a Baas client
     * @param {module:model/BaasClientCO} baasClientCO baasClientCO
     * @param {module:api/BaasApi~updateBaasClientUsingPutCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/BaasClientVO}
     */
    this.updateBaasClientUsingPut = function(baasClientCO, callback) {
      var postBody = baasClientCO;

      // verify the required parameter 'baasClientCO' is set
      if (baasClientCO === undefined || baasClientCO === null) {
        throw new Error("Missing the required parameter 'baasClientCO' when calling updateBaasClientUsingPut");
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
      var contentTypes = ['application/json'];
      var accepts = ['*/*'];
      var returnType = BaasClientVO;

      return this.apiClient.callApi(
        '/baas/client', 'PUT',
        pathParams, queryParams, collectionQueryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }
  };

  return exports;
}));
