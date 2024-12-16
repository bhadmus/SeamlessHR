from resources.common_actions import CommonActions
from data_elements.selectors import Data


class Registration(CommonActions):
    def __init__(self):
        super().__init__()
        self.userDetails = self.user_details()

    def open_home_page(self):
        self.launch_page(Data.URL)

    def open_registration_page(self):
        self.click_element(Data.registerLink)

    def verify_registration_page(self):
        self.wait_for_text_presence(Data.regPageTitle, Data.regPageTitleText)
        self.verify_text(Data.regPageTitle, Data.regPageTitleText)

    def verify_successful_registration_page(self):
        self.wait_for_text_presence(Data.regPageTitle, f"Welcome {self.userDetails[8]}")
        self.verify_text(Data.regPageTitle, f"Welcome {self.userDetails[8]}")

    def fill_registration_form(self):
        fields = []
        self.wait_for_presence(Data.regFirstNameField)
        form_fields = self.fetch_elements(Data.regFormFields)

        for i in range(len(form_fields)):
            fields.append(form_fields[i])
        for field, userDetail in zip(fields, self.userDetails):
            field.send_keys(userDetail)

    def submit_registration(self):
        self.click_element(Data.registerButton)

    def click_logout(self):
        self.click_element(Data.logoutLink)

    def insert_valid_login(self):
        self.wait_for_presence(Data.loginUsernameField)
        self.type_text(Data.loginUsernameField, self.userDetails[8])
        self.type_text(Data.loginPasswordField, 'Test1234@')

    def insert_invalid_login(self):
        self.wait_for_presence(Data.loginUsernameField)
        self.type_text(Data.loginUsernameField, 'seamlessHR')
        self.type_text(Data.loginPasswordField, 'Test1234@')

    def select_checking_account(self):
        self.wait_for_presence(Data.accountOptions)
        self.select_value(Data.accountOptions, '0')

    def select_savings_account(self):
        self.wait_for_presence(Data.accountOptions)
        self.select_value(Data.accountOptions, '1')

    def select_account_numbers(self):
        self.wait_for_selection(Data.accountNumber)
        self.select_value(Data.accountNumber, '23445')

    def click_login_button(self):
        self.click_element(Data.loginButton)

    def click_account_open_link(self):
        self.click_element(Data.accountOpeningLink)

    def click_transfer_funds_link(self):
        self.click_element(Data.transferFundsLink)

    def click_request_loan_link(self):
        self.click_element(Data.requestLoanLink)

    def click_account_open_button(self):
        self.execute_click_action(Data.submitButton)

    def verify_login_successful(self):
        self.wait_for_text_presence(Data.regPageTitle, 'Accounts Overview')
        self.verify_text(Data.regPageTitle, 'Accounts Overview')

    def verify_loan_successful(self):
        self.verify_text(Data.regPageTitle, 'Loan Request Processed')

    def verify_logout_successful(self):
        self.verify_text(Data.loginTitle, 'Customer Login')

    def click_back_button(self):
        self.click_back()

    def verify_funds_transfer_page(self):
        self.wait_for_text_presence(Data.regPageTitle, 'Transfer Funds')
        self.verify_text(Data.regPageTitle, 'Transfer Funds')

    def verify_loan_application_page(self):
        self.wait_for_text_presence(Data.regPageTitle, 'Apply for a Loan')
        self.verify_text(Data.regPageTitle, 'Apply for a Loan')

    def verify_account_opening_success(self):
        self.verify_text(Data.regPageTitle, 'Account Opened!')

    def verify_fund_transfer_success(self):
        self.verify_text(Data.regPageTitle, 'Transfer Complete!')

    def fill_in_an_amount(self):
        self.type_text(Data.amountField, '100')

    def fill_in_loan_amount(self):
        self.type_text(Data.loanAmountField, '300')

    def fill_in_down_payment(self):
        self.type_text(Data.downPaymentField, '100')

    def verify_account_opening_page(self):
        self.wait_for_text_presence(Data.regPageTitle, 'Open New Account')
        self.verify_text(Data.regPageTitle, 'Open New Account')

    def verify_error_login_message(self):
        self.wait_for_text_presence(Data.regPageTitle, 'Error!')
        self.verify_text(Data.regPageTitle, 'Error!')
        self.verify_text(Data.loginError, 'The username and password could not be verified.')
