import unittest
import sqlite3
from mylib.query import complex_query
from mylib.transform_load import load
from mylib.extract import extract


class testFDBFunctions(unittest.TestCase):
    def test_complex_query(self):
        result = complex_query()
        self.assertEqual(result, "Success", "Failed to run query")


if __name__ == "__main__":
    unittest.main()
