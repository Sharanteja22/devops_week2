import unittest
from main import to_upper 

class TestToUpper(unittest.TestCase):
    """
    Test case for the 'to_upper' function.
    Inherits from unittest.TestCase to gain testing methods.
    """
    
    def test_basic_conversion(self):
        """
        Tests if a standard lowercase/mixed-case string is correctly 
        converted to full uppercase.
        """
        name = "Prabhas"
        expected_upper_name = "PRABHAS"
        
        # ACT: Call the function under test
        actual_upper_name = to_upper(name)
        
        # ASSERT: Check if the actual result matches the expected result
        self.assertEqual(actual_upper_name, expected_upper_name)

if __name__ == '__main__':
    # This runs all methods starting with 'test_' in all unittest.TestCase classes
    unittest.main()