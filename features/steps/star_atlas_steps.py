from time import sleep

from behave import given, when, then
from page_objects.star_atlas.star_atlas_page import StarAtlasPage
from utils.webdriver import WebDriver
from utils.element_locator import ElementLocator

driver = None


@given('I am on the Star Atlas website')
def step_open_star_atlas(context):
    global driver
    driver = WebDriver.get_driver()
    driver.get("https://play.staratlas.com/")


@when('I log in with valid credentials')
def step_log_in(context):
    star_atlas_page = StarAtlasPage(driver)
    star_atlas_page.login("your_username", "your_password")


@then('I should see my profile')
def step_verify_profile(context):
    star_atlas_page = StarAtlasPage(driver)
    assert star_atlas_page.is_profile_visible()


@when('I click the "{element_name}" element')
def step_click_element(context, element_name):
    star_atlas_page = StarAtlasPage(driver)
    element_locator = ElementLocator.get_locator(element_name)
    star_atlas_page.click_element(element_locator)


@then('I should see the {page} page')
def step_verify_page(context, page):
    star_atlas_page = StarAtlasPage(driver)
    assert star_atlas_page.is_page_visible(page)


@then("10 seconds are waited")
def step_impl(context):
    sleep(10)
