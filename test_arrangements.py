from arrangements import Bit_Field
from unittest import TestCase


class TestIsBitSet(TestCase):
    def test_buildBitField(self):
        testBuildField = Bit_Field(4)
        self.assertEqual(testBuildField.bitF, 1 + 2 + 4 + 8 + 16)


    def test_isBitSet(self):
        testBuildField = Bit_Field(4)
        self.assertEqual(testBuildField.isBitSet(1), True)
        self.assertEqual(testBuildField.isBitSet(0), True)
        self.assertEqual(testBuildField.isBitSet(5), False)

    def test_should_unsetbit(self):
        testBuildField = Bit_Field(4)
        self.assertEqual(testBuildField.isBitSet(1), True, "Bit 1 was not set !")
        testBuildField.unsetBit(1)
        self.assertEqual(testBuildField.isBitSet(1), False, "Bit 1 was not unset !")

    def test_should_setbit(self):
        testBuildField = Bit_Field(4)
        self.assertEqual(testBuildField.isBitSet(1), True, "Bit 1 was not set !")
        testBuildField.unsetBit(1)
        self.assertEqual(testBuildField.isBitSet(1), False, "Bit 1 was not unset !")

