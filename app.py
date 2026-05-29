import streamlit as st

from ui.home import render_home_screen
from ui.navigation import render_navigation_controls
from ui.mode_router import render_mode_router
from utils.state import init_session_state


def main():
    st.set_page_config(
        page_title="교육용 근전도 학습 앱",
        page_icon="🧠",
        layout="centered",
        initial_sidebar_state="collapsed",
    )

    init_session_state()

    st.markdown(
        """
        <style>
        .block-container {
            padding-top: 1.2rem;
            padding-bottom: 2rem;
            max-width: 760px;
        }

        div[data-testid="stRadio"] > label {
            font-weight: 800;
            color: #0f172a;
        }

        div[data-testid="stExpander"] {
            border-radius: 12px;
        }

        .stButton > button {
            border-radius: 10px;
            font-weight: 800;
            min-height: 2.7rem;
        }

        .stSelectbox label,
        .stMultiSelect label,
        .stNumberInput label,
        .stTextInput label {
            font-weight: 700;
            color: #0f172a;
        }

        @media (max-width: 640px) {
            .block-container {
                padding-left: 0.8rem;
                padding-right: 0.8rem;
                padding-top: 0.8rem;
            }

            h1, h2, h3 {
                word-break: keep-all;
            }

            .stButton > button {
                width: 100%;
                min-height: 2.8rem;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    current_screen = st.session_state.get("current_screen", "home")

    if current_screen == "home":
        render_home_screen()
    else:
        render_navigation_controls(position="top")
        render_mode_router()
        render_navigation_controls(position="bottom")


if __name__ == "__main__":
    main()
