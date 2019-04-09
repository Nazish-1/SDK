/*
 * Hydrogen Atom API
 * The Hydrogen Atom API
 *
 * OpenAPI spec version: 1.0.0
 * Contact: info@hydrogenplatform.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */


package io.swagger.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import io.swagger.client.model.CreatePortfolioResponse;
import java.io.IOException;
import java.util.UUID;

/**
 * SpecificPortfolioResponse
 */
@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2019-04-08T13:59:38.361-04:00")
public class SpecificPortfolioResponse {
  @SerializedName("id")
  private UUID id = null;

  @SerializedName("create_date")
  private String createDate = null;

  @SerializedName("name")
  private String name = null;

  @SerializedName("account_id")
  private UUID accountId = null;

  @SerializedName("model_id")
  private UUID modelId = null;

  @SerializedName("percentage")
  private Double percentage = null;

  @SerializedName("description")
  private String description = null;

  @SerializedName("metadata")
  private Object metadata = null;

  @SerializedName("secondary_id")
  private String secondaryId = null;

  @SerializedName("update_date")
  private String updateDate = null;

  public SpecificPortfolioResponse id(UUID id) {
    this.id = id;
    return this;
  }

   /**
   * ID of the portfolio
   * @return id
  **/
  @ApiModelProperty(value = "ID of the portfolio")
  public UUID getId() {
    return id;
  }

  public void setId(UUID id) {
    this.id = id;
  }

  public SpecificPortfolioResponse createDate(String createDate) {
    this.createDate = createDate;
    return this;
  }

   /**
   * Datetime the portfolio was created
   * @return createDate
  **/
  @ApiModelProperty(value = "Datetime the portfolio was created")
  public String getCreateDate() {
    return createDate;
  }

  public void setCreateDate(String createDate) {
    this.createDate = createDate;
  }

  public SpecificPortfolioResponse name(String name) {
    this.name = name;
    return this;
  }

   /**
   * Name of the portfolio such as “Stock”
   * @return name
  **/
  @ApiModelProperty(required = true, value = "Name of the portfolio such as “Stock”")
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public SpecificPortfolioResponse accountId(UUID accountId) {
    this.accountId = accountId;
    return this;
  }

   /**
   * The ID of the account to which the portfolio belongs
   * @return accountId
  **/
  @ApiModelProperty(required = true, value = "The ID of the account to which the portfolio belongs")
  public UUID getAccountId() {
    return accountId;
  }

  public void setAccountId(UUID accountId) {
    this.accountId = accountId;
  }

  public SpecificPortfolioResponse modelId(UUID modelId) {
    this.modelId = modelId;
    return this;
  }

   /**
   * The ID of the model to which the portfolio subscribes
   * @return modelId
  **/
  @ApiModelProperty(required = true, value = "The ID of the model to which the portfolio subscribes")
  public UUID getModelId() {
    return modelId;
  }

  public void setModelId(UUID modelId) {
    this.modelId = modelId;
  }

  public SpecificPortfolioResponse percentage(Double percentage) {
    this.percentage = percentage;
    return this;
  }

   /**
   * Weight of the portfolio as a percentage of an account based on the weight of the portfolio’s model within the account’s allocation; ex. 20 representing 20%. If the account only has one portfolio input 100
   * @return percentage
  **/
  @ApiModelProperty(required = true, value = "Weight of the portfolio as a percentage of an account based on the weight of the portfolio’s model within the account’s allocation; ex. 20 representing 20%. If the account only has one portfolio input 100")
  public Double getPercentage() {
    return percentage;
  }

  public void setPercentage(Double percentage) {
    this.percentage = percentage;
  }

  public SpecificPortfolioResponse description(String description) {
    this.description = description;
    return this;
  }

   /**
   * Description for the portfolio such as “Stock Portfolio”
   * @return description
  **/
  @ApiModelProperty(value = "Description for the portfolio such as “Stock Portfolio”")
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }

  public SpecificPortfolioResponse metadata(Object metadata) {
    this.metadata = metadata;
    return this;
  }

   /**
   * Custom information associated with the portfolio in the format key:value
   * @return metadata
  **/
  @ApiModelProperty(value = "Custom information associated with the portfolio in the format key:value")
  public Object getMetadata() {
    return metadata;
  }

  public void setMetadata(Object metadata) {
    this.metadata = metadata;
  }

  public SpecificPortfolioResponse secondaryId(String secondaryId) {
    this.secondaryId = secondaryId;
    return this;
  }

   /**
   * Get secondaryId
   * @return secondaryId
  **/
  @ApiModelProperty(value = "")
  public String getSecondaryId() {
    return secondaryId;
  }

  public void setSecondaryId(String secondaryId) {
    this.secondaryId = secondaryId;
  }

  public SpecificPortfolioResponse updateDate(String updateDate) {
    this.updateDate = updateDate;
    return this;
  }

   /**
   * Datetime the portfolio was last updated
   * @return updateDate
  **/
  @ApiModelProperty(value = "Datetime the portfolio was last updated")
  public String getUpdateDate() {
    return updateDate;
  }

  public void setUpdateDate(String updateDate) {
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
    SpecificPortfolioResponse specificPortfolioResponse = (SpecificPortfolioResponse) o;
    return Objects.equals(this.id, specificPortfolioResponse.id) &&
        Objects.equals(this.createDate, specificPortfolioResponse.createDate) &&
        Objects.equals(this.name, specificPortfolioResponse.name) &&
        Objects.equals(this.accountId, specificPortfolioResponse.accountId) &&
        Objects.equals(this.modelId, specificPortfolioResponse.modelId) &&
        Objects.equals(this.percentage, specificPortfolioResponse.percentage) &&
        Objects.equals(this.description, specificPortfolioResponse.description) &&
        Objects.equals(this.metadata, specificPortfolioResponse.metadata) &&
        Objects.equals(this.secondaryId, specificPortfolioResponse.secondaryId) &&
        Objects.equals(this.updateDate, specificPortfolioResponse.updateDate);
  }

  @Override
  public int hashCode() {
    return Objects.hash(id, createDate, name, accountId, modelId, percentage, description, metadata, secondaryId, updateDate);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class SpecificPortfolioResponse {\n");
    
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    createDate: ").append(toIndentedString(createDate)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    accountId: ").append(toIndentedString(accountId)).append("\n");
    sb.append("    modelId: ").append(toIndentedString(modelId)).append("\n");
    sb.append("    percentage: ").append(toIndentedString(percentage)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    metadata: ").append(toIndentedString(metadata)).append("\n");
    sb.append("    secondaryId: ").append(toIndentedString(secondaryId)).append("\n");
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
