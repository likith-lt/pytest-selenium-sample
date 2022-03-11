import pytest
import sys
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures('driver')
class TestLink:

    def test_demo_site(self, driver):


        # Url
        print('Loading URL')
        driver.get("https://stage-demo.lambdatest.com/")

        # Let's select the location
        driver.find_element(By.ID, "headlessui-listbox-button-1").click()
        location = driver.find_element(By.ID, "Bali")
        location.click()
        print("Location is selected as Bali.")

        # Let's select the number of guests
        driver.find_element(By.ID, "headlessui-listbox-button-5").click()
        guests = driver.find_element(By.ID, "2")
        guests.click()
        print("Number of guests are selected.")

        # Searching for the results
        search = driver.find_element(By.XPATH, "//*[@id='search']")
        search.click()
        driver.implicitly_wait(3)

        # Let's select one of the hotels for booking
        reserve = driver.find_element(By.ID, "reserve-now")
        reserve.click()
        driver.implicitly_wait(3)
        proceed = driver.find_element(By.ID, "proceed")
        proceed.click()
        driver.implicitly_wait(3)
        print("Booking is confirmed.")

        # Let's download the invoice
        download = driver.find_element(By.ID, "invoice")
        download.click()
        print("Tests are run successfully!")
