/*
 * Molecule API Documentation
 * The Hydrogen Molecule API
 *
 * OpenAPI spec version: 1.3.0
 * Contact: info@hydrogenplatform.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */


package com.hydrogen.molecule.model;

import java.util.Objects;

import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.UUID;
import org.threeten.bp.OffsetDateTime;

/**
 * WebhookResponse
 */
@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-07-21T09:54:56.296Z")
public class WebhookResponse {
  @SerializedName("id")
  private UUID id = null;

  @SerializedName("url")
  private String url = null;

  /**
   * Gets or Sets moleculeService
   */
  @JsonAdapter(MoleculeServiceEnum.Adapter.class)
  public enum MoleculeServiceEnum {
    WHITELIST_ADMIN("whitelist_admin"),
    
    WHITELISTED("whitelisted"),
    
    TOKEN_TRANSFER("token_transfer"),
    
    TOKEN_BALANCE("token_balance"),
    
    TOKEN_SUPPLY_BALANCE("token_supply_balance"),
    
    CURRENCY_TRANSFER("currency_transfer"),
    
    CURRENCY_BALANCE("currency_balance"),
    
    TRANSACTION("transaction");

    private String value;

    MoleculeServiceEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static MoleculeServiceEnum fromValue(String text) {
      for (MoleculeServiceEnum b : MoleculeServiceEnum.values()) {
        if (String.valueOf(b.value).equals(text)) {
          return b;
        }
      }
      return null;
    }

    public static class Adapter extends TypeAdapter<MoleculeServiceEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final MoleculeServiceEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public MoleculeServiceEnum read(final JsonReader jsonReader) throws IOException {
        String value = jsonReader.nextString();
        return MoleculeServiceEnum.fromValue(String.valueOf(value));
      }
    }
  }

  @SerializedName("molecule_service")
  private List<MoleculeServiceEnum> moleculeService = null;

  @SerializedName("is_active")
  private Boolean isActive = null;

  @SerializedName("record_status")
  private String recordStatus = null;

  @SerializedName("create_date")
  private OffsetDateTime createDate = null;

  @SerializedName("update_date")
  private OffsetDateTime updateDate = null;

  public WebhookResponse id(UUID id) {
    this.id = id;
    return this;
  }

   /**
   * Get id
   * @return id
  **/
  @ApiModelProperty(value = "")
  public UUID getId() {
    return id;
  }

  public void setId(UUID id) {
    this.id = id;
  }

  public WebhookResponse url(String url) {
    this.url = url;
    return this;
  }

   /**
   * Get url
   * @return url
  **/
  @ApiModelProperty(value = "")
  public String getUrl() {
    return url;
  }

  public void setUrl(String url) {
    this.url = url;
  }

  public WebhookResponse moleculeService(List<MoleculeServiceEnum> moleculeService) {
    this.moleculeService = moleculeService;
    return this;
  }

  public WebhookResponse addMoleculeServiceItem(MoleculeServiceEnum moleculeServiceItem) {
    if (this.moleculeService == null) {
      this.moleculeService = new ArrayList<MoleculeServiceEnum>();
    }
    this.moleculeService.add(moleculeServiceItem);
    return this;
  }

   /**
   * Get moleculeService
   * @return moleculeService
  **/
  @ApiModelProperty(value = "")
  public List<MoleculeServiceEnum> getMoleculeService() {
    return moleculeService;
  }

  public void setMoleculeService(List<MoleculeServiceEnum> moleculeService) {
    this.moleculeService = moleculeService;
  }

  public WebhookResponse isActive(Boolean isActive) {
    this.isActive = isActive;
    return this;
  }

   /**
   * Get isActive
   * @return isActive
  **/
  @ApiModelProperty(value = "")
  public Boolean isIsActive() {
    return isActive;
  }

  public void setIsActive(Boolean isActive) {
    this.isActive = isActive;
  }

  public WebhookResponse recordStatus(String recordStatus) {
    this.recordStatus = recordStatus;
    return this;
  }

   /**
   * Get recordStatus
   * @return recordStatus
  **/
  @ApiModelProperty(value = "")
  public String getRecordStatus() {
    return recordStatus;
  }

  public void setRecordStatus(String recordStatus) {
    this.recordStatus = recordStatus;
  }

  public WebhookResponse createDate(OffsetDateTime createDate) {
    this.createDate = createDate;
    return this;
  }

   /**
   * Get createDate
   * @return createDate
  **/
  @ApiModelProperty(value = "")
  public OffsetDateTime getCreateDate() {
    return createDate;
  }

  public void setCreateDate(OffsetDateTime createDate) {
    this.createDate = createDate;
  }

  public WebhookResponse updateDate(OffsetDateTime updateDate) {
    this.updateDate = updateDate;
    return this;
  }

   /**
   * Get updateDate
   * @return updateDate
  **/
  @ApiModelProperty(value = "")
  public OffsetDateTime getUpdateDate() {
    return updateDate;
  }

  public void setUpdateDate(OffsetDateTime updateDate) {
    this.updateDate = updateDate;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    WebhookResponse webhookResponse = (WebhookResponse) o;
    return Objects.equals(this.id, webhookResponse.id) &&
        Objects.equals(this.url, webhookResponse.url) &&
        Objects.equals(this.moleculeService, webhookResponse.moleculeService) &&
        Objects.equals(this.isActive, webhookResponse.isActive) &&
        Objects.equals(this.recordStatus, webhookResponse.recordStatus) &&
        Objects.equals(this.createDate, webhookResponse.createDate) &&
        Objects.equals(this.updateDate, webhookResponse.updateDate);
  }

  @Override
  public int hashCode() {
    return Objects.hash(id, url, moleculeService, isActive, recordStatus, createDate, updateDate);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class WebhookResponse {\n");
    
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    url: ").append(toIndentedString(url)).append("\n");
    sb.append("    moleculeService: ").append(toIndentedString(moleculeService)).append("\n");
    sb.append("    isActive: ").append(toIndentedString(isActive)).append("\n");
    sb.append("    recordStatus: ").append(toIndentedString(recordStatus)).append("\n");
    sb.append("    createDate: ").append(toIndentedString(createDate)).append("\n");
    sb.append("    updateDate: ").append(toIndentedString(updateDate)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}
