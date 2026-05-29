import html
import streamlit as st

from data.cases import CASE_LIBRARY
from data.anatomy import ANATOMY
from core.formatters import (
    educational_result_text,
    get_domain_reference,
    is_abnormal_result,
)
from utils.helpers import (
    get_case_names_for_selection,
    normalize_case_item_name,
    get_compact_item_label,
)


def _esc(value):
    return html.escape("" if value is None else str(value))


def _inject_mobile_css():
    """
    모바일 가독성 향상용 CSS.
    """
    st.markdown(
        """
        <style>
        .edu-title-wrap {
            margin-bottom: 1rem;
            padding-top: 0.4rem;
        }
        .edu-app-label {
            font-size: 0.9rem;
            font-weight: 800;
            color: #64748b;
            letter-spacing: -0.3px;
            line-height: 1.35;
        }
        .edu-page-title {
            font-size: 1.48rem;
            font-weight: 900;
            color: #1e3a8a;
            letter-spacing: -0.8px;
            line-height: 1.28;
            margin-top: 0.25rem;
            word-break: keep-all;
        }
        .edu-section-title {
            font-size: 1.12rem;
            font-weight: 900;
            color: #0f172a;
            margin-top: 1.5rem;
            margin-bottom: 0.7rem;
            line-height: 1.35;
        }
        .edu-subsection-title {
            font-size: 1rem;
            font-weight: 900;
            color: #2563eb;
            margin-top: 1rem;
            margin-bottom: 0.55rem;
            padding-bottom: 0.35rem;
            border-bottom: 1px solid #e2e8f0;
            line-height: 1.35;
        }
        .edu-card {
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            padding: 0.9rem;
            margin-bottom: 0.75rem;
            box-shadow: 0 1px 2px rgba(15, 23, 42, 0.05);
            word-break: keep-all;
            overflow-wrap: anywhere;
        }
        .edu-profile {
            background: #f1f5f9;
            border-radius: 10px;
            padding: 0.75rem;
            color: #334155;
            font-size: 0.94rem;
            font-weight: 700;
            display: flex;
            flex-wrap: wrap;
            gap: 0.45rem;
            line-height: 1.45;
        }
        .edu-symptom {
            font-size: 0.98rem;
            color: #334155;
            margin-bottom: 0.5rem;
            padding-left: 0.65rem;
            border-left: 3px solid #cbd5e1;
            line-height: 1.55;
            word-break: keep-all;
        }
        .edu-exam-item {
            margin-bottom: 0.7rem;
            padding-left: 0.25rem;
            line-height: 1.45;
        }
        .edu-exam-action {
            font-size: 1rem;
            font-weight: 900;
            color: #1e3a8a;
        }
        .edu-exam-result {
            font-size: 1rem;
            font-weight: 900;
        }
        .edu-exam-anatomy {
            font-size: 0.86rem;
            color: #64748b;
            margin-top: 0.2rem;
            padding-left: 0.65rem;
            border-left: 2px solid #f1f5f9;
            font-style: italic;
            line-height: 1.45;
        }
        .finding-group-title {
            font-weight: 900;
            font-size: 1.05rem;
            margin-top: 1.3rem;
            margin-bottom: 0.55rem;
            line-height: 1.35;
        }
        .finding-name {
            font-weight: 900;
            font-size: 0.98rem;
            color: #0f172a;
            margin-bottom: 0.55rem;
            line-height: 1.4;
        }
        .result-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 0.55rem;
            margin-bottom: 0.8rem;
        }
        .result-row {
            border-radius: 10px;
            padding: 0.7rem 0.8rem;
            line-height: 1.5;
            font-size: 0.94rem;
        }
        .result-label {
            display: block;
            font-size: 0.76rem;
            font-weight: 900;
            color: #64748b;
            margin-bottom: 0.22rem;
            letter-spacing: -0.2px;
        }
        .result-value {
            display: block;
            font-size: 0.98rem;
            font-weight: 900;
            word-break: keep-all;
        }
        .result-normal {
            background: #f8fafc;
            color: #334155;
            border: 1px solid #e2e8f0;
        }
        .result-abnormal {
            background: #fff1f2;
            color: #b91c1c;
            border: 1px solid #fecdd3;
        }
        .edu-reference {
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 10px;
            padding: 0.65rem;
            margin-top: 0.55rem;
            line-height: 1.48;
        }
        .edu-ref-title {
            font-size: 0.86rem;
            font-weight: 900;
            color: #334155;
            margin-bottom: 0.35rem;
        }
        .edu-ref-line {
            font-size: 0.84rem;
            color: #475569;
            margin-bottom: 0.25rem;
        }
        .edu-note {
            font-size: 0.78rem;
            color: #64748b;
            margin-top: 0.4rem;
            line-height: 1.45;
        }
        .edu-hr {
            margin: 1.7rem 0;
            border: none;
            border-top: 2px dashed #cbd5e1;
        }
        .dx-summary {
            background-color: #eff6ff;
            border-left: 4px solid #3b82f6;
            padding: 0.8rem;
            border-radius: 8px;
            margin-bottom: 1rem;
            line-height: 1.55;
            color: #1e3a8a;
            font-size: 0.94rem;
        }
        .dx-label {
            font-weight: 900;
            color: #334155;
            font-size: 1rem;
            margin-top: 0.95rem;
            margin-bottom: 0.45rem;
        }
        .dx-line {
            font-size: 0.92rem;
            color: #475569;
            margin-bottom: 0.45rem;
            padding-left: 0.8rem;
            position: relative;
            line-height: 1.52;
        }
        .dx-line::before {
            content: "•";
            position: absolute;
            left: 0;
            color: #94a3b8;
        }
        .diff-card {
            background-color: #fffbeb;
            border: 1px solid #fde68a;
            border-left: 4px solid #f59e0b;
            border-radius: 10px;
            padding: 0.9rem;
            margin-bottom: 0.8rem;
            line-height: 1.5;
        }
        .diff-name {
            font-weight: 900;
            color: #b45309;
            font-size: 1rem;
            margin-bottom: 0.55rem;
        }
        .diff-text {
            font-size: 0.9rem;
            margin-bottom: 0.45rem;
            color: #451a03;
        }
        .diff-tip {
            background-color: #fef3c7;
            padding: 0.55rem;
            border-radius: 8px;
            font-size: 0.88rem;
            color: #0f172a;
            margin-top: 0.45rem;
        }
        @media (max-width: 640px) {
            .edu-page-title {
                font-size: 1.32rem;
            }
            .edu-card {
                padding: 0.78rem;
                border-radius: 11px;
            }
            .edu-section-title {
                font-size: 1.05rem;
            }
            .finding-name {
                font-size: 0.94rem;
            }
            .result-row {
                font-size: 0.9rem;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def _get_domain(item_name):
    normalized_name = normalize_case_item_name(item_name)
    anatomy = ANATOMY.get(normalized_name, {})
    domain = anatomy.get("domain")

    if domain:
        return normalized_name, domain

    if any(x in normalized_name for x in ["SNAP", "감각신경"]):
        return normalized_name, "sensory"
    if any(x in normalized_name for x in ["CMAP", "복합근육활동전위"]):
        return normalized_name, "motor"
    if any(x in normalized_name for x in ["F파", "F-wave"]):
        return normalized_name, "f_wave"
    if any(x in normalized_name for x in ["H 반사", "H/M", "H-reflex"]):
        return normalized_name, "h_reflex"
    if any(x in normalized_name for x in ["R1", "R2", "자극"]):
        return normalized_name, "blink"

    return normalized_name, "other"


def _side_labels(side, has_right_value=True):
    if not has_right_value:
        return ("검사결과", "")

    if side == "양측":
        return ("좌측", "우측")
    if side == "좌":
        return ("비교측(우측)", "병변측(좌측)")
    if side == "우":
        return ("비교측(좌측)", "병변측(우측)")
    return ("비교측", "병변측")


def _render_result_rows(left_val, right_val, side, domain, name):
    left_text = educational_result_text(left_val, domain=domain, item_name=name)
    right_text = educational_result_text(right_val, domain=domain, item_name=name)

    has_right = right_val not in [None, "", "-"]
    left_label, right_label = _side_labels(side, has_right)

    if not has_right:
        abnormal = is_abnormal_result(left_val)
        row_class = "result-abnormal" if abnormal else "result-normal"
        return f"""
        <div class="result-grid">
            <div class="result-row {row_class}">
                <span class="result-label">{_esc(left_label)}</span>
                <span class="result-value">{_esc(left_text)}</span>
            </div>
        </div>
        """

    left_abn = is_abnormal_result(left_val)
    right_abn = is_abnormal_result(right_val)

    left_class = "result-abnormal" if left_abn else "result-normal"
    right_class = "result-abnormal" if right_abn else "result-normal"

    return f"""
    <div class="result-grid">
        <div class="result-row {left_class}">
            <span class="result-label">{_esc(left_label)}</span>
            <span class="result-value">{_esc(left_text)}</span>
        </div>
        <div class="result-row {right_class}">
            <span class="result-label">{_esc(right_label)}</span>
            <span class="result-value">{_esc(right_text)}</span>
        </div>
    </div>
    """


def _render_reference_block(domain, name):
    ref = get_domain_reference(domain, item_name=name)

    return f"""
    <div class="edu-reference">
        <div class="edu-ref-title">📌 {_esc(ref.get("title", "검사 참고"))}</div>
        <div class="edu-ref-line"><b>정상 범위:</b> {_esc(ref.get("normal", ""))}</div>
        <div class="edu-ref-line"><b>이상 기준:</b> {_esc(ref.get("abnormal", ""))}</div>
        <div class="edu-note">※ {_esc(ref.get("note", ""))}</div>
    </div>
    """


def _render_exam_item(item):
    if ":" not in item:
        return f'<div class="edu-exam-item">• {_esc(item)}</div>'

    parts = item.split(":", 1)
    action = parts[0].strip()
    rest = parts[1].split(" - ", 1)
    result = rest[0].strip()
    anatomy_text = rest[1].strip() if len(rest) > 1 else ""

    abnormal_keywords = [
        "Fair",
        "Poor",
        "Trace",
        "감소",
        "소실",
        "1+",
        "0",
        "Areflexia",
        "지연",
        "항진",
        "양성",
        "저하",
    ]
    res_color = "#b91c1c" if any(x in result for x in abnormal_keywords) else "#059669"

    return f"""
    <div class="edu-exam-item">
        <div>
            <span class="edu-exam-action">{_esc(action)}</span>
            <span style="color:#64748b;"> : </span>
            <span class="edu-exam-result" style="color:{res_color};">{_esc(result)}</span>
        </div>
        {f'<div class="edu-exam-anatomy">{_esc(anatomy_text)}</div>' if anatomy_text else ""}
    </div>
    """


def render_case_selector_only():
    """
    사례 선택 화면.
    닫는 HTML 태그가 그대로 보이는 문제를 피하기 위해
    불완전한 div 열기/닫기 방식을 사용하지 않는다.
    """
    _inject_mobile_css()

    case_options = get_case_names_for_selection()

    st.markdown(
        """
        <div class="edu-title-wrap">
            <div class="edu-app-label">🧠 교육용 근전도 판독 보조 앱</div>
            <div class="edu-page-title">📖 대표 사례 선택</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="edu-card" style="border-top:3px solid #1e3a8a;">
            <div style="font-size:0.95rem; font-weight:800; color:#334155;">
                학습할 사례를 선택하세요.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    selected_case = st.radio("대표 사례 선택", case_options, label_visibility="collapsed")

    st.write("")
    if st.button("🚀 사례 학습 시작", type="primary", use_container_width=True):
        st.session_state["confirmed_case"] = selected_case
        st.session_state["current_screen"] = "case_detail"
        st.session_state["last_result"] = None
        st.rerun()


def render_case_learning_info(case_name):
    """
    사례 상세 정보 화면.
    검사 소견은 결과 중심으로 보여주고,
    왜 그 질환으로 해석하는지는 아래 추론 섹션에서 설명한다.
    """
    _inject_mobile_css()

    case = CASE_LIBRARY.get(case_name)
    if not case:
        st.warning("선택한 사례 정보를 찾을 수 없습니다.")
        return

    patient = case.get("patient", {})
    findings = case.get("findings", {})
    physical_exam = patient.get("physical_exam", {})
    side = patient.get("side", "미선택")

    st.markdown(
        f"""
        <div class="edu-title-wrap">
            <div class="edu-app-label">🧠 교육용 근전도 판독 보조 앱</div>
            <div class="edu-page-title">📘 {_esc(case_name)}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="edu-card">
            <div class="edu-profile">
                <span>👤 {_esc(patient.get("age", "-"))}세</span>
                <span>⚧️ {_esc(patient.get("sex", "-"))}</span>
                <span>🎯 병변측: <span style="color:#b91c1c;">{_esc(side)}</span></span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="edu-section-title">🗣️ 주요 증상</div>', unsafe_allow_html=True)
    for s in patient.get("symptoms", []):
        st.markdown(f'<div class="edu-symptom">{_esc(s)}</div>', unsafe_allow_html=True)

    st.markdown('<div class="edu-section-title">🔨 이학적 검사결과</div>', unsafe_allow_html=True)

    for exam_category, exam_items in physical_exam.items():
        st.markdown(
            f'<div class="edu-subsection-title">■ {_esc(exam_category)}</div>',
            unsafe_allow_html=True,
        )
        for item in exam_items:
            st.markdown(_render_exam_item(item), unsafe_allow_html=True)

    st.markdown('<hr class="edu-hr">', unsafe_allow_html=True)

    st.markdown('<div class="edu-section-title">⚡ 주요 검사 소견</div>', unsafe_allow_html=True)

    sensory_items, motor_items, needle_items = [], [], []
    fwave_items, hreflex_items, blink_items, other_items = [], [], [], []

    for item_name, values in findings.items():
        normalized_name, domain = _get_domain(item_name)

        if domain == "sensory":
            sensory_items.append((normalized_name, values, domain))
        elif domain == "motor":
            motor_items.append((normalized_name, values, domain))
        elif domain == "muscle":
            needle_items.append((normalized_name, values, domain))
        elif domain == "f_wave":
            fwave_items.append((normalized_name, values, domain))
        elif domain in ["h_reflex", "h_ratio"]:
            hreflex_items.append((normalized_name, values, domain))
        elif domain == "blink":
            blink_items.append((normalized_name, values, domain))
        else:
            other_items.append((normalized_name, values, domain))

    def render_finding_group(title, items, color_hex):
        if not items:
            return

        st.markdown(
            f'<div class="finding-group-title" style="color:{color_hex};">✔ {_esc(title)}</div>',
            unsafe_allow_html=True,
        )

        for name, values, domain in items:
            left_val = values[0] if len(values) > 0 else ""
            right_val = values[1] if len(values) > 1 else ""

            result_rows = _render_result_rows(left_val, right_val, side, domain, name)
            reference = _render_reference_block(domain, name)

            st.markdown(
                f"""
                <div class="edu-card">
                    <div class="finding-name">{_esc(get_compact_item_label(name))}</div>
                    {result_rows}
                    {reference}
                </div>
                """,
                unsafe_allow_html=True,
            )

    render_finding_group("감각신경전도검사(Sensory NCS, SNAP)", sensory_items, "#059669")
    render_finding_group("운동신경전도검사(Motor NCS, CMAP)", motor_items, "#2563eb")
    render_finding_group("침근전도검사(Needle EMG)", needle_items, "#d97706")
    render_finding_group("F파(F-wave) 검사", fwave_items, "#9333ea")
    render_finding_group("H-반사(H-reflex) 검사", hreflex_items, "#7c3aed")
    render_finding_group("눈깜빡반사검사(Blink reflex)", blink_items, "#7c3aed")
    render_finding_group("기타 특수검사", other_items, "#64748b")

    st.markdown('<hr class="edu-hr">', unsafe_allow_html=True)
    st.markdown(
        '<div class="edu-section-title">💡 왜 이 질환을 진단하는가?</div>',
        unsafe_allow_html=True,
    )

    teaching_dx = case.get("teaching_diagnosis", {})

    if teaching_dx.get("summary"):
        st.markdown(
            f"""
            <div class="dx-summary">
                <b>🎯 핵심 요약</b><br>
                {_esc(teaching_dx.get("summary", ""))}
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div class="edu-card" style="background:#f8fafc;">
            <div style="font-weight:900; color:#334155; margin-bottom:0.4rem;">📚 판독 기본 원칙</div>
            <div class="edu-ref-line">• 신경전도검사(NCS)의 정상 여부는 절대값이 아니라 검사실 정상범위와 비교해 판단합니다.</div>
            <div class="edu-ref-line">• 감각신경활동전위(SNAP) 보존과 척추주위근 침범은 신경뿌리병증 판단에 중요한 단서입니다.</div>
            <div class="edu-ref-line">• 침근전도검사에서 섬유자발전위(fibrillation potential)와 양성예파(positive sharp wave)는 탈신경근을 시사합니다.</div>
            <div class="edu-ref-line">• F파(F-wave)는 근위부 운동신경과 신경뿌리 평가에 유용합니다.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    for key, label in [
        ("ncs_reason", "신경전도검사 결과 해석"),
        ("emg_reason", "침근전도검사 및 특수검사 결과 해석"),
        ("integration", "최종 진단으로 연결하는 이유"),
    ]:
        if teaching_dx.get(key):
            st.markdown(f'<div class="dx-label">{_esc(label)}</div>', unsafe_allow_html=True)
            for line in teaching_dx[key]:
                st.markdown(f'<div class="dx-line">{_esc(line)}</div>', unsafe_allow_html=True)

    st.markdown('<hr class="edu-hr">', unsafe_allow_html=True)
    st.markdown(
        '<div class="edu-section-title">🔍 감별진단 가이드</div>',
        unsafe_allow_html=True,
    )

    differential_diagnoses = case.get("differential_diagnosis", [])

    if not differential_diagnoses:
        st.info("등록된 감별진단 정보가 없습니다.")
        return

    for dx_item in differential_diagnoses:
        st.markdown(
            f"""
            <div class="diff-card">
                <div class="diff-name">{_esc(dx_item.get("name", ""))}</div>
                <div class="diff-text"><b>고려 이유:</b> {_esc(dx_item.get("why_consider", ""))}</div>
                <div class="diff-text"><b>감별 포인트:</b> {_esc(dx_item.get("how_to_differentiate", ""))}</div>
                <div class="diff-tip"><b>💡 학생 팁:</b> {_esc(dx_item.get("practical_tip", ""))}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
