import streamlit as st

from data.edx_example_reports import EDX_EXAMPLE_REPORTS
from utils.korean_terms import ko
from utils.root_level_inference import (
    infer_root_scores_from_emg,
    summarize_top_roots,
    root_score_to_percent,
    infer_lesion_hint,
)


def render_direct_entry_start():
    """
    기존 라우터 호환용 시작 화면.
    """
    st.markdown(
        """
        <div style="margin-bottom:1rem;">
            <div style="font-size:1.35rem; font-weight:900; color:#1e3a8a; word-break:keep-all;">
                검사결과표 판독 학습
            </div>
            <div style="font-size:0.95rem; color:#475569; margin-top:0.4rem; line-height:1.5; word-break:keep-all;">
                실제 근전도·신경전도검사 결과표 형식의 예제를 불러와,
                신경뿌리 레벨과 신경얼기 병변을 판독하는 과정을 학습합니다.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.info(
        "이전의 수치 직접 입력 방식은 학습 효율이 낮아, 대표 검사결과표 예제 판독 방식으로 개선했습니다."
    )

    if st.button("검사결과표 예제 학습 시작", type="primary", use_container_width=True):
        st.session_state["current_screen"] = "direct_input"
        st.rerun()


def render_section_selector():
    """
    기존 app.py 또는 라우터가 호출할 수 있는 호환 함수.
    실제로는 예제 학습에서 별도 섹션 선택이 필요하지 않습니다.
    """
    return ["검사결과표 예제"]


def render_input_sections_for_side(side=None, selected_sections=None):
    """
    기존 라우터 호환 함수.
    이름은 direct_input이지만, 실제 기능은 검사결과표 예제 판독 학습입니다.
    """
    render_report_learning()


def render_report_learning():
    st.markdown(
        """
        <div style="margin-bottom:1rem;">
            <div style="font-size:1.35rem; font-weight:900; color:#1e3a8a; word-break:keep-all;">
                검사결과표 판독 학습
            </div>
            <div style="font-size:0.95rem; color:#475569; margin-top:0.4rem; line-height:1.5; word-break:keep-all;">
                대표적인 근전도·신경전도검사 결과표 예제를 선택하고,
                직접 추정 진단을 고른 뒤 정답과 해설을 확인합니다.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    render_learning_notice()

    selected_category = render_category_filter()
    selected_report_name = render_report_selector(selected_category)

    if not selected_report_name:
        st.warning("예제를 선택하세요.")
        return

    report = EDX_EXAMPLE_REPORTS[selected_report_name]

    render_report_header(report)
    render_clinical_hint(report)
    render_report_tables(report)
    render_student_answer_area(selected_report_name, report)
    render_answer_and_reasoning(selected_report_name, report)
    render_root_score_area(report)
    render_differential_and_pt_points(report)


def render_learning_notice():
    with st.expander("학습 전 안내", expanded=True):
        st.markdown(
            """
            - 이 모드는 실제 진단을 대신하지 않는 교육용 판독 학습입니다.
            - 수치의 정상범위는 검사실, 장비, 피부온도, 나이, 키, 팔다리 길이에 따라 달라질 수 있습니다.
            - 따라서 이 모드에서는 수치 자체보다 **패턴 인식**을 중심으로 학습합니다.
            - 핵심은 다음 3가지입니다.
              1. 감각신경활동전위가 보존되는가, 감소하는가
              2. 척추주위근이 이상인가, 정상인가
              3. 침범 근육들이 같은 신경뿌리인지, 여러 말초신경/신경얼기 영역인지
            """
        )


def render_category_filter():
    categories = sorted({report["category"] for report in EDX_EXAMPLE_REPORTS.values()})

    selected_category = st.selectbox(
        "예제 분류",
        ["전체"] + categories,
        key="edx_example_category",
    )

    return selected_category


def render_report_selector(selected_category):
    if selected_category == "전체":
        report_names = list(EDX_EXAMPLE_REPORTS.keys())
    else:
        report_names = [
            name
            for name, report in EDX_EXAMPLE_REPORTS.items()
            if report["category"] == selected_category
        ]

    selected_report_name = st.selectbox(
        "검사결과표 예제 선택",
        report_names,
        key="edx_example_report_name",
    )

    return selected_report_name


def render_report_header(report):
    difficulty = report.get("difficulty", "")
    side = report.get("side", "")
    lesion_type = report.get("lesion_type", "")
    level = report.get("diagnosis_level", "")

    st.markdown("### 1단계. 예제 정보")

    st.markdown(
        f"""
        <div style="border:1px solid #e2e8f0; border-radius:12px; padding:14px; background:#ffffff; margin-bottom:12px;">
            <div style="font-size:1.05rem; font-weight:900; color:#0f172a; word-break:keep-all;">
                {ko(report.get("category", ""))}
            </div>
            <div style="margin-top:6px; color:#334155;">
                <b>병변측:</b> {ko(side)} &nbsp; | &nbsp;
                <b>학습 난이도:</b> {ko(difficulty)} &nbsp; | &nbsp;
                <b>병변 유형:</b> {ko(lesion_type)} &nbsp; | &nbsp;
                <b>우세 레벨:</b> {ko(level)}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_clinical_hint(report):
    st.markdown("### 2단계. 임상 힌트")

    hints = report.get("clinical_hint", [])

    if not hints:
        st.info("등록된 임상 힌트가 없습니다.")
        return

    for hint in hints:
        st.markdown(f"- {ko(hint)}")


def render_report_tables(report):
    st.markdown("### 3단계. 검사결과표 확인")

    tabs = st.tabs([
        "감각신경전도검사",
        "운동신경전도검사",
        "침근전도검사",
        "특수검사",
    ])

    with tabs[0]:
        render_table_or_empty(report.get("sensory_ncs", []), "감각신경전도검사 자료가 없습니다.")

    with tabs[1]:
        render_table_or_empty(report.get("motor_ncs", []), "운동신경전도검사 자료가 없습니다.")

    with tabs[2]:
        render_table_or_empty(report.get("needle_emg", []), "침근전도검사 자료가 없습니다.")

    with tabs[3]:
        render_table_or_empty(report.get("special_tests", []), "특수검사 자료가 없습니다.")


def render_table_or_empty(rows, empty_message):
    if not rows:
        st.info(empty_message)
        return

    converted_rows = []
    for row in rows:
        converted_rows.append({ko(k): ko(v) for k, v in row.items()})

    st.dataframe(converted_rows, use_container_width=True, hide_index=True)


def render_student_answer_area(report_name, report):
    st.markdown("### 4단계. 먼저 직접 판단해 보기")

    all_diagnoses = [
        report_data["diagnosis"]
        for report_data in EDX_EXAMPLE_REPORTS.values()
    ]

    extra_choices = [
        "온종아리신경병증",
        "손목굴증후군",
        "팔꿈치 부위 자신경병증",
        "노신경병증",
        "다발신경병증",
        "잘 모르겠음",
    ]

    choices = sorted(set(all_diagnoses + extra_choices))

    selected_answer = st.selectbox(
        "추정 진단을 선택하세요",
        choices,
        key=f"student_answer_{report_name}",
    )

    confidence = st.slider(
        "내 판단 확신도",
        min_value=0,
        max_value=100,
        value=50,
        step=5,
        key=f"student_confidence_{report_name}",
    )

    if st.button("내 답안 저장", key=f"save_answer_{report_name}", use_container_width=True):
        st.session_state[f"saved_answer_{report_name}"] = selected_answer
        st.session_state[f"saved_confidence_{report_name}"] = confidence
        st.success("답안을 저장했습니다. 아래에서 정답과 해설을 확인하세요.")


def render_answer_and_reasoning(report_name, report):
    st.markdown("### 5단계. 정답과 해설")

    show_answer = st.checkbox(
        "정답과 해설 보기",
        key=f"show_answer_{report_name}",
        value=False,
    )

    if not show_answer:
        st.info("먼저 직접 추정 진단을 선택한 뒤 정답을 확인해 보세요.")
        return

    saved_answer = st.session_state.get(f"saved_answer_{report_name}", None)
    saved_confidence = st.session_state.get(f"saved_confidence_{report_name}", None)

    correct_answer = report.get("diagnosis", "")

    if saved_answer:
        if saved_answer == correct_answer:
            st.success(f"정답입니다. 선택한 진단: {ko(saved_answer)}")
        else:
            st.warning(f"선택한 진단: {ko(saved_answer)}")
            st.success(f"정답: {ko(correct_answer)}")

        if saved_confidence is not None:
            st.caption(f"내 판단 확신도: {saved_confidence}%")
    else:
        st.success(f"정답: {ko(correct_answer)}")

    lesion_hint = infer_lesion_hint(report)

    st.markdown("#### 핵심 판독 포인트")
    st.markdown(f"- {ko(lesion_hint)}")

    for reason in report.get("key_reasoning", []):
        st.markdown(f"- {ko(reason)}")


def render_root_score_area(report):
    st.markdown("### 6단계. 신경뿌리 레벨 점수")

    needle_emg = report.get("needle_emg", [])

    if not needle_emg:
        st.info("침근전도검사 자료가 없어 신경뿌리 점수를 계산할 수 없습니다.")
        return

    calculated_scores, abnormal_muscles, normal_muscles = infer_root_scores_from_emg(needle_emg)
    calculated_percent = root_score_to_percent(calculated_scores)
    top_roots = summarize_top_roots(calculated_scores)

    expected_scores = report.get("expected_root_scores", {})

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("#### 자동 계산 점수")
        render_score_bars(calculated_percent)

    with c2:
        st.markdown("#### 예제 기준 정답 점수")
        if expected_scores:
            render_score_bars(expected_scores)
        else:
            st.info("등록된 정답 점수가 없습니다.")

    if top_roots:
        top_text = ", ".join([f"{root}({score})" for root, score in top_roots])
        st.markdown(f"**자동 추정 상위 레벨:** {ko(top_text)}")

    with st.expander("점수 계산에 사용된 근육 보기", expanded=False):
        st.markdown("**이상 근육**")
        if abnormal_muscles:
            for muscle in abnormal_muscles:
                st.markdown(f"- {ko(muscle)}")
        else:
            st.markdown("- 없음")

        st.markdown("**정상 또는 보존 근육**")
        if normal_muscles:
            for muscle in normal_muscles:
                st.markdown(f"- {ko(muscle)}")
        else:
            st.markdown("- 없음")

    st.caption(
        "점수는 교육용입니다. 실제 판독에서는 근육 선택, 삽입활동, 휴식 시 자발전위, 수의수축 양상, 임상 증상을 함께 봅니다."
    )


def render_score_bars(scores):
    if not scores:
        st.info("점수 정보가 없습니다.")
        return

    sorted_items = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    for root, score in sorted_items:
        try:
            numeric_score = int(score)
        except Exception:
            numeric_score = 0

        if numeric_score <= 0:
            continue

        st.markdown(
            f"""
            <div style="margin-bottom:8px;">
                <div style="display:flex; justify-content:space-between; font-size:0.9rem; color:#334155;">
                    <b>{ko(root)}</b><span>{numeric_score}%</span>
                </div>
                <div style="background:#e2e8f0; border-radius:999px; height:10px; overflow:hidden;">
                    <div style="background:#2563eb; width:{min(numeric_score, 100)}%; height:10px;"></div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_differential_and_pt_points(report):
    st.markdown("### 7단계. 감별진단과 물리치료 평가 포인트")

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("#### 감별진단")
        differentials = report.get("differentials", [])
        if differentials:
            for item in differentials:
                st.markdown(f"- {ko(item)}")
        else:
            st.info("등록된 감별진단이 없습니다.")

    with c2:
        st.markdown("#### 물리치료 평가 포인트")
        pt_points = report.get("pt_points", [])
        if pt_points:
            for item in pt_points:
                st.markdown(f"- {ko(item)}")
        else:
            st.info("등록된 물리치료 평가 포인트가 없습니다.")

    render_next_learning_tip(report)


def render_next_learning_tip(report):
    diagnosis_level = report.get("diagnosis_level", "")
    lesion_type = report.get("lesion_type", "")

    st.markdown("### 학습 정리")

    if lesion_type == "radiculopathy":
        st.info(
            f"{ko(diagnosis_level)} 신경뿌리병증에서는 감각신경활동전위 보존, 척추주위근 이상, 같은 신경뿌리를 공유하는 여러 말초신경 지배근 침범을 함께 확인하세요."
        )
    elif lesion_type == "plexopathy":
        st.info(
            "신경얼기병증에서는 감각신경활동전위 감소, 여러 말초신경 영역 침범, 척추주위근 보존 여부가 핵심 감별 포인트입니다."
        )
    else:
        st.info(
            "검사결과표는 단일 수치보다 전체 패턴을 보고 해석하는 것이 중요합니다."
        )
