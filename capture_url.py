import pygetwindow as gw
from pywinauto import Desktop
import time
import pyperclip
from urllib.parse import urlparse

def get_active_window_title():
    active_window = gw.getActiveWindow()
    if active_window:
        return active_window.title
    return None

def get_browser_url(window_title):
    try:
        if "Chrome" in window_title:
            app = Desktop(backend="uia").window(title_re=".*Chrome.*")
            address_bar = app.child_window(title="Address and search bar", control_type="Edit")
        elif "Firefox" in window_title:
            app = Desktop(backend="uia").window(title_re=".*Firefox.*")
            address_bar = app.child_window(title="Search with Google or enter address", control_type="Edit")
        elif "Edge" in window_title:
            app = Desktop(backend="uia").window(title_re=".*Edge.*")
            address_bar = app.child_window(title="Address and search bar", control_type="Edit")
        else:
            print(f"No matching browser found in window title: {window_title}")
            return None

        url = address_bar.get_value()
        parsed_url = urlparse(url)
        if not parsed_url.scheme:
            url = "http://" + url
        return url
    except Exception as e:
        print(f"Error getting URL from {window_title}: {e}")
        return None

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def monitor_active_window():
    previous_window_title = ""
    previous_url = ""
    while True:
        current_window_title = get_active_window_title()
        if current_window_title:
            print(f"Current active window title: {current_window_title}")  # Debug logging
            if current_window_title != previous_window_title:
                previous_window_title = current_window_title
                if any(browser in current_window_title for browser in ["Chrome", "Firefox", "Edge"]):
                    current_url = get_browser_url(current_window_title)
                    if current_url and is_valid_url(current_url) and current_url != previous_url:
                        previous_url = current_url
                        pyperclip.copy(current_url)
                        print(f"Copied URL: {current_url}")
                    elif current_url:
                        print(f"URL unchanged: {current_url}")
        else:
            print("No active window detected.")
        time.sleep(5)  # Check every 5 seconds

if __name__ == "__main__":
    print("Starting URL capture script...")
    monitor_active_window()