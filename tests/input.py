import unittest
import sys
import os
from unittest import mock

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
# https://www.geeksforgeeks.org/python-import-from-parent-directory/
# import from parent directory
from function import ft_atoi, ft_getInputInt

class TestInputMethod(unittest.TestCase):

    def test_atoi_success_case(self):
      case = [
        ('4', 4),
        ('  4   ', 4), # spaces
        ('  4   ', 4), # tabs
      ]
      for c in case:
        self.assertEqual(ft_atoi(c[0]), c[1])

    def test_atoi_fail_case(self):
      case = [
        'a',
        '4a',
        'a4',
        '',
        '  ',
        '    '
      ]
      for c in case:
        self.assertEqual(ft_atoi(c), None)

    def test_input_success_case(self):
      case = [
        ('10', 10),
        ('  10   ', 10), # spaces
        ('  10   ', 10), # tabs
      ]
      original_input = mock.builtins.input
      for c in case:
        mock.builtins.input = lambda _: c[0]
        self.assertEqual(ft_getInputInt('', False), c[1])
      mock.builtins.input = original_input

    def test_input_fail_case(self):
      case = [
        'a',
        '4a',
        'a4',
        '',
        '  ',
        '    '
      ]

      original_input = mock.builtins.input
      for c in case:
        mock.builtins.input = lambda _: c
        self.assertEqual(ft_getInputInt('', False), None)
      

if __name__ == '__main__':
    unittest.main(verbosity=2)
