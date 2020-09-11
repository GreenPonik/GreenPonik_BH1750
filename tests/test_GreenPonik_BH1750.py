# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import sys
import unittest
from unittest.mock import patch


class SmbusMock():
    pass


class FCNTLMock:
    def __init__(self):
        pass

    def ioctl(self):
        pass


sys.modules["fcntl"] = FCNTLMock()
sys.modules["smbus"] = SmbusMock()


class Test_BH1750(unittest.TestCase):
    @patch("GreenPonik_BH1750.BH1750.BH1750")
    def test_read_bh1750(self, Mock):
        bh = Mock()
        expected = 124.3
        bh.read_bh1750.return_value = expected
        readed = bh.read_bh1750()
        self.assertIsNotNone(readed)
        self.assertTrue(type(readed).__name__ == "float")


if __name__ == "__main__":
    unittest.main()
