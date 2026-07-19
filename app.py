# this module contains streamlit code for app interface
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
        .st-key-Pill2 label[data-testid="stWidgetLabel"] p {
            font-size: 22px !important;
            font-weight: bold !important;
        }
    </style>
    ''',
    unsafe_allow_html=True
)


# initialize session state counter
if "step" not in st.session_state:
    st.session_state.step = 0

# defint callback funtion
def next_step():
    st.session_state.step += 1

def prev_step():
    st.session_state.step -= 1


# diplay header
st.title(":bank: Loan Approval Prediction App")

# render ui conditionally based on current session state
if st.session_state.step == 0:
    # display discription
    st.write("Welcome to your personal guide for the loan application process. This tool evaluates your financial profile to help you understand your chances of securing a bank loan before you officially apply.")
    st.write("**What This Tool Does:**")
    st.write("- **Instant Assessment:** Receive an immediate prediction on whether your loan application is likely to be approved or rejected.")
    st.write("- **Actionable Feedback:** If your application is flagged for potential rejection, the system will provide the specific reasons why.")
    st.write("**How to Use:**")
    st.write("Simply fill in your application details and click Predict. The system will process your information to deliver a transparent, data-driven result. Then click Get Reasons.")

    st.button("Start", type="primary", on_click=next_step)

elif st.session_state.step == 1:
    pass

elif st.session_state.step == 2:
    pass

elif st.session_state.step == 3:
    pass

elif st.session_state.step == 4:
    pass

elif st.session_state.step == 5:
    pass

elif st.session_state.step == 6:
    pass

elif st.session_state.step == 7:
    pass

elif st.session_state.step == 8:
    pass

elif st.session_state.step == 9:
    pass

elif st.session_state.step == 10:
    pass

elif st.session_state.step == 11:
    pass

elif st.session_state.step == 12:
    pass

elif st.session_state.step == 13:
    pass

elif st.session_state.step == 14:
    pass
