import streamlit as st

from data.constants import SEX_OPTIONS, SIDE_OPTIONS
from data.sections import SECTIONS
from data.anatomy import ANATOMY

from core.interpreters import (
    compose_ncs_result,
    compose_fwave_result,
    compute_hm_ratio_text,
    interpret_hm_ratio,
    get_domain_options,
    evaluate_ncs_numeric,
    NCS_CUTOFFS
)

from utils.helpers import (
    safe_index,
    simplify_level_text,
    get_motor_stimulation_labels,
    get_compact_item_label,
)
from utils.state import clear_result

DEFAULT_ARM_SET = [
    "팔 감각신경전도검사 (arm sensory NCS)",
    "팔 운동신경전도검사 (arm motor NCS)",
    "팔 침근전도검사 근육 (arm needle EMG muscles)",
]

DEFAULT_LEG_SET = [
    "다리 감각신경전도검사 (leg sensory NCS)",
    "다리 운동신경전도검사 (leg motor NCS)",
    "다리 침근전도검사 근육 (leg needle EMG muscles)",
]

DEFAULT_SPECIAL_SET = [
    "H반사 / 경직 평가 (H-reflex / Spasticity evaluation)",
    "F파 검사 (F-wave study)",
    "눈깜빡반사검사 (Blink reflex)",
]

SECTION_LABELS = {
    "팔 감각신경전도검사 (arm sensory NCS)": "팔 감각신경전도검사",
    "팔 운동신경전도검사 (arm motor NCS)": "팔 운동신경전도검사",
    "팔 침근전도검사 근육 (arm needle EMG muscles)": "팔 침근전도검사",
    "다리 감각신경전도검사 (leg sensory NCS)": "다리 감각신경전도검사",
    "다리 운동신경전도검사 (leg motor NCS)": "다리 운동신경전도검사",
    "다리 침근전도검사 근육 (leg needle EMG muscles)": "다리 침근전도검사",
    "H반사 / 경직 평가 (H-reflex / Spasticity evaluation)": "H반사 / 경직 평가",
    "F파 검사 (F-wave study)": "F파 검사",
    "눈깜빡반사검사 (Blink reflex)": "눈깜빡반사검사",
}

def get_display_section_name(section_name):
    return SECTION_LABELS.get(section_name, section_name)

def set_selected_sections(section_list):
    st.session_state["selected_sections"] = section_list.copy()
    st.session_state["selected_sections_multiselect"] = section_list.copy()

def render_direct_entry_start():
    # [UI 개선] 앱 이름(서브)과 화면 이름(메인)의 시각적 계층 분리 및 여백 최적화
    st.markdown(
        """
        <div style="margin-bottom: 1.5rem; padding-top: 0.5rem;">
            <div style="font-size: 0.95rem; font-weight: 700; color: #64748b; margin-bottom: 0.2rem; letter-spacing: -0.5px;">
                🧠 교육용 근전도 판독 보조 앱
            </div>
            <div style="font-size: 1.65rem; font-weight: 900; color: #1e3a8a; letter-spacing: -1px; line-height: 1.3;">
                🧾 검사 입력 학습 시작
            </div>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    st.markdown(
        '<div style="font-size: 1.0rem; color: #334155; font-weight: 500; margin-bottom: 1.5rem; word-break: keep-all; line-height: 1.5;">'
        '실제 임상 현장처럼 수치를 직접 입력하거나, 판독 결과를 선택하여 진단을 추론하는 모드입니다.</div>',
        unsafe_allow_html=True
    )

    # [UI 개선] 모바일 가독성을 위한 안내 가이드 뱃지 스타일
    st.markdown("""
    <div style="background-color: #f0fdfa; border-left: 4px solid #0d9488; padding: 15px; border-radius: 8px; margin-bottom: 2rem;">
        <b style="color: #115e59; font-size: 1.05rem;">💡 입력 가이드</b><br>
        <div style="font-size: 0.95rem; color: #334155; margin-top: 8px; line-height: 1.5; word-break: keep-all;">
        • 아래에서 <b>환자 정보</b>와 <b>입력 방식</b>을 설정하고 이동하세요.<br>
        • 다음 화면에서 이상 소견이 있는 검사 항목만 <b>체크(☑)</b>하세요.<br>
        • 체크하지 않은 항목은 <b>자동으로 '정상' 처리</b>됩니다.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 1. 환자 정보 설정
    st.markdown('<div style="font-weight: 800; font-size: 1.2rem; color: #0f172a; margin-bottom: 10px;">1. 환자 정보 설정</div>', unsafe_allow_html=True)
    c_age, c_sex, c_side = st.columns(3)
    with c_age:
        age = st.number_input("나이", min_value=1, max_value=120, value=st.session_state.get("age", 50), step=1)
    with c_sex:
        sex = st.selectbox("성별", SEX_OPTIONS, index=safe_index(SEX_OPTIONS, st.session_state.get("sex", "미선택")))
    with c_side:
        side = st.selectbox("병변측", SIDE_OPTIONS, index=safe_index(SIDE_OPTIONS, st.session_state.get("side", "미선택")))
    
    st.markdown("<br>", unsafe_allow_html=True)

    # 2. 데이터 입력 방식 설정
    st.markdown('<div style="font-weight: 800; font-size: 1.2rem; color: #0f172a; margin-bottom: 10px;">2. 데이터 입력 방식 설정</div>', unsafe_allow_html=True)
    input_mode = st.radio(
        "어떤 방식으로 입력하시겠습니까?",
        ["판독 결과 직접 선택 (기본)", "실제 수치 입력 (자동 판독)"],
        help="수치 입력을 선택하면 진폭과 잠복기를 숫자로 입력하여 앱이 자동으로 정상 여부를 판독합니다.",
        label_visibility="collapsed"
    )
    st.session_state["ncs_input_mode"] = input_mode

    st.markdown('<hr style="margin: 2rem 0; border: none; border-top: 2px dashed #cbd5e1;">', unsafe_allow_html=True)

    c3, c4 = st.columns(2)
    with c3:
        if st.button("🚀 입력 화면으로 이동", type="primary", use_container_width=True):
            st.session_state["age"] = age
            st.session_state["sex"] = sex
            st.session_state["side"] = side

            if "selected_sections" not in st.session_state:
                set_selected_sections([])

            st.session_state["current_screen"] = "direct_input"
            clear_result()
            st.rerun()

    with c4:
        if st.button("🔄 설정 초기화", use_container_width=True):
            clear_result()
            st.rerun()


def render_section_selector():
    all_sections = list(SECTIONS.keys())

    if "selected_sections" not in st.session_state:
        set_selected_sections([])

    # [UI 개선] 답답했던 박스 제거, 글자 크기/굵기 대폭 상향
    st.markdown('<div style="font-size: 1.3rem; font-weight: 800; color: #0f172a; margin-top: 1rem; margin-bottom: 0.5rem;">⚙️ 검사 영역 선택</div>', unsafe_allow_html=True)
    st.markdown(
        '<div style="font-size: 0.95rem; color: #475569; margin-bottom: 1.5rem; word-break: keep-all;">'
        '상단의 빠른 선택 버튼을 누르거나, 아래 드롭다운에서 원하는 검사만 개별적으로 구성하세요.</div>',
        unsafe_allow_html=True
    )

    # 1. 부위별 빠른 선택
    st.markdown('<div style="font-weight: 800; color: #2563eb; font-size: 1.1rem; margin-bottom: 8px;">1) 부위별 빠른 선택</div>', unsafe_allow_html=True)
    r1c1, r1c2, r1c3, r1c4 = st.columns(4)
    with r1c1:
        if st.button("팔 검사", use_container_width=True):
            set_selected_sections(DEFAULT_ARM_SET)
            st.rerun()
    with r1c2:
        if st.button("다리 검사", use_container_width=True):
            set_selected_sections(DEFAULT_LEG_SET)
            st.rerun()
    with r1c3:
        if st.button("전체 선택", use_container_width=True):
            set_selected_sections(all_sections)
            st.rerun()
    with r1c4:
        if st.button("모두 해제", use_container_width=True):
            set_selected_sections([])
            st.rerun()

    st.write("") 

    # 2. 특수검사 빠른 선택
    st.markdown('<div style="font-weight: 800; color: #7c3aed; font-size: 1.1rem; margin-top: 10px; margin-bottom: 8px;">2) 특수검사 빠른 선택</div>', unsafe_allow_html=True)
    s1, s2, s3, s4 = st.columns(4)
    with s1:
        if st.button("H반사 단독", use_container_width=True):
            set_selected_sections(["H반사 / 경직 평가 (H-reflex / Spasticity evaluation)"])
            st.rerun()
    with s2:
        if st.button("F파 단독", use_container_width=True):
            set_selected_sections(["F파 검사 (F-wave study)"])
            st.rerun()
    with s3:
        if st.button("눈깜빡반사", use_container_width=True):
            set_selected_sections(["눈깜빡반사검사 (Blink reflex)"])
            st.rerun()
    with s4:
        if st.button("특수 전체", use_container_width=True):
            set_selected_sections(DEFAULT_SPECIAL_SET)
            st.rerun()

    st.write("") 

    # 3. 개별 검사 직접 구성
    st.markdown('<div style="font-weight: 800; color: #059669; font-size: 1.1rem; margin-top: 10px; margin-bottom: 5px;">3) 개별 검사 직접 구성</div>', unsafe_allow_html=True)
    selected_sections = st.multiselect(
        "아래 창을 눌러 원하는 검사 영역을 직접 조합하세요.",
        options=all_sections,
        default=st.session_state.get("selected_sections", []),
        format_func=get_display_section_name,
        placeholder="👉 여기를 클릭하여 필요한 검사를 추가하세요",
        key="selected_sections_multiselect",
        label_visibility="collapsed"
    )

    st.session_state["selected_sections"] = selected_sections

    if not selected_sections:
        st.info("선택된 검사 영역이 없습니다. 위에서 검사를 선택해주세요.")

    st.markdown('<hr style="margin: 2rem 0; border: none; border-top: 2px dashed #cbd5e1;">', unsafe_allow_html=True)
    return selected_sections


def render_input_sections_for_side(side, selected_sections):
    selected_rows = []

    if not selected_sections:
        return selected_rows

    for section_name, items in SECTIONS.items():
        if section_name not in selected_sections:
            continue

        with st.expander(get_display_section_name(section_name), expanded=True):
            st.markdown('<div style="font-size:0.9rem; color:#475569; margin-bottom:12px; word-break:keep-all;">✅ 이상 소견이 있는 개별 신경/항목만 체크박스를 눌러 활성화하세요.</div>', unsafe_allow_html=True)
            
            for item in items:
                anatomy = ANATOMY.get(item, {})
                domain = anatomy.get("domain", "")
                nerve = anatomy.get("nerve", "정보 없음")
                level = simplify_level_text(anatomy.get("level", "정보 없음"))

                chk_key = f"chk_activate_{section_name}_{item}"
                is_active = st.checkbox(f"**{get_compact_item_label(item)}**", key=chk_key)
                
                if is_active:
                    st.markdown('<div style="background-color:#f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 12px; margin-top: 5px; margin-bottom: 10px;">', unsafe_allow_html=True)
                    st.markdown(
                        f'<div style="font-size: 0.85rem; color: #64748b; margin-bottom: 10px;">↳ <b>신경:</b> {nerve} | <b>레벨:</b> {level}</div>',
                        unsafe_allow_html=True
                    )

                    if domain in ["sensory", "motor"]:
                        row_payload = render_ncs_input(item, domain, side)
                    elif domain == "muscle":
                        row_payload = render_muscle_input(item, side)
                    elif domain == "f_wave":
                        row_payload = render_fwave_input(item, side)
                    elif domain == "h_reflex":
                        row_payload = render_h_reflex_input(item)
                    elif domain == "h_ratio":
                        row_payload = render_h_ratio_input(item)
                    elif domain == "blink":
                        row_payload = render_blink_input(item)
                    else:
                        row_payload = render_default_input(item, domain, side)

                    selected_rows.append(row_payload)
                    st.markdown("</div>", unsafe_allow_html=True)
                
                st.markdown('<hr style="margin:4px 0; border: none; border-top:1px dashed #e2e8f0;">', unsafe_allow_html=True)

    return selected_rows


def render_ncs_input(item, domain, side):
    stim_labels = get_motor_stimulation_labels(domain)
    input_mode = st.session_state.get("ncs_input_mode", "판독 결과 직접 선택 (기본)")

    unit_amp = "uV" if domain == "sensory" else "mV"
    
    if input_mode == "실제 수치 입력 (자동 판독)":
        cutoff = NCS_CUTOFFS.get(item, (10.0, 3.5) if domain=="sensory" else (3.0, 5.0))
        st.markdown(f'<div style="font-size: 0.85rem; color:#2563eb; margin-bottom: 8px;">💡 교육용 정상 참고치: 진폭 ≥ {cutoff[0]}{unit_amp}, 잠복기 ≤ {cutoff[1]}ms</div>', unsafe_allow_html=True)

        if side == "양측":
            c1, c2 = st.columns(2)
            with c1:
                st.markdown("**좌측**")
                l_amp = st.number_input(f"진폭 ({unit_amp})", min_value=0.0, value=0.0, step=0.1, key=f"{item}_l_amp_num")
                l_lat = st.number_input(f"잠복기 (ms)", min_value=0.0, value=0.0, step=0.1, key=f"{item}_l_lat_num")
            with c2:
                st.markdown("**우측**")
                r_amp = st.number_input(f"진폭 ({unit_amp})", min_value=0.0, value=0.0, step=0.1, key=f"{item}_r_amp_num")
                r_lat = st.number_input(f"잠복기 (ms)", min_value=0.0, value=0.0, step=0.1, key=f"{item}_r_lat_num")

            l_amp_stat, l_lat_stat = evaluate_ncs_numeric(item, domain, l_amp, l_lat)
            r_amp_stat, r_lat_stat = evaluate_ncs_numeric(item, domain, r_amp, r_lat)
            
            st.markdown(f'<div style="font-size: 0.9rem; color: #334155; margin-top: 5px;"><b>자동 판독 (좌측):</b> {l_amp_stat}, {l_lat_stat}</div>', unsafe_allow_html=True)
            st.markdown(f'<div style="font-size: 0.9rem; color: #334155;"><b>자동 판독 (우측):</b> {r_amp_stat}, {r_lat_stat}</div>', unsafe_allow_html=True)

            return {
                "item": item,
                "left": compose_ncs_result(l_amp_stat, l_lat_stat),
                "right": compose_ncs_result(r_amp_stat, r_lat_stat)
            }
        else:
            lesion_side_label = "좌측(병변측)" if side == "좌" else "우측(병변측)"
            normal_side_label = "우측(정상측)" if side == "좌" else "좌측(정상측)"
            
            c1, c2 = st.columns(2)
            with c1:
                st.markdown(f"**{normal_side_label}**")
                n_amp = st.number_input(f"진폭 ({unit_amp})", min_value=0.0, value=cutoff[0]+1.0, step=0.1, key=f"{item}_n_amp_num")
                n_lat = st.number_input(f"잠복기 (ms)", min_value=0.0, value=cutoff[1]-0.5, step=0.1, key=f"{item}_n_lat_num")
            with c2:
                st.markdown(f"**{lesion_side_label}**")
                les_amp = st.number_input(f"진폭 ({unit_amp})", min_value=0.0, value=0.0, step=0.1, key=f"{item}_les_amp_num")
                les_lat = st.number_input(f"잠복기 (ms)", min_value=0.0, value=0.0, step=0.1, key=f"{item}_les_lat_num")

            n_amp_stat, n_lat_stat = evaluate_ncs_numeric(item, domain, n_amp, n_lat)
            les_amp_stat, les_lat_stat = evaluate_ncs_numeric(item, domain, les_amp, les_lat)

            st.markdown(f'<div style="font-size: 0.9rem; color: #334155; margin-top: 5px;"><b>자동 판독 (정상측):</b> {n_amp_stat}, {n_lat_stat}</div>', unsafe_allow_html=True)
            st.markdown(f'<div style="font-size: 0.9rem; color: #b91c1c;"><b>자동 판독 (병변측):</b> {les_amp_stat}, {les_lat_stat}</div>', unsafe_allow_html=True)

            normal_result = compose_ncs_result(n_amp_stat, n_lat_stat)
            lesion_result = compose_ncs_result(les_amp_stat, les_lat_stat)

            if side == "좌":
                return {"item": item, "left": lesion_result, "right": normal_result}
            return {"item": item, "left": normal_result, "right": lesion_result}

    else:
        if side == "양측":
            c1, c2 = st.columns(2)
            with c1:
                left_amp = st.selectbox(f"좌측 {stim_labels['distal']} 진폭", ["정상 (Normal)", "감소 (Reduced)", "무반응 (No response)"], key=f"{item}_left_amp")
                left_lat = st.selectbox(f"좌측 {stim_labels['distal']} 잠복기", ["정상 (Normal)", "잠복기 지연 (Delayed latency)"], key=f"{item}_left_lat")
            with c2:
                right_amp = st.selectbox(f"우측 {stim_labels['distal']} 진폭", ["정상 (Normal)", "감소 (Reduced)", "무반응 (No response)"], key=f"{item}_right_amp")
                right_lat = st.selectbox(f"우측 {stim_labels['distal']} 잠복기", ["정상 (Normal)", "잠복기 지연 (Delayed latency)"], key=f"{item}_right_lat")
            return {"item": item, "left": compose_ncs_result(left_amp, left_lat), "right": compose_ncs_result(right_amp, right_lat)}

        lesion_side_label = "좌측(병변측)" if side == "좌" else "우측(병변측)"
        normal_side_label = "우측(정상측)" if side == "좌" else "좌측(정상측)"

        c1, c2 = st.columns(2)
        with c1:
            normal_amp = st.selectbox(f"{normal_side_label} 진폭", ["정상 (Normal)", "감소 (Reduced)", "무반응 (No response)"], key=f"{item}_normal_amp")
            normal_lat = st.selectbox(f"{normal_side_label} 잠복기", ["정상 (Normal)", "잠복기 지연 (Delayed latency)"], key=f"{item}_normal_lat")
        with c2:
            lesion_amp = st.selectbox(f"{lesion_side_label} 진폭", ["정상 (Normal)", "감소 (Reduced)", "무반응 (No response)"], key=f"{item}_lesion_amp")
            lesion_lat = st.selectbox(f"{lesion_side_label} 잠복기", ["정상 (Normal)", "잠복기 지연 (Delayed latency)"], key=f"{item}_lesion_lat")

        normal_result = compose_ncs_result(normal_amp, normal_lat)
        lesion_result = compose_ncs_result(lesion_amp, lesion_lat)

        if side == "좌":
            return {"item": item, "left": lesion_result, "right": normal_result}
        return {"item": item, "left": normal_result, "right": lesion_result}


def render_muscle_input(item, side):
    options = get_domain_options("muscle")
    if side == "양측":
        c1, c2 = st.columns(2)
        with c1:
            left = st.selectbox("좌측 침근전도", options, key=f"{item}_left_muscle")
        with c2:
            right = st.selectbox("우측 침근전도", options, key=f"{item}_right_muscle")
        return {"item": item, "left": left, "right": right}

    lesion_side_label = "좌측(병변측)" if side == "좌" else "우측(병변측)"
    normal_side_label = "우측(정상측)" if side == "좌" else "좌측(정상측)"

    c1, c2 = st.columns(2)
    with c1:
        normal = st.selectbox(f"{normal_side_label} 침근전도", options, key=f"{item}_normal_muscle")
    with c2:
        lesion = st.selectbox(f"{lesion_side_label} 침근전도", options, key=f"{item}_lesion_muscle")

    return {"item": item, "left": lesion if side=="좌" else normal, "right": normal if side=="좌" else lesion}


def render_fwave_input(item, side):
    if side == "양측":
        c1, c2 = st.columns(2)
        with c1:
            left_latency = st.selectbox("좌측 F파 잠복기", ["정상 (Normal)", "잠복기 지연 (Delayed latency)"], key=f"{item}_left_f_latency")
            left_response = st.selectbox("좌측 F파 반응", ["정상 (Normal)", "소실 (Absent)"], key=f"{item}_left_f_response")
        with c2:
            right_latency = st.selectbox("우측 F파 잠복기", ["정상 (Normal)", "잠복기 지연 (Delayed latency)"], key=f"{item}_right_f_latency")
            right_response = st.selectbox("우측 F파 반응", ["정상 (Normal)", "소실 (Absent)"], key=f"{item}_right_f_response")
        return {"item": item, "left": compose_fwave_result(left_latency, left_response), "right": compose_fwave_result(right_latency, right_response)}

    lesion_side_label = "좌측(병변측)" if side == "좌" else "우측(병변측)"
    normal_side_label = "우측(정상측)" if side == "좌" else "좌측(정상측)"

    c1, c2 = st.columns(2)
    with c1:
        normal_latency = st.selectbox(f"{normal_side_label} F파 잠복기", ["정상 (Normal)", "잠복기 지연 (Delayed latency)"], key=f"{item}_normal_f_latency")
        normal_response = st.selectbox(f"{normal_side_label} F파 반응", ["정상 (Normal)", "소실 (Absent)"], key=f"{item}_normal_f_response")
    with c2:
        lesion_latency = st.selectbox(f"{lesion_side_label} F파 잠복기", ["정상 (Normal)", "잠복기 지연 (Delayed latency)"], key=f"{item}_lesion_f_latency")
        lesion_response = st.selectbox(f"{lesion_side_label} F파 반응", ["정상 (Normal)", "소실 (Absent)"], key=f"{item}_lesion_f_response")

    normal_result = compose_fwave_result(normal_latency, normal_response)
    lesion_result = compose_fwave_result(lesion_latency, lesion_response)
    return {"item": item, "left": lesion_result if side=="좌" else normal_result, "right": normal_result if side=="좌" else lesion_result}


def render_h_reflex_input(item):
    label = "좌측 H 반사" if "좌" in item else "우측 H 반사"
    status = st.selectbox(label, ["정상 (Normal)", "지연 또는 소실 (Delayed/Absent)", "항진 또는 문턱값 감소 (Hyperactive / lower threshold)"], key=f"{item}_hreflex")
    return {"item": item, "left": status, "right": ""}


def render_h_ratio_input(item):
    st.markdown('<div style="font-size: 0.85rem; color:#065f46; margin-bottom: 8px;">💡 Hmax와 Mmax를 입력하면 H/M 비율이 자동 계산됩니다.</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        hmax = st.number_input("Hmax (mV)", min_value=0.0, value=0.0, step=0.1, key=f"{item}_hmax")
    with c2:
        mmax = st.number_input("Mmax (mV)", min_value=0.0, value=0.0, step=0.1, key=f"{item}_mmax")

    ratio, ratio_text = compute_hm_ratio_text(hmax, mmax)
    interp = interpret_hm_ratio(ratio)

    st.markdown(
        f"""
        <div style="background:#f8fafc; border:1px solid #d1fae5; padding:10px; border-radius:8px; margin-top:8px;">
            <div style="font-size:0.9rem; color:#0f172a;"><b>계산된 H/M 비율:</b> {ratio_text}</div>
            <div style="font-size:0.9rem; color:#0f172a; margin-top: 2px;"><b>해석:</b> {interp["label"]}</div>
            <div style="font-size:0.85rem; color:#475569; margin-top: 4px;">{interp["warning"]}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    result_text = "증가 가능 (May be increased)" if ratio is not None and ratio > 0.60 else "정상 (Normal)"
    return {"item": item, "left": result_text, "right": ""}


def render_blink_input(item):
    status = st.selectbox("반응 상태", ["정상 (Normal)", "지연 (Delayed)", "소실 (Absent)"], key=f"{item}_blink")
    return {"item": item, "left": status, "right": ""}


def render_default_input(item, domain, side):
    options = get_domain_options(domain, item)

    if len(options) == 1:
        return {"item": item, "left": options[0], "right": ""}

    if side == "양측":
        c1, c2 = st.columns(2)
        with c1:
            left = st.selectbox("좌측", options, key=f"{item}_left_default")
        with c2:
            right = st.selectbox("우측", options, key=f"{item}_right_default")
        return {"item": item, "left": left, "right": right}

    lesion_side_label = "좌측(병변측)" if side == "좌" else "우측(병변측)"
    normal_side_label = "우측(정상측)" if side == "좌" else "좌측(정상측)"

    c1, c2 = st.columns(2)
    with c1:
        normal = st.selectbox(normal_side_label, options, key=f"{item}_normal_default")
    with c2:
        lesion = st.selectbox(lesion_side_label, options, key=f"{item}_lesion_default")

    if side == "좌":
        return {"item": item, "left": lesion, "right": normal}
    return {"item": item, "left": normal, "right": lesion}
