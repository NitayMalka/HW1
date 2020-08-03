import unittest
import HW1


class HW1TestCase(unittest.TestCase):
    def test1_NextDay(self):
        result= HW1.NextDay((23, 6, 2017))
        self.assertEqual('24/6/2017', result)

    def test2_NextDay(self):
        result = HW1.NextDay((28, 2, 2012))
        self.assertEqual('29/2/2012', result)

    def test3_NextDay(self):
        result = HW1.NextDay((28, 2, 2015))
        self.assertEqual('1/3/2015', result)

    def test4_NextDay(self):
        result = HW1.NextDay((31, 12, 2016))
        self.assertEqual('1/1/2017', result)

    def test1_Digits(self):
        result = HW1.Digits(6)
        self.assertEqual('one digit - even', result)

    def test2_Digits(self):
        result = HW1.Digits(63)
        self.assertEqual('two digits - odd', result)

    def test3_Digits(self):
        result = HW1.Digits(163)
        self.assertEqual('three digits - even', result)

    def test4_Digits(self):
        result = HW1.Digits(1653)
        self.assertEqual('four digits - odd', result)

    def test5_Digits(self):
        result = HW1.Digits(16453)
        self.assertEqual('five digits - even', result)

    def test1_GoodOrder(self):
        result = HW1.GoodOrder(12345)
        self.assertEqual(False, result)

    def test2_GoodOrder(self):
        result = HW1.GoodOrder(264)
        self.assertEqual(True, result)

    def test3_GoodOrder(self):
        result = HW1.GoodOrder(1573)
        self.assertEqual(True, result)

    def test1_Figure(self):
        result= HW1.Figure(7)
        expected = ['      1      ', '     2 2     ', '    3   3    ', '   4     4   ', '  5       5  ', ' 6         6 ', '7654321234567']
        self.assertEqual(expected,result)

    def test1_Value(self):
        result = HW1.Value(7145)
        self.assertEqual(11, result)

    def test2_Value(self):
        result = HW1.Value(15)
        self.assertEqual(7, result)

    def test3_Value(self):
        result = HW1.Value(351)
        self.assertEqual(8, result)

    def test1_Pascal(self):
        result = HW1.Pascal(3, 2)
        self.assertEqual(3, result)

    def test2_Pascal(self):
        result = HW1.Pascal(10, 4)
        self.assertEqual(210, result)

    def test3_Pascal(self):
        result = HW1.Pascal(5, 3)
        self.assertEqual(10, result)

    def test1_Reduce(self):
        result = HW1.Reduce(-160760)
        self.assertEqual(-1676, result)

    def test2_Reduce(self):
        result = HW1.Reduce(1020034000)
        self.assertEqual(1234, result)

    def test1_IsPrimary(self):
        result = HW1.IsPrimary(23)
        self.assertEqual(True, result)

    def test2_IsPrimary(self):
        result = HW1.IsPrimary(21)
        self.assertEqual(False, result)


if __name__ == '__main__':
    unittest.main()

