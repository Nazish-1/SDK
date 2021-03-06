<?php
/**
 * EscrowTransactionResponse
 *
 * PHP version 5
 *
 * @category Class
 * @package  com\hydrogen\molecule
 * @author   Swagger Codegen team
 * @link     https://github.com/swagger-api/swagger-codegen
 */

/**
 * Molecule API Documentation
 *
 * The Hydrogen Molecule API
 *
 * OpenAPI spec version: 1.3.0
 * Contact: info@hydrogenplatform.com
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 * Swagger Codegen version: 2.4.14
 */

/**
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen
 * Do not edit the class manually.
 */

namespace com\hydrogen\molecule\Model;

use \ArrayAccess;
use \com\hydrogen\molecule\ObjectSerializer;

/**
 * EscrowTransactionResponse Class Doc Comment
 *
 * @category Class
 * @package  com\hydrogen\molecule
 * @author   Swagger Codegen team
 * @link     https://github.com/swagger-api/swagger-codegen
 */
class EscrowTransactionResponse implements ModelInterface, ArrayAccess
{
    const DISCRIMINATOR = null;

    /**
      * The original name of the model.
      *
      * @var string
      */
    protected static $swaggerModelName = 'EscrowTransactionResponse';

    /**
      * Array of property to type mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $swaggerTypes = [
        'id' => 'string',
        'payee_wallet_id' => 'string',
        'payer_wallet_id' => 'string',
        'amount' => 'double',
        'withdrawn' => 'bool',
        'escrow_address' => 'string',
        'record_status' => 'string',
        'create_date' => '\DateTime',
        'update_date' => '\DateTime'
    ];

    /**
      * Array of property to format mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $swaggerFormats = [
        'id' => 'uuid',
        'payee_wallet_id' => 'uuid',
        'payer_wallet_id' => 'uuid',
        'amount' => 'double',
        'withdrawn' => null,
        'escrow_address' => null,
        'record_status' => null,
        'create_date' => 'date-time',
        'update_date' => 'date-time'
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
        'id' => 'id',
        'payee_wallet_id' => 'payee_wallet_id',
        'payer_wallet_id' => 'payer_wallet_id',
        'amount' => 'amount',
        'withdrawn' => 'withdrawn',
        'escrow_address' => 'escrow_address',
        'record_status' => 'record_status',
        'create_date' => 'create_date',
        'update_date' => 'update_date'
    ];

    /**
     * Array of attributes to setter functions (for deserialization of responses)
     *
     * @var string[]
     */
    protected static $setters = [
        'id' => 'setId',
        'payee_wallet_id' => 'setPayeeWalletId',
        'payer_wallet_id' => 'setPayerWalletId',
        'amount' => 'setAmount',
        'withdrawn' => 'setWithdrawn',
        'escrow_address' => 'setEscrowAddress',
        'record_status' => 'setRecordStatus',
        'create_date' => 'setCreateDate',
        'update_date' => 'setUpdateDate'
    ];

    /**
     * Array of attributes to getter functions (for serialization of requests)
     *
     * @var string[]
     */
    protected static $getters = [
        'id' => 'getId',
        'payee_wallet_id' => 'getPayeeWalletId',
        'payer_wallet_id' => 'getPayerWalletId',
        'amount' => 'getAmount',
        'withdrawn' => 'getWithdrawn',
        'escrow_address' => 'getEscrowAddress',
        'record_status' => 'getRecordStatus',
        'create_date' => 'getCreateDate',
        'update_date' => 'getUpdateDate'
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
        $this->container['id'] = isset($data['id']) ? $data['id'] : null;
        $this->container['payee_wallet_id'] = isset($data['payee_wallet_id']) ? $data['payee_wallet_id'] : null;
        $this->container['payer_wallet_id'] = isset($data['payer_wallet_id']) ? $data['payer_wallet_id'] : null;
        $this->container['amount'] = isset($data['amount']) ? $data['amount'] : null;
        $this->container['withdrawn'] = isset($data['withdrawn']) ? $data['withdrawn'] : null;
        $this->container['escrow_address'] = isset($data['escrow_address']) ? $data['escrow_address'] : null;
        $this->container['record_status'] = isset($data['record_status']) ? $data['record_status'] : null;
        $this->container['create_date'] = isset($data['create_date']) ? $data['create_date'] : null;
        $this->container['update_date'] = isset($data['update_date']) ? $data['update_date'] : null;
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
     * Gets id
     *
     * @return string
     */
    public function getId()
    {
        return $this->container['id'];
    }

    /**
     * Sets id
     *
     * @param string $id id
     *
     * @return $this
     */
    public function setId($id)
    {
        $this->container['id'] = $id;

        return $this;
    }

    /**
     * Gets payee_wallet_id
     *
     * @return string
     */
    public function getPayeeWalletId()
    {
        return $this->container['payee_wallet_id'];
    }

    /**
     * Sets payee_wallet_id
     *
     * @param string $payee_wallet_id payee_wallet_id
     *
     * @return $this
     */
    public function setPayeeWalletId($payee_wallet_id)
    {
        $this->container['payee_wallet_id'] = $payee_wallet_id;

        return $this;
    }

    /**
     * Gets payer_wallet_id
     *
     * @return string
     */
    public function getPayerWalletId()
    {
        return $this->container['payer_wallet_id'];
    }

    /**
     * Sets payer_wallet_id
     *
     * @param string $payer_wallet_id payer_wallet_id
     *
     * @return $this
     */
    public function setPayerWalletId($payer_wallet_id)
    {
        $this->container['payer_wallet_id'] = $payer_wallet_id;

        return $this;
    }

    /**
     * Gets amount
     *
     * @return double
     */
    public function getAmount()
    {
        return $this->container['amount'];
    }

    /**
     * Sets amount
     *
     * @param double $amount amount
     *
     * @return $this
     */
    public function setAmount($amount)
    {
        $this->container['amount'] = $amount;

        return $this;
    }

    /**
     * Gets withdrawn
     *
     * @return bool
     */
    public function getWithdrawn()
    {
        return $this->container['withdrawn'];
    }

    /**
     * Sets withdrawn
     *
     * @param bool $withdrawn withdrawn
     *
     * @return $this
     */
    public function setWithdrawn($withdrawn)
    {
        $this->container['withdrawn'] = $withdrawn;

        return $this;
    }

    /**
     * Gets escrow_address
     *
     * @return string
     */
    public function getEscrowAddress()
    {
        return $this->container['escrow_address'];
    }

    /**
     * Sets escrow_address
     *
     * @param string $escrow_address escrow_address
     *
     * @return $this
     */
    public function setEscrowAddress($escrow_address)
    {
        $this->container['escrow_address'] = $escrow_address;

        return $this;
    }

    /**
     * Gets record_status
     *
     * @return string
     */
    public function getRecordStatus()
    {
        return $this->container['record_status'];
    }

    /**
     * Sets record_status
     *
     * @param string $record_status record_status
     *
     * @return $this
     */
    public function setRecordStatus($record_status)
    {
        $this->container['record_status'] = $record_status;

        return $this;
    }

    /**
     * Gets create_date
     *
     * @return \DateTime
     */
    public function getCreateDate()
    {
        return $this->container['create_date'];
    }

    /**
     * Sets create_date
     *
     * @param \DateTime $create_date create_date
     *
     * @return $this
     */
    public function setCreateDate($create_date)
    {
        $this->container['create_date'] = $create_date;

        return $this;
    }

    /**
     * Gets update_date
     *
     * @return \DateTime
     */
    public function getUpdateDate()
    {
        return $this->container['update_date'];
    }

    /**
     * Sets update_date
     *
     * @param \DateTime $update_date update_date
     *
     * @return $this
     */
    public function setUpdateDate($update_date)
    {
        $this->container['update_date'] = $update_date;

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


