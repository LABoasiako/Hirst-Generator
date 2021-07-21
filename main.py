from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QGraphicsDropShadowEffect, QDesktopWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys
from hirst_generator import color_extractor, color_palette, hirst_drawing_creation
import os
import icon_rc

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()   # Call the inherited classes __init__ method
        uic.loadUi('hist.ui', self)  # Load the .ui file
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # Remove PyQT MainWindow background
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(1)
        self.CentralWidget.setGraphicsEffect(self.shadow)
        # self.center()
        self.show()  # Show the GUI

        # Buttons
        self.hirst_button.clicked.connect(self.buttonPress)  # Run button press function when button is clicked



    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:   # Returns True if object is an image file
            event.accept()              # Accept event if it cant return an image
        else:
            event.ignore()              # Reject event if it cannot return an image

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:  # Returns True if object can return an image
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage:  # Returns True if object is an image file
            event.setDropAction(Qt.CopyAction)   # Accept Drop Action
            self.file_path = event.mimeData().urls()[0].toLocalFile()  # Grab first image in file path
            self.set_image(self.file_path)  # Use filepath in set_image function
            event.accept()
        else:
            event.ignore()

    def set_image(self):  # Set image function
        if self.height() > 400:  # check if height of image is greater than 400
            old_height = self.height()
            old_width = self.width()
            height = 400
            width = int((old_width * 400) / old_height)
        imageOne = QPixmap(self.file_path).scaled(width, height)
        # print(width, height)
        self.image_viewer.setPixmap(imageOne)  # Set file_path to image_label

    def buttonPress(self):
        if self.hirst_radio_button.isChecked():   # Check if the hirst radio button is checked
            try:
                if self.file_path:
                    rgb_colors = color_extractor(image=self.file_path, num=60)
                    hirst_drawing_creation(rgb_colors)
            except:
                print("No Image Selected")

        elif self.color_radio_button.isChecked():  # Check if the color palette radio button is checked
            try:
                if self.file_path:
                    rgb_colors = color_extractor(image=self.file_path, num=8)
                    color_palette(rgb_colors)
            except:
                print("No Image Selected")

    def createImage(self):
        pass


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
