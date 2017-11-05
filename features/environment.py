from browser import Browser
from features.pages.main_page import MainPage


def before_all(context):
    context.browser = Browser()
    context.main_page = MainPage()
    context.browser.login()


def before_scenario(context, scenario):
    context.main_page.archive_notes()


def after_scenario(context, scenario):
    context.main_page.archive_notes()


def after_all(context):
    context.browser.close()
