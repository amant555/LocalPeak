import unittest


def peak(array):
    if (len(array) == 0):
        return None
    return array[0]


class PeakFinder(unittest.TestCase):
    def test_input_with_no_element_then_there_is_no_peak(self):
        self.assertEqual(None, peak([]))

    def test_input_with_one_element_then_that_element_will_be_the_peak(self):
        self.assertEqual(1, peak([1]))


if __name__ == '__main__':
    unittest.main()
