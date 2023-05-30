import pickle

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


model = loadModel(r"E:\programming\python\weatherPredection\DateModel.pkl")
input_date = ["15-01-2017"]

# Convert the input_date to a 2D array with a single feature
input_data = [[int(date.split('-')[0])] for date in input_date]

prediction = model.predict(input_data)
print("Prediction:", prediction)
