import streamlit as st
import traceback
from datetime import datetime

# 1. 화면 기본 세팅 (반드시 최상단에 위치)
st.set_page_config(
    page_title="교육용 근전도 판독 보조 앱",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

try:
    # 2. 기능별 모듈 불러오기 (Import)
    from core.analyzer import analyze_case
    from core.report import make_report_text
    from ui.styles import apply_global_styles
    from ui.navigation import render_navigation_controls
    from ui.home import render_home_screen
    from ui.case_view import render_case_selector_only, render_case_learning_info
    from ui.direct_input import (
        render_direct_entry_start,
        render_input_sections_for_side,
        render_section_selector,
    )
    from ui.result_view import render_result_view
    from utils.state import init_app_state, reset_all_inputs

    def main():
        # 기본 스타일 및 상태 초기화
        apply_global_styles()
        init_app_state()

        current_screen = st.session_state.get("current_screen", "home")

        if current_screen == "home":
            render_home_screen()
            return

        render_navigation_controls(position="top")

        # ---------------- 화면 분기 (라우팅) ----------------

        if current_screen == "mode":
            # (제목은 각 컴포넌트 내부에서 모바일에 맞게 렌더링됨)
            if st.session_state.get("app_mode") == "사례 학습":
                render_case_selector_only()
            else:
                render_direct_entry_start()

        elif current_screen == "case_detail":
            # 사례 학습 화면의 공통 상단 서브타이틀
            st.markdown(
                """
                <div style="margin-bottom: 0.5rem; padding-top: 0.5rem;">
                    <div style="font-size: 0.95rem; font-weight: 700; color: #64748b; letter-spacing: -0.5px;">
                        🧠 교육용 근전도 판독 보조 앱
                    </div>
                </div>
                """, 
                unsafe_allow_html=True
            )
            confirmed_case = st.session_state.get("confirmed_case")
            if confirmed_case:
                render_case_learning_info(confirmed_case)
            else:
                st.warning("선택된 사례가 없습니다.")

        elif current_screen == "direct_input":
            # 1. 메인 제목 (계층화 및 여백 최적화)
            st.markdown(
                """
                <div style="margin-bottom: 1.5rem; padding-top: 0.5rem;">
                    <div style="font-size: 0.95rem; font-weight: 700; color: #64748b; margin-bottom: 0.2rem; letter-spacing: -0.5px;">
                        🧠 교육용 근전도 판독 보조 앱
                    </div>
                    <div style="font-size: 1.65rem; font-weight: 900; color: #1e3a8a; letter-spacing: -1px; line-height: 1.3;">
                        ⚙️ 검사 항목 직접 구성
                    </div>
                </div>
                """, 
                unsafe_allow_html=True
            )

            age = st.session_state.get("age", 50)
            sex = st.session_state.get("sex", "미선택")
            side = st.session_state.get("side", "미선택")

            # 🚨 필수 정보 누락 시 차단 및 경고 로직
            if sex == "미선택" or side == "미선택":
                st.error("🚨 필수 입력 항목 누락")
                st.warning("성별과 병변측을 정확히 선택해야 기준에 맞는 좌/우측 검사 화면이 생성됩니다. 아래 버튼을 눌러 이전 화면에서 선택을 완료해 주세요.")
                if st.button("⬅️ 프로필 입력 화면으로 돌아가기", type="primary", use_container_width=True):
                    st.session_state["current_screen"] = "mode"
                    st.rerun()
            else:
                # 2. 입력 프로필 (답답한 박스를 없애고 깔끔한 뱃지 형태로 변경)
                st.markdown(
                    f"""
                    <div style="background-color: #f1f5f9; padding: 12px; border-radius: 8px; margin-bottom: 1.5rem; color: #334155; font-size: 1rem; font-weight: 600; display: flex; flex-wrap: wrap; gap: 10px; border-left: 4px solid #3b82f6;">
                        <span>👤 {age}세</span>
                        <span>| ⚧️ {sex}</span>
                        <span>| 🎯 병변측: <span style="color:#b91c1c;">{side}</span></span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                # 3. 정상적으로 입력되었을 때만 검사 세트 선택창 렌더링
                selected_sections = render_section_selector()
                rows = render_input_sections_for_side(side, selected_sections)

                # 분석 및 초기화 버튼 영역
                c1, c2 = st.columns(2)
                with c1:
                    if st.button("🚀 분석 실행", type="primary", use_container_width=True):
                        st.session_state["last_result"] = analyze_case(age, sex, side, rows)
                        st.rerun()

                with c2:
                    if st.button("🔄 입력 초기화", use_container_width=True):
                        reset_all_inputs()
                        st.rerun()

                # 결과 출력
                if st.session_state.get("last_result"):
                    result = st.session_state["last_result"]
                    render_result_view(result)

                    st.download_button(
                        label="📝 텍스트 보고서 다운로드",
                        data=make_report_text(result).encode("utf-8"),
                        file_name=f"EMG_Analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                        mime="text/plain",
                        use_container_width=True
                    )

        render_navigation_controls(position="bottom")

    if __name__ == "__main__":
        main()

except Exception as e:
    st.error("🚨 앱 초기화 중 일부 파일이 누락되었습니다.")
    st.code(traceback.format_exc(), language="python")
