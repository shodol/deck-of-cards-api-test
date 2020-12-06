from helper.utils import DataForTest, ConfigProperties


class TestBase:

    test_data = DataForTest()
    config_properties = ConfigProperties()

    baseurl = config_properties.get("default", "baseurl")
