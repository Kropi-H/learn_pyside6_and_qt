# Version 1:
"""
from PySide6.QtWidgets import QApplication, QPushButton, QMainWindow

# The sys module is responsible for processing command line arguments
import sys

def button_clicked():
  print("You clicked the button, did't you!") 

# We need only one QAplicaton instance per location
# We can ommit sys.argv and use only QApplication ([])
app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Our first MainWindow App")

button = QPushButton()
button.setText("Press Me!")

button.clicked.connect(button_clicked)

window.setCentralWidget(button)
window.show()

# Start the event loop (run the program)
app.exec()

# Loops stopped
"""

# Version 2:
"""
from PySide6.QtWidgets import QApplication, QPushButton, QMainWindow

# The sys module is responsible for processing command line arguments
import sys

def button_clicked(data):
  print("You clicked the button, did't you!", data) 

# We need only one QAplicaton instance per location
# We can ommit sys.argv and use only QApplication ([])
app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Our first MainWindow App")

button = QPushButton()
button.setText(f"Press Me!")
button.setCheckable(True)

button.clicked.connect(button_clicked)

window.setCentralWidget(button)
window.show()

# Start the event loop (run the program)
app.exec()

# Loops stopped
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QSlider

# The sys module is responsible for processing command line arguments
import sys

def respond_to_slider(data):
  print("Slider move to: ", data)

app = QApplication()
slider = QSlider(Qt.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(25)


slider.valueChanged.connect(respond_to_slider)
slider.show()

app.exec()