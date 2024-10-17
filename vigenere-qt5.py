import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton

class VigenereCipher:
    def __init__(self):
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def encrypt(self, plaintext, key):
        ciphertext = ''
        key = key.upper()
        plaintext = plaintext.upper()
        key_length = len(key)
        key_as_int = [self.alphabet.index(i) for i in key]

        for i, char in enumerate(plaintext):
            if char in self.alphabet:
                idx = (self.alphabet.index(char) + key_as_int[i % key_length]) % 26
                ciphertext += self.alphabet[idx]
            else:
                ciphertext += char

        return ciphertext

    def decrypt(self, ciphertext, key):
        plaintext = ''
        key = key.upper()
        ciphertext = ciphertext.upper()
        key_length = len(key)
        key_as_int = [self.alphabet.index(i) for i in key]

        for i, char in enumerate(ciphertext):
            if char in self.alphabet:
                idx = (self.alphabet.index(char) - key_as_int[i % key_length]) % 26
                plaintext += self.alphabet[idx]
            else:
                plaintext += char

        return plaintext

class VigenereCipherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.cipher = VigenereCipher()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Key input
        key_layout = QHBoxLayout()
        key_label = QLabel('Key:')
        self.key_input = QLineEdit()
        key_layout.addWidget(key_label)
        key_layout.addWidget(self.key_input)
        layout.addLayout(key_layout)

        # Plaintext input
        plaintext_label = QLabel('Plaintext:')
        self.plaintext_input = QTextEdit()
        layout.addWidget(plaintext_label)
        layout.addWidget(self.plaintext_input)

        # Encrypt button
        encrypt_button = QPushButton('Encrypt')
        encrypt_button.clicked.connect(self.encrypt_text)
        layout.addWidget(encrypt_button)

        # Ciphertext output
        ciphertext_label = QLabel('Ciphertext:')
        self.ciphertext_output = QTextEdit()
        self.ciphertext_output.setReadOnly(True)
        layout.addWidget(ciphertext_label)
        layout.addWidget(self.ciphertext_output)

        # Decrypt button
        decrypt_button = QPushButton('Decrypt')
        decrypt_button.clicked.connect(self.decrypt_text)
        layout.addWidget(decrypt_button)

        self.setLayout(layout)
        self.setWindowTitle('Vigenère Cipher')
        self.setGeometry(300, 300, 400, 400)

    def encrypt_text(self):
        key = self.key_input.text()
        plaintext = self.plaintext_input.toPlainText()
        if key and plaintext:
            ciphertext = self.cipher.encrypt(plaintext, key)
            self.ciphertext_output.setPlainText(ciphertext)

    def decrypt_text(self):
        key = self.key_input.text()
        ciphertext = self.ciphertext_output.toPlainText()
        if key and ciphertext:
            plaintext = self.cipher.decrypt(ciphertext, key)
            self.plaintext_input.setPlainText(plaintext)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = VigenereCipherApp()
    ex.show()
    sys.exit(app.exec_())
