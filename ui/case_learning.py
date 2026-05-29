import streamlit as st

try:
    from data.cases import CASE_LIBRARY
except Exception:
    CASE_LIBRARY = {}


def _get_case_names():
    if not CASE_LIBRARY:
        return []
    return list(CASE_LIBRARY.keys())


def _render_patient_info(case):
    patient = case.get("patient", {})

    st.markdown("### 환자 정보")

    age = patient.get("age", "정보 없음")
    sex = patient.get("sex", "정보 없음")
    side = patient.get("side", "정보 없음")

    st.markdown(
        f"""
        <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:12px; padding:12px; margin-bottom:12px;">
            <div><b>나이:</b> {age}</div>
            <div><b>성별:</b> {sex}</div>
            <div><b>주된 병변측:</b> {side}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    symptoms = patient.get("symptoms", [])
    if symptoms:
        st.markdown("#### 주요 증상")
        for item in symptoms:
            st.markdown(f"- {item}")

    physical_exam = patient.get("physical_exam", {})
    if physical_exam:
        st.markdown("#### 이학적 검사")
        for title, lines in physical_exam.items():
            with st.expander(title, expanded=False):
                if isinstance(lines, list):
                    for line in lines:
                        st.markdown(f"- {line}")
                else:
                    st.markdown(str(lines))


def _render_findings(case):
    findings = case.get("findings", {})

    st.markdown("### 전기진단검사 소견")

    if not findings:
        st.info("등록된 검사 소견이 없습니다.")
        return

    for test_name, result in findings.items():
        if isinstance(result, tuple) and len(result) == 2:
            left_or_normal, right_or_abnormal = result
            st.markdown(
                f"""
                <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:10px; margin-bottom:8px;">
                    <div style="font-weight:800; color:#0f172a; word-break:keep-all;">{test_name}</div>
                    <div style="font-size:0.92rem; color:#334155; margin-top:4px;">
                        기준/비교: {left_or_normal}<br>
                        사례 소견: {right_or_abnormal}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.markdown(f"- **{test_name}**: {result}")


def _render_teaching_diagnosis(case):
    diagnosis = case.get("teaching_diagnosis", {})

    st.markdown("### 해석과 학습 포인트")

    if not diagnosis:
        st.info("등록된 해석 정보가 없습니다.")
        return

    summary = diagnosis.get("summary")
    if summary:
        st.success(summary)

    ncs_reason = diagnosis.get("ncs_reason", [])
    if ncs_reason:
        with st.expander("신경전도검사 해석", expanded=True):
            for line in ncs_reason:
                st.markdown(f"- {line}")

    emg_reason = diagnosis.get("emg_reason", [])
    if emg_reason:
        with st.expander("침근전도검사 해석", expanded=True):
            for line in emg_reason:
                st.markdown(f"- {line}")

    integration = diagnosis.get("integration", [])
    if integration:
        with st.expander("통합 해석", expanded=True):
            for line in integration:
                st.markdown(f"- {line}")


def _render_differential_diagnosis(case):
    differentials = case.get("differential_diagnosis", [])

    st.markdown("### 감별진단")

    if not differentials:
        st.info("등록된 감별진단 정보가 없습니다.")
        return

    for diff in differentials:
        name = diff.get("name", "감별진단")
        with st.expander(name, expanded=False):
            why = diff.get("why_consider")
            how = diff.get("how_to_differentiate")
            tip = diff.get("practical_tip")

            if why:
                st.markdown("**왜 고려하나요?**")
                st.markdown(f"- {why}")

            if how:
                st.markdown("**어떻게 구분하나요?**")
                st.markdown(f"- {how}")

            if tip:
                st.markdown("**실습 팁**")
                st.markdown(f"- {tip}")


def _render_pt_learning_box(case_name):
    st.markdown("### 물리치료 관점에서 생각해보기")

    lower_keywords = ["허리", "다리", "발", "종아리", "정강", "엉덩", "경직"]
    upper_keywords = ["목", "팔", "손", "엄지", "손목", "자신경", "노신경", "정중신경"]

    if any(keyword in case_name for keyword in lower_keywords):
        points = [
            "보행 중 발처짐, 무릎 조절, 엉덩관절 안정성을 확인합니다.",
            "감각저하가 있으면 피부 보호와 낙상 위험 교육이 필요합니다.",
            "근력저하 양상이 신경뿌리, 말초신경, 신경얼기 중 어디에 가까운지 연결해 봅니다.",
            "보조기, 보행훈련, 균형훈련, 기능적 전기자극 적용 가능성을 검토합니다.",
        ]
    elif any(keyword in case_name for keyword in upper_keywords):
        points = [
            "손 기능, 집기, 손목 안정성, 팔꿉관절 조절을 평가합니다.",
            "목 움직임과 팔 증상의 관련성을 확인합니다.",
            "말초 포착신경병증에서는 압박 자세와 반복 사용 습관을 확인합니다.",
            "신경가동성 운동, 자세 교육, 보조기 적용 가능성을 검토합니다.",
        ]
    else:
        points = [
            "검사 소견을 기능 제한과 연결해서 해석합니다.",
            "근력, 감각, 반사, 보행 또는 손 기능을 함께 평가합니다.",
            "진행성 약화나 급성 악화가 있으면 의학적 평가가 우선입니다.",
        ]

    for point in points:
        st.markdown(f"- {point}")


def render_case_list():
    st.markdown(
        """
        <div style="margin-bottom:1rem;">
            <div style="font-size:1.35rem; font-weight:900; color:#1e3a8a; word-break:keep-all;">
                사례 학습
            </div>
            <div style="font-size:0.95rem; color:#475569; margin-top:0.4rem; line-height:1.5; word-break:keep-all;">
                대표 환자 사례를 통해 증상, 이학적 검사, 신경전도검사, 침근전도검사를 연결하여 병변 위치를 추론합니다.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    case_names = _get_case_names()

    if not case_names:
        st.error("사례 데이터가 없습니다. `data/cases.py`의 CASE_LIBRARY를 확인해 주세요.")
        return

    selected_case = st.selectbox(
        "학습할 사례를 선택하세요",
        case_names,
        index=0,
    )

    st.session_state["selected_case_name"] = selected_case

    if st.button("선택한 사례 학습하기", type="primary", use_container_width=True):
        st.session_state["confirmed_case"] = selected_case
        st.session_state["current_screen"] = "case_detail"
        st.rerun()

    st.markdown("### 사례 목록")
    for name in case_names:
        st.markdown(f"- {name}")


def render_case_detail():
    case_name = st.session_state.get("confirmed_case")

    if not case_name:
        st.warning("선택된 사례가 없습니다.")
        st.session_state["current_screen"] = "case_learning"
        st.rerun()
        return

    case = CASE_LIBRARY.get(case_name)

    if not case:
        st.error("해당 사례를 찾을 수 없습니다.")
        return

    st.markdown(
        f"""
        <div style="margin-bottom:1rem;">
            <div style="font-size:1.25rem; font-weight:900; color:#1e3a8a; word-break:keep-all;">
                {case_name}
            </div>
            <div style="font-size:0.92rem; color:#64748b; margin-top:0.3rem; word-break:keep-all;">
                사례를 읽고 병변 위치와 감별진단을 생각해 보세요.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    tab1, tab2, tab3, tab4 = st.tabs(["환자 정보", "검사 소견", "해석", "물리치료 관점"])

    with tab1:
        _render_patient_info(case)

    with tab2:
        _render_findings(case)

    with tab3:
        _render_teaching_diagnosis(case)
        _render_differential_diagnosis(case)

    with tab4:
        _render_pt_learning_box(case_name)

    st.warning("본 사례는 교육용 예시이며 실제 임상 진단을 대체하지 않습니다.")


def render_case_learning():
    current_screen = st.session_state.get("current_screen", "case_learning")

    if current_screen == "case_detail":
        render_case_detail()
    else:
        render_case_list()
