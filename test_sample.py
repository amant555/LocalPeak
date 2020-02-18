import unittest


def peak(array):
    if (len(array) == 0):
        return None
    return array[0]


class PeakFinder(unittest.TestCase):
    def test_input_with_no_element_then_there_is_no_peak(self):
        self.assertEqual(None, peak([]))


if __name__ == '__main__':
    unittest.main()
