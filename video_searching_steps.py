from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

@given('I am on the YouTube homepage')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.youtube.com/")

@when('I enter "{search_term}" into the search bar')
def step_impl(context, search_term):
    search_input = context.driver.find_element(By.NAME, "search_query")
    search_input.send_keys(search_term)

@when('I click the search button')
def step_impl(context):
    search_button = context.driver.find_element(By.ID, "search-icon-legacy")
    search_button.click()
    time.sleep(5) 

@then('I should see a list of videos related to "{search_term}"')
def step_impl(context, search_term):
    search_result_heading = context.driver.find_element(By.TAG_NAME, "h1")
    assert search_term.lower() in search_result_heading.text.lower()
