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
    define(['ApiClient'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    module.exports = factory(require('../ApiClient'));
  } else {
    // Browser globals (root is window)
    if (!root.MoleculeApiDocumentation) {
      root.MoleculeApiDocumentation = {};
    }
    root.MoleculeApiDocumentation.WalletKeyResponse = factory(root.MoleculeApiDocumentation.ApiClient);
  }
}(this, function(ApiClient) {
  'use strict';

  /**
   * The WalletKeyResponse model module.
   * @module model/WalletKeyResponse
   * @version 1.3.0
   */

  /**
   * Constructs a new <code>WalletKeyResponse</code>.
   * @alias module:model/WalletKeyResponse
   * @class
   */
  var exports = function() {
  };

  /**
   * Constructs a <code>WalletKeyResponse</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/WalletKeyResponse} obj Optional instance to populate.
   * @return {module:model/WalletKeyResponse} The populated <code>WalletKeyResponse</code> instance.
   */
  exports.constructFromObject = function(data, obj) {
    if (data) {
      obj = obj || new exports();
      if (data.hasOwnProperty('id'))
        obj.id = ApiClient.convertToType(data['id'], 'String');
      if (data.hasOwnProperty('key_id'))
        obj.keyId = ApiClient.convertToType(data['key_id'], 'String');
      if (data.hasOwnProperty('key_server'))
        obj.keyServer = ApiClient.convertToType(data['key_server'], 'String');
      if (data.hasOwnProperty('private_key'))
        obj.privateKey = ApiClient.convertToType(data['private_key'], 'String');
      if (data.hasOwnProperty('address'))
        obj.address = ApiClient.convertToType(data['address'], 'String');
      if (data.hasOwnProperty('record_status'))
        obj.recordStatus = ApiClient.convertToType(data['record_status'], 'String');
      if (data.hasOwnProperty('is_active'))
        obj.isActive = ApiClient.convertToType(data['is_active'], 'Boolean');
      if (data.hasOwnProperty('create_date'))
        obj.createDate = ApiClient.convertToType(data['create_date'], 'Date');
      if (data.hasOwnProperty('update_date'))
        obj.updateDate = ApiClient.convertToType(data['update_date'], 'Date');
    }
    return obj;
  }

  /**
   * @member {String} id
   */
  exports.prototype.id = undefined;

  /**
   * @member {String} keyId
   */
  exports.prototype.keyId = undefined;

  /**
   * @member {String} keyServer
   */
  exports.prototype.keyServer = undefined;

  /**
   * @member {String} privateKey
   */
  exports.prototype.privateKey = undefined;

  /**
   * @member {String} address
   */
  exports.prototype.address = undefined;

  /**
   * @member {String} recordStatus
   */
  exports.prototype.recordStatus = undefined;

  /**
   * @member {Boolean} isActive
   */
  exports.prototype.isActive = undefined;

  /**
   * @member {Date} createDate
   */
  exports.prototype.createDate = undefined;

  /**
   * @member {Date} updateDate
   */
  exports.prototype.updateDate = undefined;

  return exports;

}));
