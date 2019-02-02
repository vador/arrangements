import arrangements
from unittest import TestCase


class TestIsBitSet(TestCase):
    def test_isBitSet(self):
        testBuildField = arrangements.buildBitField(4)
        self.assertEqual(arrangements.isBitSet(1, testBuildField), True)
        self.assertEqual(arrangements.isBitSet(0, testBuildField), True)
        self.assertEqual(arrangements.isBitSet(5, testBuildField), False)


