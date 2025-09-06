# import the required packages

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
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


# variables

cur_tab_index = 0
tabs = ['']


def prompt(uv):
    global SIA_STATE, cur_tab_index, tabs
    if re.search('refresh|reload', uv):
        refresh_tab()
        print('reloading')
        return
    elif re.search('tab', uv):
        if re.search('forward', uv):
            driver.forward()
            return
        elif re.search('close', uv):
            if re.search('empty', uv):
                i = 0
                while i < len(tabs):
                    print(tabs[i])
                    if tabs[i] == '':
                        print(i)
                        cur_tab_index = i
                        driver.switch_to.window(driver.window_handles[i])
                        close_tab()
                        if len(tabs) == 1:
                            break
                    else:
                        i += 1

            result_index = find_matching_sentence(tabs, uv)
            if result_index == -1:
                close_tab()
                return
            else:
                print(result_index)
                driver.switch_to.window(driver.window_handles[result_index])
                cur_tab_index = result_index
                close_tab()
                return
        elif re.search('new|another', uv):
            new_tab()
            print(tabs)
            SIA_STATE = 0
            return
        elif re.search('go|change|back', uv):
            print(tabs)
            result_index = find_matching_sentence(tabs, uv)
            if result_index == -1:
                if re.search('back', uv):
                    driver.back()
                    return
            else:
                print(result_index)
                driver.switch_to.window(driver.window_handles[result_index])
                cur_tab_index = result_index
                return

    if re.search('forward', uv):
        driver.forward()
        return
    elif re.search('back', uv):
        driver.back()
        return

    if SIA_STATE == 0:
        print(f'searching for {uv}')
        driver.get(f'https://www.google.com/search?q={uv}')
        tabs[cur_tab_index] = driver.title
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


def refresh_tab():
    driver.refresh()


def new_tab():
    global cur_tab_index, tabs
    cur_tab_index = len(tabs)
    print(cur_tab_index)
    driver.execute_script("window.open('', '_blank');")
    # time.sleep(1)
    print(cur_tab_index)
    print(len(driver.window_handles))
    driver.switch_to.window(driver.window_handles[-1])
    tabs.append(driver.title)


def close_tab():
    global cur_tab_index
    del tabs[cur_tab_index]
    if len(tabs) == 0:
        new_tab()
        cur_tab_index -= 1
        driver.switch_to.window(driver.window_handles[cur_tab_index])
    else:
        cur_tab_index = 0
    driver.close()
    time.sleep(4)
    driver.switch_to.window(driver.window_handles[cur_tab_index])


def find_matching_sentence(sentences, new_sentence):
    # Iterate through the list of sentences
    for index, sentence in enumerate(sentences):
        # Skip empty sentences
        if not sentence:
            continue

        # Use regular expression to find matching words
        matches = re.findall(r'\b\w+\b', sentence)
        for match in matches:
            if match in new_sentence.split():
                return index  # Return the index if a match is found

    return -1  # Return -1 if no match is found


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

