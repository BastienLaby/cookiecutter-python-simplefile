from unittest import TestCase

from {{ cookiecutter.project_name }}.{{ cookiecutter.project_name }} import main_func


class MyTest(TestCase):

    def test_main_func(self):
        main_func()
