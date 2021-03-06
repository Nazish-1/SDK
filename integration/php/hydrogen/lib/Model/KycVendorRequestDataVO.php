<?php
/**
 * KycVendorRequestDataVO
 *
 * PHP version 5
 *
 * @category Class
 * @package  com\hydrogen\integration
 * @author   Swagger Codegen team
 * @link     https://github.com/swagger-api/swagger-codegen
 */

/**
 * Hydrogen Integration API
 *
 * The Hydrogen Integration API
 *
 * OpenAPI spec version: 1.2.1
 * Contact: info@hydrogenplatform.com
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 * Swagger Codegen version: 2.4.14
 */

/**
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen
 * Do not edit the class manually.
 */

namespace com\hydrogen\integration\Model;

use \ArrayAccess;
use \com\hydrogen\integration\ObjectSerializer;

/**
 * KycVendorRequestDataVO Class Doc Comment
 *
 * @category Class
 * @package  com\hydrogen\integration
 * @author   Swagger Codegen team
 * @link     https://github.com/swagger-api/swagger-codegen
 */
class KycVendorRequestDataVO implements ModelInterface, ArrayAccess
{
    const DISCRIMINATOR = null;

    /**
      * The original name of the model.
      *
      * @var string
      */
    protected static $swaggerModelName = 'KycVendorRequestDataVO';

    /**
      * Array of property to type mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $swaggerTypes = [
        'address' => '\com\hydrogen\integration\Model\ClientAddress[]',
        'country_of_residence' => 'string',
        'date_of_birth' => '\DateTime',
        'electron_document_id' => 'string',
        'email' => 'string',
        'first_name' => 'string',
        'gender' => 'string',
        'identification_number' => 'string',
        'identification_number_type' => 'string',
        'last_name' => 'string',
        'metadata' => 'object',
        'middle_name' => 'string',
        'phone_number' => 'string'
    ];

    /**
      * Array of property to format mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $swaggerFormats = [
        'address' => null,
        'country_of_residence' => null,
        'date_of_birth' => 'date-time',
        'electron_document_id' => 'uuid',
        'email' => null,
        'first_name' => null,
        'gender' => null,
        'identification_number' => null,
        'identification_number_type' => null,
        'last_name' => null,
        'metadata' => null,
        'middle_name' => null,
        'phone_number' => null
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
        'address' => 'address',
        'country_of_residence' => 'country_of_residence',
        'date_of_birth' => 'date_of_birth',
        'electron_document_id' => 'electron_document_id',
        'email' => 'email',
        'first_name' => 'first_name',
        'gender' => 'gender',
        'identification_number' => 'identification_number',
        'identification_number_type' => 'identification_number_type',
        'last_name' => 'last_name',
        'metadata' => 'metadata',
        'middle_name' => 'middle_name',
        'phone_number' => 'phone_number'
    ];

    /**
     * Array of attributes to setter functions (for deserialization of responses)
     *
     * @var string[]
     */
    protected static $setters = [
        'address' => 'setAddress',
        'country_of_residence' => 'setCountryOfResidence',
        'date_of_birth' => 'setDateOfBirth',
        'electron_document_id' => 'setElectronDocumentId',
        'email' => 'setEmail',
        'first_name' => 'setFirstName',
        'gender' => 'setGender',
        'identification_number' => 'setIdentificationNumber',
        'identification_number_type' => 'setIdentificationNumberType',
        'last_name' => 'setLastName',
        'metadata' => 'setMetadata',
        'middle_name' => 'setMiddleName',
        'phone_number' => 'setPhoneNumber'
    ];

    /**
     * Array of attributes to getter functions (for serialization of requests)
     *
     * @var string[]
     */
    protected static $getters = [
        'address' => 'getAddress',
        'country_of_residence' => 'getCountryOfResidence',
        'date_of_birth' => 'getDateOfBirth',
        'electron_document_id' => 'getElectronDocumentId',
        'email' => 'getEmail',
        'first_name' => 'getFirstName',
        'gender' => 'getGender',
        'identification_number' => 'getIdentificationNumber',
        'identification_number_type' => 'getIdentificationNumberType',
        'last_name' => 'getLastName',
        'metadata' => 'getMetadata',
        'middle_name' => 'getMiddleName',
        'phone_number' => 'getPhoneNumber'
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
        $this->container['address'] = isset($data['address']) ? $data['address'] : null;
        $this->container['country_of_residence'] = isset($data['country_of_residence']) ? $data['country_of_residence'] : null;
        $this->container['date_of_birth'] = isset($data['date_of_birth']) ? $data['date_of_birth'] : null;
        $this->container['electron_document_id'] = isset($data['electron_document_id']) ? $data['electron_document_id'] : null;
        $this->container['email'] = isset($data['email']) ? $data['email'] : null;
        $this->container['first_name'] = isset($data['first_name']) ? $data['first_name'] : null;
        $this->container['gender'] = isset($data['gender']) ? $data['gender'] : null;
        $this->container['identification_number'] = isset($data['identification_number']) ? $data['identification_number'] : null;
        $this->container['identification_number_type'] = isset($data['identification_number_type']) ? $data['identification_number_type'] : null;
        $this->container['last_name'] = isset($data['last_name']) ? $data['last_name'] : null;
        $this->container['metadata'] = isset($data['metadata']) ? $data['metadata'] : null;
        $this->container['middle_name'] = isset($data['middle_name']) ? $data['middle_name'] : null;
        $this->container['phone_number'] = isset($data['phone_number']) ? $data['phone_number'] : null;
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
     * Gets address
     *
     * @return \com\hydrogen\integration\Model\ClientAddress[]
     */
    public function getAddress()
    {
        return $this->container['address'];
    }

    /**
     * Sets address
     *
     * @param \com\hydrogen\integration\Model\ClientAddress[] $address address
     *
     * @return $this
     */
    public function setAddress($address)
    {
        $this->container['address'] = $address;

        return $this;
    }

    /**
     * Gets country_of_residence
     *
     * @return string
     */
    public function getCountryOfResidence()
    {
        return $this->container['country_of_residence'];
    }

    /**
     * Sets country_of_residence
     *
     * @param string $country_of_residence country_of_residence
     *
     * @return $this
     */
    public function setCountryOfResidence($country_of_residence)
    {
        $this->container['country_of_residence'] = $country_of_residence;

        return $this;
    }

    /**
     * Gets date_of_birth
     *
     * @return \DateTime
     */
    public function getDateOfBirth()
    {
        return $this->container['date_of_birth'];
    }

    /**
     * Sets date_of_birth
     *
     * @param \DateTime $date_of_birth date_of_birth
     *
     * @return $this
     */
    public function setDateOfBirth($date_of_birth)
    {
        $this->container['date_of_birth'] = $date_of_birth;

        return $this;
    }

    /**
     * Gets electron_document_id
     *
     * @return string
     */
    public function getElectronDocumentId()
    {
        return $this->container['electron_document_id'];
    }

    /**
     * Sets electron_document_id
     *
     * @param string $electron_document_id electron_document_id
     *
     * @return $this
     */
    public function setElectronDocumentId($electron_document_id)
    {
        $this->container['electron_document_id'] = $electron_document_id;

        return $this;
    }

    /**
     * Gets email
     *
     * @return string
     */
    public function getEmail()
    {
        return $this->container['email'];
    }

    /**
     * Sets email
     *
     * @param string $email email
     *
     * @return $this
     */
    public function setEmail($email)
    {
        $this->container['email'] = $email;

        return $this;
    }

    /**
     * Gets first_name
     *
     * @return string
     */
    public function getFirstName()
    {
        return $this->container['first_name'];
    }

    /**
     * Sets first_name
     *
     * @param string $first_name first_name
     *
     * @return $this
     */
    public function setFirstName($first_name)
    {
        $this->container['first_name'] = $first_name;

        return $this;
    }

    /**
     * Gets gender
     *
     * @return string
     */
    public function getGender()
    {
        return $this->container['gender'];
    }

    /**
     * Sets gender
     *
     * @param string $gender gender
     *
     * @return $this
     */
    public function setGender($gender)
    {
        $this->container['gender'] = $gender;

        return $this;
    }

    /**
     * Gets identification_number
     *
     * @return string
     */
    public function getIdentificationNumber()
    {
        return $this->container['identification_number'];
    }

    /**
     * Sets identification_number
     *
     * @param string $identification_number identification_number
     *
     * @return $this
     */
    public function setIdentificationNumber($identification_number)
    {
        $this->container['identification_number'] = $identification_number;

        return $this;
    }

    /**
     * Gets identification_number_type
     *
     * @return string
     */
    public function getIdentificationNumberType()
    {
        return $this->container['identification_number_type'];
    }

    /**
     * Sets identification_number_type
     *
     * @param string $identification_number_type identification_number_type
     *
     * @return $this
     */
    public function setIdentificationNumberType($identification_number_type)
    {
        $this->container['identification_number_type'] = $identification_number_type;

        return $this;
    }

    /**
     * Gets last_name
     *
     * @return string
     */
    public function getLastName()
    {
        return $this->container['last_name'];
    }

    /**
     * Sets last_name
     *
     * @param string $last_name last_name
     *
     * @return $this
     */
    public function setLastName($last_name)
    {
        $this->container['last_name'] = $last_name;

        return $this;
    }

    /**
     * Gets metadata
     *
     * @return object
     */
    public function getMetadata()
    {
        return $this->container['metadata'];
    }

    /**
     * Sets metadata
     *
     * @param object $metadata metadata
     *
     * @return $this
     */
    public function setMetadata($metadata)
    {
        $this->container['metadata'] = $metadata;

        return $this;
    }

    /**
     * Gets middle_name
     *
     * @return string
     */
    public function getMiddleName()
    {
        return $this->container['middle_name'];
    }

    /**
     * Sets middle_name
     *
     * @param string $middle_name middle_name
     *
     * @return $this
     */
    public function setMiddleName($middle_name)
    {
        $this->container['middle_name'] = $middle_name;

        return $this;
    }

    /**
     * Gets phone_number
     *
     * @return string
     */
    public function getPhoneNumber()
    {
        return $this->container['phone_number'];
    }

    /**
     * Sets phone_number
     *
     * @param string $phone_number phone_number
     *
     * @return $this
     */
    public function setPhoneNumber($phone_number)
    {
        $this->container['phone_number'] = $phone_number;

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


