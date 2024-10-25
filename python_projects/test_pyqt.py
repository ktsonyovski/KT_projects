import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('PyQt5 Test')
window.setGeometry(100, 100, 280, 80)
window.show()
sys.exit(app.exec_())
