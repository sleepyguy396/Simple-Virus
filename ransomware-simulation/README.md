# Python Ransomware Simulation
# Python File Encryption & Decryption Simulator

A demonstration script built using Python's `cryptography` library (`Fernet`) to illustrate how symmetric encryption algorithms encrypt and restore files within a directory. Developed for educational research and understanding cryptographic data protection mechanisms.

---

## 📌 Features

* **Symmetric Encryption (AES-128):** Utilizes `Fernet` (authenticated 128-bit AES in CBC mode) for strong file-level data protection.
* **Automated Key Management:** Generates and reads a local symmetric key file (`random_key.key`) for encryption/decryption routines.
* **Recursive Directory Traversal:** Uses `os.walk()` to recursively navigate and process files across targeted subdirectories.
* **In-Place Decryption:** Demonstrates data recovery by decrypting previously locked files back to their original state using the stored key.

---

## 🛠️ Requirements

* **Python:** `3.8+`
* **Dependencies:**
  * `cryptography` – Recipe and primitive cryptography library for Python

---

## ⚠️ Warning: Always test encryption scripts inside a dedicated test folder with non-critical sample files.

## ⚠️ Safety & Legal Disclaimer
This repository is created strictly for educational, defensive research, and academic purposes to demonstrate how file-level symmetric encryption works.

Authorized Use Only: Never run file encryption scripts on system-critical directories or hardware without permission.

Data Loss Precaution: Ensure you always maintain a backup of key files (.key) when working with symmetric encryption routines.

Liability: The author assumes no responsibility or liability for misuse or accidental loss of data resulting from this code.
