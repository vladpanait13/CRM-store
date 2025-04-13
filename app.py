import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QLabel, QVBoxLayout, QWidget, QLineEdit, QComboBox, QMessageBox, QHBoxLayout, QSpinBox)
from PyQt6.QtCore import Qt

# Simple database in memory
supermarket_data = []

class SuperMarketApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Supermarket")
        self.setGeometry(100, 100, 1000, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.create_form()
        self.create_table()
        self.load_data()

    def create_form(self):
        form_layout = QHBoxLayout()

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Product Name")
        self.category_input = QComboBox()
        self.category_input.addItems(["Fruits", "Vegetables", "Meat", "Drinks", "Sweets"])
        self.price_input = QLineEdit()
        self.price_input.setPlaceholderText("Price")
        self.stock_input = QSpinBox()
        self.stock_input.setRange(0, 1000)

        self.add_button = QPushButton("Add Product")
        self.add_button.clicked.connect(self.add_product)

        form_layout.addWidget(self.name_input)
        form_layout.addWidget(self.category_input)
        form_layout.addWidget(self.price_input)
        form_layout.addWidget(QLabel("Stock:"))
        form_layout.addWidget(self.stock_input)
        form_layout.addWidget(self.add_button)

        self.layout.addLayout(form_layout)

    def create_table(self):
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Name", "Category", "Price", "Stock", "Action"])
        self.layout.addWidget(self.table)

    def load_data(self):
        self.table.setRowCount(0)
        for row_idx, item in enumerate(supermarket_data):
            self.table.insertRow(row_idx)
            self.table.setItem(row_idx, 0, QTableWidgetItem(item["name"]))
            self.table.setItem(row_idx, 1, QTableWidgetItem(item["category"]))
            self.table.setItem(row_idx, 2, QTableWidgetItem(f"{item["price"]:.2f} EUR"))
            self.table.setItem(row_idx, 3, QTableWidgetItem(str(item["stock"])))

            delete_button = QPushButton("Delete")
            delete_button.clicked.connect(lambda checked, idx=row_idx: self.delete_product(idx))
            self.table.setCellWidget(row_idx, 4, delete_button)

    def add_product(self):
        name = self.name_input.text()
        category = self.category_input.currentText()
        try:
            price = float(self.price_input.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "Price has to be a number")
            return

        stock = self.stock_input.value()

        if name.strip() == "":
            QMessageBox.warning(self, "Error", "Name is mandatory")
            return

        supermarket_data.append({
            "name": name,
            "category": category,
            "price": price,
            "stock": stock
        })

        self.name_input.clear()
        self.price_input.clear()
        self.stock_input.setValue(0)
        self.load_data()

    def delete_product(self, index):
        del supermarket_data[index]
        self.load_data()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SuperMarketApp()
    window.show()
    sys.exit(app.exec())


        


