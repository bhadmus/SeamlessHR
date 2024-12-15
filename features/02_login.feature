Feature: Test for the Login Scenarios

  Background: User should be able to access the login page
    Given I am on the home page

  Scenario: With a valid credentials, user should be able to login
    When I insert "valid" login credentials
    And I click on the "Log in" button
    Then I should see the "Accounts Overview" page
    And I click on the "Log Out" link

  Scenario: With a invalid credentials, user should not be able to login
    When I insert "invalid" login credentials
    And I click on the "Log in" button
    Then I should see the "Error" page