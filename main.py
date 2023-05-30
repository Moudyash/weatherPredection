import sys
import pickle
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox
from datetime import datetime


class MainWindow(QMainWindow):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.setWindowTitle("Date Picker")
        self.setGeometry(300, 300, 300, 200)

        self.date_label = QLabel(self)
        self.date_label.setText("Select a date:")
        self.date_label.move(50, 50)

        self.date_entry = QLineEdit(self)
        self.date_entry.move(150, 50)

        self.predict_button = QPushButton(self)
        self.predict_button.setText("Predict")
        self.predict_button.move(100, 100)
        self.predict_button.clicked.connect(self.predict_date)

    def predict_date(self):
        input_date = self.date_entry.text()

        # Convert the input_date to a datetime object
        datetime_obj = datetime.strptime(input_date, "%d-%m-%Y")

        # Extract the year from the datetime object
        year = datetime_obj.year

        # Convert the year to a 2D array with a single feature
        input_data = [[year]]

        prediction = self.model.predict(input_data)
        QMessageBox.information(self, "Prediction", f"The predicted value is: {prediction}")


def loadModel(fileName):
    try:
        with open(fileName, 'rb') as file:
            model = pickle.load(file)
        print("Model loaded successfully.")
        return model
    except FileNotFoundError:
        print("Model file not found.")
    except Exception as e:
        print("Error while loading the model.", str(e))


# Load the model
model = loadModel(r"E:\programming\python\weatherPredection\DateModel.pkl")
input_date = ["15-01-2016"]

# Convert the input_date to a 2D array with a single feature
input_data = [[int(date.split('-')[0])] for date in input_date]

prediction = model.predict(input_data)
print("Prediction:", prediction)

app = QApplication(sys.argv)
window = MainWindow(model)
window.show()
sys.exit(app.exec_())
