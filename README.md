# Task: launching autotests for different interface languages
We want the online store we are developing to work equally well for users from any country. To make sure that the solution supports different languages, we plan to run a set of autotests for each language. As an autotest developer, you need to implement a solution that will allow you to run autotests for different user languages by passing the desired language on the command line.

* Create a GitHub repository where the files will be stored conftest.py and test_items.py .
* Add to the file conftest.py a handler that reads the language parameter from the command line.
* Implement in the file conftest.py the logic of launching the browser with the specified user language. The browser must be declared in the browser fixture and passed to the test as a parameter.
* To the test_items file.py write a test that verifies that the product page on the site contains an add to cart button. For example, you can check the product available at http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207 /.
* The test should be run with the language parameter with the following command:
pytest --language=es test_items.py
* and pass successfully. It is enough that the code works only for the Chome browser.
* Send a link to this repository as a response to this task.
* Send the decision for review to other students. Do not forget that the decision can be submitted for review only once.
* Check the solutions of at least three other students to get points for the task.
