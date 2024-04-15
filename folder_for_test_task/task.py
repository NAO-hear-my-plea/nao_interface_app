import unittest


def uniq_sum(list1, list2) -> list:
    return sorted(list(set(list1 + list2)))
    # unique = []
    # list = list1 + list2
    # for el in list:
    #     if list.count(el) <= 1:
    #         unique.append(el)
    #     else:
    #         if el not in unique:
    #             unique.append(el)
    #
    # unique.sort()
    #
    # return unique

class TestUniqSum(unittest.TestCase):
    def test_uniq_sum(self):
        self.assertEqual([1, 2, 3, 4], uniq_sum([1, 2], [3, 4]))
        self.assertEqual([1, 2, 7, 11, 13], uniq_sum([1, 2], [11, 7, 13]))
        self.assertEqual([1, 2], uniq_sum([1, 2], [2, 1]))
        self.assertEqual([1, 2, 3, 4], uniq_sum([1, 2, 3], [2, 3, 4]))
        self.assertEqual([2, 3], uniq_sum([2, 2, 2], [3, 3, 3]))
        self.assertEqual([1, 2, 3], uniq_sum([2, 1, 2], [3, 1, 3]))
        self.assertEqual([1, 2, 3], uniq_sum([1, 3, 1, 3, 1, 3, 1, 3], [2, 2, 2, 2, 2, 3, 3, 2, 3]))
        self.assertEqual([1, 2, 4, 5, 9], uniq_sum([1, 2, 4], [4, 5, 2, 9, 9, 9, 5, 1, 4]))


if __name__ == '__main__':
    unittest.main()
