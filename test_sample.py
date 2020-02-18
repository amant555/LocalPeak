import unittest


def peak(array):
    if len(array) == 0:
        return None
    if len(array) > 1:
        for i in range(len(array)):
            if i == 0 and array[i] > array[i + 1]:
                return array[i]
            elif i == len(array) - 1 and array[i] > array[i - 1]:
                return array[i]
            elif array[i]>array[i+1] and array[i]>array[i-1]:
                return array[i]
    return array[0]


class PeakFinder(unittest.TestCase):
    def test_input_with_no_element_then_there_is_no_peak(self):
        self.assertEqual(None, peak([]))

    def test_input_with_one_element_then_that_element_will_be_the_peak(self):
        self.assertEqual(1, peak([1]))

    def test_input_with_two_element_then_the_bigger_element_will_be_the_peak(self):
        self.assertEqual(2, peak([1, 2]))

    def test_input_with_three_element_then_the_element_that_is_bigger_than_surrounding_will_be_the_peak(self):
        self.assertEqual(2, peak([1, 2, 1]))


if __name__ == '__main__':
    unittest.main()
