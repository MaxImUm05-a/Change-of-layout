import keyboard as kb
import pyperclip as pc
import pyautogui as pg

CYR_TO_LAT = {
    'й': 'q', 'ц': 'w', 'у': 'e', 'к': 'r', 'е': 't', 'н': 'y', 'г': 'u', 'ш': 'i', 'щ': 'o', 'з': 'p',
    'х': '[', 'ї': ']', 'ф': 'a', 'і': 's', 'в': 'd', 'а': 'f', 'п': 'g', 'р': 'h', 'о': 'j', 'л': 'k',
    'д': 'l', 'ж': ';', 'є': '\'', 'я': 'z', 'ч': 'x', 'с': 'c', 'м': 'v', 'и': 'b', 'т': 'n', 'ь': 'm',
    'б': ',', 'ю': '.', '.': '/'
}


def change(eng):
    uasp = []
    for x in range(len(eng)):
          try:
             uasp.append(CYR_TO_LAT[eng[x]])
          except:
                uasp.append(eng[x])
    ua = ''.join(uasp)
    return ua

def main():
    pg.hotkey('ctrl', 'c')
    eng = pc.paste()
    ua = change(eng)
    pc.copy(ua)
    pg.hotkey('ctrl', 'v')

def add():
    kb.add_hotkey('shift', main)