import streamlit as st

from data.constants import MODE_CASE, MODE_ABNORMAL_CHECK, MODE_DIRECT
from utils.state import clear_result


def render_home_screen():
    st.markdown(
        """
        <div style="margin-bottom: 1.2rem;">
            <div style="font-size: 1.55rem; font-weight: 900; color: #1e3a8a; line-height: 1.35; word-break: keep-all;">
                교육용 근전도·신경전도검사 학습 앱
            </div>
            <div style="font-size: 0.98rem; color: #475569; margin-top: 0.5rem; line-height: 1.55; word-break: keep-all;">
                물리치료학과 학생과 임상물리치료사를 위한
                <b>전기진단검사 결과 해석 학습 도구</b>입니다.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:12px; padding:14px; margin-bottom:1rem;">
            <div style="font-weight:800; color:#0f172a; margin-bottom:8px;">학습 모드 안내</div>
            <div style="font-size:0.95rem; color:#334155; line-height:1.55; word-break:keep-all;">
                <b>1. 사례 학습</b>: 대표 환자 사례를 통해 증상, 이학적 검사, 근전도 소견을 연결합니다.<br>
                <b>2. 이상 소견 체크 학습</b>: 검사결과표에서 비정상 소견만 체크하고 병변 위치와 질환군을 추론합니다.<br>
                <b>3. 검사결과표 판독 학습</b>: 실제 검사결과표 형식의 예제를 보고 패턴 중심으로 판독을 연습합니다.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.warning(
        "본 앱은 교육용입니다. 실제 진단과 치료 결정은 환자 병력, 진찰, 영상검사, 검사실 기준을 종합하여 전문 의료진이 판단해야 합니다."
    )

    selected_mode = st.radio(
        "학습 모드 선택",
        [MODE_CASE, MODE_ABNORMAL_CHECK, MODE_DIRECT],
        index=0,
    )

    if selected_mode == MODE_CASE:
        st.info("대표 질환 사례를 통해 병변 위치와 감별진단을 학습합니다.")
    elif selected_mode == MODE_ABNORMAL_CHECK:
        st.info("검사결과표에서 이상 소견만 체크하여 자동 추론 결과를 확인합니다.")
    else:
        st.info("대표 검사결과표 예제를 보고 직접 판독한 뒤 정답과 해설을 확인합니다.")

    if st.button("학습 시작", type="primary", use_container_width=True):
        st.session_state["app_mode"] = selected_mode
        st.session_state["current_screen"] = "mode"
        clear_result()
        st.rerun()
