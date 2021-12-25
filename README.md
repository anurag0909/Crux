The test cases for the given assignment are scripted in the attached files.

In order to execute these test cases, below are the steps/guidelines that need to be followed:

Install python 3.9 & IDE - Pycharm in your machine.

Required libraries:    pip, selenium, pytest, pytest-html, openpyxl.


Class description:

Data --> variables - in this class all the paths for driver, excel having test cases, variables to find the elements, example xpaths

Data --> genericFunctions - in this class all the commonly used functions are mentioned, example, to generate the date, fetch values from excel, etc.

functionSteps --> Crux - in this class, the various functions for the steps to be followed to execute the test cases are mentioned.

Executor --> Test_Executor - from this class, functions for the execution of test cases is mentioned.

In order to execute the test cases, there are 2 ways by which we can do it,

a. Set the configuration of Test_Executor.py as pytest and use the play button in the IDE.

b. Open the terminal in the IDE and execute the following command -

pytest -v -s --html=Report\report1.html --self-contained-html Executor\Test_Executor.py

This command will generate an html report of the test case execution and will save in Report forlder in the project.

At relevant instances, the screenshots are captured and saved in Screenshots folder in the project.
