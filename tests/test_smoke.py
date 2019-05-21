import pytest


class TestSample:

    @pytest.mark.smoke
    def test_smoke_1(self):
        assert False

    @pytest.mark.smoke
    def test_smoke_2(self):
        assert True
