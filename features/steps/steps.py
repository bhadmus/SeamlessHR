from behave import *
from resources.objects import *

data = Registration()

use_step_matcher("parse")


@given("I am on the home page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    data.open_home_page()


@step('I click on the "{string}" link')
def step_impl(context, string):
    """
    :param string:
    :type context: behave.runner.Context
    """
    match string:
        case 'Register':
            data.open_registration_page()
        case 'Log Out':
            data.click_logout()
        case 'Open New Account':
            data.click_account_open_link()
        case 'Transfer Funds':
            data.click_transfer_funds_link()
        case 'Request Loan':
            data.click_request_loan_link()


@then('I should see the "{string}" page')
def step_impl(context, string):
    """
    :param string:
    :type context: behave.runner.Context
    """
    match string:
        case 'Registration':
            data.verify_registration_page()
        case 'success':
            data.verify_successful_registration_page()
        case 'Accounts Overview':
            data.verify_login_successful()
        case 'Error':
            data.verify_error_login_message()
        case 'Open New Account':
            data.verify_account_opening_page()
        case 'Account Opened':
            data.verify_account_opening_success()
        case 'Transfer Funds':
            data.verify_funds_transfer_page()
        case 'Transfer Complete':
            data.verify_fund_transfer_success()
        case 'Loan Request Processed':
            data.verify_loan_successful()
        case 'Log in':
            data.verify_logout_successful()


@when("I fully fill the registration details")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    data.fill_registration_form()


@step('I click on the "{string}" button')
def step_impl(context, string):
    """
    :param string:
    :type context: behave.runner.Context
    """
    match string:
        case 'Register':
            data.submit_registration()
        case 'Log in':
            data.click_login_button()
        case 'Open New Account':
            data.click_account_open_button()
        case 'Transfer Funds':
            data.click_account_open_button()
        case 'Apply Now':
            data.click_account_open_button()
        case 'back':
            data.click_back_button()


@when('I insert "{string}" login credentials')
def step_impl(context, string):
    """
    :param string:
    :type context: behave.runner.Context
    """
    match string:
        case 'valid':
            data.insert_valid_login()
        case 'invalid':
            data.insert_invalid_login()


@given("I am logged in")
def step_impl(context):
    context.execute_steps('''
        Given I am on the home page
        When I insert "valid" login credentials
        And I click on the "Log in" button
        Then I should see the "Accounts Overview" page
    ''')


@when('I select "{string}" account')
def step_impl(context, string):
    """
    :param string:
    :type context: behave.runner.Context
    """
    match string:
        case 'checking':
            data.select_checking_account()
        case 'savings':
            data.select_savings_account()


@when("I fill in an amount")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    data.fill_in_an_amount()


@step('I insert "{string}"')
def step_impl(context, string):
    """
    :param string:
    :type context: behave.runner.Context
    """
    match string:
        case 'loan amount':
            data.fill_in_loan_amount()
        case 'down payment':
            data.fill_in_down_payment()
