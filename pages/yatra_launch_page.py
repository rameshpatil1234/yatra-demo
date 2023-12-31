import logging

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from generic.base_test import BaseTest
from generic.utilities import Utils
from pages.search_flights_results_page import SearchFlightResults


class LaunchPage(BaseTest):
    log = Utils.custom_logger(log_Level=logging.INFO)

    def __init__(self, driver):
        # super().__init__(driver)
        self.driver = driver

    dept_from = (By.XPATH, "//input[@id='BE_flight_origin_city']")
    going_to = (By.XPATH, "//input[@id='BE_flight_arrival_city']")
    dept_date = (By.XPATH, "//input[@id='BE_flight_origin_date']")
    all_dates = (By.XPATH, "//div[@id='monthWrapper']//td[@class!='inActiveTD']")
    search_btn = (By.XPATH, "//input[@value='Search Flights']")
    search_results_list = (By.XPATH, "//div[@class='viewport']//div[1]/li")

    def getDepartFromField(self):
        return self.wait_until_element_is_clickable(*self.dept_from)

    def getSearchResultsList(self):
        return self.wait_for_presence_of_all_elements(*self.search_results_list)

    def enterDepartFromLocation(self, depart_location):
        self.getDepartFromField().click()
        self.log.info('clicked on dept from')
        self.getDepartFromField().send_keys(depart_location)
        search_results = self.getSearchResultsList()
        print(len(search_results))
        for result in search_results:
            print(result.text)
            if depart_location in result.text:
                result.click()
                break
        self.getDepartFromField().send_keys(Keys.ENTER)

    def getGoingToField(self):
        return self.wait_until_element_is_clickable(*self.going_to)

    def enterGoingToLocation(self, going_to_location):
        self.getGoingToField().click()
        self.log.info('clicked on going to')
        self.getGoingToField().send_keys(going_to_location)
        search_results = self.getSearchResultsList()
        print(len(search_results))
        for result in search_results:
            print(result.text)
            if going_to_location in result.text:
                result.click()
                break

    def getDepartDate(self):
        return self.wait_until_element_is_clickable(*self.dept_date)

    def getAllDatesField(self):
        return self.wait_for_presence_of_all_elements(*self.all_dates)

    def selectDepartDate(self, deptdate):
        self.getDepartDate().click()
        all_dates_results = self.getAllDatesField()
        for date in all_dates_results:
            if date.get_attribute("data-date") == deptdate:
                date.click()
                break

    def click_search(self):
        self.driver.find_element(*self.search_btn).click()

    def search_flights(self, depart_location, going_to_location, deptdate):
        self.enterDepartFromLocation(depart_location)
        self.enterGoingToLocation(going_to_location)
        self.selectDepartDate(deptdate)
        self.click_search()
        search_flight_results = SearchFlightResults(self.driver)
        return search_flight_results
