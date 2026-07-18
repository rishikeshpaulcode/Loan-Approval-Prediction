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


if __name__ == "__main__":
    pass
