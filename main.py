from mean_var_std import calculate
import unittest
import test_module

unittest.main(module='test_module', exit=False, verbosity=2)

# Quick manual test
print(calculate([0,1,2,3,4,5,6,7,8]))
