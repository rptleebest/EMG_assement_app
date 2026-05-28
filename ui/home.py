import streamlit as st
from data.constants import MODE_CASE, MODE_DIRECT
from utils.state import clear_result

def render_home_screen():
    # 1. 메인 제목 (모바일에서 깨지지 않도록 크기 1.8rem으로 최적화, 자간 축소)
    st.markdown(
        """
        <div style="
            font-size: 1.8rem; 
            font-weight: 900; 
            color: #1e3a8a; 
            letter-spacing: -1.5px;
            margin-bottom: 0.5rem;
            line-height: 1.3;
        ">
        교육용 근전도 판독 보조 앱
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    # 2. 앱 소개글 (문장을 짧게 압축하여 모바일 가독성 극대화)
    st.markdown(
        """
        <div style="
            font-size: 1rem; 
            color: #475569; 
            font-weight: 500; 
            margin-bottom: 1.5rem; 
            line-height: 1.5;
            word-break: keep-all;
        ">
        물리치료학과 학생을 위한 <b>근전도(EMG/NCS) 해석 훈련 앱</b>입니다.<br>
        실제 데이터를 바탕으로 병변을 추론하고 감별 진단 능력을 기를 수 있습니다.
        </div>
        """,
        unsafe_allow_html=True
    )

    # 3. 학습 안내 카드 (아이콘 활용 및 핵심어 강조)
    st.markdown(
        """
        <div style="background-color: #f8fafc; padding: 15px; border-radius: 10px; border: 1px solid #e2e8f0; margin-bottom: 1.5rem;">
            <div style="font-weight: 700; font-size: 1.1rem; margin-bottom: 10px; color: #0f172a;">📌 학습 안내</div>
            <div style="font-size: 0.95rem; margin-bottom: 8px; color: #334155; word-break: keep-all;">
                ✔ <b>사례 학습</b>: 임상 증상과 신경/침근전도 소견을 연결하여 진단 흐름을 파악합니다.
            </div>
            <div style="font-size: 0.95rem; margin-bottom: 12px; color: #334155; word-break: keep-all;">
                ✔ <b>검사 정보 입력</b>: 이상 소견을 직접 선택하여 의심 병변 및 질환을 추론합니다.
            </div>
            <div style="font-size: 0.9rem; color: #b91c1c; font-weight: 600; word-break: keep-all; background-color: #fee2e2; padding: 8px; border-radius: 5px;">
                🚨 주의: 본 앱은 교육용 참고 자료이며, 실제 임상 진단을 대체할 수 없습니다.
            </div>
        </div>
        """, 
        unsafe_allow_html=True
    )

    # 4. 모드 선택 섹션
    st.markdown('<div style="font-weight: 700; font-size: 1.1rem; margin-bottom: 10px; color: #0f172a;"> 학습 모드 선택</div>', unsafe_allow_html=True)
    selected_mode = st.radio(
        "진행할 학습 모드를 선택하세요",
        [MODE_CASE, MODE_DIRECT],
        label_visibility="collapsed"
    )

    # 5. 선택된 모드에 따른 힌트 박스 (모바일용 폰트 0.95rem 적용)
    if selected_mode == MODE_CASE:
        st.markdown("""
        <div style="background-color: #f0fdfa; border-left: 4px solid #0d9488; padding: 12px; border-radius: 4px; margin-bottom: 1.5rem;">
            <b style="color: #115e59; font-size: 1rem;">📖 사례 학습</b><br>
            <span style="font-size: 0.95rem; color: #334155; word-break: keep-all;">증상과 근전도 소견을 바탕으로 진단과 감별 포인트를 익히는 모드입니다.</span>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="background-color: #eff6ff; border-left: 4px solid #2563eb; padding: 12px; border-radius: 4px; margin-bottom: 1.5rem;">
            <b style="color: #1e3a8a; font-size: 1rem;">✍️ 검사 정보 입력 학습</b><br>
            <span style="font-size: 0.95rem; color: #334155; word-break: keep-all;">판독 결과를 직접 입력하면 진단명과 병변 위치, 감별진단 가이드가 제공됩니다.</span>
        </div>
        """, unsafe_allow_html=True)

    # 6. 시작 버튼 (모바일 화면 전체 너비 사용)
    if st.button("🚀 학습 시작", type="primary", use_container_width=True):
        st.session_state["app_mode"] = selected_mode
        st.session_state["current_screen"] = "mode"
        clear_result()
        st.rerun()
