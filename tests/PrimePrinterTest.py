from contextlib import redirect_stdout
import os
import pytest

from app.PrimePrinter import PrimePrinter


class TestPrimePrinter:

    @pytest.fixture
    def setup_test(self):
        with open('lead.txt', 'w') as f:
            with redirect_stdout(f):
                PrimePrinter.main(self)

        yield None
        os.remove("lead.txt")

    def test_should_output_matches_gold(self, setup_test):

        try:
            self._lead = open("lead.txt", "r")
            self._gold = open("gold.txt", "r")

            while True:
                line = self._gold.readline()
                if not line:
                    break
                assert line == self._lead.readline()

            assert not self._lead.readline()

        finally:
            self._lead.close()
            self._gold.close()
