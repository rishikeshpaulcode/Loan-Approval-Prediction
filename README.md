# Loan Approval Prediction App

A data-driven application that predicts whether a loan application will be approved or rejected and explains the main reasons behind a potential rejection.

## Overview

This project helps loan applicants understand their approval likelihood before submitting an application. It provides:

- **Instant assessment** of approval vs rejection.
- **Actionable feedback** for rejected applications.
- **Interactive input flow** for applicant details.
- **Model-based explanations** for rejection reasons using feature contributions.

## Features

- Input applicant details through a guided Streamlit interface.
- Predict loan approval probability using a pre-trained model.
- Display a probability chart and approval/rejection verdict.
- Provide rejection reasons ranked by model contribution.
- Support loan amount updates to compare outcomes.

## Links
- Kaggle notebook: https://www.kaggle.com/code/rishikeshpaul/loan-approval-prediction
- Streamlit app: https://rishi-loan-approval-predictor.streamlit.app

## Project Structure

- `app.py` — Streamlit application with multi-step input flow and prediction logic.
- `loan_approval_model/model_interface.py` — model integration, encoding, prediction, and contribution explanation.
- `loan_approval_model/category_codes.json` — categorical encoding reference for model input.
- `loan_approval_model/approved_feature_means.json` — approved-case feature means used to label numerical rejection reasons.
- `loan_approval_model/loan_approval_predictor.pkl` — serialized trained model used for prediction.
- `requirements.txt` — required Python dependencies.
- `loan-approval-prediction-notebook.ipynb` — exploratory notebook for analysis and model development.
- `test_data.txt` — sample test input data for validating the prediction flow.

## Installation

1. Create a Python environment (recommended):

```bash
python -m venv .venv
```

2. Activate the environment:

Windows PowerShell:
```powershell
.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the App

Start the application with Streamlit:

```bash
streamlit run app.py
```

Then open the provided local URL in your browser.

## How to Use

1. Click **Start** to begin the guided input flow.
2. Enter applicant details such as age, gender, education, income, work experience, home ownership, loan amount, interest rate, loan intent, credit history length, and credit score.
3. Click **Predict** after the final input step.
4. View the approval/rejection probability and verdict.
5. If the model predicts rejection, review the ranked reasons for rejection.
6. Adjust the loan amount and use **Update** to see how changes affect the outcome.

## Prediction Logic

The app uses the loan approval model to generate:

- `custom_pridict_proba` — class probability scores for approval and rejection.
- `custom_predict` — approval or rejection verdict with a rejection threshold.
- `get_contri_features` — SHAP-based explanation of why the model favors rejection.

Rejection reasons are derived from features with positive contribution toward rejection, and numerical values are compared against approved-case means.

## Dependencies

Key dependencies include:

- `streamlit`
- `numpy`
- `scikit-learn`
- `shap`
- `plotly`

## Notes

- This application is intended for educational and informational use.
- The prediction is based on a statistical model and may not reflect final bank decisions.
- Ensure the `loan_approval_model/loan_approval_predictor.pkl` model file is available before running the app.

## License

This project is licensed under the terms of the included `LICENSE` file.
