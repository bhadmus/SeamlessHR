Feature: Fund Transfer journey


  Scenario: User should be able to transfer funds successfully
    Given I am logged in
    When I click on the "Transfer Funds" link
    Then I should see the "Transfer Funds" page
    When I fill in an amount
    And I click on the "Transfer Funds" button
    Then I should see the "Transfer Complete" page
    And I click on the "Log Out" link