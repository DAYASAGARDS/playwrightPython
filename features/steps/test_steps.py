from pages.login_page import LoginPage
from pages.pim_page import PimPage
from behave import given, when, then

@given("I open the OrangeHRM login page")
def step_open_login(context):
    print("Opening login page...")
    context.login_page = LoginPage(context.page)
    context.login_page.load()
    print("Login page opened.")

@when("I login with valid credentials")
def step_login(context):
    context.login_page.login()

@when("I navigate to the PIM tab")
def step_navigate_pim(context):
    context.pim_page = PimPage(context.page)
    context.pim_page.go_to_pim()

@then("I should see the employee list")
def step_see_employees(context):
    employees = context.pim_page.get_employee_names()
    assert len(employees) > 0
    print("Employees:", employees)