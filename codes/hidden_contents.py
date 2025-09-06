# import the required packages

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Set up Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")


# global variables

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()


def find_clickable_elements():
    clickable_elements = driver.find_elements(By.CSS_SELECTOR, "a, button, input[type='button'], input[type='submit']")
    print(len(clickable_elements))
    tag_names = [element.tag_name for element in clickable_elements]

    # Create an empty dictionary to store counts
    count_dict = {}

    # Iterate through the list and update counts
    for item in tag_names:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1

    # Print the unique values and their counts
    for key, value in count_dict.items():
        print(f"{key}: {value}")

    script = """
    function findElementsWithEventListeners() {
        const elementsWithEventListeners = [];

        const allElements = document.querySelectorAll('*');

        allElements.forEach(element => {

        const eventNames = getEventNames(element);
        
            if (eventNames.length > 0) {
                elementsWithEventListeners.push({
                    element: element,
                    eventNames: eventNames
                });
            }
        });
        
        return elementsWithEventListeners;
    }
    
    // Function to get event names attached to an element
    function getEventNames(element) {
        const eventNames = [];
        
        // Loop through standard event names
        const standardEvents = ['click', 'change', 'mouseover', 'keydown', 'etc.'];
        
        standardEvents.forEach(eventName => {
            if (typeof element['on' + eventName] === 'function') {
                eventNames.push(eventName);
            }
        });
        
        // Additionally, you can check for custom events if applicable
        
        return eventNames;
    }
    
    // Usage
    const elementsWithEventListeners = findElementsWithEventListeners();
    return elementsWithEventListeners 
    """

    event_listeners = driver.execute_script(script)

    # Print the elements with their associated event listeners
    print(event_listeners)


def analyse_website():
    pass


def perform_action(action):
    if action == 'open':
        pass


def user_input():
    uv = input("what would you like to do? \t:")
    return uv


if __name__ == '__main__':
    driver.get("https://www.amazon.com/")
    find_clickable_elements()
    while True:
        user_voice = user_input()
        if user_voice == 'x':
            break
