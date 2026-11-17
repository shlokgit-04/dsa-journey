import sys, unittest, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "day32"))

class TestDay32(unittest.TestCase):
    def test_isomorphic(self):
        from isomorphic_strings import Solution
        s = Solution()
        self.assertTrue(s.isIsomorphic("egg", "add"))
        self.assertFalse(s.isIsomorphic("foo", "bar"))
        self.assertTrue(s.isIsomorphic("paper", "title"))
        self.assertFalse(s.isIsomorphic("badc", "baba"))

    def test_subarray_sum(self):
        from subarray_sum import Solution
        s = Solution()
        self.assertEqual(s.subarraySum([1, 1, 1], 2), 2)
        self.assertEqual(s.subarraySum([1, 2, 3], 3), 2)
        self.assertEqual(s.subarraySum([1], 0), 0)
        self.assertEqual(s.subarraySum([1, -1, 1, -1], 0), 4)

    def test_contiguous_array(self):
        from contiguous_array import Solution
        s = Solution()
        self.assertEqual(s.findMaxLength([0, 1]), 2)
        self.assertEqual(s.findMaxLength([0, 1, 0]), 2)
        self.assertEqual(s.findMaxLength([0, 0, 1, 0, 0, 0, 1, 1]), 6)

if __name__ == "__main__":
    unittest.main()
