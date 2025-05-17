Feature: OrangeHRM login and employee list

  Scenario: Login and view employee list
    Given I open the OrangeHRM login page
    When I login with valid credentials
    And I navigate to the PIM tab
    Then I should see the employee list
