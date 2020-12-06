import requests
import pytest
from .test_base import TestBase


class TestNewDeck(TestBase):

    @pytest.mark.first
    @pytest.mark.parametrize("param_name, param_val, remaining_expected", [
                            (None, None, 52),
                            ("newDeck_param_joker", "false", 52),
                            ("newDeck_param_joker", "true", 54)
    ])
    def test_new_deck(self, param_name, param_val, remaining_expected):
        """
        This method runs 3 test cases for "A Brand New Deck" endpoint
        """
        endpoint = self.config_properties.get("default", "newDeck_endpoint")

        # construct query parameter if supplied
        param_query = ""
        if param_name is not None:
            param_query = "?" + self.config_properties.get("default", param_name).replace(f"<{param_name}>", param_val)
        url = self.baseurl + endpoint + param_query

        # call the endpoint
        response = requests.get(url)

        # parse the response
        status_code = response.status_code
        success = response.json()["success"]
        deck_id = response.json()["deck_id"]
        remaining = response.json()["remaining"]

        # validate
        assert status_code == 200
        assert success
        assert len(deck_id) > 0
        assert remaining == remaining_expected

        # save "deck_id" and "remaining" in test data for later use
        self.test_data.update({"deck_id": deck_id, "remaining": remaining})
