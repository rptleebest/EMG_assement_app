import streamlit as st

from data.constants import BODY_REGION_OPTIONS, SIDE_OPTIONS
from data.abnormal_findings import ABNORMAL_GUIDE, ABNORMAL_CHECK_GROUPS
from utils.interpretation import interpret_findings, summarize_pattern
from utils.terminology import term


def render_criteria_guide():
    st.markdown("### 먼저 확인하세요: 이상 소견 체크 기준")

    with st.expander("교육용 기준 안내 보기", expanded=True):
        for title, lines in ABNORMAL_GUIDE.items():
            st.markdown(f"**{title}**")
            for line in lines:
                st.markdown(f"- {line}")
            st.markdown("")

        st.caption(
            "정확한 정상범위는 검사실마다 다릅니다. 검사결과표에 제시된 정상범위 또는 판독 문구를 우선 참고하세요."
        )


def render_region_and_context():
    st.markdown("### 1단계. 환자 정보와 검사 부위 선택")

    c1, c2 = st.columns(2)
    with c1:
        region = st.selectbox("주요 문제 부위", BODY_REGION_OPTIONS)
    with c2:
        side = st.selectbox("주된 병변측", SIDE_OPTIONS, index=0)

    symptoms = st.multiselect(
        "주요 증상",
        [
            "저림",
            "방사통",
            "감각저하",
            "근력저하",
            "발처짐",
            "손목처짐",
            "야간 손저림",
            "보행장애",
            "반사 저하",
            "반사 항진",
            "경직",
            "발목간대경련",
        ],
    )

    return region, side, symptoms


def render_abnormal_checklist():
    st.markdown("### 2단계. 검사결과표에서 이상 소견만 체크하세요")

    selected_codes = []

    for group_name, items in ABNORMAL_CHECK_GROUPS.items():
        with st.expander(group_name, expanded=False):
            for item in items:
                checked = st.checkbox(
                    item["label"],
                    key=f"abn_{item['code']}",
                    help=item.get("hint", ""),
                )
                if checked:
                    selected_codes.append(item["code"])
                    st.caption(f"의미: {item.get('hint', '')}")

    return selected_codes


def render_selected_summary(region, side, symptoms, selected_codes):
    st.markdown("### 3단계. 입력 요약")

    if not selected_codes:
        st.info("아직 체크한 이상 소견이 없습니다.")
        return

    st.markdown(
        f"""
        <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px; margin-bottom:12px;">
            <div><b>주요 부위:</b> {region}</div>
            <div><b>병변측:</b> {side}</div>
            <div><b>증상:</b> {", ".join(symptoms) if symptoms else "선택 없음"}</div>
            <div><b>체크한 이상 소견 수:</b> {len(selected_codes)}개</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_result_card(result, rank):
    confidence = result["confidence"]

    if confidence >= 75:
        color = "#dc2626"
        badge = "가능성 높음"
    elif confidence >= 45:
        color = "#ea580c"
        badge = "가능성 중간"
    else:
        color = "#64748b"
        badge = "가능성 낮음"

    st.markdown(
        f"""
        <div style="border:1px solid #e2e8f0; border-radius:12px; padding:14px; margin-bottom:14px; background:#ffffff;">
            <div style="display:flex; justify-content:space-between; align-items:center; gap:8px;">
                <div style="font-size:1.05rem; font-weight:900; color:#0f172a; word-break:keep-all;">
                    {rank}. {result["name"]}
                </div>
                <div style="font-size:0.82rem; font-weight:800; color:white; background:{color}; padding:4px 8px; border-radius:999px;">
                    {badge}
                </div>
            </div>
            <div style="margin-top:8px; color:#334155; font-size:0.95rem;">
                <b>추정 병변 위치:</b> {result["lesion"]}
            </div>
            <div style="margin-top:4px; color:#334155; font-size:0.95rem;">
                <b>교육용 일치도:</b> {confidence}%
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.expander("왜 이렇게 해석하나요?", expanded=True):
        for line in result["teaching"]:
            st.markdown(f"- {line}")

    with st.expander("물리치료 평가 포인트", expanded=False):
        for line in result["pt_points"]:
            st.markdown(f"- {line}")

    with st.expander("함께 감별할 질환", expanded=False):
        for item in result["differentials"]:
            st.markdown(f"- {item}")


def render_interpretation_results(region, selected_codes):
    st.markdown("### 4단계. 자동 추론 결과")

    if not selected_codes:
        st.info("이상 소견을 체크하면 자동 추론 결과가 표시됩니다.")
        return

    results = interpret_findings(selected_codes, selected_region=region)
    pattern_comments = summarize_pattern(selected_codes)

    used_terms = set()

    st.markdown("#### 핵심 패턴 요약")
    if pattern_comments:
        for comment in pattern_comments:
            st.markdown(f"- {comment}")
    else:
        st.markdown("- 아직 특정 패턴이 뚜렷하지 않습니다. 추가 소견을 체크해 보세요.")

    st.markdown("#### 가능성 순위")
    if not results:
        st.warning("현재 체크 조합만으로는 뚜렷한 질환군을 추론하기 어렵습니다.")
        return

    for idx, result in enumerate(results, start=1):
        render_result_card(result, idx)

    st.markdown("#### 용어 정리")
    st.markdown(f"- {term('SNAP', used_terms)}: 감각신경의 전기적 반응입니다.")
    st.markdown(f"- {term('CMAP', used_terms)}: 운동신경 자극으로 근육에서 기록되는 전기적 반응입니다.")
    st.markdown(f"- {term('FIB', used_terms)}와 {term('PSW', used_terms)}: 휴식 시 보이면 탈신경을 시사합니다.")
    st.markdown(f"- {term('MUAP', used_terms)}: 수의수축 때 관찰되는 운동단위의 전기적 활동입니다.")
    st.markdown(f"- {term('RADICULOPATHY', used_terms)}: 신경뿌리 수준의 병변입니다.")
    st.markdown(f"- {term('PLEXOPATHY', used_terms)}: 신경얼기 수준의 병변입니다.")


def render_abnormal_check_learning():
    st.markdown(
        """
        <div style="margin-bottom: 1rem;">
            <div style="font-size:1.35rem; font-weight:900; color:#1e3a8a; word-break:keep-all;">
                이상 소견 체크 학습
            </div>
            <div style="font-size:0.95rem; color:#475569; margin-top:0.4rem; line-height:1.5; word-break:keep-all;">
                검사결과표에서 비정상 소견만 체크하여 병변 위치와 질환군을 추론합니다.
                세부 수치를 모두 입력하지 않아도 학습할 수 있도록 구성했습니다.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    render_criteria_guide()

    region, side, symptoms = render_region_and_context()

    selected_codes = render_abnormal_checklist()

    render_selected_summary(region, side, symptoms, selected_codes)

    if st.button("결과 해석하기", type="primary", use_container_width=True):
        st.session_state["abnormal_region"] = region
        st.session_state["abnormal_side"] = side
        st.session_state["abnormal_symptoms"] = symptoms
        st.session_state["abnormal_selected_codes"] = selected_codes

    saved_codes = st.session_state.get("abnormal_selected_codes", selected_codes)
    saved_region = st.session_state.get("abnormal_region", region)

    render_interpretation_results(saved_region, saved_codes)
