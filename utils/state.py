import streamlit as st


DEFAULT_SESSION_STATE = {
    "current_screen": "home",
    "app_mode": None,
    "confirmed_case": None,
    "selected_case_name": None,
    "result": None,
    "abnormal_region": None,
    "abnormal_side": None,
    "abnormal_symptoms": [],
    "abnormal_selected_codes": [],
}


def init_session_state():
    for key, value in DEFAULT_SESSION_STATE.items():
        if key not in st.session_state:
            st.session_state[key] = value


def clear_result():
    st.session_state["result"] = None


def reset_to_home():
    for key, value in DEFAULT_SESSION_STATE.items():
        st.session_state[key] = value


def clear_abnormal_check_state():
    st.session_state["abnormal_region"] = None
    st.session_state["abnormal_side"] = None
    st.session_state["abnormal_symptoms"] = []
    st.session_state["abnormal_selected_codes"] = []


def clear_case_state():
    st.session_state["confirmed_case"] = None
    st.session_state["selected_case_name"] = None
