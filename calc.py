"""Calc is a simple calculator app."""

import sys

# Import QApplication and the required widgets from PyQt5.QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget

__version__ = '0.1'

# Create a subclass of QMainWindow to setup the calculator's GUI


class CalcUi(QMainWindow):
    """Calc's GUI."""

    def __init__(self):
        """View initializer."""
        super().__init__()
        # Set some main window's properties
        self.setWindowTitle('Calc')
        self.setFixedSize(235, 235)
        # Set the central widget
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)

# Client code


def main():
    """Main function."""
    # Create an instance of QApplication
    calc = QApplication(sys.argv)
    # Show the calculator's GUI
    view = CalcUi()
    view.show()
    # Execute the calculator's main loop
    sys.exit(calc.exec_())


if __name__ == '__main__':
    main()
