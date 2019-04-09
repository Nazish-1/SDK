=begin
#Hydrogen Atom API

#The Hydrogen Atom API

OpenAPI spec version: 1.0.0
Contact: info@hydrogenplatform.com
Generated by: https://github.com/swagger-api/swagger-codegen.git
Swagger Codegen version: 2.4.2-SNAPSHOT

=end

require 'spec_helper'
require 'json'
require 'date'

# Unit tests for AtomApi::GoalWithdrawalConfig
# Automatically generated by swagger-codegen (github.com/swagger-api/swagger-codegen)
# Please update as you see appropriate
describe 'GoalWithdrawalConfig' do
  before do
    # run before each test
    @instance = AtomApi::GoalWithdrawalConfig.new
  end

  after do
    # run after each test
  end

  describe 'test an instance of GoalWithdrawalConfig' do
    it 'should create an instance of GoalWithdrawalConfig' do
      expect(@instance).to be_instance_of(AtomApi::GoalWithdrawalConfig)
    end
  end
  describe 'test attribute "with_start_reference"' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
      # validator = Petstore::EnumTest::EnumAttributeValidator.new('String', ["a_end", "d_end"])
      # validator.allowable_values.each do |value|
      #   expect { @instance.with_start_reference = value }.not_to raise_error
      # end
    end
  end

  describe 'test attribute "with_start_period"' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  describe 'test attribute "with_end_reference"' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
      # validator = Petstore::EnumTest::EnumAttributeValidator.new('String', ["a_end", "d_end"])
      # validator.allowable_values.each do |value|
      #   expect { @instance.with_end_reference = value }.not_to raise_error
      # end
    end
  end

  describe 'test attribute "with_end_period"' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  describe 'test attribute "with_amount"' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  describe 'test attribute "with_frequency"' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
      # validator = Petstore::EnumTest::EnumAttributeValidator.new('String', ["year", "six_months", "quarter", "month", "two_weeks", "week", "day"])
      # validator.allowable_values.each do |value|
      #   expect { @instance.with_frequency = value }.not_to raise_error
      # end
    end
  end

  describe 'test attribute "with_inflation"' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

end