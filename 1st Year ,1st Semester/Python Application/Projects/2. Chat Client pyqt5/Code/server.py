import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QSplitter, QVBoxLayout, QDialog, QLineEdit, QPushButton, QApplication, QTextEdit, QLabel)
import socket
from threading import Thread, Event
import time
import os

conn = None
server_event = Event()


class NameDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Enter Your Name")
        self.resize(300, 100)

        self.layout = QVBoxLayout()

        self.name_label = QLabel("Enter your name:")
        self.layout.addWidget(self.name_label)

        self.name_field = QLineEdit()
        self.layout.addWidget(self.name_field)

        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_name)
        self.layout.addWidget(self.submit_button)

        self.setLayout(self.layout)

        self.name = ""

    def submit_name(self):
        self.name = self.name_field.text()
        self.accept()


class Window(QDialog):
    def __init__(self, name):
        super().__init__()
        self.flag = 0

        self.setWindowTitle("Abid Chat Application-Server")
        self.resize(500, 500)

        self.name = name

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)

        # Set the background color of the dialog
        self.setStyleSheet("background-color: #f0e6fa;")  # Light purple color

        # Get the directory of the current script file
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Construct the path to the logo file relative to the current directory
        logo_path = os.path.join(current_dir, 'logo.jpg')

        # Set the window icon using the constructed path
        self.setWindowIcon(QtGui.QIcon(logo_path))

        self.chat = QTextEdit()
        self.chat.setReadOnly(True)
        self.chat.setStyleSheet("color: green; background-color: white; border: 2px solid #ddd; border-radius: 10px; padding: 8px; font-size: 22px;")

        self.chatTextField = QLineEdit()
        self.chatTextField.setPlaceholderText("Type here")
        self.chatTextField.setStyleSheet("color: black; background-color: white; border: 2px solid #ddd; border-radius: 10px; padding: 8px; font-size: 22px;")  # Set text color, background, and font size


        self.btnSend = QPushButton("Send", self)
        self.btnSend.setStyleSheet("background-color: #0084ff; color: white; border: none; border-radius: 10px; padding: 10px 20px;font-size: 16px;")  # Blue color for send button
        self.btnSend.clicked.connect(self.send)

        self.btnExit = QPushButton("Exit", self)
        self.btnExit.setStyleSheet("background-color: #FF5733; color: white; border: none; border-radius: 10px; padding: 10px 20px;font-size: 16px;")
        self.btnExit.clicked.connect(self.exit_application)

        self.btnClear = QPushButton("Clear", self)
        self.btnClear.setStyleSheet("background-color: #4CAF50; color: white; border: none; border-radius: 10px; padding: 10px 20px;font-size: 16px;")  # Green color for the clear button
        self.btnClear.clicked.connect(self.clear_messages)

        splitter = QSplitter(QtCore.Qt.Vertical)
        splitter.addWidget(self.chat)
        splitter.addWidget(self.chatTextField)
        splitter.setSizes([400, 100])

        splitter2 = QSplitter(QtCore.Qt.Vertical)
        splitter2.addWidget(splitter)
        splitter2.addWidget(self.btnSend)
        splitter2.addWidget(self.btnExit)
        splitter2.addWidget(self.btnClear)
        splitter2.setSizes([200, 10, 10, 10])

        layout.addWidget(splitter2)


    def send(self):
        text = self.chatTextField.text()
        timestamp = time.strftime('%H:%M')
        text_formatted = f'<font color="gray">[{timestamp}]</font> <b>{self.name}:</b> {text}'
        self.chat.append(text_formatted)
        global conn
        conn.send(f"[{timestamp}] {self.name}: {text}".encode())
        self.chatTextField.setText("")

    def clear_messages(self):
        self.chat.clear()

    def exit_application(self):
        global server_event
        server_event.set()
        global conn
        if conn:
            conn.close()
        sys.exit()


class ServerThread(Thread):
    def __init__(self, window):
        Thread.__init__(self)
        self.window = window

    def run(self):
        TCP_IP = '0.0.0.0'
        TCP_PORT = 80
        BUFFER_SIZE = 20
        tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        tcpServer.bind((TCP_IP, TCP_PORT))
        threads = []

        tcpServer.listen(4)
        tcpServer.settimeout(0.1)
        while not server_event.is_set():
            print("Multithreaded Python server : Waiting for connections from TCP clients...")
            global conn
            try:
                (conn, (ip, port)) = tcpServer.accept()
            except socket.timeout:
                continue
            newthread = ClientThread(ip, port, window)
            newthread.start()
            threads.append(newthread)

        for t in threads:
            t.join()

        tcpServer.close()


class ClientThread(Thread):

    def __init__(self, ip, port, window):
        Thread.__init__(self)
        self.window = window
        self.ip = ip
        self.port = port
        print("[+] New server socket thread started for " + ip + ":" + str(port))

    def run(self):
        while True:
            global conn
            data = conn.recv(2048)
            window.chat.append('<font color="blue">{}</font>'.format(data.decode("utf-8")))  # Received messages are displayed in blue
            print(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    name_dialog = NameDialog()
    if name_dialog.exec_() == QDialog.Accepted:
        name = name_dialog.name
        window = Window(name)
        serverThread = ServerThread(window)
        serverThread.start()
        window.show()

        sys.exit(app.exec_())
