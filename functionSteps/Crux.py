from Data import variables
from Data import genericFunctions
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def basicCase():
    variables.driver.maximize_window()
    variables.driver.get("https://cruxintelligence.com/")
    WebDriverWait(variables.driver, 10).until(EC.visibility_of_element_located((By.XPATH, variables.logo)))
    time.sleep(2)
    if variables.driver.find_element_by_xpath(variables.cookies).is_displayed():
        variables.driver.find_element_by_xpath(variables.cookies).click()
        genericFunctions.capture_screenshot()
    else:
        print("No cookies observed...")
        genericFunctions.capture_screenshot()

    variables.driver.find_element_by_link_text("PRODUCT").click()
    time.sleep(2)
    assert variables.driver.current_url.__contains__("product")
    time.sleep(2)
    genericFunctions.capture_screenshot()
    time.sleep(1)

    variables.driver.find_element_by_link_text("CONFIGURATIONS").click()
    time.sleep(2.5)
    assert variables.driver.current_url.__contains__("configurations")
    time.sleep(2)
    genericFunctions.capture_screenshot()
    time.sleep(1)

    variables.driver.find_element_by_link_text("ABOUT US").click()
    time.sleep(2.5)
    assert variables.driver.current_url.__contains__("about-us")
    time.sleep(2)
    genericFunctions.capture_screenshot()
    time.sleep(1)

    variables.driver.find_element_by_link_text("PRESS").click()
    time.sleep(2.5)
    assert variables.driver.current_url.__contains__("press")
    time.sleep(2)
    genericFunctions.capture_screenshot()
    time.sleep(1)

    variables.driver.find_element_by_partial_link_text("LEADERSHIP").click()
    time.sleep(2.5)
    assert variables.driver.current_url.__contains__("leadership")
    time.sleep(2)
    genericFunctions.capture_screenshot()
    time.sleep(1)

    variables.driver.find_element_by_link_text("LOG IN").click()
    time.sleep(2.5)
    page_text = variables.driver.find_element_by_xpath(variables.login_text).text
    assert page_text == "Log In"
    time.sleep(2)
    genericFunctions.capture_screenshot()
    time.sleep(1)


def check_aboutUs():
    variables.driver.find_element_by_xpath(variables.about_us).click()
    WebDriverWait(variables.driver, 10).until(EC.visibility_of_element_located((By.XPATH, variables.logo)))
    time.sleep(3)
    genericFunctions.capture_screenshot()
    action = ActionChains(variables.driver)
    action.send_keys(Keys.END).perform()
    time.sleep(1.5)
    genericFunctions.capture_screenshot()
    time.sleep(3)
    WebDriverWait(variables.driver, 10).until(EC.visibility_of_element_located((By.XPATH, variables.google_play_store)))
    try:
        if variables.driver.find_element_by_xpath(variables.google_play_store).is_displayed():
            variables.driver.find_element_by_xpath(variables.google_play_store).click()
            if len(variables.driver.window_handles) > 1:
                time.sleep(1.6)
                variables.driver.switch_to.window(window_name=variables.driver.window_handles[1])
                WebDriverWait(variables.driver, 10).until(EC.visibility_of_element_located((By.XPATH, variables.google_play_store_app_name)))
                print("Google Play Store : ", variables.driver.find_element_by_xpath(variables.google_play_store_app_name).text)
                genericFunctions.capture_screenshot()
                variables.driver.switch_to.window(window_name=variables.driver.window_handles[0])
                time.sleep(1.5)
                if (variables.driver.find_element_by_xpath(variables.apple_store).is_displayed()):
                    variables.driver.find_element_by_xpath(variables.apple_store).click()
                    variables.driver.set_page_load_timeout(30)
                    variables.driver.switch_to.window(window_name=variables.driver.window_handles[2])
                    WebDriverWait(variables.driver, 30).until(EC.visibility_of_element_located((By.XPATH, variables.apple_store_app_name)))
                    time.sleep(1.5)
                    print("Apple Store : ", variables.driver.find_element_by_xpath(variables.apple_store_app_name).text)
                    genericFunctions.capture_screenshot()
    except TimeoutError as TE:
        print("Application taking too much time to load......")


def scheduleDemo():
    variables.driver.find_element_by_xpath(variables.learn_more).click()
    WebDriverWait(variables.driver, 15).until(EC.visibility_of_element_located((By.XPATH, variables.demo_text)))
    print(variables.driver.find_element_by_xpath(variables.demo_text).text)
    # variables.driver.set_page_load_timeout(30)
    variables.driver.execute_script("window.scrollTo(0, 200)")
    ifr = variables.driver.find_element_by_xpath(variables.frame2)
    variables.driver.switch_to.frame(ifr)
    no_of_elements = len(variables.driver.find_elements_by_xpath(variables.total_demo_options))
    v = genericFunctions.random_date(no_of_elements) #3
    demo_options = "//*[@id='page-region']//div[2]/a["+v+"]"
    textval = demo_options + "/div/div[2]"
    demo_option_selected = variables.driver.find_element_by_xpath(textval).text
    print(demo_option_selected)
    variables.driver.find_element_by_xpath(demo_options).click()
    time.sleep(5)
    schedule_screen_text = variables.driver.find_element_by_xpath(variables.schedule_demo_screen_label).text
    assert demo_option_selected == schedule_screen_text