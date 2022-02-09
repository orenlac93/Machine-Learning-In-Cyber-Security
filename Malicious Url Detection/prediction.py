import pickle
import preprocessing

# get URL from user input
url = [input("Enter your URL: ")]

# read the URL Classification model
with open('models/url_model.pkl', 'rb') as f:
    clf = pickle.load(f)

# load the model prediction for the given URL (the URL is preprocessed)
New_predict_load = clf.predict(preprocessing.preProcess(url))

print('This URL is:')
print(New_predict_load)
