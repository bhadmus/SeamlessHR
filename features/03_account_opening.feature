Feature: Account Opening journey

  Background: User should be logged in
    Given I am logged in

  Scenario: User should be able to open a checking account successfully
    When I click on the "Open New Account" link
    Then I should see the "Open New Account" page
    When I select "checking" account
    And I click on the "Open New Account" button
    Then I should see the "Account Opened" page
    And I click on the "Log Out" link

  Scenario: User should be able to open a savings account successfully
    When I click on the "Open New Account" link
    Then I should see the "Open New Account" page
    When I select "savings" account
    And I click on the "Open New Account" button
    Then I should see the "Account Opened" page
    And I click on the "Log Out" link