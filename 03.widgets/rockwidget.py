from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout

class RockWidget(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Rock Widget")
    button1 = QPushButton("Button One")
    button1.clicked.connect(self.button_one_clicked)
    button2 = QPushButton("Button Two")
    button2.clicked.connect(self.button_two_clicked)

    h_button_layout = QHBoxLayout()
    h_button_layout.addWidget(button1)
    h_button_layout.addWidget(button2)

    v_button_layout = QVBoxLayout()
    v_button_layout.addWidget(button1)
    v_button_layout.addWidget(button2)


    self.setLayout(v_button_layout)

  def button_one_clicked(self):
    print("Button One is clicked")

  def button_two_clicked(self):
    print("Button Two is clicked")