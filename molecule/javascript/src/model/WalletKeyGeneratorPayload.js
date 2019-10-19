/**
 * Hydrogen Molecule API
 * The Hydrogen Molecule API
 *
 * OpenAPI spec version: 1.0.0
 * Contact: info@hydrogenplatform.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 *
 * Swagger Codegen version: 2.4.8-SNAPSHOT
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
    if (!root.molecule_api) {
      root.molecule_api = {};
    }
    root.molecule_api.WalletKeyGeneratorPayload = factory(root.molecule_api.ApiClient);
  }
}(this, function(ApiClient) {
  'use strict';




  /**
   * The WalletKeyGeneratorPayload model module.
   * @module model/WalletKeyGeneratorPayload
   * @version 1.0.0
   */

  /**
   * Constructs a new <code>WalletKeyGeneratorPayload</code>.
   * @alias module:model/WalletKeyGeneratorPayload
   * @class
   * @param walletId {String} The ID of the wallet the keys are generating for
   */
  var exports = function(walletId) {
    var _this = this;

    _this['wallet_id'] = walletId;
  };

  /**
   * Constructs a <code>WalletKeyGeneratorPayload</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/WalletKeyGeneratorPayload} obj Optional instance to populate.
   * @return {module:model/WalletKeyGeneratorPayload} The populated <code>WalletKeyGeneratorPayload</code> instance.
   */
  exports.constructFromObject = function(data, obj) {
    if (data) {
      obj = obj || new exports();

      if (data.hasOwnProperty('wallet_id')) {
        obj['wallet_id'] = ApiClient.convertToType(data['wallet_id'], 'String');
      }
    }
    return obj;
  }

  /**
   * The ID of the wallet the keys are generating for
   * @member {String} wallet_id
   */
  exports.prototype['wallet_id'] = undefined;



  return exports;
}));

