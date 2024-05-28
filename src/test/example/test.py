import unittest


class TestExample(unittest.TestCase):
    def testEqual(self) -> None:
        self.assertEqual("hello", "hello")

    def testNotEqual(self) -> None:
        self.assertNotEqual("hello", "world")
