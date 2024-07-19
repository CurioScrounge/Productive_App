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
        if "Google Chrome" in window_title:
            app = Desktop(backend="uia").window(title_re=".*Google Chrome.*")
            url = app.child_window(title="Address and search bar", control_type="Edit").get_value()
        elif "Mozilla Firefox" in window_title:
            app = Desktop(backend="uia").window(title_re=".*Mozilla Firefox.*")
            url = app.child_window(title="Search with Google or enter address", control_type="Edit").get_value()
        elif "Microsoft Edge" in window_title:
            app = Desktop(backend="uia").window(title_re=".*Microsoft Edge.*")
            url = app.child_window(title="Address and search bar", control_type="Edit").get_value()
        else:
            return None

        parsed_url = urlparse(url)
        if not parsed_url.scheme:
            url = "http://" + url
        return url
    except Exception as e:
        print(f"Error getting URL from {window_title}: {e}")
        return None

def monitor_active_window():
    previous_window_title = ""
    previous_url = ""
    while True:
        current_window_title = get_active_window_title()
        if current_window_title != previous_window_title:
            previous_window_title = current_window_title
            if any(browser in current_window_title for browser in ["Google Chrome", "Mozilla Firefox", "Microsoft Edge"]):
                current_url = get_browser_url(current_window_title)
                if current_url and current_url != previous_url:
                    previous_url = current_url
                    pyperclip.copy(current_url)
                    print(f"Copied URL: {current_url}")
                elif current_url:
                    print(f"URL unchanged: {current_url}")
        time.sleep(2)  # Check every 2 seconds

if __name__ == "__main__":
    print("Starting URL capture script...")
    monitor_active_window()