from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
    
import time
import pyautogui
import pytest

class TestRegister():

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(executable_path='C:/chromedriver_win32/chromedriver.exe')
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        yield
        self.driver.close()

    def test_pageTitle(self,setup):
        self.driver.get("https://demoqa.com/automation-practice-form")
        assert self.driver.title == 'ToolsQA'


    def test_registerForm(self,setup):
        self.driver.get("https://demoqa.com/automation-practice-form")
        self.driver.find_element_by_id("firstName").send_keys("Rievaldhi")
        time.sleep(2)
        self.driver.find_element_by_id("lastName").send_keys("test")
        time.sleep(2)
        self.driver.find_element_by_id("userEmail").send_keys("rievaldhi.test@gmail.com")
        time.sleep(2)
        self.driver.find_element_by_css_selector('#genterWrapper > div.col-md-9.col-sm-12 > div:nth-child(1) > label').click()
        time.sleep(2)
        self.driver.find_element_by_id("userNumber").send_keys("0812345678")
        time.sleep(2)
        self.driver.find_element_by_id("dateOfBirthInput").click()
        self.driver.find_element_by_id("dateOfBirthInput").send_keys("27 Jul 1999")
        pyautogui.press("left", presses=11)
        pyautogui.press("backspace", presses=11)
        time.sleep(2)
        pyautogui.press("enter")
        time.sleep(2)
        self.driver.find_element_by_id('subjectsContainer').click()
        pyautogui.typewrite("computer")
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(2)
        scroll = self.driver.find_element_by_id("uploadPicture")
        actions = ActionChains(self.driver)
        actions.move_to_element(scroll).perform()
        time.sleep(2)
        self.driver.find_element_by_css_selector('#hobbiesWrapper > div.col-md-9.col-sm-12 > div:nth-child(1) > label').click()
        time.sleep(2)
        self.driver.find_element_by_id("uploadPicture").send_keys("C:/Users/ASUS/Pictures/download.png")
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="currentAddress"]').send_keys("Rievaldhi test using selenium with python")
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="state"]/div/div[1]').click()
        pyautogui.typewrite("rajasthan")
        pyautogui.press("enter")
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="city"]/div/div[2]').click()
        pyautogui.typewrite("panipat")
        pyautogui.press("enter")
        time.sleep(5)

        try : 
            WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div')))
            print("Pop up appears")
            time.sleep(3)
            self.driver.find_element_by_id("closeLargeModal").click()
            print("Pop up closed")

        except TimeoutException:
            print("Pop up NOT appears")
            pass
        time.sleep(4)
        assert self.driver.title == 'ToolsQA'

