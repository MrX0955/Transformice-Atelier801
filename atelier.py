import base64
import hashlib
import tkinter  as tk
import os
import time
from colorama   import Fore
from tkinter    import filedialog

def main():
    if os.name == "nt":
        os.system("title Atelier801 - CleinKelvinn")
    root = tk.Tk()
    root.withdraw()
    
    file = filedialog.askopenfile(
        parent=root,
        mode="rb",
        title="Atelier801 - CleinKelvinn",
        filetypes=(("Text files", "*.txt"), ("All files", "*.*")),
    )
    
    if file is None:
        print(f"\n{Fore.LIGHTRED_EX} [!] Something Wrong!{Fore.RESET}")
        return

    with open(file.name, "r", encoding="utf-8", errors="ignore") as f:
        ext = f.readlines()
        
    total = 0
    os.system("cls" if os.name == "nt" else "clear")
    print(f"{Fore.RED} 🍻 Progress.. {total}/{len(ext)}", end="\r")
    start_time = time.time()
    
    SALT = bytes([
        0xF7, 0x1A, 0xA6, 0xDE, 0x8F, 0x17, 0x76, 0xA8,
        0x03, 0x9D, 0x32, 0xB8, 0xA1, 0x56, 0xB2, 0xA9,
        0x3E, 0xDD, 0x43, 0x9D, 0xC5, 0xDD, 0xCE, 0x56,
        0xD3, 0xB7, 0xA4, 0x05, 0x4A, 0x0D, 0x08, 0xB0
    ])

    with open("EncryptedOutput.txt", "a", errors="ignore") as output_file:
        for line in ext:
            try:
                email, password = line.strip().split(":")
            except ValueError:
                continue

            sha256 = hashlib.sha256(password.encode())
            hex256 = sha256.hexdigest().encode() + SALT
            hashed = hashlib.sha256(hex256).digest()
            encoded = base64.b64encode(hashed).decode()

            output_file.write(f"{email}:{encoded}:{password}\n")
            total += 1
            print(f"{Fore.RED} 🍻 Progress.. {total}/{len(ext)}", end="\r")

    elapsed_time = round(time.time() - start_time)
    print(f"\n\n{Fore.LIGHTGREEN_EX} 🌐 Job Has Been Finished! \n ⏳ Work Time: {elapsed_time} Second(s){Fore.RESET}")

if __name__ == "__main__":
    main()

#Updated June 27, 2024 at 7:00 AM ~ Made By CleinKelvinn
