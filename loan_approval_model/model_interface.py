# use this module to interact with loan_approval_predictor model
import numpy as np
import pickle
import json
import shap

# global variables
threshold = 0.25
feature_list = ("age", "gender", "education", "income", "emp_exp", "home_ownership", "loan_amount", "loan_intent", "interest_rate", "loan_percent_income", "credit_history_length", "credit_score")
numerical_features = ("age", "income", "emp_exp", "loan_amount", "interest_rate", "loan_percent_income", "credit_hist_length", "credit_score")
categorical_features = ("gender", "education", "home_ownership", "loan_intent")

with open("loan_approval_model/category_codes.json", "rb") as file:
    category_codes = json.load(file)

with open("loan_approval_model/approved_feature_means.json", "rb") as file:
    approved_feature_means = json.load(file)

# load model
with open('loan_approval_model/loan_approval_predictor.pkl', 'rb') as file:
    model = pickle.load(file)

# function to encode features to modle understandable format
def to_num(features):
    input_arr = np.empty(12, dtype=np.float64)

    for feature in features:
        if feature in categorical_features:
            value = category_codes[feature].index(features[feature])
        else:
            value = features[feature]
        
        input_arr[feature_list.index(feature)] = value

    return input_arr[np.newaxis, :]


# fuction to get predicted probabilites for each class
def custom_pridict_proba(features):
    input_arr = to_num(features)
    return model.predict_proba(input_arr)[0]


# function to get predicted class
def custom_predict(features):
    class_proba = custom_pridict_proba(features)
    
    if class_proba[1] >= threshold:
        return 1
    return 0


# function to get features contributing to loan rejection
def get_contri_features(features):
    explainer = shap.TreeExplainer(model)
    input_arr = to_num(features)

    shap_values = explainer(input_arr)
    shap_scores = shap_values.values[0, :, 1].reshape(13, 1)
    feature_idx = np.arange(13).reshape(13, 1)
    feature_contri_arr = np.concatenate([feature_idx, shap_scores], axis=1)

    contri_features_raw = feature_contri_arr[feature_contri_arr[:, 1] > 0]
    contri_features_sorted = contri_features_raw[contri_features_raw[: 1].argsort()[::-1]]

    contri_features = []
    for i in range(len(contri_features_sorted)):
        name = feature_list[contri_features_sorted[i, 0].astype(np.int64)]

        if name in numerical_features:
            if features[name] > approved_feature_means[name]:
                reason = "High"
            else:
                reason = "Low"
        else:
            reason = features[name]
        contri_features.append((name, reason))

    return contri_features
