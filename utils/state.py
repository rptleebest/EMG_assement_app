import streamlit as st


def init_app_state():
    defaults = {
        "current_screen": "home",
        "app_mode": None,
        "confirmed_case": None,
        "last_result": None,
        "age": 50,
        "sex": "미선택",
        "side": "미선택",
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def clear_result():
    st.session_state["last_result"] = None


def reset_all_inputs():
    keep_keys = {
        "current_screen",
        "app_mode",
        "confirmed_case",
        "age",
        "sex",
        "side",
    }

    removable_keys = [k for k in list(st.session_state.keys()) if k not in keep_keys]
    for key in removable_keys:
        del st.session_state[key]

    st.session_state["last_result"] = None