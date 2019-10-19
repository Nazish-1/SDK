/*
 * Hydrogen Molecule API
 * The Hydrogen Molecule API
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
import java.math.BigDecimal;
import java.util.UUID;

/**
 * TokenBalanceSpecificResponse
 */
@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2019-09-19T14:52:04.375-04:00")
public class TokenBalanceSpecificResponse {
  @SerializedName("id")
  private UUID id = null;

  @SerializedName("balance")
  private BigDecimal balance = null;

  @SerializedName("wallet_id")
  private UUID walletId = null;

  @SerializedName("token_id")
  private UUID tokenId = null;

  @SerializedName("create_date")
  private String createDate = null;

  @SerializedName("update_date")
  private String updateDate = null;

  public TokenBalanceSpecificResponse id(UUID id) {
    this.id = id;
    return this;
  }

   /**
   * ID of the token balance
   * @return id
  **/
  @ApiModelProperty(value = "ID of the token balance")
  public UUID getId() {
    return id;
  }

  public void setId(UUID id) {
    this.id = id;
  }

  public TokenBalanceSpecificResponse balance(BigDecimal balance) {
    this.balance = balance;
    return this;
  }

   /**
   * Token balance of the wallet
   * @return balance
  **/
  @ApiModelProperty(value = "Token balance of the wallet")
  public BigDecimal getBalance() {
    return balance;
  }

  public void setBalance(BigDecimal balance) {
    this.balance = balance;
  }

  public TokenBalanceSpecificResponse walletId(UUID walletId) {
    this.walletId = walletId;
    return this;
  }

   /**
   * The ID of the associated wallet
   * @return walletId
  **/
  @ApiModelProperty(value = "The ID of the associated wallet")
  public UUID getWalletId() {
    return walletId;
  }

  public void setWalletId(UUID walletId) {
    this.walletId = walletId;
  }

  public TokenBalanceSpecificResponse tokenId(UUID tokenId) {
    this.tokenId = tokenId;
    return this;
  }

   /**
   * The ID of the associated token.
   * @return tokenId
  **/
  @ApiModelProperty(value = "The ID of the associated token.")
  public UUID getTokenId() {
    return tokenId;
  }

  public void setTokenId(UUID tokenId) {
    this.tokenId = tokenId;
  }

  public TokenBalanceSpecificResponse createDate(String createDate) {
    this.createDate = createDate;
    return this;
  }

   /**
   * Datetime the currency balance record was created
   * @return createDate
  **/
  @ApiModelProperty(value = "Datetime the currency balance record was created")
  public String getCreateDate() {
    return createDate;
  }

  public void setCreateDate(String createDate) {
    this.createDate = createDate;
  }

  public TokenBalanceSpecificResponse updateDate(String updateDate) {
    this.updateDate = updateDate;
    return this;
  }

   /**
   * Datetime the currency balance record was updated
   * @return updateDate
  **/
  @ApiModelProperty(value = "Datetime the currency balance record was updated")
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
    TokenBalanceSpecificResponse tokenBalanceSpecificResponse = (TokenBalanceSpecificResponse) o;
    return Objects.equals(this.id, tokenBalanceSpecificResponse.id) &&
        Objects.equals(this.balance, tokenBalanceSpecificResponse.balance) &&
        Objects.equals(this.walletId, tokenBalanceSpecificResponse.walletId) &&
        Objects.equals(this.tokenId, tokenBalanceSpecificResponse.tokenId) &&
        Objects.equals(this.createDate, tokenBalanceSpecificResponse.createDate) &&
        Objects.equals(this.updateDate, tokenBalanceSpecificResponse.updateDate);
  }

  @Override
  public int hashCode() {
    return Objects.hash(id, balance, walletId, tokenId, createDate, updateDate);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TokenBalanceSpecificResponse {\n");
    
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    balance: ").append(toIndentedString(balance)).append("\n");
    sb.append("    walletId: ").append(toIndentedString(walletId)).append("\n");
    sb.append("    tokenId: ").append(toIndentedString(tokenId)).append("\n");
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
