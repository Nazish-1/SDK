/*
 * Molecule API Documentation
 * The Hydrogen Molecule API
 *
 * OpenAPI spec version: 1.3.0
 * Contact: info@hydrogenplatform.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 *
 * Swagger Codegen version: 2.4.14
 *
 * Do not edit the class manually.
 *
 */

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD.
    define(['expect.js', '../../src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require('../../src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.MoleculeApiDocumentation);
  }
}(this, function(expect, MoleculeApiDocumentation) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new MoleculeApiDocumentation.EscrowTransactionApi();
  });

  describe('(package)', function() {
    describe('EscrowTransactionApi', function() {
      describe('createEscrowTransactionUsingPost', function() {
        it('should call createEscrowTransactionUsingPost successfully', function(done) {
          // TODO: uncomment, update parameter values for createEscrowTransactionUsingPost call and complete the assertions
          /*
          var escrowDepositParams = new MoleculeApiDocumentation.EscrowDepositParams();
          escrowDepositParams.payeeWalletId = """00000000-0000-0000-0000-000000000000";
          escrowDepositParams.payerWalletId = """00000000-0000-0000-0000-000000000000";
          escrowDepositParams.amount = 0.0;
          escrowDepositParams.recordStatus = "";

          instance.createEscrowTransactionUsingPost(escrowDepositParams, function(error, data, response) {
            if (error) {
              done(error);
              return;
            }
            // TODO: update response assertions
            expect(data).to.be.a(MoleculeApiDocumentation.EscrowTransactionResponse);
            expect(data.id).to.be.a('string');
            expect(data.id).to.be("""00000000-0000-0000-0000-000000000000");
            expect(data.payeeWalletId).to.be.a('string');
            expect(data.payeeWalletId).to.be("""00000000-0000-0000-0000-000000000000");
            expect(data.payerWalletId).to.be.a('string');
            expect(data.payerWalletId).to.be("""00000000-0000-0000-0000-000000000000");
            expect(data.amount).to.be.a('number');
            expect(data.amount).to.be(0.0);
            expect(data.withdrawn).to.be.a('boolean');
            expect(data.withdrawn).to.be(false);
            expect(data.escrowAddress).to.be.a('string');
            expect(data.escrowAddress).to.be("");
            expect(data.recordStatus).to.be.a('string');
            expect(data.recordStatus).to.be("");
            expect(data.createDate).to.be.a(Date);
            expect(data.createDate).to.be(new Date());
            expect(data.updateDate).to.be.a(Date);
            expect(data.updateDate).to.be(new Date());

            done();
          });
          */
          // TODO: uncomment and complete method invocation above, then delete this line and the next:
          done();
        });
      });
      describe('getEscrowTransactionAllUsingGet', function() {
        it('should call getEscrowTransactionAllUsingGet successfully', function(done) {
          // TODO: uncomment, update parameter values for getEscrowTransactionAllUsingGet call and complete the assertions
          /*
          var opts = {};
          opts.page = 56;
          opts.size = 56;
          opts.orderBy = "orderBy_example";
          opts.ascending = true;
          opts.getLatest = true;

          instance.getEscrowTransactionAllUsingGet(opts, function(error, data, response) {
            if (error) {
              done(error);
              return;
            }
            // TODO: update response assertions
            expect(data).to.be.a(MoleculeApiDocumentation.PageEscrowTransactionResponse);
            {
              let dataCtr = data.content;
              expect(dataCtr).to.be.an(Array);
              expect(dataCtr).to.not.be.empty();
              for (let p in dataCtr) {
                let data = dataCtr[p];
                expect(data).to.be.a(MoleculeApiDocumentation.EscrowTransactionResponse);
                expect(data.id).to.be.a('string');
                expect(data.id).to.be("""00000000-0000-0000-0000-000000000000");
                expect(data.payeeWalletId).to.be.a('string');
                expect(data.payeeWalletId).to.be("""00000000-0000-0000-0000-000000000000");
                expect(data.payerWalletId).to.be.a('string');
                expect(data.payerWalletId).to.be("""00000000-0000-0000-0000-000000000000");
                expect(data.amount).to.be.a('number');
                expect(data.amount).to.be(0.0);
                expect(data.withdrawn).to.be.a('boolean');
                expect(data.withdrawn).to.be(false);
                expect(data.escrowAddress).to.be.a('string');
                expect(data.escrowAddress).to.be("");
                expect(data.recordStatus).to.be.a('string');
                expect(data.recordStatus).to.be("");
                expect(data.createDate).to.be.a(Date);
                expect(data.createDate).to.be(new Date());
                expect(data.updateDate).to.be.a(Date);
                expect(data.updateDate).to.be(new Date());

                      }
            }
            expect(data.first).to.be.a('boolean');
            expect(data.first).to.be(false);
            expect(data.last).to.be.a('boolean');
            expect(data.last).to.be(false);
            expect(data._number).to.be.a('number');
            expect(data._number).to.be(0);
            expect(data.numberOfElements).to.be.a('number');
            expect(data.numberOfElements).to.be(0);
            expect(data.size).to.be.a('number');
            expect(data.size).to.be(0);
            {
              let dataCtr = data.sort;
              expect(dataCtr).to.be.an(Array);
              expect(dataCtr).to.not.be.empty();
              for (let p in dataCtr) {
                let data = dataCtr[p];
                expect(data).to.be.a(MoleculeApiDocumentation.Sort);
                expect(data.ascending).to.be.a('boolean');
                expect(data.ascending).to.be(true);
                expect(data.descending).to.be.a('boolean');
                expect(data.descending).to.be(false);
                expect(data.direction).to.be.a('string');
                expect(data.direction).to.be("DESC");
                expect(data.ignoreCase).to.be.a('boolean');
                expect(data.ignoreCase).to.be(false);
                expect(data.nullHandling).to.be.a('string');
                expect(data.nullHandling).to.be("NATIVE");
                expect(data.property).to.be.a('string');
                expect(data.property).to.be("updateDate");

                      }
            }
            expect(data.totalElements).to.be.a('number');
            expect(data.totalElements).to.be("0");
            expect(data.totalPages).to.be.a('number');
            expect(data.totalPages).to.be(0);

            done();
          });
          */
          // TODO: uncomment and complete method invocation above, then delete this line and the next:
          done();
        });
      });
      describe('getEscrowTransactionUsingGet', function() {
        it('should call getEscrowTransactionUsingGet successfully', function(done) {
          // TODO: uncomment, update parameter values for getEscrowTransactionUsingGet call and complete the assertions
          /*
          var escrowTransactionId = "escrowTransactionId_example";

          instance.getEscrowTransactionUsingGet(escrowTransactionId, function(error, data, response) {
            if (error) {
              done(error);
              return;
            }
            // TODO: update response assertions
            expect(data).to.be.a(MoleculeApiDocumentation.EscrowTransactionResponse);
            expect(data.id).to.be.a('string');
            expect(data.id).to.be("""00000000-0000-0000-0000-000000000000");
            expect(data.payeeWalletId).to.be.a('string');
            expect(data.payeeWalletId).to.be("""00000000-0000-0000-0000-000000000000");
            expect(data.payerWalletId).to.be.a('string');
            expect(data.payerWalletId).to.be("""00000000-0000-0000-0000-000000000000");
            expect(data.amount).to.be.a('number');
            expect(data.amount).to.be(0.0);
            expect(data.withdrawn).to.be.a('boolean');
            expect(data.withdrawn).to.be(false);
            expect(data.escrowAddress).to.be.a('string');
            expect(data.escrowAddress).to.be("");
            expect(data.recordStatus).to.be.a('string');
            expect(data.recordStatus).to.be("");
            expect(data.createDate).to.be.a(Date);
            expect(data.createDate).to.be(new Date());
            expect(data.updateDate).to.be.a(Date);
            expect(data.updateDate).to.be(new Date());

            done();
          });
          */
          // TODO: uncomment and complete method invocation above, then delete this line and the next:
          done();
        });
      });
      describe('updateEscrowTransactionUsingPut', function() {
        it('should call updateEscrowTransactionUsingPut successfully', function(done) {
          // TODO: uncomment, update parameter values for updateEscrowTransactionUsingPut call and complete the assertions
          /*
          var escrowTransactionId = "escrowTransactionId_example";
          var opts = {};
          opts.escrowDepositParams = new MoleculeApiDocumentation.EscrowDepositParams();
          opts.escrowDepositParams.payeeWalletId = """00000000-0000-0000-0000-000000000000";
          opts.escrowDepositParams.payerWalletId = """00000000-0000-0000-0000-000000000000";
          opts.escrowDepositParams.amount = 0.0;
          opts.escrowDepositParams.recordStatus = "";

          instance.updateEscrowTransactionUsingPut(escrowTransactionId, opts, function(error, data, response) {
            if (error) {
              done(error);
              return;
            }
            // TODO: update response assertions
            expect(data).to.be.a(MoleculeApiDocumentation.EscrowTransactionResponse);
            expect(data.id).to.be.a('string');
            expect(data.id).to.be("""00000000-0000-0000-0000-000000000000");
            expect(data.payeeWalletId).to.be.a('string');
            expect(data.payeeWalletId).to.be("""00000000-0000-0000-0000-000000000000");
            expect(data.payerWalletId).to.be.a('string');
            expect(data.payerWalletId).to.be("""00000000-0000-0000-0000-000000000000");
            expect(data.amount).to.be.a('number');
            expect(data.amount).to.be(0.0);
            expect(data.withdrawn).to.be.a('boolean');
            expect(data.withdrawn).to.be(false);
            expect(data.escrowAddress).to.be.a('string');
            expect(data.escrowAddress).to.be("");
            expect(data.recordStatus).to.be.a('string');
            expect(data.recordStatus).to.be("");
            expect(data.createDate).to.be.a(Date);
            expect(data.createDate).to.be(new Date());
            expect(data.updateDate).to.be.a(Date);
            expect(data.updateDate).to.be(new Date());

            done();
          });
          */
          // TODO: uncomment and complete method invocation above, then delete this line and the next:
          done();
        });
      });
    });
  });

}));