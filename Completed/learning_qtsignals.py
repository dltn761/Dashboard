from PySide6.QtWidgets import QApplication, QSlider
from PySide6.QtCore import Qt

def respond_to_slider(data):
    print("Slider moved to: ", data)

app = QApplication()
slider = QSlider(Qt.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(25)

slider.valueChanged.connect(respond_to_slider)

slider.show()
app.exec()