Ensemble Test submission

```markdown
# Goodreads Automation Tests

Automated test suite for Goodreads website using Selenium WebDriver and pytest.

## Requirements

- Python 3.7+
- Chrome browser
- Internet connection

## Installation

1. Clone the repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Update the credentials in `test_goodreads.py`:

```python
EMAIL = "your_email@gmail.com"
PASSWORD = "your_password"
```

## Running Tests

Run all tests:

```bash
pytest test_goodreads.py -v
```

Run with output capture disabled (to see print statements):

```bash
pytest test_goodreads.py -v -s
```

Run a specific test:

```bash
pytest test_goodreads.py::test_search_and_want_to_read -v -s
```

## Test Scenarios

### 1. Sign Up and Login
- Navigate to Goodreads
- Click Sign up button
- Fill registration form
- Sign in with existing account
- Verify successful login

### 2. Search and Add to "Want to Read"
- Search for a book
- Select book from results
- Click "Want to Read" button
- Verify book added to shelf

### 3. Search and Add Review
- Search for a book
- Select book from results
- Click "Write a Review"
- Enter review text
- Submit review
- Verify review posted

## Files
 `conftest.py` | pytest configuration and fixtures 
 `pages.py` | Page Object Model for Goodreads 
 `test_goodreads.py` |Test cases 
 `requirements.txt`  Python dependencies 

## Notes

- CAPTCHA requires manual intervention during login (30 second wait)
- Email verification is skipped for sign up
- Tests use an existing account for login

## Troubleshooting

If tests fail:
1. Make sure Chrome is updated
2. Check internet connection
3. Verify credentials are correct
4. Increase wait time for CAPTCHA in `fill_sign_in()` method
```
