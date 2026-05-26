import streamlit as st
from data.cases import CASE_LIBRARY
from data.anatomy import ANATOMY
from core.formatters import normalize_result_text
from utils.helpers import get_case_names_for_selection, normalize_case_item_name, get_compact_item_label

def render_case_selector_only():
    case_options = get_case_names_for_selection()

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="case-section-label">📖 대표 사례 선택</div>', unsafe_allow_html=True)
    selected_case = st.radio(
        "대표 사례 선택",
        case_options,
        label_visibility="collapsed"
    )

    if st.button("사례 학습 시작", type="primary", use_container_width=True):
        st.session_state["confirmed_case"] = selected_case
        st.session_state["current_screen"] = "case_detail"
        st.session_state["last_result"] = None
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)


def render_case_learning_info(case_name):
    case = CASE_LIBRARY.get(case_name)
    if not case:
        st.warning("선택한 사례 정보를 찾을 수 없습니다.")
        return

    patient = case.get("patient", {})
    findings = case.get("findings", {})
    physical_exam = patient.get("physical_exam", {})

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown(f'<div class="case-title-mobile">📘 {case_name}</div>', unsafe_allow_html=True)
    st.markdown(
        f'<div class="case-subtitle-mobile">연령: {patient.get("age", "-")}세 | 성별: {patient.get("sex", "-")} | 병변측: {patient.get("side", "-")}</div>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="case-section-label">🗣️ 주요 증상</div>', unsafe_allow_html=True)
    for s in patient.get("symptoms", []):
        st.markdown(f'<div class="case-bullet">• {s}</div>', unsafe_allow_html=True)

    st.markdown('<div class="case-section-label">🧪 이학적 검사결과</div>', unsafe_allow_html=True)
    # 이학적 검사를 카테고리별로 예쁘게 출력
    for exam_category, exam_items in physical_exam.items():
        st.markdown(f'<div class="finding-item-title" style="margin-top:12px; color:#2563eb;">■ {exam_category}</div>', unsafe_allow_html=True)
        items_html = "".join([f'<div class="case-bullet" style="margin-left: 10px;">• {item}</div>' for item in exam_items])
        st.markdown(f'<div class="case-text-block">{items_html}</div>', unsafe_allow_html=True)

    st.markdown('<hr class="strong-divider">', unsafe_allow_html=True)
    st.markdown('<div class="case-section-label">⚡ 주요 검사 소견</div>', unsafe_allow_html=True)

    # 결과를 도메인별로 그룹화
    sensory_items, motor_items, needle_items, reflex_items = [], [], [], []
    for item_name, values in findings.items():
        normalized_name = normalize_case_item_name(item_name)
        anatomy = ANATOMY.get(normalized_name, {})
        domain = anatomy.get("domain")
        
        if domain == "sensory":
            sensory_items.append((normalized_name, values))
        elif domain == "motor":
            motor_items.append((normalized_name, values))
        elif domain == "muscle":
            needle_items.append((normalized_name, values))
        else: # h_reflex, h_ratio, f_wave, blink 등
            reflex_items.append((normalized_name, values))

    def render_finding_group(title, items):
        if not items:
            return
        st.markdown(f'<div class="finding-item-title" style="margin-top:16px; color:#065f46;">✔ {title}</div>', unsafe_allow_html=True)
        for name, values in items:
            left_val = values[0] if len(values) > 0 else ""
            right_val = values[1] if len(values) > 1 else ""
            st.markdown(
                f"""
                <div class="case-text-block" style="padding: 8px 11px;">
                    <div style="font-weight: 600; font-size: 0.88rem; color: #0f172a;">{get_compact_item_label(name)}</div>
                    <div class="finding-subtext" style="margin-bottom:0;">좌측/정상측: {normalize_result_text(left_val)}</div>
                    <div class="finding-subtext" style="margin-bottom:0;">우측/병변측: {normalize_result_text(right_val)}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

    render_finding_group("감각신경전도검사", sensory_items)
    render_finding_group("운동신경전도검사", motor_items)
    render_finding_group("침근전도검사", needle_items)
    render_finding_group("특수 및 반사검사", reflex_items)

    teaching_dx = case.get("teaching_diagnosis", {})
    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
    st.markdown('<div class="case-section-label">💡 왜 이 질환을 진단하는가?</div>', unsafe_allow_html=True)

    if teaching_dx.get("summary"):
        st.markdown(f'<div class="case-bullet" style="font-weight:600; color:#1d4ed8;">• 핵심 요약: {teaching_dx["summary"]}</div>', unsafe_allow_html=True)

    for key, label in [("ncs_reason", "신경전도검사 기반 추론"), ("emg_reason", "침근전도 및 기타검사 기반 추론"), ("integration", "종합 해석")]:
        if teaching_dx.get(key):
            st.markdown(f'<div class="case-subheading">{label}</div>', unsafe_allow_html=True)
            for line in teaching_dx[key]:
                st.markdown(f'<div class="case-bullet">• {line}</div>', unsafe_allow_html=True)

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
    st.markdown('<div class="case-section-label">🔍 감별진단 가이드</div>', unsafe_allow_html=True)
    for idx, dx_item in enumerate(case.get("differential_diagnosis", []), 1):
        st.markdown(
            f"""
            <div class="case-text-block" style="background:#fffaf3; border-left:4px solid #f59e0b;">
                <div class="finding-item-title" style="color:#b45309;">{idx}. {dx_item.get("name", "")}</div>
                <div class="finding-subtext"><b>고려 이유:</b> {dx_item.get("why_consider", "")}</div>
                <div class="finding-subtext"><b>감별 포인트:</b> {dx_item.get("how_to_differentiate", "")}</div>
                <div class="finding-subtext" style="color:#0f172a; font-weight:600;"><b>💡 학생 팁:</b> {dx_item.get("practical_tip", "")}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("</div>", unsafe_allow_html=True)