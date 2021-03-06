/**
 * Hydrogen Atom API
 * The Hydrogen Atom API
 *
 * OpenAPI spec version: 1.7.0
 * Contact: info@hydrogenplatform.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 *
 * Swagger Codegen version: 2.2.3
 *
 * Do not edit the class manually.
 *
 */

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD. Register as an anonymous module.
    define(['ApiClient', 'model/FundingRequestMap'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    module.exports = factory(require('../ApiClient'), require('./FundingRequestMap'));
  } else {
    // Browser globals (root is window)
    if (!root.HydrogenNucleusApi) {
      root.HydrogenNucleusApi = {};
    }
    root.HydrogenNucleusApi.Roundup = factory(root.HydrogenNucleusApi.ApiClient, root.HydrogenNucleusApi.FundingRequestMap);
  }
}(this, function(ApiClient, FundingRequestMap) {
  'use strict';




  /**
   * The Roundup model module.
   * @module model/Roundup
   * @version 1.7.0
   */

  /**
   * Constructs a new <code>Roundup</code>.
   * Roundup Object
   * @alias module:model/Roundup
   * @class
   * @param accountId {String} account_id
   * @param clientId {String} client_id
   * @param roundupSettingId {String} roundup_setting_id
   */
  var exports = function(accountId, clientId, roundupSettingId) {
    var _this = this;

    _this['account_id'] = accountId;
    _this['client_id'] = clientId;



    _this['roundup_setting_id'] = roundupSettingId;


  };

  /**
   * Constructs a <code>Roundup</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/Roundup} obj Optional instance to populate.
   * @return {module:model/Roundup} The populated <code>Roundup</code> instance.
   */
  exports.constructFromObject = function(data, obj) {
    if (data) {
      obj = obj || new exports();

      if (data.hasOwnProperty('account_id')) {
        obj['account_id'] = ApiClient.convertToType(data['account_id'], 'String');
      }
      if (data.hasOwnProperty('client_id')) {
        obj['client_id'] = ApiClient.convertToType(data['client_id'], 'String');
      }
      if (data.hasOwnProperty('create_date')) {
        obj['create_date'] = ApiClient.convertToType(data['create_date'], 'Date');
      }
      if (data.hasOwnProperty('funding_requests')) {
        obj['funding_requests'] = ApiClient.convertToType(data['funding_requests'], [FundingRequestMap]);
      }
      if (data.hasOwnProperty('id')) {
        obj['id'] = ApiClient.convertToType(data['id'], 'String');
      }
      if (data.hasOwnProperty('roundup_setting_id')) {
        obj['roundup_setting_id'] = ApiClient.convertToType(data['roundup_setting_id'], 'String');
      }
      if (data.hasOwnProperty('total_roundup_amount')) {
        obj['total_roundup_amount'] = ApiClient.convertToType(data['total_roundup_amount'], 'Number');
      }
      if (data.hasOwnProperty('update_date')) {
        obj['update_date'] = ApiClient.convertToType(data['update_date'], 'Date');
      }
    }
    return obj;
  }

  /**
   * account_id
   * @member {String} account_id
   */
  exports.prototype['account_id'] = undefined;
  /**
   * client_id
   * @member {String} client_id
   */
  exports.prototype['client_id'] = undefined;
  /**
   * @member {Date} create_date
   */
  exports.prototype['create_date'] = undefined;
  /**
   * @member {Array.<module:model/FundingRequestMap>} funding_requests
   */
  exports.prototype['funding_requests'] = undefined;
  /**
   * @member {String} id
   */
  exports.prototype['id'] = undefined;
  /**
   * roundup_setting_id
   * @member {String} roundup_setting_id
   */
  exports.prototype['roundup_setting_id'] = undefined;
  /**
   * totalRoundupAmount
   * @member {Number} total_roundup_amount
   */
  exports.prototype['total_roundup_amount'] = undefined;
  /**
   * @member {Date} update_date
   */
  exports.prototype['update_date'] = undefined;



  return exports;
}));


