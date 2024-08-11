import sys
import os

from PyQt6.QtWidgets import QApplication
from PyQt6 import QtGui
from ui.main_ui import res
from ui.app import MainWindow
from logger_setup import logger

basedir = os.path.dirname(__file__)

try:
    from ctypes import windll  # Only exists on Windows.
    myappid = 'mycompany.myproduct.subproduct.version'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass


def run_app():
    """
        Runs the application.

        This function initiarlizes the application, creates the main window,
        and starts the event loop.

        Raises:
            Exception: If an error occurs during the execution of the application.

    """
    logger.info("ENTER BY PORTAL START YES!")
    try:
        app = QApplication(sys.argv)
        app.setWindowIcon(QtGui.QIcon(os.path.join(basedir, 'procto.icns')))
        window = MainWindow()
        window.show()
        window.resize(300, 330)
        sys.exit(app.exec())
    except Exception as e:
        logger.error(f"Error at portal {e}", exc_info=True)
    

if __name__ == "__main__":
    run_app()
