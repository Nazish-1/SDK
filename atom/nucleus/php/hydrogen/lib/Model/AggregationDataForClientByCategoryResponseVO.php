<?php
/**
 * AggregationDataForClientByCategoryResponseVO
 *
 * PHP version 5
 *
 * @category Class
 * @package  com\hydrogen\nucleus
 * @author   Swagger Codegen team
 * @link     https://github.com/swagger-api/swagger-codegen
 */

/**
 * Hydrogen Atom API
 *
 * The Hydrogen Atom API
 *
 * OpenAPI spec version: 1.7.0
 * Contact: info@hydrogenplatform.com
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 * Swagger Codegen version: 2.4.14
 */

/**
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen
 * Do not edit the class manually.
 */

namespace com\hydrogen\nucleus\Model;

use \ArrayAccess;
use \com\hydrogen\nucleus\ObjectSerializer;

/**
 * AggregationDataForClientByCategoryResponseVO Class Doc Comment
 *
 * @category Class
 * @package  com\hydrogen\nucleus
 * @author   Swagger Codegen team
 * @link     https://github.com/swagger-api/swagger-codegen
 */
class AggregationDataForClientByCategoryResponseVO implements ModelInterface, ArrayAccess
{
    const DISCRIMINATOR = null;

    /**
      * The original name of the model.
      *
      * @var string
      */
    protected static $swaggerModelName = 'AggregationDataForClientByCategoryResponseVO';

    /**
      * Array of property to type mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $swaggerTypes = [
        'aggregation_account_details' => '\com\hydrogen\nucleus\Model\AggregateDataByCategoryForClientFromDbVO[]',
        'category' => 'string',
        'total_available_balance' => 'double',
        'total_balance' => 'double'
    ];

    /**
      * Array of property to format mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $swaggerFormats = [
        'aggregation_account_details' => null,
        'category' => null,
        'total_available_balance' => 'double',
        'total_balance' => 'double'
    ];

    /**
     * Array of property to type mappings. Used for (de)serialization
     *
     * @return array
     */
    public static function swaggerTypes()
    {
        return self::$swaggerTypes;
    }

    /**
     * Array of property to format mappings. Used for (de)serialization
     *
     * @return array
     */
    public static function swaggerFormats()
    {
        return self::$swaggerFormats;
    }

    /**
     * Array of attributes where the key is the local name,
     * and the value is the original name
     *
     * @var string[]
     */
    protected static $attributeMap = [
        'aggregation_account_details' => 'aggregation_account_details',
        'category' => 'category',
        'total_available_balance' => 'total_available_balance',
        'total_balance' => 'total_balance'
    ];

    /**
     * Array of attributes to setter functions (for deserialization of responses)
     *
     * @var string[]
     */
    protected static $setters = [
        'aggregation_account_details' => 'setAggregationAccountDetails',
        'category' => 'setCategory',
        'total_available_balance' => 'setTotalAvailableBalance',
        'total_balance' => 'setTotalBalance'
    ];

    /**
     * Array of attributes to getter functions (for serialization of requests)
     *
     * @var string[]
     */
    protected static $getters = [
        'aggregation_account_details' => 'getAggregationAccountDetails',
        'category' => 'getCategory',
        'total_available_balance' => 'getTotalAvailableBalance',
        'total_balance' => 'getTotalBalance'
    ];

    /**
     * Array of attributes where the key is the local name,
     * and the value is the original name
     *
     * @return array
     */
    public static function attributeMap()
    {
        return self::$attributeMap;
    }

    /**
     * Array of attributes to setter functions (for deserialization of responses)
     *
     * @return array
     */
    public static function setters()
    {
        return self::$setters;
    }

    /**
     * Array of attributes to getter functions (for serialization of requests)
     *
     * @return array
     */
    public static function getters()
    {
        return self::$getters;
    }

    /**
     * The original name of the model.
     *
     * @return string
     */
    public function getModelName()
    {
        return self::$swaggerModelName;
    }

    

    

    /**
     * Associative array for storing property values
     *
     * @var mixed[]
     */
    protected $container = [];

    /**
     * Constructor
     *
     * @param mixed[] $data Associated array of property values
     *                      initializing the model
     */
    public function __construct(array $data = null)
    {
        $this->container['aggregation_account_details'] = isset($data['aggregation_account_details']) ? $data['aggregation_account_details'] : null;
        $this->container['category'] = isset($data['category']) ? $data['category'] : null;
        $this->container['total_available_balance'] = isset($data['total_available_balance']) ? $data['total_available_balance'] : null;
        $this->container['total_balance'] = isset($data['total_balance']) ? $data['total_balance'] : null;
    }

    /**
     * Show all the invalid properties with reasons.
     *
     * @return array invalid properties with reasons
     */
    public function listInvalidProperties()
    {
        $invalidProperties = [];

        return $invalidProperties;
    }

    /**
     * Validate all the properties in the model
     * return true if all passed
     *
     * @return bool True if all properties are valid
     */
    public function valid()
    {
        return count($this->listInvalidProperties()) === 0;
    }


    /**
     * Gets aggregation_account_details
     *
     * @return \com\hydrogen\nucleus\Model\AggregateDataByCategoryForClientFromDbVO[]
     */
    public function getAggregationAccountDetails()
    {
        return $this->container['aggregation_account_details'];
    }

    /**
     * Sets aggregation_account_details
     *
     * @param \com\hydrogen\nucleus\Model\AggregateDataByCategoryForClientFromDbVO[] $aggregation_account_details aggregation_account_details
     *
     * @return $this
     */
    public function setAggregationAccountDetails($aggregation_account_details)
    {
        $this->container['aggregation_account_details'] = $aggregation_account_details;

        return $this;
    }

    /**
     * Gets category
     *
     * @return string
     */
    public function getCategory()
    {
        return $this->container['category'];
    }

    /**
     * Sets category
     *
     * @param string $category category
     *
     * @return $this
     */
    public function setCategory($category)
    {
        $this->container['category'] = $category;

        return $this;
    }

    /**
     * Gets total_available_balance
     *
     * @return double
     */
    public function getTotalAvailableBalance()
    {
        return $this->container['total_available_balance'];
    }

    /**
     * Sets total_available_balance
     *
     * @param double $total_available_balance total_available_balance
     *
     * @return $this
     */
    public function setTotalAvailableBalance($total_available_balance)
    {
        $this->container['total_available_balance'] = $total_available_balance;

        return $this;
    }

    /**
     * Gets total_balance
     *
     * @return double
     */
    public function getTotalBalance()
    {
        return $this->container['total_balance'];
    }

    /**
     * Sets total_balance
     *
     * @param double $total_balance total_balance
     *
     * @return $this
     */
    public function setTotalBalance($total_balance)
    {
        $this->container['total_balance'] = $total_balance;

        return $this;
    }
    /**
     * Returns true if offset exists. False otherwise.
     *
     * @param integer $offset Offset
     *
     * @return boolean
     */
    public function offsetExists($offset)
    {
        return isset($this->container[$offset]);
    }

    /**
     * Gets offset.
     *
     * @param integer $offset Offset
     *
     * @return mixed
     */
    public function offsetGet($offset)
    {
        return isset($this->container[$offset]) ? $this->container[$offset] : null;
    }

    /**
     * Sets value based on offset.
     *
     * @param integer $offset Offset
     * @param mixed   $value  Value to be set
     *
     * @return void
     */
    public function offsetSet($offset, $value)
    {
        if (is_null($offset)) {
            $this->container[] = $value;
        } else {
            $this->container[$offset] = $value;
        }
    }

    /**
     * Unsets offset.
     *
     * @param integer $offset Offset
     *
     * @return void
     */
    public function offsetUnset($offset)
    {
        unset($this->container[$offset]);
    }

    /**
     * Gets the string presentation of the object
     *
     * @return string
     */
    public function __toString()
    {
        if (defined('JSON_PRETTY_PRINT')) { // use JSON pretty print
            return json_encode(
                ObjectSerializer::sanitizeForSerialization($this),
                JSON_PRETTY_PRINT
            );
        }

        return json_encode(ObjectSerializer::sanitizeForSerialization($this));
    }
}

