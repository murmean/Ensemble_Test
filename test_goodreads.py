import pytest
from pages import Goodreads

DummyEmail = "dummydummy123123123@gmail.com"
DummyPassword = "DummyPassword"
DummyUsername = "DummyUsername"
EMAIL = "ratiumarianalexandru@gmail.com"
PASSWORD = "Testamazon123@"


def test_signup_and_login(driver):
    g = Goodreads(driver)

    g.open()
    g.click_signup()
    g.fill_signup(DummyEmail, DummyPassword, DummyUsername)
    g.open()
    g.click_signin()
    g.fill_sign_in(EMAIL, PASSWORD)

    if g.verify_logged_in():
        print("Successfully logged in")
    else:
        print("Failed to log in")
        pytest.fail("Failed to log in")
    assert "goodreads" in driver.title.lower()


def test_search_and_want_to_read(driver):
    g = Goodreads(driver)

    g.open()
    g.click_signin()
    g.fill_sign_in(EMAIL, PASSWORD)
    g.verify_logged_in()

    g.click_search_bar()
    g.enter_book_name("Harry Potter")
    g.click_search_button()
    assert g.verify_search_results(), "Search results not displayed"

    g.click_desired_book()
    assert g.verify_book_page_loaded(), "Book page not loaded"

    g.click_want_to_read()
    assert g.verify_book_added_to_shelf(), "Book not added to Want to Read shelf"


def test_search_and_review(driver):
    g = Goodreads(driver)

    g.open()
    g.click_signin()
    g.fill_sign_in(EMAIL, PASSWORD)
    g.verify_logged_in()

    g.click_search_bar()
    g.enter_book_name("Harry Potter")
    g.click_search_button()
    assert g.verify_search_results(), "Search results not displayed"

    g.click_desired_book()
    assert g.verify_book_page_loaded(), "Book page not loaded"

    g.click_write_review()
    g.write_review("This book is awesome!")
    assert g.verify_review_added(), "Review not added"