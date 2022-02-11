import base64
import hashlib
import urllib.parse
import os
from colorama import Fore
import tkinter
from tkinter import filedialog


root = tkinter.Tk()
root.withdraw()

class load_combos:
    global email, password

    print('\n')
    print(f" {Fore.LIGHTCYAN_EX} ~ [?] 𝐂𝐨𝐦𝐛𝐨𝐥𝐢𝐬𝐭'𝐢 𝐒𝐞𝐜𝐦𝐞𝐤 𝐢𝐜𝐢𝐧 𝐄𝐍𝐓𝐄𝐑'𝐞 𝐁𝐚𝐬..")
    input()

    fileNameCombo = filedialog.askopenfile(parent=root, mode='rb', title='𝐂𝐨𝐦𝐛𝐨𝐥𝐢𝐬𝐭 𝐃𝐨𝐬𝐲𝐚𝐬𝐢𝐧𝐢 𝐒𝐞𝐜!',
                                       filetype=(("txt", "*.txt"), ("All files", "*.txt")))
    if fileNameCombo is None:
        print()
        print(f" {Fore.LIGHTRED_EX} [!] 𝐃𝐨𝐠𝐫𝐮 𝐂𝐨𝐦𝐛𝐨𝐥𝐢𝐬𝐭'𝐢 𝐒𝐞𝐜.")
    else:
        print(Fore.LIGHTCYAN_EX)
        hawli = print(" ~ 𝐂𝐨𝐦𝐛𝐨𝐥𝐢𝐬𝐭 𝐘𝐮𝐤𝐥𝐞𝐧𝐢𝐲𝐨𝐫..\n")
        os.system('cls')
        print(Fore.MAGENTA)
        print()
        with open(fileNameCombo.name, 'r', encoding='utf-8') as e:
            ext = e.readlines()
            for line in ext:
                email = line.split(":")[0].replace('\n', '')
                password = line.split(":")[1].replace('\n', "")
                capture = email + ":" + password

                string = password

                SALT = bytes((
	                0xf7, 0x1a, 0xa6, 0xde, 0x8f, 0x17, 0x76, 0xa8, 0x03, 0x9d, 0x32, 0xb8, 0xa1, 0x56, 0xb2, 0xa9,
	                0x3e, 0xdd, 0x43, 0x9d, 0xc5, 0xdd, 0xce, 0x56, 0xd3, 0xb7, 0xa4, 0x05, 0x4a, 0x0d, 0x08, 0xb0
                ))


                sha256 = hashlib.sha256(string.encode()) # hash the password with SHA256
                hex256 = sha256.hexdigest().encode() # convert it into hexdecamals
                hex256 += SALT # salt it

                hashed = hashlib.sha256(hex256).digest() # re-hash it
                last = base64.b64encode(hashed) # return it in base64 bytes

                savefile = open("hashli.txt", "a")
                savefile.write("{}:{}:{}\n".format(email, last, password))