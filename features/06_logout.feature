Feature: Loan Application journey


  Scenario: User should be able to logout successfully
    Given I am logged in
    And I click on the "Log Out" link
    Then I should see the "Log in" page