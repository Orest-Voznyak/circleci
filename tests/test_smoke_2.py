import pytest


class TestSample:

    @pytest.mark.smoke
    def test_smoke_3(self):
        assert True

    @pytest.mark.smoke
    def test_smoke_4(self):
        assert True
