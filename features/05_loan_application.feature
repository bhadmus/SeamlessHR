Feature: Loan Application journey


  Scenario: User should be able to apply for a loan successfully
    Given I am logged in
    When I click on the "Request Loan" link
    Then I should see the "Apply for a Loan" page
    When I insert "loan amount"
    And I insert "down payment"
    And I click on the "Apply Now" button
    Then I should see the "Loan Request Processed" page
    And I click on the "Log Out" link