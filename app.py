import pyautogui as pa
import pyperclip
import time
import webbrowser

webbrowser.open_new_tab("https://www.google.com")
# time.sleep(1)

pyperclip.copy("平泉町 観光")
time.sleep(1)
# pa.hotkey("command", "v")
# なぜかhotkeyだと「v」と入力され、謎の韓国人歌手が表示される
pa.keyDown("command")
pa.keyDown("v")
pa.keyUp("v")
pa.keyUp("command")
time.sleep(1)
pa.press("enter")
time.sleep(1)

pa.screenshot("evidence.png")
