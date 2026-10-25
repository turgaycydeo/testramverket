import sys

from playwright.sync_api import sync_playwright

from src.features.pages.add_book_page import AddBookPage
from src.features.pages.base_page import BasePage
from src.features.pages.catalog_page import CatalogPage
from src.features.pages.favorites_page import FavoritesPage
from src.features.pages.stats_page import StatsPage


def before_all(context):
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")

    headless = context.config.userdata.getbool("headless", True)

    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=headless)


def before_scenario(context, scenario):
    context.page = context.browser.new_page()
    context.page.set_default_timeout(3_000)

    context.header = BasePage(context.page)

    context.catalog = CatalogPage(context.page)
    context.add_book = AddBookPage(context.page)
    context.favorites = FavoritesPage(context.page)
    context.stats = StatsPage(context.page)
    context.views = {
        "Katalog": context.catalog,
        "Lägg till bok": context.add_book,
        "Mina böcker": context.favorites,
        "Statistik": context.stats,
    }


def after_scenario(context, scenario):
    if context.page:
        context.page.close()


def after_all(context):
    if context.browser:
        context.browser.close()
    if context.playwright:
        context.playwright.stop()
