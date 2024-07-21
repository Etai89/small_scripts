import pyautogui
import pyperclip
def get_mouse_position():
    x, y = pyautogui.position()
    print(f"Current mouse position: ({x}, {y})")
    pyperclip.copy(f"{x}, {y}")  # Copy mouse position to clipboard
get_mouse_position()


