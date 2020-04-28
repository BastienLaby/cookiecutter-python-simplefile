# python -m unittest tests.py

from unittest import TestCase

from {{ cookiecutter.project_name }} import main_func


class MyTest(TestCase):

    def setUp(self):
        super(MyTest, self).setUp()

    def tearDown(self):
        super(MyTest, self).tearDown()

    def my_custom_test(self):
        pass


if __name__ == "__main__":
    from unittest import main
    main()