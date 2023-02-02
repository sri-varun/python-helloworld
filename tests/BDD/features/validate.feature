Feature: highlowtest

Scenario: Validate high or low value
    Given I pass number less than 100
    When I get a success response code
    Then I validate the low scenario

Scenario: Validate by sending invalid data
    When I pass invalid data
    Then I validate get invalid response
