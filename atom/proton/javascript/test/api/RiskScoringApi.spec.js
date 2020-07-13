/*
 * Hydrogen Proton API
 * Financial engineering module of Hydrogen Atom
 *
 * OpenAPI spec version: 1.7.18
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
    factory(root.expect, root.HydrogenProtonApi);
  }
}(this, function(expect, HydrogenProtonApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new HydrogenProtonApi.RiskScoringApi();
  });

  describe('(package)', function() {
    describe('RiskScoringApi', function() {
      describe('dimensionalRiskScore', function() {
        it('should call dimensionalRiskScore successfully', function(done) {
          // TODO: uncomment, update parameter values for dimensionalRiskScore call and complete the assertions
          /*
          var dimensionalRiskScoreRequest = new HydrogenProtonApi.DimensionalRiskScoreRequest();
          dimensionalRiskScoreRequest.dimWeights = [0.0];
          dimensionalRiskScoreRequest.answerWeights = [0.0];
          dimensionalRiskScoreRequest.clientId = """00000000-0000-0000-0000-000000000000";
          dimensionalRiskScoreRequest.dims = [""];
          dimensionalRiskScoreRequest.answerDims = [[""]];
          dimensionalRiskScoreRequest.answers = [];
          dimensionalRiskScoreRequest.maxAnswers = [];
          dimensionalRiskScoreRequest.questionnaireId = """00000000-0000-0000-0000-000000000000";
          dimensionalRiskScoreRequest.postScore = false;

          instance.dimensionalRiskScore(dimensionalRiskScoreRequest, function(error, data, response) {
            if (error) {
              done(error);
              return;
            }
            // TODO: update response assertions
            let dataCtr = data;
            expect(dataCtr).to.be.an(Object);
            expect(dataCtr).to.not.be.empty();
            for (let p in dataCtr) {
              let data = dataCtr[p];
              expect(data).to.be.a(Object);
              // expect(data).to.be(null);
            }

            done();
          });
          */
          // TODO: uncomment and complete method invocation above, then delete this line and the next:
          done();
        });
      });
      describe('riskAllocation', function() {
        it('should call riskAllocation successfully', function(done) {
          // TODO: uncomment, update parameter values for riskAllocation call and complete the assertions
          /*
          var riskAllocationRequest = new HydrogenProtonApi.RiskAllocationRequest();
          riskAllocationRequest.allocations = ["""00000000-0000-0000-0000-000000000000"];
          riskAllocationRequest.useProxyData = false;
          riskAllocationRequest.clientId = """00000000-0000-0000-0000-000000000000";
          riskAllocationRequest.riskScore = ;
          riskAllocationRequest.optConfig = ;
          riskAllocationRequest.marketDataSource = "nucleus";
          riskAllocationRequest.allocationMethod = "select";

          instance.riskAllocation(riskAllocationRequest, function(error, data, response) {
            if (error) {
              done(error);
              return;
            }
            // TODO: update response assertions
            let dataCtr = data;
            expect(dataCtr).to.be.an(Object);
            expect(dataCtr).to.not.be.empty();
            for (let p in dataCtr) {
              let data = dataCtr[p];
              expect(data).to.be.a(Object);
              // expect(data).to.be(null);
            }

            done();
          });
          */
          // TODO: uncomment and complete method invocation above, then delete this line and the next:
          done();
        });
      });
      describe('riskScore', function() {
        it('should call riskScore successfully', function(done) {
          // TODO: uncomment, update parameter values for riskScore call and complete the assertions
          /*
          var riskScoreRequest = new HydrogenProtonApi.RiskScoreRequest();
          riskScoreRequest.clientId = """00000000-0000-0000-0000-000000000000";
          riskScoreRequest.answers = [];
          riskScoreRequest.weights = [0.0];
          riskScoreRequest.maxAnswers = [];
          riskScoreRequest.questionnaireId = """00000000-0000-0000-0000-000000000000";
          riskScoreRequest.postScore = false;

          instance.riskScore(riskScoreRequest, function(error, data, response) {
            if (error) {
              done(error);
              return;
            }
            // TODO: update response assertions
            let dataCtr = data;
            expect(dataCtr).to.be.an(Object);
            expect(dataCtr).to.not.be.empty();
            for (let p in dataCtr) {
              let data = dataCtr[p];
              expect(data).to.be.a(Object);
              // expect(data).to.be(null);
            }

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