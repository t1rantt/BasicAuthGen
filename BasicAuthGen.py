#!/usr/bin/env python3

import sys
import base64
from pathlib import Path

try:
    import pyperclip
except ImportError:
    pyperclip = None


def load_list(path):
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            return [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"[!] Error leyendo {path}: {e}")
        sys.exit(1)


def main():
    if len(sys.argv) != 3:
        print(f"Uso: {sys.argv[0]} <users.txt> <passwords.txt>")
        sys.exit(1)

    users_path = Path(sys.argv[1])
    passwords_path = Path(sys.argv[2])

    users = load_list(users_path)
    passwords = load_list(passwords_path)

    output_file = "list.txt"
    total = 0

    with open(output_file, "w", encoding="utf-8") as out:
        for user in users:
            for password in passwords:

                # user:password
                combo1 = f"{user}:{password}"
                encoded1 = base64.b64encode(combo1.encode()).decode()
                out.write(encoded1 + "\n")
                total += 1

                # password:user
                combo2 = f"{password}:{user}"
                encoded2 = base64.b64encode(combo2.encode()).decode()
                out.write(encoded2 + "\n")
                total += 1

    print(f"[+] Generado {output_file} con {total} combinaciones")

    # Copiar al clipboard (carga completa al final)
    try:
        with open(output_file, "r", encoding="utf-8") as f:
            output_text = f.read()

        if pyperclip:
            pyperclip.copy(output_text)
            print("[+] Contenido copiado al clipboard")
        else:
            print("[!] pyperclip no instalado. Instálalo con: pip install pyperclip")
    except Exception as e:
        print(f"[!] Error copiando al clipboard: {e}")


if __name__ == "__main__":
    main()
