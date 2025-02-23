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



2. Automation Challenge

2.1 UI tests

Located in the "UITest" directory

Stack: Python + Playwright + PyTest

Contains:
- Functional UI tests - functionalTest folder
- Complex E2E scenarios mentioned as User Stories in the Application description - e2eTests folder

Test are structured in the following way:
- Test layer (e2eTests and functionalTest folders) - contains test description with usage of keywords
- Keywords layer (Keywords folder) - business description of action which should be done. Contains asserts and relations with POM
- Page objects (pom folder) - pages descriptions with some page related logic, locators
- Objects (pom/objects folder) - a piece of my POM. Represents some repetable elemets and modals as a seoarate objects

In addition you can find following:
- utils folder - helpers and some test data constants
- conftest.py - pyTest fixtures

Important note: I woud like to mention that this solution is not perfect, since I had a lack of personal time.
I tried to focus on tests itself, test coverage and proper test structure.
You may notice my comments in the most problematic places of the code what would be nice to refactor or optimize.