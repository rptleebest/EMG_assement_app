import streamlit as st

from utils.state import clear_result, clear_case_state, clear_abnormal_check_state, reset_to_home


def render_navigation_controls(position="top"):
    current_screen = st.session_state.get("current_screen", "home")

    if current_screen == "home":
        return

    c1, c2 = st.columns(2)

    with c1:
        if st.button("처음으로", key=f"home_btn_{position}", use_container_width=True):
            reset_to_home()
            st.rerun()

    with c2:
        if st.button("이전으로", key=f"back_btn_{position}", use_container_width=True):
            if current_screen in ["case_learning", "abnormal_check", "direct_input"]:
                st.session_state["current_screen"] = "mode"
                clear_result()

            elif current_screen == "case_detail":
                st.session_state["current_screen"] = "case_learning"
                clear_case_state()
                clear_result()

            elif current_screen == "mode":
                st.session_state["current_screen"] = "home"
                clear_result()
                clear_case_state()
                clear_abnormal_check_state()

            else:
                st.session_state["current_screen"] = "mode"
                clear_result()

            st.rerun()

    st.markdown("<hr/>", unsafe_allow_html=True)
