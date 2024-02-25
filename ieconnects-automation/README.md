# IE Connects

This project contains Python scripts to automate various tasks on the IEConnects platform. The scripts use Selenium WebDriver to interact with the website and perform tasks such as logging in, navigating to club and events pages, etc.

## Setup

Create the file `credentials.yaml`:
```yaml
username: [studnet.email@student.ie.edu]
password: [your_password]
```

## Modules



`ieconnects_login.py`
---

This module contains the functions to login to ieConnects. It uses the `credentials.yaml` file to get the username and password.

`ieconnects_login.py` contains the following functions:

`login()`: Logs in to ieConnects and returns the `requests.Session()` object.`

```python
from ieconnects_login import login, DEFAULT_HYPER
from selenium import webdriver

driver = webdriver.Firefox()

session = login(
    driver=driver,
    HYPER_i=DEFAULT_HYPER,
    username_i='username', # read from yaml
    password_i='password' # read from yaml
)
```

After the login, the `driver` object will be in the `ieConnects` page. You can then use other moduels to interact with the page.


`ieconnects_club.py`
---

This module contains the functions to interact with the club and events pages on ieConnects. It should be used after logging in with the `ieconnects_login.py` module.

`ieconnects_club.py` contains the following functions:

`open_club_page(driver: webdriver.Firefox, club_id: str) -> webdriver.Firefox`:
This function navigates to the club page specified by the `club_id` parameter. The `driver` parameter should be a logged-in webdriver instance.

Example usage:
```python
from ieconnects_club import open_club_page

driver = open_club_page(driver, '300003041')
```

`open_events_page(driver: webdriver.Firefox, past_events: bool = False) -> webdriver.Firefox`:
This function navigates to the events page. If `past_events` is set to `True`, it will navigate to the past events page. The `driver` parameter should be a logged-in webdriver instance.

Example usage:
```python
from ieconnects_club import open_events_page

driver = open_events_page(driver, past_events=True)
```

After using these functions, the `driver` object will be on the respective page. You can then interact with the page as needed.
