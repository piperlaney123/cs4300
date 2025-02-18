from homework1.task7 import *
import numpy as np

# test w/ pytest
class TestClass:
    test_array = create_random_array(10)
    
    # test array func
    def test_create_array_func(self):
        assert type(self.test_array) == type(np.array([1, 2, 3]))

    # test count length func with np's built-in size func
    def test_length_func(self):
        assert np.size(self.test_array) == count_array_length(self.test_array)

    # test max func with np's built-in max func
    def test_max_func(self):
        assert np.max(self.test_array) == find_max(self.test_array)

    # test min func with np's built-in min func
    def test_min_func(self):
        assert np.min(self.test_array) == find_min(self.test_array)