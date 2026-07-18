# use this module to interact with loan_approval_predictor model
import numpy as np
import pickle
import json

# load category codes map
with open('category_codes.json', 'r') as file:
    category_codes = json.loads(file)

# load model
with open('loan_approval_predictor.pkl', 'rb') as file:
    model = pickle.load(file)

# function to encode features to modle understandable format
def to_num(features):
    # return dummy value
    return list(range(13))


# fuction to get predicted probabilites for each class
def custom_pridict_proba(features):
    # return dummy value
    return [0.8, 0.2]


# function to get predicted class
def custom_predict(features):
    # return dummy value
    return 0


# function to get features contributing to loan rejection
def get_contri_features():
    pass
