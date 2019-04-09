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
import java.io.IOException;
import org.threeten.bp.LocalDate;

/**
 * AllocationAssetSizeResponseInner
 */
@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2019-04-08T13:59:38.361-04:00")
public class AllocationAssetSizeResponseInner {
  @SerializedName("date")
  private LocalDate date = null;

  @SerializedName("value")
  private Double value = null;

  public AllocationAssetSizeResponseInner date(LocalDate date) {
    this.date = date;
    return this;
  }

   /**
   * Date for this asset size record
   * @return date
  **/
  @ApiModelProperty(required = true, value = "Date for this asset size record")
  public LocalDate getDate() {
    return date;
  }

  public void setDate(LocalDate date) {
    this.date = date;
  }

  public AllocationAssetSizeResponseInner value(Double value) {
    this.value = value;
    return this;
  }

   /**
   * “Growth of a dollar” within the allocation on the particular date
   * @return value
  **/
  @ApiModelProperty(required = true, value = "“Growth of a dollar” within the allocation on the particular date")
  public Double getValue() {
    return value;
  }

  public void setValue(Double value) {
    this.value = value;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AllocationAssetSizeResponseInner allocationAssetSizeResponseInner = (AllocationAssetSizeResponseInner) o;
    return Objects.equals(this.date, allocationAssetSizeResponseInner.date) &&
        Objects.equals(this.value, allocationAssetSizeResponseInner.value);
  }

  @Override
  public int hashCode() {
    return Objects.hash(date, value);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AllocationAssetSizeResponseInner {\n");
    
    sb.append("    date: ").append(toIndentedString(date)).append("\n");
    sb.append("    value: ").append(toIndentedString(value)).append("\n");
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
