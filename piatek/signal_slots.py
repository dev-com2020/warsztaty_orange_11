import sys
from functools import partial
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


def greet(name):
    if msgLabel.text():
        msgLabel.setText("")
    else:
        msgLabel.setText(f'Witaj {name}!')


app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
button = QPushButton("powitanie")
button.clicked.connect(partial(greet, "w programie!"))
layout.addWidget(button)
msgLabel = QLabel("")
layout.addWidget(msgLabel)
window.setLayout(layout)
window.show()
sys.exit(app.exec())
