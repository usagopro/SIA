from selenium import webdriver
from selenium.webdriver.common.by import By


def dfs_traversal(element):
    # print(element.text)  # Print the text of the current element
    if element.is_enabled():
        if element.tag_name == 'button':
            print(element.tag_name + ' is and button')
        elif element.tag_name == 'a':
            print(element.tag_name + ' is an anchor tag')
        elif element.get_attribute('onclick') is not None:
            print(element.tag_name + ' has an onclick attribute')

    for index, ele in enumerate(element.find_elements(By.XPATH, "./*")):
        dfs_traversal(ele)

driver = webdriver.Chrome()  # Initialize the WebDriver
driver.get("https://www.google.com/search?q=amazon")  # Navigate to the webpage

anchor_tags = driver.find_elements(By.TAG_NAME, 'a')
print(len(anchor_tags))
# root_element = driver.find_element(By.TAG_NAME, "html")  # Start from the HTML root element
# dfs_traversal(root_element)  # Perform DFS traversal

driver.quit()  # Close the WebDriver when done
