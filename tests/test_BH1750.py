# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import sys
import unittest
from unittest.mock import patch


class SmbusMock():
    # simultate the smbus method just for tests
    pass


class FCNTLMock:
    def ioctl(self):
        # simultate the FCNTL.ioctl method just for tests
        pass


sys.modules["fcntl"] = FCNTLMock()
sys.modules["smbus"] = SmbusMock()


class TestBH1750(unittest.TestCase):
    @patch("GreenPonik_BH1750.BH1750.BH1750")
    def test_read_bh1750(self, mock_bh1750):
        bh = mock_bh1750()
        expected = 124.3
        bh.read_bh1750.return_value = expected
        readed = bh.read_bh1750()
        self.assertIsNotNone(readed)
        self.assertTrue(type(readed).__name__ == "float")


if __name__ == "__main__":
    unittest.main()
