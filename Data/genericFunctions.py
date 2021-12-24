from Data import variables
from datetime import datetime
import random

def capture_screenshot():
    variables.driver.get_screenshot_as_png()
    now = datetime.now()
    current_time = now.strftime("%H.%M.%S")
    current_date = now.date()
    abc = variables.screenshot + str(current_date) + ' ' + str(current_time) + '.png'
    # print(abc)
    variables.driver.save_screenshot(abc)

def random_date(x):
    num = random.randrange(0, x)
    vallue = str(num)
    return vallue