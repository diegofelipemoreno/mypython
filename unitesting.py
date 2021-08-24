import unittest
'''
class CheckNumbers(unittest.TestCase):
    def test_int_float(self):
        self.assertEquals(1, 1)

if __name__ == "__main__":
    unittest.main()

print("-"*30)
'''

from collections import defaultdict

class StatsList(list):
    def mean(self):
        return sum(self) / len(self)
    def median(self):
        if len(self) % 2:
            return self[int(len(self) / 2)]
        else:
            idx = int(len(self) / 2)
            return (self[idx] + self[idx-1]) / 2
    def mode(self):
        freqs = defaultdict(int)
        for item in self:
            freqs[item] += 1
        mode_freq = max(freqs.values())
        modes = []
        for item, value in freqs.items():
            if value == mode_freq:
                modes.append(item)
        return modes

my_list = [1, 2, 2, 3, 3, 4]
my_stat_list = StatsList(my_list)

print(my_stat_list.mean(), '----->')
print(my_stat_list.median(), '----->')
print(my_stat_list.mode(), '----->')

class TestValidInputs(unittest.TestCase):
    def setUp(self):
        self.stats = StatsList([1, 2, 2, 3, 3, 4])

    def test_mean(self):
        self.assertEqual(self.stats.mean(), 2.5)

    def test_median(self):
        self.assertEqual(self.stats.median(), 2.5)

    def test_mode(self):
        self.assertEqual(self.stats.mode(), [2, 3])

if __name__ == "__main__":
    unittest.main()


print("-"*30)


import unittest
import sys

class SkipTests(unittest.TestCase):
    @unittest.expectedFailure
    def test_fails(self):
        self.assertEqual(False, True)

    @unittest.skip("Test is useless")
    def test_skip(self):
        self.assertEqual(False, True)

    @unittest.skipIf(sys.version_info.mirror == 1, "broken on 3.1")
    def test_skipif(self):
        self.assertEqual(False, True)
    
    @unittest.skipUnless(sys.platform.startswith("linux"), "broken on linux")
    def test_skipunless(self):
        self.assertEqual(False, True)

if __name__ == "__main__":
    unittest.main()


print("-"*30)

# -------------------------- pytest tool ---------------------------------------------

class TestNumbers:
    def test_int_float():
        assert 1 == 1.0

    def test_int_str(self):
        assert 1 == "1"