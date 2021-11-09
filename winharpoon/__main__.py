from PySide6.QtGui import *
from PySide6.QtWidgets import *

if __name__ == "__main__":
    app = QApplication([])
    app.setQuitOnLastWindowClosed(False)
      
    # Adding an icon
    icon = QIcon("assets/harpoon16x16.png")
      
    # Adding item on the menu bar
    tray = QSystemTrayIcon()
    tray.setIcon(icon)
    tray.setVisible(True)
      
    # Creating the options
    menu = QMenu()
      
    # To quit the app
    quit = QAction("Quit")
    quit.triggered.connect(app.quit)
    menu.addAction(quit)
      
    # Adding options to the System Tray
    tray.setContextMenu(menu)
      
    app.exec()
