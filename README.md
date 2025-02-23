# PaylocityTestAutomationChallenge

Hello!

Let's consider each part of the QA Challenge separately:



1. Bug Finding Challenge

All of the bugs could be found here - https://docs.google.com/spreadsheets/d/1_sS8izR2vARIcHSFrh9ZCRnTDaPts7s0gYB98zBBFqg/edit?usp=sharing

Please, let me know if you don't have access. My email - dart.betelgeize@gmail.com

Document structure:
- BUGS tab contains all of the discovered bugs. Tag column could be used to divide all of the bugs into: UI and API according to the challange requironments
- Opened questions tab contains all unclear moments

Important assumption:
I didn't understand fully the calculation logic so made an assumption that following formulas are correct:
- Benefits Cost = 1000/26 + 500/26*x where x is dependents number
- Net Pay = Gross Pay - Benefits Cost
- Gross Pay = Salary/26

I also used the same formulas in test automation

Testing types not included in the testing scope: security, performance



2. Automation Challenge

Important notes:
- I woud like to mention that this solution is not perfect, since I had a lack of personal time. You may notice my comments in the most problematic places of the code what would be nice to refactor or optimize.
- Not all of the tests are covered by test automation since I wanted to focus on the proper test structure and the framework architecture in general, but not on the test coverage due of lack of time. You may notice my comments in test files with suggested test that should be covered, but not implemented yet.
- All of the tests are working and passing

2.1 UI tests

Located in the "UITest" directory

Stack: Python + Playwright + PyTest

Contains:
- Functional UI tests - functionalTest folder (not all of the possible tests are covered)
- Complex E2E scenarios mentioned as User Stories in the Application description - e2eTests folder (all covered)

Test are structured in the following way:
- Test layer (e2eTests and functionalTest folders) - contains test description with usage of keywords in a BDD way
- Keywords layer (Keywords folder) - business description of action which should be done. Contains asserts and relations with POM
- Page objects (pom folder) - pages descriptions with some page related logic, locators
- Objects (pom/objects folder) - a piece of my POM. Represents some repetable elemets and modals as a seoarate objects

In addition you can find following:
- utils folder - helpers and some test data constants (common folder located in the project root)
- conftest.py - pyTest fixtures


2.2 API tests

Located in the "APITest" directory

Stack: Python + PyTest + pydantic lib

Contains:
So far it contains only 2 basic positive tests for two API endpoints.
The rest of endpoints could be easily covered in the same way.

Test are structured in the following way:
- Test layer (test folder) - contains test description in a BDD
- API clients (api_client folder) - descriptions of API request and response validations + some related functions
- Models (models folder) - models used for response validation

In addition you can find following:
- utils folder - helpers and some test data constants (common folder located in the project root)
- conftest.py - pyTest fixtures
- response_validator.py - check that response it correct, not inside the test but in api clients