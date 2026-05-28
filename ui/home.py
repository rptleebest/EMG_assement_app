import streamlit as st
from data.constants import MODE_CASE, MODE_DIRECT
from utils.state import clear_result


def render_home_screen():
    # 시각적 위계를 최적화한 메인 제목
    st.markdown(
        """
        <div style="
            font-size: 2.4rem; 
            font-weight: 800; 
            color: #1e3a8a; 
            font-family: 'Pretendard', 'Noto Sans KR', sans-serif;
            letter-spacing: -1px;
            margin-bottom: 0.5rem;
            line-height: 1.3;
        ">
        🧠 교육용 근전도 판독 보조 앱
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    # 가독성을 높인 부제목 (설명)
    st.markdown(
        """
        <div style="
            font-size: 1.1rem; 
            color: #475569; 
            font-weight: 500; 
            margin-bottom: 2rem; 
            line-height: 1.5;
        ">
        물리치료학과 학생의 근전도 사례 학습과 기본 해석 훈련을 위한 교육용 앱입니다. 더불어 임상에서 근전도 검사 결과를 직접 입력하여 질환을 자동으로 추론해보는 보조 도구입니다.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="warn-card">', unsafe_allow_html=True)
    st.markdown("### 📌 학습 안내")
    st.markdown('<div class="case-bullet">• <b>사례 학습</b>: 임상양상과 신경전도·침근전도 소견을 연결합니다.</div>', unsafe_allow_html=True)
    st.markdown('<div class="case-bullet">• <b>검사 정보 입력 학습</b>: 이상 소견을 직접 선택해 병변 위치와 질환을 추론합니다.</div>', unsafe_allow_html=True)
    st.markdown('<div class="case-bullet" style="color: #b91c1c;">• <b>본 앱은 교육용이며 실제 임상 진단을 대체하지 않습니다.</b></div>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("### 🎯 진행할 학습 모드 선택")
    selected_mode = st.radio(
        "진행할 학습 모드를 선택하세요",
        [MODE_CASE, MODE_DIRECT],
        label_visibility="collapsed"
    )

    if selected_mode == MODE_CASE:
        st.markdown("""
        <div class="section-hint" style="background-color: #f0fdfa; border-left: 4px solid #0d9488;">
        <b style="color: #115e59; font-size: 1.05rem;">📖 사례 학습</b><br>
        증상과 근전도 소견을 바탕으로 진단과 감별 포인트를 익히는 모드입니다.
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="section-hint" style="background-color: #eff6ff; border-left: 4px solid #2563eb;">
        <b style="color: #1e3a8a; font-size: 1.05rem;">✍️ 검사 정보 입력 학습</b><br>
        판독지의 결과를 입력하면 진단명과 병변 위치 및 감별진단이 자동으로 출력됩니다.
        </div>
        """, unsafe_allow_html=True)

    st.write("") # 버튼 위 여백 추가
    if st.button("🚀 학습 시작", type="primary", use_container_width=True):
        st.session_state["app_mode"] = selected_mode
        st.session_state["current_screen"] = "mode"
        clear_result()
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)
