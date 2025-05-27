import sys
from PySide6.QtWidgets import QApplication, QLabel, QPushButton
from PySide6.QtCore import Slot

#slot will be explained later but have it each function
@Slot()
def say_hello():
    print("Clicked! Hello!")

#creates the application
app = QApplication(sys.argv)

#creates a button
button = QPushButton("Click me")

#connecting the button to the say_hello function
button.clicked.connect(say_hello)
#showing the button
button.show()
#run the main QtLoop
app.exec()