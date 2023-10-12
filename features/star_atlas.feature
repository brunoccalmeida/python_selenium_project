Feature: Star Atlas Automation

  Background:
    Given I am on the Star Atlas website

  Scenario: Replenish my ships
    When I click the "fleet_button" element
    Then 10 seconds are waited
