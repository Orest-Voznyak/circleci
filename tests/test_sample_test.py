import pytest


class TestSample:

    @pytest.mark.smoke
    def test_smoke(self):
        assert True

    @pytest.mark.smoke
    def test_smoke(self):
        assert True

    def test_regression(self):
        assert True

    @pytest.mark.end_to_end
    def test_regression(self):
        assert True
