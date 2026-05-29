import streamlit as st

from data.constants import BODY_REGION_OPTIONS, SIDE_OPTIONS
from utils.interpretation import interpret_findings, summarize_pattern
from utils.korean_terms import ko


# =========================================================
# 교육용 기본 기준
# =========================================================

EDU_CRITERIA = {
    "sensory_amp_low_uv": 10.0,
    "sensory_latency_high_ms": 3.5,
    "sensory_velocity_low_ms": 40.0,
    "motor_amp_low_mv": 4.0,
    "motor_latency_high_ms": 4.5,
    "motor_velocity_low_ms": 40.0,
    "side_to_side_amp_ratio": 0.5,
}


SENSORY_NERVES = [
    "정중신경",
    "자신경",
    "노신경",
    "얕은종아리신경",
    "장딴지신경",
    "기타",
]

MOTOR_NERVES = [
    "정중신경",
    "자신경",
    "노신경",
    "종아리신경",
    "깊은종아리신경",
    "정강신경",
    "넓적다리신경",
    "기타",
]

EMG_MUSCLES = [
    "목 척추주위근",
    "허리 척추주위근",
    "삼각근",
    "위팔두갈래근",
    "위팔노근",
    "노쪽손목폄근",
    "위팔세갈래근",
    "짧은엄지벌림근",
    "첫째등쪽뼈사이근",
    "가쪽넓은근",
    "엉덩허리근",
    "큰볼기근",
    "중간볼기근",
    "뒤넓적다리근",
    "장딴지근",
    "가자미근",
    "앞정강근",
    "긴종아리근",
    "긴엄지폄근",
    "기타",
]


EMG_MUSCLE_MAP = {
    "목 척추주위근": {
        "nerve": "척수신경 뒤가지",
        "roots": ["C4", "C5", "C6", "C7", "C8", "T1"],
        "tags": ["paraspinal", "cervical"],
    },
    "허리 척추주위근": {
        "nerve": "척수신경 뒤가지",
        "roots": ["L2", "L3", "L4", "L5", "S1"],
        "tags": ["paraspinal", "lumbar"],
    },
    "삼각근": {
        "nerve": "겨드랑신경",
        "roots": ["C5", "C6"],
        "tags": ["c5_c6"],
    },
    "위팔두갈래근": {
        "nerve": "근육피부신경",
        "roots": ["C5", "C6"],
        "tags": ["c5_c6"],
    },
    "위팔노근": {
        "nerve": "노신경",
        "roots": ["C5", "C6"],
        "tags": ["c5_c6"],
    },
    "노쪽손목폄근": {
        "nerve": "노신경",
        "roots": ["C6", "C7"],
        "tags": ["c5_c6", "c7"],
    },
    "위팔세갈래근": {
        "nerve": "노신경",
        "roots": ["C6", "C7", "C8"],
        "tags": ["c7"],
    },
    "짧은엄지벌림근": {
        "nerve": "정중신경",
        "roots": ["C8", "T1"],
        "tags": ["c8_t1", "median"],
    },
    "첫째등쪽뼈사이근": {
        "nerve": "자신경",
        "roots": ["C8", "T1"],
        "tags": ["c8_t1", "ulnar"],
    },
    "가쪽넓은근": {
        "nerve": "넓적다리신경",
        "roots": ["L2", "L3", "L4"],
        "tags": ["l4", "plexus"],
    },
    "엉덩허리근": {
        "nerve": "허리신경얼기",
        "roots": ["L2", "L3", "L4"],
        "tags": ["plexus"],
    },
    "큰볼기근": {
        "nerve": "아래볼기신경",
        "roots": ["L5", "S1", "S2"],
        "tags": ["s1", "plexus"],
    },
    "중간볼기근": {
        "nerve": "위볼기신경",
        "roots": ["L4", "L5", "S1"],
        "tags": ["l5", "plexus"],
    },
    "뒤넓적다리근": {
        "nerve": "궁둥신경",
        "roots": ["L5", "S1", "S2"],
        "tags": ["s1", "sciatic", "plexus"],
    },
    "장딴지근": {
        "nerve": "정강신경",
        "roots": ["S1", "S2"],
        "tags": ["s1", "tibial"],
    },
    "가자미근": {
        "nerve": "정강신경",
        "roots": ["S1", "S2"],
        "tags": ["s1", "tibial"],
    },
    "앞정강근": {
        "nerve": "깊은종아리신경",
        "roots": ["L4", "L5"],
        "tags": ["l5", "peroneal"],
    },
    "긴종아리근": {
        "nerve": "얕은종아리신경",
        "roots": ["L5", "S1"],
        "tags": ["l5", "peroneal"],
    },
    "긴엄지폄근": {
        "nerve": "깊은종아리신경",
        "roots": ["L5"],
        "tags": ["l5", "peroneal"],
    },
}


# =========================================================
# 기존 라우터 호환 함수
# =========================================================

def render_direct_entry_start():
    st.markdown(
        """
        <div style="margin-bottom:1rem;">
            <div style="font-size:1.35rem; font-weight:900; color:#1e3a8a; word-break:keep-all;">
                수치 직접 입력 학습
            </div>
            <div style="font-size:0.95rem; color:#475569; margin-top:0.4rem; line-height:1.5; word-break:keep-all;">
                실제 근전도·신경전도검사 결과표의 수치를 직접 입력하고,
                입력된 수치와 침근전도 패턴을 바탕으로 병변 위치와 질환군을 교육용으로 추론합니다.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.warning(
        "본 모드는 교육용입니다. 실제 정상범위는 검사실, 장비, 피부온도, 나이, 키, 팔다리 길이, 자극·기록 위치에 따라 달라질 수 있습니다."
    )

    st.markdown("### 입력 방식")

    st.markdown(
        """
        - 검사결과표에 `normal`, `reduced`, `delayed`, `no response`가 적혀 있으면 그 판독을 우선 참고하세요.
        - 수치만 있을 경우 아래 교육용 기준으로 자동 분류합니다.
        - 정상범위가 결과표에 제시되어 있다면 앱의 기본 기준보다 결과표의 정상범위를 우선하세요.
        """
    )

    c1, c2 = st.columns(2)

    with c1:
        region = st.selectbox(
            "주요 문제 부위",
            BODY_REGION_OPTIONS,
            key="direct_region_select_start",
        )

    with c2:
        side = st.selectbox(
            "주된 병변측",
            SIDE_OPTIONS,
            key="direct_side_select_start",
        )

    st.session_state["direct_region"] = region
    st.session_state["side"] = side

    if st.button("수치 입력 시작", type="primary", use_container_width=True):
        st.session_state["current_screen"] = "direct_input"
        st.rerun()


def render_section_selector():
    st.markdown("### 1단계. 입력할 검사 영역 선택")

    selected_sections = st.multiselect(
        "검사 영역",
        [
            "운동신경전도검사",
            "감각신경전도검사",
            "침근전도검사",
            "F파/H반사",
        ],
        default=[
            "운동신경전도검사",
            "감각신경전도검사",
            "침근전도검사",
        ],
        key="direct_selected_sections",
    )

    return selected_sections


def render_input_sections_for_side(side, selected_sections):
    render_direct_criteria_guide()

    region = st.session_state.get("direct_region", "목-팔")
    side = st.session_state.get("side", side)

    c1, c2 = st.columns(2)
    with c1:
        region = st.selectbox(
            "주요 문제 부위",
            BODY_REGION_OPTIONS,
            index=BODY_REGION_OPTIONS.index(region) if region in BODY_REGION_OPTIONS else 0,
            key="direct_region_select_main",
        )
    with c2:
        side = st.selectbox(
            "주된 병변측",
            SIDE_OPTIONS,
            index=SIDE_OPTIONS.index(side) if side in SIDE_OPTIONS else 0,
            key="direct_side_select_main",
        )

    st.session_state["direct_region"] = region
    st.session_state["side"] = side

    all_rows = []

    sensory_rows = []
    motor_rows = []
    emg_rows = []
    special_rows = []

    if "감각신경전도검사" in selected_sections:
        sensory_rows = render_sensory_input()
        all_rows.extend(sensory_rows)

    if "운동신경전도검사" in selected_sections:
        motor_rows = render_motor_input()
        all_rows.extend(motor_rows)

    if "침근전도검사" in selected_sections:
        emg_rows = render_needle_emg_input()
        all_rows.extend(emg_rows)

    if "F파/H반사" in selected_sections:
        special_rows = render_special_input()
        all_rows.extend(special_rows)

    if st.button("수치 기반 자동 해석", type="primary", use_container_width=True):
        selected_codes, detail_comments = infer_codes_from_direct_input(
            region=region,
            sensory_rows=sensory_rows,
            motor_rows=motor_rows,
            emg_rows=emg_rows,
            special_rows=special_rows,
        )

        st.session_state["direct_selected_codes"] = selected_codes
        st.session_state["direct_detail_comments"] = detail_comments
        st.session_state["direct_result_region"] = region

    selected_codes = st.session_state.get("direct_selected_codes", [])
    detail_comments = st.session_state.get("direct_detail_comments", [])
    result_region = st.session_state.get("direct_result_region", region)

    render_direct_results(result_region, selected_codes, detail_comments)

    return all_rows


# =========================================================
# 안내
# =========================================================

def render_direct_criteria_guide():
    st.markdown("### 먼저 확인하세요: 수치 입력 판정 기준")

    with st.expander("교육용 기준 안내 보기", expanded=False):
        st.markdown("**공통 원칙**")
        st.markdown("- 검사결과표에 제시된 정상범위 또는 판독 문구를 우선합니다.")
        st.markdown("- 수치만 입력한 경우 앱의 교육용 기준으로 이상 여부를 추정합니다.")
        st.markdown("- 반응이 없으면 진폭, 잠복기, 전도속도보다 `반응 소실`이 가장 중요한 이상 소견입니다.")

        st.markdown("**감각신경전도검사**")
        st.markdown(f"- 감각 진폭이 약 {EDU_CRITERIA['sensory_amp_low_uv']} μV 미만이면 진폭 감소로 봅니다.")
        st.markdown(f"- 감각 잠복기가 약 {EDU_CRITERIA['sensory_latency_high_ms']} ms 초과이면 잠복기 지연으로 봅니다.")
        st.markdown(f"- 감각 전도속도가 약 {EDU_CRITERIA['sensory_velocity_low_ms']} m/s 미만이면 전도속도 저하로 봅니다.")

        st.markdown("**운동신경전도검사**")
        st.markdown(f"- 운동 진폭이 약 {EDU_CRITERIA['motor_amp_low_mv']} mV 미만이면 진폭 감소로 봅니다.")
        st.markdown(f"- 원위운동잠복기가 약 {EDU_CRITERIA['motor_latency_high_ms']} ms 초과이면 지연으로 봅니다.")
        st.markdown(f"- 운동 전도속도가 약 {EDU_CRITERIA['motor_velocity_low_ms']} m/s 미만이면 전도속도 저하로 봅니다.")

        st.markdown("**침근전도검사**")
        st.markdown("- 휴식 시 섬유자발전위 또는 양성예파가 있으면 활동성 탈신경 소견입니다.")
        st.markdown("- 수의수축 시 운동단위전위가 없으면 심한 운동축삭 손상을 시사합니다.")
        st.markdown("- 척추주위근 이상은 신경뿌리병증 판단에 중요합니다.")
        st.markdown("- 척추주위근은 정상인데 여러 말초신경 영역의 근육이 이상이면 신경얼기병증을 고려합니다.")


# =========================================================
# 감각신경전도검사 입력
# =========================================================

def render_sensory_input():
    st.markdown("### 2단계. 감각신경전도검사 입력")

    rows = []

    count = st.number_input(
        "감각신경전도검사 입력 행 수",
        min_value=0,
        max_value=8,
        value=3,
        step=1,
        key="sensory_row_count",
    )

    for i in range(int(count)):
        with st.expander(f"감각신경전도검사 {i + 1}", expanded=i == 0):
            c1, c2 = st.columns(2)

            with c1:
                side = st.selectbox(
                    "측",
                    ["미선택", "좌", "우", "양측"],
                    key=f"sensory_side_{i}",
                )
                nerve = st.selectbox(
                    "신경",
                    SENSORY_NERVES,
                    key=f"sensory_nerve_{i}",
                )

            with c2:
                site = st.text_input(
                    "자극/기록 부위",
                    value="",
                    placeholder="예: wrist/second digit, calf/ankle",
                    key=f"sensory_site_{i}",
                )
                response = st.selectbox(
                    "결과표 판독",
                    ["수치로 판단", "정상", "진폭 감소", "잠복기 지연", "전도속도 저하", "반응 소실"],
                    key=f"sensory_response_{i}",
                )

            c3, c4, c5 = st.columns(3)

            with c3:
                latency = st.number_input(
                    "잠복기 또는 peak latency (ms)",
                    min_value=0.0,
                    max_value=50.0,
                    value=0.0,
                    step=0.1,
                    key=f"sensory_latency_{i}",
                )

            with c4:
                amplitude = st.number_input(
                    "진폭 (μV)",
                    min_value=0.0,
                    max_value=500.0,
                    value=0.0,
                    step=0.1,
                    key=f"sensory_amp_{i}",
                )

            with c5:
                velocity = st.number_input(
                    "전도속도 (m/s)",
                    min_value=0.0,
                    max_value=100.0,
                    value=0.0,
                    step=0.1,
                    key=f"sensory_velocity_{i}",
                )

            rows.append(
                {
                    "type": "sensory",
                    "side": side,
                    "nerve": nerve,
                    "site": site,
                    "response": response,
                    "latency": latency,
                    "amplitude": amplitude,
                    "velocity": velocity,
                    "item": f"{side} {nerve} 감각신경전도검사",
                    "left": "",
                    "right": "",
                }
            )

    return rows


# =========================================================
# 운동신경전도검사 입력
# =========================================================

def render_motor_input():
    st.markdown("### 3단계. 운동신경전도검사 입력")

    rows = []

    count = st.number_input(
        "운동신경전도검사 입력 행 수",
        min_value=0,
        max_value=10,
        value=3,
        step=1,
        key="motor_row_count",
    )

    for i in range(int(count)):
        with st.expander(f"운동신경전도검사 {i + 1}", expanded=i == 0):
            c1, c2 = st.columns(2)

            with c1:
                side = st.selectbox(
                    "측",
                    ["미선택", "좌", "우", "양측"],
                    key=f"motor_side_{i}",
                )
                nerve = st.selectbox(
                    "신경",
                    MOTOR_NERVES,
                    key=f"motor_nerve_{i}",
                )

            with c2:
                record_muscle = st.text_input(
                    "기록 근육",
                    value="",
                    placeholder="예: 짧은엄지벌림근, 짧은발가락폄근, 앞정강근",
                    key=f"motor_record_muscle_{i}",
                )
                response = st.selectbox(
                    "결과표 판독",
                    ["수치로 판단", "정상", "진폭 감소", "잠복기 지연", "전도속도 저하", "전도차단 의심", "반응 소실"],
                    key=f"motor_response_{i}",
                )

            c3, c4, c5 = st.columns(3)

            with c3:
                latency = st.number_input(
                    "원위잠복기 또는 onset latency (ms)",
                    min_value=0.0,
                    max_value=50.0,
                    value=0.0,
                    step=0.1,
                    key=f"motor_latency_{i}",
                )

            with c4:
                amp_unit = st.selectbox(
                    "진폭 단위",
                    ["mV", "μV"],
                    key=f"motor_amp_unit_{i}",
                )
                amplitude = st.number_input(
                    f"진폭 ({amp_unit})",
                    min_value=0.0,
                    max_value=20000.0,
                    value=0.0,
                    step=0.1,
                    key=f"motor_amp_{i}",
                )

            with c5:
                velocity = st.number_input(
                    "전도속도 (m/s)",
                    min_value=0.0,
                    max_value=100.0,
                    value=0.0,
                    step=0.1,
                    key=f"motor_velocity_{i}",
                )

            rows.append(
                {
                    "type": "motor",
                    "side": side,
                    "nerve": nerve,
                    "record_muscle": record_muscle,
                    "response": response,
                    "latency": latency,
                    "amplitude": amplitude,
                    "amp_unit": amp_unit,
                    "velocity": velocity,
                    "item": f"{side} {nerve} 운동신경전도검사",
                    "left": "",
                    "right": "",
                }
            )

    return rows


# =========================================================
# 침근전도검사 입력
# =========================================================

def render_needle_emg_input():
    st.markdown("### 4단계. 침근전도검사 입력")

    rows = []

    count = st.number_input(
        "침근전도검사 입력 근육 수",
        min_value=0,
        max_value=16,
        value=6,
        step=1,
        key="emg_row_count",
    )

    for i in range(int(count)):
        with st.expander(f"침근전도검사 근육 {i + 1}", expanded=i == 0):
            c1, c2 = st.columns(2)

            with c1:
                side = st.selectbox(
                    "측",
                    ["미선택", "좌", "우", "양측"],
                    key=f"emg_side_{i}",
                )
                muscle = st.selectbox(
                    "근육",
                    EMG_MUSCLES,
                    key=f"emg_muscle_{i}",
                )

            with c2:
                custom_muscle = st.text_input(
                    "기타 근육명",
                    value="",
                    placeholder="기타 선택 시 입력",
                    key=f"emg_custom_muscle_{i}",
                )
                rest_state = st.selectbox(
                    "휴식 시 상태",
                    ["정상", "섬유자발전위/양성예파", "근육다발수축전위", "기타 이상"],
                    key=f"emg_rest_state_{i}",
                )

            c3, c4 = st.columns(2)

            with c3:
                volition_state = st.selectbox(
                    "수의수축 시 상태",
                    ["정상", "동원 감소", "운동단위전위 없음", "만성 신경원성 변화"],
                    key=f"emg_volition_state_{i}",
                )

            with c4:
                manual_nerve = st.text_input(
                    "말초신경/신경뿌리 메모",
                    value="",
                    placeholder="예: 노신경 C5-C6, 깊은종아리신경 L5",
                    key=f"emg_manual_nerve_{i}",
                )

            actual_muscle = custom_muscle if muscle == "기타" and custom_muscle else muscle
            mapped = EMG_MUSCLE_MAP.get(actual_muscle, {})

            rows.append(
                {
                    "type": "emg",
                    "side": side,
                    "muscle": actual_muscle,
                    "rest_state": rest_state,
                    "volition_state": volition_state,
                    "manual_nerve": manual_nerve,
                    "mapped_nerve": mapped.get("nerve", ""),
                    "roots": mapped.get("roots", []),
                    "tags": mapped.get("tags", []),
                    "item": f"{side} {actual_muscle} 침근전도검사",
                    "left": "",
                    "right": "",
                }
            )

    return rows


# =========================================================
# F파/H반사 입력
# =========================================================

def render_special_input():
    st.markdown("### 5단계. F파/H반사 입력")

    rows = []

    count = st.number_input(
        "F파/H반사 입력 행 수",
        min_value=0,
        max_value=6,
        value=2,
        step=1,
        key="special_row_count",
    )

    for i in range(int(count)):
        with st.expander(f"F파/H반사 {i + 1}", expanded=i == 0):
            c1, c2 = st.columns(2)

            with c1:
                test_name = st.selectbox(
                    "검사",
                    ["F파", "H반사"],
                    key=f"special_test_{i}",
                )
                side = st.selectbox(
                    "측",
                    ["미선택", "좌", "우", "양측"],
                    key=f"special_side_{i}",
                )

            with c2:
                response = st.selectbox(
                    "판독",
                    ["정상", "지연", "소실", "항진", "H/M 비율 증가"],
                    key=f"special_response_{i}",
                )
                latency = st.number_input(
                    "잠복기 (ms, 선택)",
                    min_value=0.0,
                    max_value=100.0,
                    value=0.0,
                    step=0.1,
                    key=f"special_latency_{i}",
                )

            rows.append(
                {
                    "type": "special",
                    "test_name": test_name,
                    "side": side,
                    "response": response,
                    "latency": latency,
                    "item": f"{side} {test_name}",
                    "left": "",
                    "right": "",
                }
            )

    return rows


# =========================================================
# 수치 → 이상 코드 추론
# =========================================================

def infer_codes_from_direct_input(region, sensory_rows, motor_rows, emg_rows, special_rows):
    codes = set()
    comments = []

    sensory_abnormal_count = 0
    motor_abnormal_count = 0
    emg_abnormal_count = 0

    sensory_reduced = False
    sensory_preserved = False
    motor_reduced = False
    motor_absent = False

    paraspinal_abnormal = False
    paraspinal_normal = False

    emg_tags_abnormal = []
    abnormal_nerves = set()
    abnormal_roots = set()

    # -----------------------------
    # 감각신경전도검사
    # -----------------------------
    for row in sensory_rows:
        response = row["response"]
        amp = row["amplitude"]
        latency = row["latency"]
        velocity = row["velocity"]
        nerve = row["nerve"]

        row_abnormal = False

        if response == "정상":
            sensory_preserved = True
            comments.append(f"{row['side']} {nerve} 감각신경활동전위가 정상으로 입력되었습니다.")

        elif response == "진폭 감소":
            codes.add("snap_reduced")
            sensory_reduced = True
            row_abnormal = True
            comments.append(f"{row['side']} {nerve} 감각 진폭 감소가 입력되었습니다.")

        elif response == "잠복기 지연":
            codes.add("sensory_latency_delayed")
            row_abnormal = True
            comments.append(f"{row['side']} {nerve} 감각 잠복기 지연이 입력되었습니다.")

        elif response == "전도속도 저하":
            codes.add("conduction_velocity_slow")
            row_abnormal = True
            comments.append(f"{row['side']} {nerve} 감각 전도속도 저하가 입력되었습니다.")

        elif response == "반응 소실":
            codes.add("snap_absent")
            codes.add("snap_reduced")
            sensory_reduced = True
            row_abnormal = True
            comments.append(f"{row['side']} {nerve} 감각 반응 소실이 입력되었습니다.")

        else:
            if amp > 0 and amp < EDU_CRITERIA["sensory_amp_low_uv"]:
                codes.add("snap_reduced")
                sensory_reduced = True
                row_abnormal = True
                comments.append(f"{row['side']} {nerve} 감각 진폭 {amp} μV는 교육용 기준상 낮습니다.")

            if latency > EDU_CRITERIA["sensory_latency_high_ms"]:
                codes.add("sensory_latency_delayed")
                row_abnormal = True
                comments.append(f"{row['side']} {nerve} 감각 잠복기 {latency} ms는 교육용 기준상 지연입니다.")

            if velocity > 0 and velocity < EDU_CRITERIA["sensory_velocity_low_ms"]:
                codes.add("conduction_velocity_slow")
                row_abnormal = True
                comments.append(f"{row['side']} {nerve} 감각 전도속도 {velocity} m/s는 교육용 기준상 낮습니다.")

            if not row_abnormal and (amp > 0 or latency > 0 or velocity > 0):
                sensory_preserved = True

        if row_abnormal:
            sensory_abnormal_count += 1

    if sensory_preserved and not sensory_reduced:
        codes.add("snap_preserved")

    if sensory_abnormal_count >= 2:
        codes.add("distal_symmetric_sensory")
        if region == "전신/양측":
            codes.add("distal_symmetric_pattern")

    # -----------------------------
    # 운동신경전도검사
    # -----------------------------
    for row in motor_rows:
        response = row["response"]
        amp = row["amplitude"]
        amp_unit = row["amp_unit"]
        latency = row["latency"]
        velocity = row["velocity"]
        nerve = row["nerve"]

        row_abnormal = False

        amp_mv = amp / 1000.0 if amp_unit == "μV" else amp

        if response == "정상":
            comments.append(f"{row['side']} {nerve} 운동반응이 정상으로 입력되었습니다.")

        elif response == "진폭 감소":
            codes.add("cmap_reduced")
            motor_reduced = True
            row_abnormal = True
            comments.append(f"{row['side']} {nerve} 운동 진폭 감소가 입력되었습니다.")

        elif response == "잠복기 지연":
            codes.add("motor_latency_delayed")
            row_abnormal = True
            comments.append(f"{row['side']} {nerve} 원위운동잠복기 지연이 입력되었습니다.")

        elif response == "전도속도 저하":
            codes.add("conduction_velocity_slow")
            row_abnormal = True
            comments.append(f"{row['side']} {nerve} 운동 전도속도 저하가 입력되었습니다.")

        elif response == "전도차단 의심":
            codes.add("conduction_block")
            row_abnormal = True
            comments.append(f"{row['side']} {nerve} 전도차단 의심 소견이 입력되었습니다.")

        elif response == "반응 소실":
            codes.add("cmap_absent")
            codes.add("cmap_reduced")
            motor_absent = True
            motor_reduced = True
            row_abnormal = True
            comments.append(f"{row['side']} {nerve} 운동 반응 소실이 입력되었습니다.")

        else:
            if amp_mv > 0 and amp_mv < EDU_CRITERIA["motor_amp_low_mv"]:
                codes.add("cmap_reduced")
                motor_reduced = True
                row_abnormal = True
                comments.append(f"{row['side']} {nerve} 운동 진폭 {amp_mv:.2f} mV는 교육용 기준상 낮습니다.")

            if latency > EDU_CRITERIA["motor_latency_high_ms"]:
                codes.add("motor_latency_delayed")
                row_abnormal = True
                comments.append(f"{row['side']} {nerve} 운동 잠복기 {latency} ms는 교육용 기준상 지연입니다.")

            if velocity > 0 and velocity < EDU_CRITERIA["motor_velocity_low_ms"]:
                codes.add("conduction_velocity_slow")
                row_abnormal = True
                comments.append(f"{row['side']} {nerve} 운동 전도속도 {velocity} m/s는 교육용 기준상 낮습니다.")

        if row_abnormal:
            motor_abnormal_count += 1
            abnormal_nerves.add(nerve)

            if "종아리" in nerve:
                codes.add("peroneal_neuropathy_pattern")
            if nerve == "정중신경":
                codes.add("median_wrist_pattern")
            if nerve == "자신경":
                codes.add("ulnar_elbow_pattern")
            if nerve == "노신경":
                codes.add("radial_neuropathy_pattern")

    if motor_absent:
        codes.add("cmap_absent")

    if motor_abnormal_count >= 2:
        codes.add("distal_symmetric_motor")
        if region == "전신/양측":
            codes.add("distal_symmetric_pattern")

    # -----------------------------
    # 침근전도검사
    # -----------------------------
    for row in emg_rows:
        muscle = row["muscle"]
        rest_state = row["rest_state"]
        volition_state = row["volition_state"]
        tags = row["tags"]
        roots = row["roots"]
        mapped_nerve = row["mapped_nerve"]

        is_rest_abnormal = rest_state in ["섬유자발전위/양성예파", "근육다발수축전위", "기타 이상"]
        is_volition_abnormal = volition_state in ["동원 감소", "운동단위전위 없음", "만성 신경원성 변화"]

        if is_rest_abnormal or is_volition_abnormal:
            emg_abnormal_count += 1
            emg_tags_abnormal.extend(tags)

            if mapped_nerve:
                abnormal_nerves.add(mapped_nerve)
            for root in roots:
                abnormal_roots.add(root)

            if "paraspinal" in tags:
                paraspinal_abnormal = True

            if rest_state == "섬유자발전위/양성예파":
                codes.add("fib_psw")
                comments.append(f"{row['side']} {muscle}에서 섬유자발전위/양성예파가 입력되었습니다.")

            if rest_state == "근육다발수축전위":
                codes.add("fasciculation")
                comments.append(f"{row['side']} {muscle}에서 근육다발수축전위가 입력되었습니다.")

            if volition_state == "동원 감소":
                codes.add("reduced_recruitment")
                comments.append(f"{row['side']} {muscle}에서 운동단위전위 동원 감소가 입력되었습니다.")

            if volition_state == "운동단위전위 없음":
                codes.add("no_muap")
                comments.append(f"{row['side']} {muscle}에서 수의수축 시 운동단위전위 없음이 입력되었습니다.")

            if volition_state == "만성 신경원성 변화":
                codes.add("chronic_neurogenic")
                comments.append(f"{row['side']} {muscle}에서 만성 신경원성 변화가 입력되었습니다.")

        else:
            if "paraspinal" in tags:
                paraspinal_normal = True

    if paraspinal_abnormal:
        codes.add("paraspinal_abnormal")
    elif paraspinal_normal:
        codes.add("paraspinal_normal")

    # 분절/근육 패턴
    if emg_tags_abnormal.count("c5_c6") >= 2:
        codes.add("c5_c6_muscle_pattern")

    if emg_tags_abnormal.count("c7") >= 1:
        codes.add("c7_muscle_pattern")

    if emg_tags_abnormal.count("c8_t1") >= 1:
        codes.add("c8_t1_muscle_pattern")

    if emg_tags_abnormal.count("l4") >= 1:
        codes.add("l4_pattern")

    if emg_tags_abnormal.count("l5") >= 2:
        codes.add("l5_pattern")

    if emg_tags_abnormal.count("s1") >= 2:
        codes.add("s1_pattern")

    if emg_tags_abnormal.count("peroneal") >= 2:
        codes.add("peroneal_neuropathy_pattern")

    if emg_tags_abnormal.count("plexus") >= 4:
        codes.add("lumbosacral_plexus_pattern")

    # 여러 신경/같은 뿌리 분포 판단
    if len(abnormal_nerves) >= 2:
        codes.add("multiple_peripheral_nerves")

    if len(abnormal_roots) >= 1 and len(abnormal_nerves) >= 2:
        codes.add("same_root_multiple_nerves")

    if len(abnormal_nerves) == 1 and emg_abnormal_count >= 1:
        codes.add("single_peripheral_nerve")

    # 신경뿌리 vs 신경얼기 힌트
    if paraspinal_abnormal and not sensory_reduced:
        codes.add("snap_preserved")
        comments.append("감각신경활동전위 보존과 척추주위근 이상 조합은 신경뿌리병증을 지지합니다.")

    if sensory_reduced and paraspinal_normal and len(abnormal_nerves) >= 2:
        codes.add("lumbosacral_plexus_pattern")
        comments.append("감각신경활동전위 감소, 여러 말초신경 영역 침범, 척추주위근 보존은 신경얼기병증을 시사합니다.")

    # -----------------------------
    # F파/H반사
    # -----------------------------
    for row in special_rows:
        test_name = row["test_name"]
        response = row["response"]

        if test_name == "F파" and response in ["지연", "소실"]:
            codes.add("f_wave_delayed_absent")
            comments.append("F파 지연 또는 소실이 입력되었습니다.")

        if test_name == "H반사" and response in ["지연", "소실"]:
            codes.add("h_reflex_delayed_absent")
            comments.append("H반사 지연 또는 소실이 입력되었습니다.")

        if test_name == "H반사" and response in ["항진", "H/M 비율 증가"]:
            codes.add("h_reflex_hyperactive")
            comments.append("H반사 항진 또는 H/M 비율 증가가 입력되었습니다.")

    # -----------------------------
    # 부위 기반 보정
    # -----------------------------
    if region == "전신/양측" and sensory_abnormal_count >= 2 and motor_abnormal_count >= 1:
        codes.add("distal_symmetric_pattern")

    if region == "뇌졸중 후 경직":
        if "h_reflex_hyperactive" in codes:
            comments.append("뇌졸중 후 경직 문맥에서 H반사 항진은 중추성 반사 흥분성 증가와 연결됩니다.")

    return list(codes), comments


# =========================================================
# 결과 출력
# =========================================================

def render_direct_results(region, selected_codes, detail_comments):
    st.markdown("### 6단계. 자동 해석 결과")

    if not selected_codes:
        st.info("수치를 입력한 뒤 `수치 기반 자동 해석`을 누르면 결과가 표시됩니다.")
        return

    with st.expander("수치에서 추출된 이상 소견 코드", expanded=False):
        for code in selected_codes:
            st.code(code)

    st.markdown("#### 입력 수치 기반 해석 요약")

    if detail_comments:
        for comment in detail_comments:
            st.markdown(f"- {ko(comment)}")
    else:
        st.markdown("- 뚜렷한 이상 소견이 자동 추출되지 않았습니다.")

    pattern_comments = summarize_pattern(selected_codes)

    if pattern_comments:
        st.markdown("#### 핵심 패턴")
        for comment in pattern_comments:
            st.markdown(f"- {ko(comment)}")

    results = interpret_findings(selected_codes, selected_region=region)

    st.markdown("#### 가능성 순위")

    if not results:
        st.warning("현재 입력만으로는 뚜렷한 질환군을 추론하기 어렵습니다. 감각신경전도검사, 운동신경전도검사, 침근전도검사를 더 입력해 보세요.")
        return

    for idx, result in enumerate(results, start=1):
        render_direct_result_card(result, idx)

    render_image_based_learning_notes(selected_codes)


def render_direct_result_card(result, rank):
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
                    {rank}. {ko(result["name"])}
                </div>
                <div style="font-size:0.82rem; font-weight:800; color:white; background:{color}; padding:4px 8px; border-radius:999px;">
                    {badge}
                </div>
            </div>
            <div style="margin-top:8px; color:#334155; font-size:0.95rem;">
                <b>추정 병변 위치:</b> {ko(result["lesion"])}
            </div>
            <div style="margin-top:4px; color:#334155; font-size:0.95rem;">
                <b>교육용 일치도:</b> {confidence}%
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.expander("해석 근거", expanded=True):
        for line in result["teaching"]:
            st.markdown(f"- {ko(line)}")

    with st.expander("물리치료 평가 포인트", expanded=False):
        for line in result["pt_points"]:
            st.markdown(f"- {ko(line)}")

    with st.expander("감별진단", expanded=False):
        for item in result["differentials"]:
            st.markdown(f"- {ko(item)}")


def render_image_based_learning_notes(selected_codes):
    st.markdown("#### 결과표 읽기 학습 포인트")

    selected_codes = set(selected_codes)

    if "c5_c6_muscle_pattern" in selected_codes and "paraspinal_abnormal" in selected_codes:
        st.success(
            "정중신경 감각/운동 반응이 보존되고, 목 척추주위근과 C5-C6 관련 근육에서 탈신경 소견이 있으면 C5-C6 목 신경뿌리병증 패턴을 우선 생각합니다."
        )

    if "lumbosacral_plexus_pattern" in selected_codes and "paraspinal_normal" in selected_codes:
        st.success(
            "다리의 여러 말초신경 영역 근육이 침범되고 감각신경활동전위가 감소하지만 허리 척추주위근이 정상이라면 허리엉치신경얼기병증 패턴을 고려합니다."
        )

    if "peroneal_neuropathy_pattern" in selected_codes:
        st.info(
            "발처짐에서 온종아리신경병증을 의심할 때는 발목관절 등굽힘과 가쪽번짐 약화, 발목관절 안쪽번짐 보존 여부를 함께 확인하세요."
        )

    if "snap_preserved" in selected_codes and "paraspinal_abnormal" in selected_codes:
        st.info(
            "감각신경활동전위 보존과 척추주위근 이상은 신경뿌리병증을 지지하는 조합입니다."
        )

    if "snap_reduced" in selected_codes and "paraspinal_normal" in selected_codes:
        st.info(
            "감각신경활동전위 감소와 척추주위근 보존은 신경뿌리보다 신경얼기 또는 말초신경 수준 병변을 더 의심하게 합니다."
        )
