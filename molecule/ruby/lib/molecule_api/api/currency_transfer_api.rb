=begin
#Molecule API Documentation

#The Hydrogen Molecule API

OpenAPI spec version: 1.3.0
Contact: info@hydrogenplatform.com
Generated by: https://github.com/swagger-api/swagger-codegen.git
Swagger Codegen version: 2.4.14

=end

require 'uri'

module MoleculeApi
  class CurrencyTransferApi
    attr_accessor :api_client

    def initialize(api_client = ApiClient.default)
      @api_client = api_client
    end
    # Creates Currency Transfer record
    # @param currency_transfer_params It enables a user to transfer Currency
    # @param [Hash] opts the optional parameters
    # @return [TransactionSuccessResponse]
    def create_currency_transfer_using_post(currency_transfer_params, opts = {})
      data, _status_code, _headers = create_currency_transfer_using_post_with_http_info(currency_transfer_params, opts)
      data
    end

    # Creates Currency Transfer record
    # @param currency_transfer_params It enables a user to transfer Currency
    # @param [Hash] opts the optional parameters
    # @return [Array<(TransactionSuccessResponse, Fixnum, Hash)>] TransactionSuccessResponse data, response status code and response headers
    def create_currency_transfer_using_post_with_http_info(currency_transfer_params, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: CurrencyTransferApi.create_currency_transfer_using_post ...'
      end
      # verify the required parameter 'currency_transfer_params' is set
      if @api_client.config.client_side_validation && currency_transfer_params.nil?
        fail ArgumentError, "Missing the required parameter 'currency_transfer_params' when calling CurrencyTransferApi.create_currency_transfer_using_post"
      end
      # resource path
      local_var_path = '/currency_transfer'

      # query parameters
      query_params = {}

      # header parameters
      header_params = {}
      # HTTP header 'Accept' (if needed)
      header_params['Accept'] = @api_client.select_header_accept(['application/json'])

      # form parameters
      form_params = {}

      # http body (model)
      post_body = @api_client.object_to_http_body(currency_transfer_params)
      auth_names = ['oauth2']
      data, status_code, headers = @api_client.call_api(:POST, local_var_path,
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => 'TransactionSuccessResponse')
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: CurrencyTransferApi#create_currency_transfer_using_post\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end
    # Fetch Currency Transfer record list
    # @param [Hash] opts the optional parameters
    # @option opts [String] :wallet_id To filter response Currency Transfer list by Wallet ID
    # @option opts [String] :currency_id To filter response Currency Transfer list by Currency ID
    # @option opts [Integer] :page To filter response Currency Transfer list by page number
    # @option opts [Integer] :size Number of records per page
    # @option opts [String] :order_by Field to sort record list
    # @option opts [BOOLEAN] :ascending Sorting order
    # @option opts [BOOLEAN] :get_latest To fetch latest (one) record
    # @return [PageCurrencyTransferResponse]
    def get_currency_transfer_all_using_get(opts = {})
      data, _status_code, _headers = get_currency_transfer_all_using_get_with_http_info(opts)
      data
    end

    # Fetch Currency Transfer record list
    # @param [Hash] opts the optional parameters
    # @option opts [String] :wallet_id To filter response Currency Transfer list by Wallet ID
    # @option opts [String] :currency_id To filter response Currency Transfer list by Currency ID
    # @option opts [Integer] :page To filter response Currency Transfer list by page number
    # @option opts [Integer] :size Number of records per page
    # @option opts [String] :order_by Field to sort record list
    # @option opts [BOOLEAN] :ascending Sorting order
    # @option opts [BOOLEAN] :get_latest To fetch latest (one) record
    # @return [Array<(PageCurrencyTransferResponse, Fixnum, Hash)>] PageCurrencyTransferResponse data, response status code and response headers
    def get_currency_transfer_all_using_get_with_http_info(opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: CurrencyTransferApi.get_currency_transfer_all_using_get ...'
      end
      # resource path
      local_var_path = '/currency_transfer'

      # query parameters
      query_params = {}
      query_params[:'wallet_id'] = opts[:'wallet_id'] if !opts[:'wallet_id'].nil?
      query_params[:'currency_id'] = opts[:'currency_id'] if !opts[:'currency_id'].nil?
      query_params[:'page'] = opts[:'page'] if !opts[:'page'].nil?
      query_params[:'size'] = opts[:'size'] if !opts[:'size'].nil?
      query_params[:'order_by'] = opts[:'order_by'] if !opts[:'order_by'].nil?
      query_params[:'ascending'] = opts[:'ascending'] if !opts[:'ascending'].nil?
      query_params[:'get_latest'] = opts[:'get_latest'] if !opts[:'get_latest'].nil?

      # header parameters
      header_params = {}
      # HTTP header 'Accept' (if needed)
      header_params['Accept'] = @api_client.select_header_accept(['application/json'])

      # form parameters
      form_params = {}

      # http body (model)
      post_body = nil
      auth_names = ['oauth2']
      data, status_code, headers = @api_client.call_api(:GET, local_var_path,
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => 'PageCurrencyTransferResponse')
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: CurrencyTransferApi#get_currency_transfer_all_using_get\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end
    # Fetch Currency Transfer record details
    # @param currency_transfer_id Currency Transfer ID
    # @param [Hash] opts the optional parameters
    # @return [CurrencyTransferResponse]
    def get_currency_transfer_using_get(currency_transfer_id, opts = {})
      data, _status_code, _headers = get_currency_transfer_using_get_with_http_info(currency_transfer_id, opts)
      data
    end

    # Fetch Currency Transfer record details
    # @param currency_transfer_id Currency Transfer ID
    # @param [Hash] opts the optional parameters
    # @return [Array<(CurrencyTransferResponse, Fixnum, Hash)>] CurrencyTransferResponse data, response status code and response headers
    def get_currency_transfer_using_get_with_http_info(currency_transfer_id, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: CurrencyTransferApi.get_currency_transfer_using_get ...'
      end
      # verify the required parameter 'currency_transfer_id' is set
      if @api_client.config.client_side_validation && currency_transfer_id.nil?
        fail ArgumentError, "Missing the required parameter 'currency_transfer_id' when calling CurrencyTransferApi.get_currency_transfer_using_get"
      end
      # resource path
      local_var_path = '/currency_transfer/{currency_transfer_id}'.sub('{' + 'currency_transfer_id' + '}', currency_transfer_id.to_s)

      # query parameters
      query_params = {}

      # header parameters
      header_params = {}
      # HTTP header 'Accept' (if needed)
      header_params['Accept'] = @api_client.select_header_accept(['application/json'])

      # form parameters
      form_params = {}

      # http body (model)
      post_body = nil
      auth_names = ['oauth2']
      data, status_code, headers = @api_client.call_api(:GET, local_var_path,
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => 'CurrencyTransferResponse')
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: CurrencyTransferApi#get_currency_transfer_using_get\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end
  end
end