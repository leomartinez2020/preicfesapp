import re
from playwright.sync_api import Page, expect


def test_homepage_has_Playwright_in_title_and_get_started_link_linking_to_the_intro_page(page: Page):
    page.goto("https://bestpreicfes.com/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Bestpreicfes - Inicio"))

    # create a locator
    blog_elem = page.get_by_text("Blog")

    # Expect an attribute "to be strictly equal" to the value.
    expect(blog_elem).to_have_attribute("href", "/blog/posts/")

    # Click the get started link.
    blog_elem.click()

    # Expects the URL to contain intro.
    expect(page).to_have_url(re.compile(".*blog"))
