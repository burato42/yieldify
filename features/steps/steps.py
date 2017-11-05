from behave import given, when, then
from features.pages.main_page import MainPageLocator
from hamcrest import assert_that, equal_to
from faker import Faker


@given('I am logged in and I am in Google Keep page')
def step_impl(context):
    print(context.browser.driver.title)


@given('there is a text note on the page')
def step_impl(context):
    context.main_page.click_element(*MainPageLocator.TAKE_NOTE)
    context.main_page.fill(Faker().company(), *MainPageLocator.TITLE)
    context.main_page.fill(Faker().company(), *MainPageLocator.TAKE_NOTE)
    context.main_page.click_element(*MainPageLocator.DONE)


@when('I click on Take a note field')
def step_impl(context):
    context.main_page.click_element(*MainPageLocator.TAKE_NOTE)


@when('I enter title "{title}"')
def step_impl(context, title):
    context.main_page.fill(title, *MainPageLocator.TITLE)


@when('I enter text "{text}"')
def step_impl(context, text):
    context.main_page.fill(text, *MainPageLocator.TAKE_NOTE)


@when('I press Done')
def step_impl(context):
    context.main_page.click_element(*MainPageLocator.DONE)


@when('I open More menu')
def step_impl(context):
    context.main_page.press_more()


@when('press Delete note')
def step_impl(context):
    context.main_page.get_element(*MainPageLocator.DELETE_NOTE).click()


@then('the new note is on the page and I can click it')
def step_impl(context):
    context.main_page.click_last_note(*MainPageLocator.NOTE)


@then('the saved title is equal to "{title}"')
def step_impl(context, title):
    title_element = context.main_page.get_elements(*MainPageLocator.OPEN_NOTE_TITLE)[0]
    title_element.click()
    assert_that(title_element.text, equal_to(title))


@then('the saved text is equal to "{text}"')
def step_impl(context, text):
    text_elements = context.main_page.get_elements(*MainPageLocator.OPEN_NOTE_TITLE)
    if len(text_elements) == 2:
        text_element = text_elements[1]
    else:
        text_element = text_elements[0]
    text_element.click()
    assert_that(text_element.text, equal_to(text))


@then('the note is not present on the page')
def step_impl(context):
    assert_that(len(context.main_page.get_elements(*MainPageLocator.NOTE)), equal_to(0))
