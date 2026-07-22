# use this module to interact with loan_approval_predictor model
import numpy as np
import pickle
import json

# global variables
threshold = 0.4
feature_list = ("age", "gender", "education", "income", "emp_exp", "home_ownership", "loan_amount", "loan_intent", "interest_rate", "loan_percent_income", "credit_history_length", "credit_score", "prev_loan_defaults")
with open('loan_approval_model/category_codes.json', 'rb') as file:
    category_codes = json.load(file)

# load model
with open('loan_approval_model/loan_approval_predictor.pkl', 'rb') as file:
    model = pickle.load(file)

# function to encode features to modle understandable format
def to_num(features):
    input_arr = np.empty(13, dtype=np.float64)

    for feature in features:
        if feature in category_codes:
            value = category_codes[feature].index(features[feature])
        else:
            value = features[feature]
        
        input_arr[feature_list.index(feature)] = value

    return input_arr[np.newaxis, :]


# fuction to get predicted probabilites for each class
def custom_pridict_proba(features):
    # return dummy value
    input_arr = to_num(features)
    return model.predict_proba(input_arr)[0]


# function to get predicted class
def custom_predict(features):
    class_proba = custom_pridict_proba(features)
    
    if class_proba[1] >= threshold:
        return 1
    return 0


# function to get features contributing to loan rejection
def get_contri_features():
    pass
