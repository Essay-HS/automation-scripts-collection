import pyautogui
import time
import os

# Give yourself a moment to switch to the correct screen
time.sleep(2)

# Maximize the Firefox window manually before running or automate it:
# pyautogui.hotkey("command", "space")  # Open Spotlight (macOS)
# pyautogui.write("firefox")
# pyautogui.press("return")
# time.sleep(2)

# Move mouse to the Firefox search bar and click
pyautogui.click(40, 1040)  # Replace with your actual screen coordinates

# Type the search query
pyautogui.write("teddy bear")
pyautogui.press("return")

# Wait for search results to load
time.sleep(4)

# Scroll down to ensure first result is visible
pyautogui.scroll(-500)

# Screenshot the page
screenshot_path = os.path.expanduser("~/Desktop/teddy_bear_search_pyauto.png")
pyautogui.screenshot(screenshot_path)
print(f"✅ Screenshot saved to {screenshot_path}")
