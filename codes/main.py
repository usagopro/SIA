# import the required packages

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import re
import time


# global variables

SIA_STATE = 0

# Set up Chrome options for headless mode
chrome_options = Options()
# chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()


def prompt(uv):
    global SIA_STATE
    if SIA_STATE == 0:
        print(f'searching for {uv}')
        driver.get(f'https://www.google.com/search?q={uv}')
        SIA_STATE = 1
    pass


def analyse_website():
    webpage_text = driver.find_element(By.TAG_NAME, 'html').text
    print(webpage_text)
    anchor_tags = driver.find_elements(By.TAG_NAME, 'a')
    print('a: ', len(anchor_tags))
    anchor_list = []

    # Loop through each anchor tag and extract attribute-value pairs
    # for anchor_tag in anchor_tags:
    #     attributes = anchor_tag.get_attribute("outerHTML")  # Get the HTML of the anchor tag
    #     anchor_dict = {}
    #     # Parse the HTML to extract attribute-value pairs
    #     for attr in anchor_tag.get_property("attributes"):
    #         attribute_name = attr["name"]
    #         attribute_value = attr["value"]
    #         anchor_dict[attribute_name] = attribute_value
    #     anchor_list.append(anchor_dict)

    # print(len(anchor_list))

    button_elements = driver.find_elements(By.TAG_NAME, 'button')
    print('buttons: ', len(button_elements))
    button_list = []

    # Loop through each anchor tag and extract attribute-value pairs
    # for button_element in button_elements:
    #     attributes = button_element.get_attribute("outerHTML")  # Get the HTML of the button element
    #     button_dict = {}
    #     # Parse the HTML to extract attribute-value pairs
    #     for attr in button_element.get_property("attributes"):
    #         attribute_name = attr["name"]
    #         attribute_value = attr["value"]
    #         button_dict[attribute_name] = attribute_value
    #     button_list.append(button_dict)

    # print(len(button_list))

    href_links = driver.find_elements(By.XPATH, "//*[@href]")
    print('hrefs: ', len(href_links))

    form_elements = driver.find_elements(By.TAG_NAME, "form")
    print('forms: ', len(form_elements))

    input_elements = driver.find_elements(By.TAG_NAME, 'input')
    meter_elements = driver.find_elements(By.TAG_NAME, 'meter')
    object_elements = driver.find_elements(By.TAG_NAME, 'object')
    optgroup_elements = driver.find_elements(By.TAG_NAME, 'optgroup')
    option_elements = driver.find_elements(By.TAG_NAME, 'option')
    output_elements = driver.find_elements(By.TAG_NAME, 'output')
    textarea_elements = driver.find_elements(By.TAG_NAME, 'textarea')
    select_elements = driver.find_elements(By.TAG_NAME, 'select')
    progress_elements = driver.find_elements(By.TAG_NAME, 'progress')

    audio_elements = driver.find_elements(By.TAG_NAME, 'audio')
    embed_elements = driver.find_elements(By.TAG_NAME, 'embed')
    figure_elements = driver.find_elements(By.TAG_NAME, 'figure')
    img_elements = driver.find_elements(By.TAG_NAME, 'img')
    picture_elements = driver.find_elements(By.TAG_NAME, 'picture')
    source_elements = driver.find_elements(By.TAG_NAME, 'source')
    video_elements = driver.find_elements(By.TAG_NAME, 'video')


def perform_action(action):
    if action == 'open':
        pass


def user_input():
    uv = input("what would you like to do? \t:")
    return uv


if __name__ == '__main__':
    while True:
        user_voice = user_input()
        if user_voice == 'x':
            break
        prompt(user_voice)
    driver.quit()

