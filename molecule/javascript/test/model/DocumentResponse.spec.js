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

  describe('(package)', function() {
    describe('DocumentResponse', function() {
      beforeEach(function() {
        instance = new MoleculeApiDocumentation.DocumentResponse();
      });

      it('should create an instance of DocumentResponse', function() {
        // TODO: update the code to test DocumentResponse
        expect(instance).to.be.a(MoleculeApiDocumentation.DocumentResponse);
      });

      it('should have the property documents (base name: "documents")', function() {
        // TODO: update the code to test the property documents
        expect(instance).to.have.property('documents');
        // expect(instance.documents).to.be(expectedValueLiteral);
      });

    });
  });

}));
