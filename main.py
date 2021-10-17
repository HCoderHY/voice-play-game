import pyautogui
import speech_recognition as sr
import os

m = sr.Microphone(device_index=1)
r = sr.Recognizer()

with m as s:
    print("Говори...")
    audio = r.listen(s)

but = r.recognize_google(audio, language="ru-RU").lower()
while True:
    if but == "ехать" or but == "вперёд" or but == "дальше" or but == "газ" or but == "газз" or but == "поехали" or but == "иди" or but == "идти" or but == "пошол" or but == "пошол вперёд":
        pyautogui.keyDown("w")
        pyautogui.keyDown("w")
        pyautogui.keyDown("w")
    elif but == "назад" or but == "ехать назад" or but == "поехали назад" or but == "задка" or but == "иди назад" or but == "идти назад" or but == "пошол назад" or but == "пошол задкой":
        pyautogui.keyDown("s")
        pyautogui.keyDown("s")
        pyautogui.keyDown("s")
    elif but == "влево" or but == "на лево" or but == "налево" or but == "поехали в лево" or but == "иди влево" or but == "идти на лево" or but == "пошол налево" or but == "пошол влево" or but == "идти налево" or but == "пошол на лево":
        pyautogui.keyDown("a")
        pyautogui.keyDown("a")
        pyautogui.keyDown("a")
    elif but == "вправо" or but == "на право" or but == "направо" or but == "поехали в право" or but == "иди вправо" or but == "идти на право" or but == "пошол направо" or but == "пошол вправо" or but == "идти направо" or but == "пошол на право":
        pyautogui.keyDown("d")
        pyautogui.keyDown("d")
        pyautogui.keyDown("d")
    else:
        print(f"не распознано: {but}")
    os.system("start BFG.exe")
