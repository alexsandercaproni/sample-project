import unittest
from project_name.hello_world import *


class TestString(unittest.TestCase):
    """
    Our basic test class
    """

    def test_hello_world(self):
        """
        The actual test.
        Any method which starts with ``_test`` will considered as a test case.
        """

        res = say_hello_world()

        # Success
        self.assertEqual(res, 'Hello World')

    def test_hello_world_failure(self):
        """
        The actual test.
        Any method which starts with ``_test`` will considered as a test case.
        """

        res = say_hello_world()

        # Failure
        self.assertEqual(res, 'Hello-World')


if __name__ == '__main__':
    unittest.main()
