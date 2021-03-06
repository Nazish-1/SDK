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
  class TokenTransferApi
    attr_accessor :api_client

    def initialize(api_client = ApiClient.default)
      @api_client = api_client
    end
    # Creates Token Transfer record
    # @param token_transfer_params It enables a user to transfer Tokens
    # @param [Hash] opts the optional parameters
    # @return [TransactionSuccessResponse]
    def create_token_transfer_using_post(token_transfer_params, opts = {})
      data, _status_code, _headers = create_token_transfer_using_post_with_http_info(token_transfer_params, opts)
      data
    end

    # Creates Token Transfer record
    # @param token_transfer_params It enables a user to transfer Tokens
    # @param [Hash] opts the optional parameters
    # @return [Array<(TransactionSuccessResponse, Fixnum, Hash)>] TransactionSuccessResponse data, response status code and response headers
    def create_token_transfer_using_post_with_http_info(token_transfer_params, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: TokenTransferApi.create_token_transfer_using_post ...'
      end
      # verify the required parameter 'token_transfer_params' is set
      if @api_client.config.client_side_validation && token_transfer_params.nil?
        fail ArgumentError, "Missing the required parameter 'token_transfer_params' when calling TokenTransferApi.create_token_transfer_using_post"
      end
      # resource path
      local_var_path = '/token_transfer'

      # query parameters
      query_params = {}

      # header parameters
      header_params = {}
      # HTTP header 'Accept' (if needed)
      header_params['Accept'] = @api_client.select_header_accept(['application/json'])

      # form parameters
      form_params = {}

      # http body (model)
      post_body = @api_client.object_to_http_body(token_transfer_params)
      auth_names = ['oauth2']
      data, status_code, headers = @api_client.call_api(:POST, local_var_path,
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => 'TransactionSuccessResponse')
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: TokenTransferApi#create_token_transfer_using_post\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end
    # Fetch Token Transfer record list
    # @param [Hash] opts the optional parameters
    # @option opts [String] :wallet_id To filter response Token Transfer list by Wallet ID
    # @option opts [Integer] :page To filter response Token Transfer list by page number
    # @option opts [Integer] :size Number of records per page
    # @option opts [String] :order_by Field to sort record list
    # @option opts [BOOLEAN] :ascending Sorting order
    # @option opts [BOOLEAN] :get_latest To fetch latest (one) record
    # @return [PageTokenTransferResponse]
    def get_token_transfer_all_using_get(opts = {})
      data, _status_code, _headers = get_token_transfer_all_using_get_with_http_info(opts)
      data
    end

    # Fetch Token Transfer record list
    # @param [Hash] opts the optional parameters
    # @option opts [String] :wallet_id To filter response Token Transfer list by Wallet ID
    # @option opts [Integer] :page To filter response Token Transfer list by page number
    # @option opts [Integer] :size Number of records per page
    # @option opts [String] :order_by Field to sort record list
    # @option opts [BOOLEAN] :ascending Sorting order
    # @option opts [BOOLEAN] :get_latest To fetch latest (one) record
    # @return [Array<(PageTokenTransferResponse, Fixnum, Hash)>] PageTokenTransferResponse data, response status code and response headers
    def get_token_transfer_all_using_get_with_http_info(opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: TokenTransferApi.get_token_transfer_all_using_get ...'
      end
      # resource path
      local_var_path = '/token_transfer'

      # query parameters
      query_params = {}
      query_params[:'wallet_id'] = opts[:'wallet_id'] if !opts[:'wallet_id'].nil?
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
        :return_type => 'PageTokenTransferResponse')
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: TokenTransferApi#get_token_transfer_all_using_get\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end
    # Fetch Token Transfer record details
    # @param token_transfer_id Token Transfer ID
    # @param [Hash] opts the optional parameters
    # @return [TokenTransferResponse]
    def get_token_transfer_using_get(token_transfer_id, opts = {})
      data, _status_code, _headers = get_token_transfer_using_get_with_http_info(token_transfer_id, opts)
      data
    end

    # Fetch Token Transfer record details
    # @param token_transfer_id Token Transfer ID
    # @param [Hash] opts the optional parameters
    # @return [Array<(TokenTransferResponse, Fixnum, Hash)>] TokenTransferResponse data, response status code and response headers
    def get_token_transfer_using_get_with_http_info(token_transfer_id, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: TokenTransferApi.get_token_transfer_using_get ...'
      end
      # verify the required parameter 'token_transfer_id' is set
      if @api_client.config.client_side_validation && token_transfer_id.nil?
        fail ArgumentError, "Missing the required parameter 'token_transfer_id' when calling TokenTransferApi.get_token_transfer_using_get"
      end
      # resource path
      local_var_path = '/token_transfer/{token_transfer_id}'.sub('{' + 'token_transfer_id' + '}', token_transfer_id.to_s)

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
        :return_type => 'TokenTransferResponse')
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: TokenTransferApi#get_token_transfer_using_get\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end
  end
end
