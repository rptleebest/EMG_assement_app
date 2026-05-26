import streamlit as st
from data.constants import MODE_CASE, MODE_DIRECT
from utils.state import clear_result


def render_home_screen():
    st.markdown('<div class="main-title">교육용 근전도 판독 보조 앱</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtle">물리치료학과 학생의 근전도 사례 학습과 기본 해석 훈련을 위한 교육용 앱입니다.</div>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="warn-card">', unsafe_allow_html=True)
    st.markdown("### 📌 학습 안내")
    st.markdown('<div class="case-bullet">• 사례 학습: 임상양상과 신경전도·침근전도 소견을 연결합니다.</div>', unsafe_allow_html=True)
    st.markdown('<div class="case-bullet">• 검사 정보 입력 학습: 이상 소견을 직접 선택해 병변 위치와 질환을 추론합니다.</div>', unsafe_allow_html=True)
    st.markdown('<div class="case-bullet">• 본 앱은 학생 교육용이며 실제 임상 진단을 대체하지 않습니다.</div>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("### 진행할 학습 모드 선택")
    selected_mode = st.radio(
        "진행할 학습 모드를 선택하세요",
        [MODE_CASE, MODE_DIRECT],
        label_visibility="collapsed"
    )

    if selected_mode == MODE_CASE:
        st.markdown("""
        <div class="section-hint">
        <b>사례 학습</b><br>
        증상과 근전도 소견을 바탕으로 진단과 감별 포인트를 익히는 모드입니다.
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="section-hint">
        <b>검사 정보 입력 학습</b><br>
        판독지의 결과를 입력하면 진단명과 병변 위치 및 감별진단이 자동으로 출력됩니다.
        </div>
        """, unsafe_allow_html=True)

    if st.button("학습시작", type="primary", use_container_width=True):
        st.session_state["app_mode"] = selected_mode
        st.session_state["current_screen"] = "mode"
        clear_result()
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)