import pygetwindow as gw
import pyperclip
import pyautogui

def get_chrome_tabs():
    # Activate the Chrome window
    chrome_window = gw.getWindowsWithTitle('Google Chrome')[0]
    chrome_window.activate()
    tab_url_list = []
    pyautogui.hotkey('ctrl', 't')
    pyautogui.hotkey('ctrl', 'w')
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.hotkey('ctrl', 'c')
    tab_url = pyperclip.paste()
    # print(tab_url)
    while tab_url not in tab_url_list:

        tab_url_list.append(tab_url)
        pyautogui.hotkey('ctrl', 'tab')
        pyautogui.hotkey('ctrl', 'l')
        pyautogui.hotkey('ctrl', 'c')
        tab_url = pyperclip.paste()

    # Split the clipboard content by newlines to get individual URLs

    # Close the new tab (optional, remove if not needed)

    return tab_url_list

if __name__ == '__main__':
    urls = get_chrome_tabs()
    print("Open tab URLs:")
    for url in urls:
        print(url)
