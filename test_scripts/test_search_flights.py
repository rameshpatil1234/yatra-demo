import logging
import pytest
import softest
from generic.utilities import Utils
from pages.yatra_launch_page import LaunchPage
from ddt import ddt, data,unpack,file_data


@pytest.mark.usefixtures("setup","log_on_failure")
@ddt
class TestSearchAndVerify(softest.TestCase):
    log = Utils.custom_logger(log_Level=logging.INFO)

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.ut = Utils()

    @data(*Utils.read_data_from_excel("data/input.xlsx","yatra_lp"))
    @unpack
    def test_search_flights(self, goingfrom, goingto, date, stop):
        search_flights_result = self.lp.search_flights(goingfrom, goingto, date)
        self.lp.page_scroll()
        search_flights_result.filter_flights_by_stop(stop)
        all_stops = search_flights_result.get_search_flight_results()
        self.log.info(len(all_stops))
        self.ut.assert_list_item_text(all_stops, stop)

