/**
 * Hydrogen Atom API
 * The Hydrogen Atom API
 *
 * OpenAPI spec version: 1.0.0
 * Contact: info@hydrogenplatform.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 *
 * Swagger Codegen version: 2.4.2-SNAPSHOT
 *
 * Do not edit the class manually.
 *
 */

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD. Register as an anonymous module.
    define(['ApiClient', 'model/CreateFaqResponse', 'model/FaqPayloadFaqKeywords', 'model/SecondaryId'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    module.exports = factory(require('../ApiClient'), require('./CreateFaqResponse'), require('./FaqPayloadFaqKeywords'), require('./SecondaryId'));
  } else {
    // Browser globals (root is window)
    if (!root.atom_api) {
      root.atom_api = {};
    }
    root.atom_api.SpecificFaqResponse = factory(root.atom_api.ApiClient, root.atom_api.CreateFaqResponse, root.atom_api.FaqPayloadFaqKeywords, root.atom_api.SecondaryId);
  }
}(this, function(ApiClient, CreateFaqResponse, FaqPayloadFaqKeywords, SecondaryId) {
  'use strict';




  /**
   * The SpecificFaqResponse model module.
   * @module model/SpecificFaqResponse
   * @version 1.0.0
   */

  /**
   * Constructs a new <code>SpecificFaqResponse</code>.
   * @alias module:model/SpecificFaqResponse
   * @class
   * @implements module:model/CreateFaqResponse
   * @param question {String} Value for the question in the FAQ
   * @param answer {String} Value for the answer to the question in the FAQ
   */
  var exports = function(question, answer) {
    var _this = this;

    CreateFaqResponse.call(_this, question, answer);

  };

  /**
   * Constructs a <code>SpecificFaqResponse</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/SpecificFaqResponse} obj Optional instance to populate.
   * @return {module:model/SpecificFaqResponse} The populated <code>SpecificFaqResponse</code> instance.
   */
  exports.constructFromObject = function(data, obj) {
    if (data) {
      obj = obj || new exports();

      CreateFaqResponse.constructFromObject(data, obj);
      if (data.hasOwnProperty('update_date')) {
        obj['update_date'] = ApiClient.convertToType(data['update_date'], 'String');
      }
    }
    return obj;
  }

  /**
   * Datetime the FAQ was last updated
   * @member {String} update_date
   */
  exports.prototype['update_date'] = undefined;

  // Implement CreateFaqResponse interface:
  /**
   * Value for the question in the FAQ
   * @member {String} question
   */
exports.prototype['question'] = undefined;

  /**
   * Value for the answer to the question in the FAQ
   * @member {String} answer
   */
exports.prototype['answer'] = undefined;

  /**
   * Category that the FAQ falls under
   * @member {String} category
   */
exports.prototype['category'] = undefined;

  /**
   * Subcategory that the FAQ falls under within a category
   * @member {String} subcategory
   */
exports.prototype['subcategory'] = undefined;

  /**
   * Indicates if the FAQ is active. Defaults to true which indicates that the FAQ is active
   * @member {Boolean} is_active
   * @default true
   */
exports.prototype['is_active'] = true;

  /**
   * Order number of the FAQ. For example 3 indicates it’s the third FAQ in a list. Must be a whole number
   * @member {Number} number
   */
exports.prototype['number'] = undefined;

  /**
   * File name used to optimize finding the FAQ in a search engine query
   * @member {String} seo_name
   */
exports.prototype['seo_name'] = undefined;

  /**
   * @member {Array.<module:model/FaqPayloadFaqKeywords>} faq_keywords
   */
exports.prototype['faq_keywords'] = undefined;

  /**
   * Indicator for whether or not this is a featured FAQ. Defaults to false indicating it is not featured
   * @member {Boolean} is_featured
   * @default false
   */
exports.prototype['is_featured'] = false;

  /**
   * @member {module:model/SecondaryId} secondary_id
   */
exports.prototype['secondary_id'] = undefined;

  /**
   * ID of the FAQ
   * @member {String} id
   */
exports.prototype['id'] = undefined;

  /**
   * Datetime the FAQ was created
   * @member {String} create_date
   */
exports.prototype['create_date'] = undefined;



  return exports;
}));

