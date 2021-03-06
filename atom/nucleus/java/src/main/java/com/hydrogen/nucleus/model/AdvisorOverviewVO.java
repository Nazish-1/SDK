/*
 * Hydrogen Atom API
 * The Hydrogen Atom API
 *
 * OpenAPI spec version: 1.7.0
 * Contact: info@hydrogenplatform.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */


package com.hydrogen.nucleus.model;

import java.util.Objects;

import com.google.gson.annotations.SerializedName;
import io.swagger.annotations.ApiModelProperty;

import java.util.ArrayList;
import java.util.List;

/**
 * AdvisorOverviewVO
 */
@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-06-04T05:11:20.520Z")
public class AdvisorOverviewVO {
  @SerializedName("account_list")
  private List<AccountAdvisorVO> accountList = null;

  @SerializedName("client_list")
  private List<ClientAdvisorOverviewVO> clientList = null;

  @SerializedName("total_accounts_managed")
  private Integer totalAccountsManaged = null;

  @SerializedName("total_assets_managed")
  private Double totalAssetsManaged = null;

  @SerializedName("total_clients_managed")
  private Integer totalClientsManaged = null;

  public AdvisorOverviewVO accountList(List<AccountAdvisorVO> accountList) {
    this.accountList = accountList;
    return this;
  }

  public AdvisorOverviewVO addAccountListItem(AccountAdvisorVO accountListItem) {
    if (this.accountList == null) {
      this.accountList = new ArrayList<AccountAdvisorVO>();
    }
    this.accountList.add(accountListItem);
    return this;
  }

   /**
   * Get accountList
   * @return accountList
  **/
  @ApiModelProperty(value = "")
  public List<AccountAdvisorVO> getAccountList() {
    return accountList;
  }

  public void setAccountList(List<AccountAdvisorVO> accountList) {
    this.accountList = accountList;
  }

  public AdvisorOverviewVO clientList(List<ClientAdvisorOverviewVO> clientList) {
    this.clientList = clientList;
    return this;
  }

  public AdvisorOverviewVO addClientListItem(ClientAdvisorOverviewVO clientListItem) {
    if (this.clientList == null) {
      this.clientList = new ArrayList<ClientAdvisorOverviewVO>();
    }
    this.clientList.add(clientListItem);
    return this;
  }

   /**
   * Get clientList
   * @return clientList
  **/
  @ApiModelProperty(value = "")
  public List<ClientAdvisorOverviewVO> getClientList() {
    return clientList;
  }

  public void setClientList(List<ClientAdvisorOverviewVO> clientList) {
    this.clientList = clientList;
  }

  public AdvisorOverviewVO totalAccountsManaged(Integer totalAccountsManaged) {
    this.totalAccountsManaged = totalAccountsManaged;
    return this;
  }

   /**
   * Get totalAccountsManaged
   * @return totalAccountsManaged
  **/
  @ApiModelProperty(value = "")
  public Integer getTotalAccountsManaged() {
    return totalAccountsManaged;
  }

  public void setTotalAccountsManaged(Integer totalAccountsManaged) {
    this.totalAccountsManaged = totalAccountsManaged;
  }

  public AdvisorOverviewVO totalAssetsManaged(Double totalAssetsManaged) {
    this.totalAssetsManaged = totalAssetsManaged;
    return this;
  }

   /**
   * Get totalAssetsManaged
   * @return totalAssetsManaged
  **/
  @ApiModelProperty(value = "")
  public Double getTotalAssetsManaged() {
    return totalAssetsManaged;
  }

  public void setTotalAssetsManaged(Double totalAssetsManaged) {
    this.totalAssetsManaged = totalAssetsManaged;
  }

  public AdvisorOverviewVO totalClientsManaged(Integer totalClientsManaged) {
    this.totalClientsManaged = totalClientsManaged;
    return this;
  }

   /**
   * Get totalClientsManaged
   * @return totalClientsManaged
  **/
  @ApiModelProperty(value = "")
  public Integer getTotalClientsManaged() {
    return totalClientsManaged;
  }

  public void setTotalClientsManaged(Integer totalClientsManaged) {
    this.totalClientsManaged = totalClientsManaged;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AdvisorOverviewVO advisorOverviewVO = (AdvisorOverviewVO) o;
    return Objects.equals(this.accountList, advisorOverviewVO.accountList) &&
        Objects.equals(this.clientList, advisorOverviewVO.clientList) &&
        Objects.equals(this.totalAccountsManaged, advisorOverviewVO.totalAccountsManaged) &&
        Objects.equals(this.totalAssetsManaged, advisorOverviewVO.totalAssetsManaged) &&
        Objects.equals(this.totalClientsManaged, advisorOverviewVO.totalClientsManaged);
  }

  @Override
  public int hashCode() {
    return Objects.hash(accountList, clientList, totalAccountsManaged, totalAssetsManaged, totalClientsManaged);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AdvisorOverviewVO {\n");
    
    sb.append("    accountList: ").append(toIndentedString(accountList)).append("\n");
    sb.append("    clientList: ").append(toIndentedString(clientList)).append("\n");
    sb.append("    totalAccountsManaged: ").append(toIndentedString(totalAccountsManaged)).append("\n");
    sb.append("    totalAssetsManaged: ").append(toIndentedString(totalAssetsManaged)).append("\n");
    sb.append("    totalClientsManaged: ").append(toIndentedString(totalClientsManaged)).append("\n");
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

