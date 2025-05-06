# Ver.1: Spagetti coding
"""
from PySide6.QtWidgets import QApplication, QPushButton, QMainWindow

# The sys module is responsible for processing command line arguments
import sys

# We need only one QAplicaton instance per location
# We can ommit sys.argv and use only QApplication ([])
app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Our first MainWindow App")

button = QPushButton()
button.setText("Press Me!")

window.setCentralWidget(button)
window.show()

# Start the event loop (run the program)
app.exec()

# Loops stopped
"""

# Ver.2: Setting up a separeate class
"""
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class ButtonHolder(QMainWindow):
  def __init__ (self):
    super().__init__()
    self.setWindowTitle("Button Holder App")
    button = QPushButton("Press Me!")

    # Set up the button as our central widget
    self.setCentralWidget(button)

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Our first MainWindow App")

window = ButtonHolder()

window.show()
app.exec()
"""

import sys
from PySide6.QtWidgets import QApplication
from button_holder import ButtonHolder

app = QApplication(sys.argv)


window = ButtonHolder()

window.show()
app.exec()