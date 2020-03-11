# -*- coding: utf-8 -*-

import unittest

from tlf35584 import HexToCmd, CmdToHex


class TestApp(unittest.TestCase):
    def setUp(self):
        pass

    def test_CmdToHex(self):
        result = CmdToHex(1, 34, 255)
        self.assertEqual(result, 'c5ff')

    def test_HexToCmd(self):
        result = HexToCmd("adb5")
        self.assertEqual(result, {'RW': 1, 'Addr': 22, 'Value': 218, 'P': 1})


def suite():
    suite = unittest.TestSuite()
    suite.addTests(
        unittest.TestLoader().loadTestsFromTestCase(TestApp)
    )

    return suite


if __name__ == '__main__':

    unittest.TextTestRunner(verbosity=2).run(suite())