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


package com.hydrogen.molecule.api;

import com.hydrogen.molecule.ApiException;
import com.hydrogen.molecule.model.PageWalletPermissionResponse;
import com.hydrogen.molecule.model.WalletPermissionResponse;
import com.hydrogen.molecule.model.WalletPermissionUpdateParams;

import java.util.UUID;

import org.junit.Test;
import org.junit.Ignore;

/**
 * API tests for WalletPermissionApi
 */
@Ignore
public class WalletPermissionApiTest {

    private final WalletPermissionApi api = new WalletPermissionApi();

    
    /**
     * Fetch Wallet list with client&#39;s permissions
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getWalletPermissionAllUsingGetTest() throws ApiException {
        UUID nucleusClientId = null;
        Boolean isActive = null;
        Integer page = null;
        Integer size = null;
        String orderBy = null;
        Boolean ascending = null;
        Boolean getLatest = null;
        PageWalletPermissionResponse response = api.getWalletPermissionAllUsingGet(nucleusClientId, isActive, page, size, orderBy, ascending, getLatest);

        // TODO: test validations
    }
    
    /**
     * Fetch Wallet&#39;s client permissions details
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getWalletPermissionUsingGetTest() throws ApiException {
        UUID walletId = null;
        WalletPermissionResponse response = api.getWalletPermissionUsingGet(walletId);

        // TODO: test validations
    }
    
    /**
     * Update client&#39;s permission for provided Wallet
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void updateWalletPermissionUsingPutTest() throws ApiException {
        UUID walletId = null;
        WalletPermissionUpdateParams clientPermissions = null;
        WalletPermissionResponse response = api.updateWalletPermissionUsingPut(walletId, clientPermissions);

        // TODO: test validations
    }
    
}
