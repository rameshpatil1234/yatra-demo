import logging
import time
from selenium.webdriver.common.by import By
from generic.base_test import BaseTest
from generic.utilities import Utils


class SearchFlightResults(BaseTest):
    log = Utils.custom_logger(log_Level=logging.INFO)

    def __init__(self, driver):
        # super().__init__(driver)
        self.driver = driver

    filter_by_one_stop = (By.XPATH, "//p[text()='1']")
    filter_by_two_stop = (By.XPATH, "//p[text()='2']")
    filter_by_non_stop = (By.XPATH, "//p[text()='0']")
    search_flight_results = (
    By.XPATH, "//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stop(s)')]")

    def get_flight_by_one_stop(self):
        return self.driver.find_element(*self.filter_by_one_stop)

    def get_flight_by_two_stop(self):
        return self.driver.find_element(*self.filter_by_two_stop)

    def get_flight_by_non_stop(self):
        return self.driver.find_element(*self.filter_by_non_stop)

    def get_search_flight_results(self):
        return self.wait_for_presence_of_all_elements(*self.search_flight_results)

    def filter_flights_by_stop(self, by_stop):
        if by_stop == "1 Stop":
            self.get_flight_by_one_stop().click()
            self.log.info('selected flights with 1 stop')
        elif by_stop == '2 Stops(s)':
            self.get_flight_by_two_stop().click()
            self.log.info('selected flights with 2 stops')
        elif by_stop == 'Non Stop':
            self.get_flight_by_non_stop().click()
            self.log.info('selected flights with non stop')
        else:
            self.log.info('please provide valid filter option')
        time.sleep(5)
