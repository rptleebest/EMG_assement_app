import streamlit as st
from utils.state import clear_result


def render_navigation_controls(position="top"):
    current_screen = st.session_state.get("current_screen", "home")
    if current_screen == "home":
        return

    c1, c2 = st.columns(2)

    with c1:
        if st.button("🏠 처음으로", key=f"home_btn_{position}", use_container_width=True):
            st.session_state["current_screen"] = "home"
            st.session_state["confirmed_case"] = None
            clear_result()
            st.rerun()

    with c2:
        if st.button("⬅️ 이전으로", key=f"back_btn_{position}", use_container_width=True):
            if current_screen == "case_detail":
                st.session_state["current_screen"] = "mode"
                st.session_state["confirmed_case"] = None
            elif current_screen == "direct_input":
                st.session_state["current_screen"] = "mode"
            elif current_screen == "mode":
                st.session_state["current_screen"] = "home"
            clear_result()
            st.rerun()

    st.markdown("<hr/>", unsafe_allow_html=True)