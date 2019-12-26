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
    root.molecule_api.WebhookUpdatePayload = factory(root.molecule_api.ApiClient);
  }
}(this, function(ApiClient) {
  'use strict';




  /**
   * The WebhookUpdatePayload model module.
   * @module model/WebhookUpdatePayload
   * @version 1.0.0
   */

  /**
   * Constructs a new <code>WebhookUpdatePayload</code>.
   * @alias module:model/WebhookUpdatePayload
   * @class
   */
  var exports = function() {
    var _this = this;




  };

  /**
   * Constructs a <code>WebhookUpdatePayload</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/WebhookUpdatePayload} obj Optional instance to populate.
   * @return {module:model/WebhookUpdatePayload} The populated <code>WebhookUpdatePayload</code> instance.
   */
  exports.constructFromObject = function(data, obj) {
    if (data) {
      obj = obj || new exports();

      if (data.hasOwnProperty('molecule_service')) {
        obj['molecule_service'] = ApiClient.convertToType(data['molecule_service'], ['String']);
      }
      if (data.hasOwnProperty('url')) {
        obj['url'] = ApiClient.convertToType(data['url'], 'String');
      }
      if (data.hasOwnProperty('is_active')) {
        obj['is_active'] = ApiClient.convertToType(data['is_active'], 'Boolean');
      }
    }
    return obj;
  }

  /**
   * The array of molecule services for a webhook to notify.
   * @member {Array.<String>} molecule_service
   */
  exports.prototype['molecule_service'] = undefined;
  /**
   * The url you want to receive the payloads to.
   * @member {String} url
   */
  exports.prototype['url'] = undefined;
  /**
   * Indicates if this webhook is active.
   * @member {Boolean} is_active
   */
  exports.prototype['is_active'] = undefined;



  return exports;
}));

