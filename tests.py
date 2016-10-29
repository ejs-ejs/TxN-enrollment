#!/usr/bin/env python
import unittest
import doctest
import txagreement
from subprocess import check_output


class TestTxAgrrement(unittest.TestCase):
    def test_render_agreement(self):
        pdf = txagreement.render_agreement({
            "member": {
                "Name": "Jonas Jonavičius",
                "address": "Bistryčios g. 13, Vilnius",
				"phone": "+10 34 223322",
				"email": "jonas@jonavicius.net"
            },
            "number": "01234567",
        })
        self.assertEqual(check_output(["file", "-ib", "-"], input=pdf).strip(),
                         b"application/pdf; charset=binary")


if __name__ == "__main__":
    unittest.main()
