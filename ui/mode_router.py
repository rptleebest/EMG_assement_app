import streamlit as st

from data.constants import MODE_CASE, MODE_ABNORMAL_CHECK, MODE_DIRECT
from ui.case_learning import render_case_learning
from ui.abnormal_check_input import render_abnormal_check_learning


def _render_direct_input_safely():
    try:
        from ui.direct_input import render_direct_entry_start, render_section_selector, render_input_sections_for_side

        if st.session_state.get("current_screen") != "direct_input":
            render_direct_entry_start()
            return

        st.markdown(
            """
            <div style="margin-bottom:1rem;">
                <div style="font-size:1.35rem; font-weight:900; color:#1e3a8a; word-break:keep-all;">
                    수치 직접 입력 학습
                </div>
                <div style="font-size:0.95rem; color:#475569; margin-top:0.4rem; line-height:1.5; word-break:keep-all;">
                    진폭, 잠복기, 전도속도 등 세부 수치를 직접 입력하는 심화 학습 모드입니다.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        side = st.session_state.get("side", "미선택")
        selected_sections = render_section_selector()
        rows = render_input_sections_for_side(side, selected_sections)

        if rows:
            st.success(f"입력된 검사 항목: {len(rows)}개")
            with st.expander("입력 요약 보기", expanded=False):
                for row in rows:
                    st.markdown(f"- **{row.get('item', '')}**: 좌측 `{row.get('left', '')}`, 우측 `{row.get('right', '')}`")

        st.caption("수치 직접 입력 결과의 자동 해석은 검사실 기준에 따라 달라질 수 있으므로 교육용으로만 사용하세요.")

    except Exception as exc:
        st.error("수치 직접 입력 학습 화면을 불러오는 중 문제가 발생했습니다.")
        st.caption(f"오류 내용: {exc}")
        st.info("기존 `ui/direct_input.py` 파일의 함수 이름과 구조를 확인해 주세요.")


def render_mode_selection_screen():
    selected_mode = st.session_state.get("app_mode")

    st.markdown(
        """
        <div style="margin-bottom:1rem;">
            <div style="font-size:1.35rem; font-weight:900; color:#1e3a8a; word-break:keep-all;">
                학습 모드
            </div>
            <div style="font-size:0.95rem; color:#475569; margin-top:0.4rem; line-height:1.5; word-break:keep-all;">
                선택한 학습 모드로 이동합니다.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if not selected_mode:
        st.warning("학습 모드가 선택되지 않았습니다. 처음 화면으로 돌아가 모드를 선택해 주세요.")
        return

    st.info(f"선택한 모드: {selected_mode}")

    if selected_mode == MODE_CASE:
        if st.button("사례 학습 시작", type="primary", use_container_width=True):
            st.session_state["current_screen"] = "case_learning"
            st.rerun()

    elif selected_mode == MODE_ABNORMAL_CHECK:
        if st.button("이상 소견 체크 학습 시작", type="primary", use_container_width=True):
            st.session_state["current_screen"] = "abnormal_check"
            st.rerun()

    elif selected_mode == MODE_DIRECT:
        if st.button("수치 직접 입력 학습 시작", type="primary", use_container_width=True):
            st.session_state["current_screen"] = "direct_input_start"
            st.rerun()

    else:
        st.error("알 수 없는 학습 모드입니다.")


def render_mode_router():
    current_screen = st.session_state.get("current_screen", "home")

    if current_screen == "mode":
        render_mode_selection_screen()

    elif current_screen == "case_learning":
        render_case_learning()

    elif current_screen == "case_detail":
        render_case_learning()

    elif current_screen == "abnormal_check":
        render_abnormal_check_learning()

    elif current_screen in ["direct_input_start", "direct_input"]:
        _render_direct_input_safely()

    else:
        st.warning("알 수 없는 화면입니다. 처음 화면으로 돌아가 주세요.")
