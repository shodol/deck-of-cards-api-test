import requests
import pytest
from .test_base import TestBase


class TestDrawCards(TestBase):

    @pytest.mark.parametrize("param_name, param_val", [
                            (None, None),
                            ("drawCards_param_count", 1),
                            ("drawCards_param_count", 2),
                            ("drawCards_param_count", 0),
                            ("drawCards_param_count", -1)
    ])
    def test_new_deck(self, param_name, param_val):
        """
        This method runs 5 test cases for "Draw a Card" endpoint
        """
        # get "deck_id" and "remaining" from the test data
        deck_id_tdata = self.test_data.get("deck_id")[0]
        remaining_tdata = self.test_data.get("remaining")[0]

        # define expected results for each case taking test data into account
        if param_val is None:
            param_val = 1

        cards_expected = param_val
        success_expected = True
        error_expected = False
        remaining_expected = max(0, remaining_tdata - cards_expected)

        if param_val <= 0:
            param_val = remaining_tdata - param_val
            cards_expected = min(remaining_tdata, param_val)
            remaining_expected = 0

        if param_val > remaining_tdata:
            success_expected = False
            cards_expected = max(0, remaining_tdata)
            error_expected = True

        # construct query parameter if supplied
        param_query = ""
        if param_name is not None:
            param_query = self.config_properties.get("default", param_name)
            param_query = "?" + param_query.replace(f"<{param_name}>", str(param_val))

        # provide "deck_id" in the URI
        endpoint = self.config_properties.get("default", "drawCards_endpoint")
        endpoint = endpoint.replace("<drawCards_endpoint>", deck_id_tdata)
        url = self.baseurl + endpoint + param_query

        # call the endpoint
        response = requests.get(url)

        # parse the response
        status_code = response.status_code
        success = response.json()["success"]
        deck_id = response.json()["deck_id"]
        cards = len(response.json()["cards"])
        remaining = response.json()["remaining"]

        # validate
        assert status_code == 200
        assert success == success_expected
        assert deck_id == deck_id_tdata
        assert cards == cards_expected
        assert remaining == remaining_expected
        if error_expected:
            error = response.json()["error"]
            assert "Not enough cards remaining to draw" in error

        # update the test data with recent changes
        self.test_data.update({"deck_id": deck_id, "remaining": remaining})
