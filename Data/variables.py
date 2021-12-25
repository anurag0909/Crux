from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\anurag.agrawal\\Desktop\\CruxIntelligence\\chromedriver.exe")
screenshot = "C:\\Users\\anurag.agrawal\\Desktop\\CruxIntelligence\\Screenshots\\"
source_excel = "C:\\Users\\anurag.agrawal\\Desktop\\CruxIntelligence\\Data\\TestCases.xlsx"

logo = "//div//a[@rel = 'home']"
check_element = "//div[@class = 'col-md-5'][1]"
tab_headers = "//div[@id= 'navbarNavDropdown']//li"
product_video = "//body/div[@id = 'player']//video"
login_text = "//*[@id='page']/div[2]/div/div/div/div[1]"
about_us = "//div/ul/li/a[@title = 'About Us']"
google_play_store = "//*[@id='wrapper-footer']/div/div[1]/div[1]/a[1]/img"
google_play_store_app_name = "//div//h1/span[contains(text(), 'Crux Intelligence')]"
apple_store = "//*[@id='wrapper-footer']/div/div[1]/div[1]/a[2]"
apple_store_app_name = "//header/h1[text() = 'Crux Intelligence']"
cookies = "//div/a[contains(text(), 'Accept')]"
learn_more = "//*[@id='myP']/nav/div/a[2]"
demo_text = "//div/h1[text() = 'Request a Demo']"
total_demo_options = "//*[@id='page-region']//div[2]/a"
frame1= "//*[@id='page']/div[2]//div/section[2]//div/iframe"
frame2 = "//div[@class = 'calendly-inline-widget']/iframe"
schedule_demo_screen_label = "//*[@id='page-region']//div[1]//div[1]/div[2]//div[1]/h1"