from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@given(u'that we have gone to {site}')
def step_impl(context, site):
    context.site = site
    context.browser = webdriver.Chrome()
    if not site.startswith("http"):
        site = "https://" + site
    context.browser.get(site)
    time.sleep(5)

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

@then('I should see a message indicating that there are no results for "{search_term}"')
def step_impl(context, search_term):
    wait = WebDriverWait(context.driver, 10)
    no_results_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div#container yt-icon")))
    assert f"No results found for {search_term}" in no_results_message.get_attribute("aria-label")

