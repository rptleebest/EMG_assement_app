import streamlit as st
from data.cases import CASE_LIBRARY
from data.anatomy import ANATOMY
from core.formatters import normalize_result_text
from utils.helpers import get_case_names_for_selection, normalize_case_item_name, get_compact_item_label

def render_case_selector_only():
    case_options = get_case_names_for_selection()

    st.markdown(
        """
        <div style="margin-bottom: 1.2rem; padding-top: 0.5rem;">
            <div style="font-size: 0.95rem; font-weight: 700; color: #64748b; margin-bottom: 0.2rem; letter-spacing: -0.5px;">
                🧠 교육용 근전도 판독 보조 앱
            </div>
            <div style="font-size: 1.65rem; font-weight: 900; color: #1e3a8a; letter-spacing: -1px; line-height: 1.3;">
                📖 대표 사례 선택
            </div>
        </div>
        """, 
        unsafe_allow_html=True
    )

    st.markdown('<div class="section-card" style="padding: 1rem; border-top: 3px solid #1e3a8a;">', unsafe_allow_html=True)
    selected_case = st.radio("대표 사례 선택", case_options, label_visibility="collapsed")

    st.write("") 
    if st.button("🚀 사례 학습 시작", type="primary", use_container_width=True):
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

    # [중복 방지] 서브타이틀만 출력 (메인타이틀은 카드 내부에 존재)
    st.markdown(
        """
        <div style="margin-bottom: 0.5rem; padding-top: 0.5rem;">
            <div style="font-size: 0.9rem; font-weight: 700; color: #64748b; letter-spacing: -0.5px;">
                🧠 교육용 근전도 판독 보조 앱
            </div>
        </div>
        """, unsafe_allow_html=True
    )

    st.markdown('<div class="section-card" style="padding: 1.2rem; margin-bottom: 1rem;">', unsafe_allow_html=True)
    st.markdown(f'<div style="font-size: 1.4rem; font-weight: 800; color: #1e3a8a; margin-bottom: 0.8rem; word-break: keep-all;">📘 {case_name}</div>', unsafe_allow_html=True)
    st.markdown(
        f"""
        <div style="background-color: #f1f5f9; padding: 10px; border-radius: 8px; color: #334155; font-size: 0.95rem; font-weight: 600; display: flex; flex-wrap: wrap; gap: 10px;">
            <span>👤 {patient.get("age", "-")}세</span>
            <span>| ⚧️ {patient.get("sex", "-")}</span>
            <span>| 🎯 병변측: <span style="color:#b91c1c;">{patient.get("side", "-")}</span></span>
        </div>
        """, unsafe_allow_html=True
    )

    # 주요 증상
    st.markdown('<div style="font-size: 1.15rem; font-weight: 700; color: #0f172a; margin-top: 1.5rem; margin-bottom: 0.8rem;">🗣️ 주요 증상</div>', unsafe_allow_html=True)
    for s in patient.get("symptoms", []):
        st.markdown(f'<div style="font-size: 1rem; color: #334155; margin-bottom: 6px; padding-left: 10px; border-left: 3px solid #cbd5e1; word-break: keep-all;">{s}</div>', unsafe_allow_html=True)

    # 이학적 검사 결과 (2층 계층 구조 적용)
    st.markdown('<div style="font-size: 1.15rem; font-weight: 700; color: #0f172a; margin-top: 1.8rem; margin-bottom: 0.8rem;">🔨 이학적 검사결과</div>', unsafe_allow_html=True)
    
    for exam_category, exam_items in physical_exam.items():
        st.markdown(f'<div style="font-weight: 800; color: #2563eb; font-size: 1.05rem; margin-top: 15px; margin-bottom: 8px; border-bottom: 1px solid #e2e8f0; padding-bottom: 4px;">■ {exam_category}</div>', unsafe_allow_html=True)
        
        for item in exam_items:
            if ":" in item:
                parts = item.split(":", 1)
                action = parts[0].strip()
                rest = parts[1].split(" - ", 1)
                result = rest[0].strip()
                anatomy = rest[1].strip() if len(rest) > 1 else ""
                
                # 결과값 강조 색상 설정 (이상 소견 시 빨간색)
                res_color = "#b91c1c" if any(x in result for x in ["Fair", "Poor", "Trace", "감소", "소실", "1+", "0"]) else "#059669"

                st.markdown(
                    f"""
                    <div style="margin-bottom: 12px; padding-left: 5px;">
                        <div style="font-size: 1.05rem; line-height: 1.4;">
                            <span style="font-weight: 800; color: #1e3a8a;">{action}</span>
                            <span style="color: #64748b;"> : </span>
                            <span style="font-weight: 800; color: {res_color};">{result}</span>
                        </div>
                        {f'<div style="font-size: 0.88rem; color: #64748b; margin-top: 2px; padding-left: 12px; border-left: 2px solid #f1f5f9; font-style: italic; word-break: keep-all;">{anatomy}</div>' if anatomy else ""}
                    </div>
                    """, unsafe_allow_html=True
                )
            else:
                st.markdown(f'<div style="font-size: 1rem; color: #475569; margin-bottom: 8px; padding-left: 5px;">• {item}</div>', unsafe_allow_html=True)

    st.markdown('<hr style="margin: 2rem 0; border: none; border-top: 2px dashed #cbd5e1;">', unsafe_allow_html=True)
    
    # 주요 검사 소견
    st.markdown('<div style="font-size: 1.15rem; font-weight: 700; color: #0f172a; margin-bottom: 1rem;">⚡ 주요 검사 소견</div>', unsafe_allow_html=True)

    sensory_items, motor_items, needle_items = [], [], []
    blink_items, fwave_items, hreflex_items, other_reflex_items = [], [], [], []

    for item_name, values in findings.items():
        normalized_name = normalize_case_item_name(item_name)
        anatomy = ANATOMY.get(normalized_name, {})
        domain = anatomy.get("domain")
        
        if domain == "sensory": sensory_items.append((normalized_name, values))
        elif domain == "motor": motor_items.append((normalized_name, values))
        elif domain == "muscle": needle_items.append((normalized_name, values))
        else: 
            if any(x in normalized_name for x in ["R1", "R2", "자극"]): blink_items.append((normalized_name, values))
            elif any(x in normalized_name for x in ["F파", "F-wave"]): fwave_items.append((normalized_name, values))
            elif any(x in normalized_name for x in ["H 반사", "H/M"]): hreflex_items.append((normalized_name, values))
            else: other_reflex_items.append((normalized_name, values))

    def render_finding_group(title, items, color_hex):
        if not items: return
        st.markdown(f'<div style="font-weight: 700; color: {color_hex}; font-size: 1.1rem; margin-top: 1.5rem; margin-bottom: 0.5rem;">✔ {title}</div>', unsafe_allow_html=True)
        for name, values in items:
            left_val = values[0] if len(values) > 0 else ""
            right_val = values[1] if len(values) > 1 else ""
            if right_val == "" or right_val == "-":
                html = f'<div style="color: #b91c1c; font-weight: 800; font-size: 0.95rem;">결과: {normalize_result_text(left_val)}</div>'
            else:
                html = f"""
                <div style="display: flex; flex-direction: column; gap: 4px; font-size: 0.9rem;">
                    <div style="color: #64748b;"><span style="display:inline-block; width: 65px;">정상측:</span> {normalize_result_text(left_val)}</div>
                    <div style="color: #b91c1c; font-weight: 800; font-size: 0.95rem; background: #fff1f2; padding: 2px 5px; border-radius: 4px; width: fit-content;">
                        <span style="display:inline-block; width: 60px; color:#ef4444;">병변측:</span> {normalize_result_text(right_val)}
                    </div>
                </div>
                """
            st.markdown(
                f"""
                <div style="background-color: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 12px; margin-bottom: 8px; box-shadow: 0 1px 2px rgba(0,0,0,0.05);">
                    <div style="font-weight: 700; font-size: 0.95rem; color: #0f172a; margin-bottom: 8px;">{get_compact_item_label(name)}</div>
                    {html}
                </div>
                """, unsafe_allow_html=True
            )

    render_finding_group("감각신경전도검사", sensory_items, "#059669")
    render_finding_group("운동신경전도검사", motor_items, "#2563eb")
    render_finding_group("침근전도검사", needle_items, "#d97706")
    render_finding_group("눈깜빡반사(Blink Reflex) 검사", blink_items, "#7c3aed")
    render_finding_group("F파(F-wave) 검사", fwave_items, "#9333ea")
    render_finding_group("H-반사(H-reflex) 검사", hreflex_items, "#8b5cf6")
    render_finding_group("기타 특수검사", other_reflex_items, "#a855f7")

    # 진단 추론 및 감별 진단
    st.markdown('<hr style="margin: 2rem 0; border: none; border-top: 2px dashed #cbd5e1;">', unsafe_allow_html=True)
    teaching_dx = case.get("teaching_diagnosis", {})
    st.markdown('<div style="font-size: 1.15rem; font-weight: 700; color: #0f172a; margin-bottom: 1rem;">💡 왜 이 질환을 진단하는가?</div>', unsafe_allow_html=True)
    if teaching_dx.get("summary"):
        st.markdown(f'<div style="background-color: #eff6ff; border-left: 4px solid #3b82f6; padding: 12px; border-radius: 4px; margin-bottom: 1.2rem;"><b style="color: #1d4ed8; font-size:1rem;">🎯 핵심 요약</b><br><span style="font-size: 0.95rem; color: #1e3a8a; line-height:1.5;">{teaching_dx["summary"]}</span></div>', unsafe_allow_html=True)

    for key, label in [("ncs_reason", "신경전도검사 기반 추론"), ("emg_reason", "침근전도 및 기타검사 추론"), ("integration", "종합 해석")]:
        if teaching_dx.get(key):
            st.markdown(f'<div style="font-weight: 700; color: #334155; font-size: 1.05rem; margin-top: 1rem; margin-bottom: 0.5rem;">{label}</div>', unsafe_allow_html=True)
            for line in teaching_dx[key]:
                st.markdown(f'<div style="font-size: 0.95rem; color: #475569; margin-bottom: 6px; padding-left: 12px; position: relative;"><span style="position: absolute; left: 0; color: #94a3b8;">•</span>{line}</div>', unsafe_allow_html=True)

    st.markdown('<hr style="margin: 2rem 0; border: none; border-top: 2px dashed #cbd5e1;">', unsafe_allow_html=True)
    st.markdown('<div style="font-size: 1.15rem; font-weight: 700; color: #0f172a; margin-bottom: 1rem;">🔍 감별진단 가이드</div>', unsafe_allow_html=True)
    
    differential_diagnoses = case.get("differential_diagnosis", [])
    for idx, dx_item in enumerate(differential_diagnoses, 1):
        st.markdown(f"""
            <div style="background-color: #fffbeb; border: 1px solid #fde68a; border-left: 4px solid #f59e0b; border-radius: 8px; padding: 15px; margin-bottom: 12px;">
                <div style="font-weight: 800; color: #b45309; font-size: 1.05rem; margin-bottom: 10px;">{dx_item.get("name", "")}</div>
                <div style="font-size: 0.95rem; margin-bottom: 6px; color: #451a03;"><b style="color: #92400e;">고려 이유:</b> {dx_item.get("why_consider", "")}</div>
                <div style="font-size: 0.95rem; margin-bottom: 8px; color: #451a03;"><b style="color: #92400e;">감별 포인트:</b> {dx_item.get("how_to_differentiate", "")}</div>
                <div style="background-color: #fef3c7; padding: 8px; border-radius: 6px; font-size: 0.9rem; color: #0f172a;"><b>💡 학생 팁:</b> {dx_item.get("practical_tip", "")}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
