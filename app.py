# this module contains streamlit code for app interface
from loan_approval_model import model_interface as mi
import plotly.express as px
import streamlit as st

# create custom styles
st.markdown(
    '''
    <style>
        div.stButton > button p {
            font-size: 21px !important;
            forn-weight: bold !important;
        }
    </style>
    ''',
    unsafe_allow_html=True
)
st.markdown(
    '''
    <style>
        div[data-testid="stSelectbox"] label[data-testid="stWidgetLabel"] p {
            font-size: 22px !important;
            font-weight: bold !important;
        }
    </style>
    ''',
    unsafe_allow_html=True
)
st.markdown(
    '''
    <style>
        div[data-testid="stNumberInput"] label[data-testid="stWidgetLabel"] p {
            font-size: 22px !important;
            font-weight: bold !important;
        }
    </style>
    ''',
    unsafe_allow_html=True
)
st.markdown(
    '''
    <style>
        .st-key-Pill1 label[data-testid="stWidgetLabel"] p,
        .st-key-Pill2 label[data-testid="stWidgetLabel"] p,
        .st-key-Pill3 label[data-testid="stWidgetLabel"] p,
        .st-key-Pill4 label[data-testid="stWidgetLabel"] p,
        .st-key-Pill5 label[data-testid="stWidgetLabel"] p {
            font-size: 22px !important;
            font-weight: bold !important;
        }
    </style>
    ''',
    unsafe_allow_html=True
)


# initialize session state counter
ss = st.session_state

if "step" not in ss:
    ss.step = 0

if "inputs" not in ss:
    ss.inputs = {}

# define callback funtion
def next_step():
    ss.step += 1

def prev_step():
    ss.step -= 1


# diplay header
st.title(":bank: Loan Approval Prediction App")

# display progress bar (if required)
st.markdown("<div style='margin-top: 50px;'></div>", unsafe_allow_html=True)
if 0 < ss.step < 12:
    st.progress(
        ss.step / 11,
        text=f"Question {st.session_state.step} of 11"
    )
    st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)

# display descripton / question / prediction based on current session state
if ss.step == 0:
    st.write("Welcome to your personal guide for the loan application process. This tool evaluates your financial profile to help you understand your chances of securing a bank loan before you officially apply.")
    st.write("**What This Tool Does:**")
    st.write("- **Instant Assessment:** Receive an immediate prediction on whether your loan application is likely to be approved or rejected.")
    st.write("- **Actionable Feedback:** If your application is flagged for potential rejection, the system will provide the specific reasons why.")
    st.write("**How to Use:**")
    st.write("Simply fill in your application details and click Predict. The system will process your information to deliver a transparent, data-driven result. Then click Get Reasons.")

elif ss.step == 1:
    st.subheader("Enter your age:")
    ss.inputs["age"] = st.number_input(
        label="age",
        min_value=1,
        max_value=100,
        value="min",
        step=1,
        label_visibility="collapsed"
    ) 

elif ss.step == 2:
    st.subheader("Select your gender:")
    ss.inputs["gender"] = st.pills(
        label="gender",
        options=["Female", "Male"],
        selection_mode="single",
        key="pill1",
        label_visibility="collapsed"
    )

elif ss.step == 3:
    st.subheader("Select you Highest Education level:")
    ss.inputs["education"] = st.pills(
        label="education",
        options=["High School", "Associate", "Bachelor", "Master", "Doctorate"],
        selection_mode="single",
        key="pill2",
        label_visibility="collapsed"
    )

elif ss.step == 4:
    st.subheader("Enter you Income per year (in dollars):")
    ss.inputs["income"] = st.number_input(
        label="income",
        min_value=1.00,
        value="min",
        format="%.2f",
        label_visibility="collapsed"
    )

elif ss.step == 5:
    st.subheader("How many years of work experience do you have?")
    ss.inputs["emp_exp"] = st.number_input(
        label="emp_exp",
        min_value=0,
        max_value=60,
        value="min",
        step=1,
        label_visibility="collapsed"
    )

elif ss.step == 6:
    st.subheader("Select your Home Ownership status:")
    ss.inputs["home_ownership"] = st.pills(
        label="home_ownership",
        options=["Other", "Rent", "Mortgage", "Own"],
        selection_mode="single",
        key="pill3",
        label_visibility="collapsed"
    )

elif ss.step == 7:
    st.subheader("Enter required Loan amount (in dollars):")
    ss.inputs["loan_amount"] = st.number_input(
        label="loan_amount",
        value=0.0,
        format="%.2f",
        label_visibility="collapsed"
    )

elif ss.step == 8:
    st.subheader("Enter Interest Rate:")
    ss.inputs["interest_rate"] = st.number_input(
        label="interest_rate",
        min_value=1.0,
        max_value=25.0,
        value="min",
        format="%.2f",
        label_visibility="collapsed"
    )

elif ss.step == 9:
    st.subheader("What is purpose of loan application:")
    ss.inputs["loan_intent"] = st.pills(
        label="loan_intent",
        options=["Debtconsolidation", "Medical", "Home Improvement", "Personal", "Education", "Venture"],
        selection_mode="single",
        key="pill4",
        label_visibility="collapsed"
    )

elif ss.step == 10:
    st.subheader("Enter your credit history length (in years):")
    ss.inputs["credit_history_length"] = st.number_input(
        label="credit_history_length",
        min_value=0,
        max_value=60,
        value="min",
        step=1,
        label_visibility="collapsed"
    )

elif ss.step == 11:
    st.subheader("Enter your Credit Score:")
    ss.inputs["credit_score"] = st.number_input(
        label="credit_score",
        min_value=300,
        max_value=850,
        value="min",
        step=1,
        label_visibility="collapsed"
    )

elif ss.step == 12:
    # check number of features
    if len(ss.inputs) == 11:
        ss.inputs["loan_percent_income"] = ss.inputs["loan_amount"] / ss.inputs["income"]

        # get prediction results
        result_proba = mi.custom_pridict_proba(ss.inputs)
        result_verdict = mi.custom_predict(ss.inputs)
    
        # display predictions
        st.subheader("Predicton Results:")
        st.write("Note: This is a statistical model and can make mistakes.")
        categories = ["Approval", "Rejection"]
        category_colors = {
            "Approval": "#2ca02c",
            "Rejection": "#d62728"
        }
        fig = px.pie(
            values=result_proba,
            names=categories,
            color=categories,
            color_discrete_map=category_colors,
            hole=0.7
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # display rejection reasons
        if result_verdict == 1:
            st.write("Your loan application may get rejected. Click below to get most probable reasons.")
        
            if st.button("Get Reasons", type="primary"):
                st.write("Rejection reasons (sorted in decreasing level of influence):")
                contri_features = mi.get_contri_features(ss.inputs)
        
                i = 1
                for name, reason in contri_features:
                    name_formatted = name.replace("_", " ").title()
        
                    if name in mi.numerical_features_features:
                        st.write(f"{i}. {name_formatted} is too {reason}")
                    else:
                        st.write(f"{i}. {name_formatted} is \'{reason}\'")
                    i += 1
        else:
            st.write("Your loan application will most likely be approved :wink:")
    else:
        st.write("Some of the fields have missing values.")


# display buttons
st.markdown("<div style='margin-top: 80px;'></div>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    if 0 < ss.step < 12:
        st.button("Prev", type="primary", on_click=prev_step)
with col2:
    if ss.step == 0:
        st.button("Start", type="primary", on_click=next_step)
with col3:
    if 0 < ss.step < 11:
        st.button("Next", type="primary", on_click=next_step)
    elif ss.step == 11:
        st.button("Predict", type="primary", on_click=next_step)
