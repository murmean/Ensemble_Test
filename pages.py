from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Goodreads:

    BASE_URL = "https://www.goodreads.com/"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.BASE_URL)

    def click_signup(self):
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign up with email"))).click()

    def fill_signup(self, email, password, username):
        self.wait.until(EC.presence_of_element_located((By.ID, "ap_customer_name"))).send_keys(username)
        self.wait.until(EC.presence_of_element_located((By.ID, "ap_email"))).send_keys(email)
        self.wait.until(EC.presence_of_element_located((By.ID, "ap_password"))).send_keys(password)
        self.wait.until(EC.presence_of_element_located((By.ID, "ap_password_check"))).send_keys(password)
        self.driver.find_element(By.ID, "continue").click()

    def click_signin(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.gr-hyperlink[href='/user/sign_in']"))).click()
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign in with email"))).click()

    def fill_sign_in(self, email, password):
        self.wait.until(EC.presence_of_element_located((By.ID, "ap_email"))).send_keys(email)
        self.wait.until(EC.presence_of_element_located((By.ID, "ap_password"))).send_keys(password)
        self.driver.find_element(By.ID, "signInSubmit").click()
        print("Waiting 5 seconds for CAPTCHA...")
        time.sleep(5)

    def verify_logged_in(self):
        try:
            self.wait.until(EC.presence_of_element_located((
                By.CSS_SELECTOR, "a.dropdown__trigger--profileMenu"
            )))
            return True
        except:
            return False

    def search_book(self, book_name):
        search = self.wait.until(EC.presence_of_element_located((By.NAME, "q")))
        search.send_keys(book_name)
        search.submit()

    def click_first_book(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.bookTitle"))).click()

    def click_want_to_read(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Want to Read']"))).click()
        time.sleep(2)

    def click_shelf_dropdown(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[aria-label='Tap to choose a shelf for this book']"))).click()
        time.sleep(1)

    def click_read(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Read']"))).click()
        time.sleep(2)

    def refresh_page(self):
        self.driver.refresh()
        time.sleep(3)

    def close_modal(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Close']"))).click()
        time.sleep(2)

    def click_write_review(self):
        time.sleep(3)
        button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Write a Review']/ancestor::button")))
        self.driver.execute_script("arguments[0].click();", button)
        time.sleep(2)

    def write_review(self, text):
        review_box = self.wait.until(EC.presence_of_element_located((By.ID, "review_review_usertext")))
        review_box.send_keys(text)
        time.sleep(1)
        submit_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input.gr-button[type='submit'][value='Post']")))
        submit_button.click()
        time.sleep(3)

    def click_search_bar(self):
        search = self.wait.until(EC.element_to_be_clickable((By.NAME, "q")))
        search.click()

    def enter_book_name(self, book_name):
        search = self.wait.until(EC.presence_of_element_located((By.NAME, "q")))
        search.send_keys(book_name)

    def click_search_button(self):
        search = self.wait.until(EC.presence_of_element_located((By.NAME, "q")))
        search.submit()

    def verify_search_results(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.bookTitle")))
            return True
        except:
            return False

    def click_desired_book(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.bookTitle"))).click()

    def verify_book_page_loaded(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1.Text.Text__title1")))
            return True
        except:
            return False

    def verify_book_added_to_shelf(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Want to Read')]")))
            return True
        except:
            return False

    def verify_review_added(self):
        try:
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//a[@class='userReview' and contains(text(), 'TestUser')]")))
            return True
        except:
            return False