from unittest import TestCase
import arrangements

class TestBit_Field(TestCase):
    def test_buildBitField(self):
        testBuildField = arrangements.Bit_Field(4)
        self.assertEqual(testBuildField.bitF, 1 + 2 + 4 + 8 + 16)

