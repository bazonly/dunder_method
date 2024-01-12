import runpy

import tests_point_1
import tests_point_2
import tests_point_3
import tests_point_4
import tests_point_5

tests = [tests_point_1, tests_point_2, tests_point_3, tests_point_4, tests_point_5]

for test in tests:
    test_name = test.__name__
    runpy.run_module(test_name)