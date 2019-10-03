/**
 * Hydrogen Atom API
 * The Hydrogen Atom API
 *
 * OpenAPI spec version: 1.0.1
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
    define(['ApiClient', 'model/BudgetPayloadAggregationAccounts', 'model/BudgetPayloadBudget', 'model/CreateBudgetResponse', 'model/SecondaryId'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    module.exports = factory(require('../ApiClient'), require('./BudgetPayloadAggregationAccounts'), require('./BudgetPayloadBudget'), require('./CreateBudgetResponse'), require('./SecondaryId'));
  } else {
    // Browser globals (root is window)
    if (!root.atom_api) {
      root.atom_api = {};
    }
    root.atom_api.SpecificBudgetResponse = factory(root.atom_api.ApiClient, root.atom_api.BudgetPayloadAggregationAccounts, root.atom_api.BudgetPayloadBudget, root.atom_api.CreateBudgetResponse, root.atom_api.SecondaryId);
  }
}(this, function(ApiClient, BudgetPayloadAggregationAccounts, BudgetPayloadBudget, CreateBudgetResponse, SecondaryId) {
  'use strict';




  /**
   * The SpecificBudgetResponse model module.
   * @module model/SpecificBudgetResponse
   * @version 1.0.1
   */

  /**
   * Constructs a new <code>SpecificBudgetResponse</code>.
   * @alias module:model/SpecificBudgetResponse
   * @class
   * @implements module:model/CreateBudgetResponse
   * @param name {String} Name of the budget
   * @param clientId {String} The ID of the client the budget belongs to
   * @param currencyCode {String} Alphabetic currency code for the base currency of the budget, limited to 3 characters.
   * @param budget {Array.<module:model/BudgetPayloadBudget>} 
   * @param frequencyUnit {module:model/BudgetPayload.FrequencyUnitEnum} Frequency of the budget. Value may be daily, weekly, bi-weekly, monthly, semi-monthly, quarterly, or annually
   */
  var exports = function(name, clientId, currencyCode, budget, frequencyUnit) {
    var _this = this;

    CreateBudgetResponse.call(_this, name, clientId, currencyCode, budget, frequencyUnit);

  };

  /**
   * Constructs a <code>SpecificBudgetResponse</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/SpecificBudgetResponse} obj Optional instance to populate.
   * @return {module:model/SpecificBudgetResponse} The populated <code>SpecificBudgetResponse</code> instance.
   */
  exports.constructFromObject = function(data, obj) {
    if (data) {
      obj = obj || new exports();

      CreateBudgetResponse.constructFromObject(data, obj);
      if (data.hasOwnProperty('update_date')) {
        obj['update_date'] = ApiClient.convertToType(data['update_date'], 'String');
      }
    }
    return obj;
  }

  /**
   * Datetime the budget was last updated
   * @member {String} update_date
   */
  exports.prototype['update_date'] = undefined;

  // Implement CreateBudgetResponse interface:
  /**
   * Name of the budget
   * @member {String} name
   */
exports.prototype['name'] = undefined;

  /**
   * The ID of the client the budget belongs to
   * @member {String} client_id
   */
exports.prototype['client_id'] = undefined;

  /**
   * Alphabetic currency code for the base currency of the budget, limited to 3 characters.
   * @member {String} currency_code
   */
exports.prototype['currency_code'] = undefined;

  /**
   * @member {Array.<module:model/BudgetPayloadBudget>} budget
   */
exports.prototype['budget'] = undefined;

  /**
   * Frequency of the budget. Value may be daily, weekly, bi-weekly, monthly, semi-monthly, quarterly, or annually
   * @member {module:model/BudgetPayload.FrequencyUnitEnum} frequency_unit
   */
exports.prototype['frequency_unit'] = undefined;

  /**
   * Number of frequency_unit between each budget. For example, if the frequency_unit is weekly and the frequency is 2, this means the budget occurs every two weeks. Default is 1
   * @member {Number} frequency
   */
exports.prototype['frequency'] = undefined;

  /**
   * The ID of the account the budget belongs to
   * @member {String} account_id
   */
exports.prototype['account_id'] = undefined;

  /**
   * The ID of a goal mapped to the budget
   * @member {String} goal_id
   */
exports.prototype['goal_id'] = undefined;

  /**
   * @member {Array.<module:model/BudgetPayloadAggregationAccounts>} aggregation_accounts
   */
exports.prototype['aggregation_accounts'] = undefined;

  /**
   * The start date for the budget
   * @member {Date} start_date
   */
exports.prototype['start_date'] = undefined;

  /**
   * The end date for the budget
   * @member {Date} end date
   */
exports.prototype['end date'] = undefined;

  /**
   * Custom information associated with the budget in the format key:value
   * @member {Object} metadata
   */
exports.prototype['metadata'] = undefined;

  /**
   * @member {module:model/SecondaryId} secondary_id
   */
exports.prototype['secondary_id'] = undefined;

  /**
   * ID of the budget
   * @member {String} id
   */
exports.prototype['id'] = undefined;

  /**
   * Datetime the budget was created
   * @member {String} create_date
   */
exports.prototype['create_date'] = undefined;



  return exports;
}));

