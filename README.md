# python-testing
Some tests for testing UI using Playwright, and API using requests. Tests run every each push and Allure results deploy on GitHub Pages.

##Local running
###Console
`pytest` - run tests without any report in 1 thread

`--headful` - Playwright will run in headful mode

`pytest -n <thread count>` - run tests in "thread count" threads

`pytest --alluredir=/tmp/my_allure_results` - run tests with collection of results

`allure serve /tmp/my_allure_results` generate report

