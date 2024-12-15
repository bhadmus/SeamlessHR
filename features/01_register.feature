Feature: Test for the Registration journey

  Scenario: User should be able to register successfully
        Given I am on the home page
        And I click on the "Register" link
        Then I should see the "Registration" page
        When I fully fill the registration details
        And I click on the "Register" button
        Then I should see the "success" page
        And I click on the "Log Out" link