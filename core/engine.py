# engine.py
from collections import defaultdict
from datetime import datetime
from app_data import ANATOMY, SECTIONS

# ==========================================
# UI 및 분석 보조 함수
# ==========================================

def get_side_labels(side):
    """선택된 병변측을 바탕으로 UI 라벨을 반환합니다."""
    if side == "좌":
        return {"normal_side": "우측", "lesion_side": "좌측"}
    if side == "우":
        return {"normal_side": "좌측", "lesion_side": "우측"}
    return {"normal_side": "반대측", "lesion_side": "병변측"}

def get_domain_options(domain, item=None):
    """신경, 근육, 반사 등 각 도메인에 맞는 정확한 선택지만 제공합니다."""
    if domain in ["sensory", "motor"]:
        return ["정상 (Normal)", "감소 (Reduced)", "잠복기 지연 (Delayed latency)", "무반응 (No response)"]
    if domain == "muscle":
        return ["정상 (Normal)", "비정상 자발전위 출현 (Abnormal spontaneous activity)"]
    if domain == "reflex":
        if item in ["H 반사 (좌)", "H 반사 (우)"]:
            return ["정상 (Normal)", "지연 또는 소실 (Delayed/Absent)", "항진 또는 역치 감소 (Hyperactive / lower threshold)"]
        if item == "H/M 비율":
            return ["정상 (Normal)", "증가 가능 (May be increased)"]
        if item == "좌우 비교":
            return ["정상 (Normal)", "병변측 H 반사 흥분성 증가 가능"]
        # Blink reflex defaults
        return ["정상 (Normal)", "지연 (Delayed)", "지연 또는 소실 (Delayed/Absent)", "양측 지연 또는 소실 (Bilateral delayed/absent)"]
    return ["정상 (Normal)"]

def is_abnormal(value):
    """문자열의 대소문자 차이를 극복하고 비정상 여부를 판별합니다."""
    if value is None:
        return False
    value = str(value).strip().lower()
    if value == "" or value == "미선택":
        return False

    normal_aliases = {
        "정상",
        "normal",
        "정상 (normal)",
        "정상 (normal)"
    }
    return value not in {x.lower() for x in normal_aliases}

def summarize_status(left, right, side="미선택"):
    """결과 출력 시 좌/우 구분을 명확히 해줍니다."""
    if str(right).strip() == "":
        return f"결과: {left}"
    if side == "양측":
        return f"좌측: {left} / 우측: {right}"
    if side == "좌":
        return f"좌측(병변측): {left} / 우측(정상측): {right}"
    if side == "우":
        return f"좌측(정상측): {left} / 우측(병변측): {right}"
    return f"좌측: {left} / 우측: {right}"

def severity_text(total_abnormal, no_response_count):
    if no_response_count >= 2 or total_abnormal >= 6:
        return "중등도 이상"
    if total_abnormal >= 3:
        return "경도-중등도"
    if total_abnormal >= 1:
        return "경도"
    return "뚜렷한 이상 없음"

def infer_numeric_status(domain, normal_amp, lesion_amp, normal_latency, lesion_latency, spontaneous=False):
    """수치형 입력 시 규칙 기반으로 자동 판정합니다."""
    if domain in ["sensory", "motor"]:
        if lesion_amp == 0:
            return "무반응 (No response)"
        if normal_latency > 0 and lesion_latency >= normal_latency * 1.2:
            return "잠복기 지연 (Delayed latency)"
        if normal_amp > 0 and lesion_amp <= normal_amp * 0.6:
            return "감소 (Reduced)"
        return "정상 (Normal)"
    if spontaneous:
        return "비정상 자발전위 출현 (Abnormal spontaneous activity)"
    return "정상 (Normal)"

def find_section_for_item(item_name):
    for section, items in SECTIONS.items():
        if item_name in items:
            return section
    return None

# ==========================================
# 규칙 엔진 (Rule-based Analysis Engine)
# ==========================================
def analyze_case(age, sex, side, selected_rows):
    scores = defaultdict(int)
    reasons = []
    suggestions = set()
    lesion_tags = set()
    involved_nerves = set()
    involved_levels = set()

    sensory_abnormal = 0
    motor_abnormal = 0
    muscle_abnormal = 0
    reflex_abnormal = 0
    paraspinal_abnormal = 0
    no_response_count = 0
    delayed_count = 0
    reduced_count = 0
    spontaneous_count = 0

    arm_abnormal = 0
    leg_abnormal = 0
    face_abnormal = 0

    median_related = 0
    ulnar_related = 0
    radial_related = 0
    peroneal_related = 0
    tibial_related = 0
    femoral_related = 0
    arm_plexus_hint = 0
    leg_plexus_hint = 0
    neck_root_hint = 0
    low_back_root_hint = 0

    blink_r1_abnormal = 0
    blink_r2_abnormal = 0
    blink_right_stim_abnormal = 0
    blink_left_stim_abnormal = 0

    abnormal_items = []

    for row in selected_rows:
        left = row["left"]
        right = row["right"]

        if not (is_abnormal(left) or is_abnormal(right)):
            continue

        item = row["item"]
        if item not in ANATOMY:
            continue

        a = ANATOMY[item]

        involved_nerves.add(a["nerve"])
        involved_levels.add(a["level"])

        if a["region"] == "arm":
            arm_abnormal += 1
        elif a["region"] == "leg":
            leg_abnormal += 1
        elif a["region"] == "face":
            face_abnormal += 1

        if a["domain"] == "sensory":
            sensory_abnormal += 1
        elif a["domain"] == "motor":
            motor_abnormal += 1
        elif a["domain"] == "muscle":
            muscle_abnormal += 1
        elif a["domain"] == "reflex":
            reflex_abnormal += 1

        if "척추주위근" in item:
            paraspinal_abnormal += 1

        vals = [str(left).lower(), str(right).lower()]
        if any("감소" in v or "reduced" in v for v in vals):
            reduced_count += 1
        if any("지연" in v or "delayed" in v for v in vals):
            delayed_count += 1
        if any("무반응" in v or "no response" in v for v in vals):
            no_response_count += 1
        if any("자발전위" in v or "spontaneous" in v for v in vals):
            spontaneous_count += 1

        if "정중신경" in item or "짧은엄지벌림근" in item:
            median_related += 1
        if "자신경" in item or "첫째등쪽뼈사이근" in item or "새끼벌림근" in item:
            ulnar_related += 1
        if "노신경" in item or "뒤뼈사이신경" in item or "집게폄근" in item or "손목폄근" in item or "위팔세갈래근" in item:
            radial_related += 1
        if "종아리신경" in item or "앞정강근" in item or "짧은발가락폄근" in item or "긴종아리근" in item or "깊은종아리신경" in item:
            peroneal_related += 1
        if "정강신경" in item or "장딴지근" in item or "가자미근" in item:
            tibial_related += 1
        if "넙다리신경" in item or "가쪽넓은근" in item or "엉덩허리근" in item:
            femoral_related += 1
        if "가쪽아래팔피부신경" in item or "겨드랑신경" in item or "근피신경" in item:
            arm_plexus_hint += 1
        if "중간볼기근" in item or "큰볼기근" in item or "뒤넙다리근" in item:
            leg_plexus_hint += 1
        if "목 척추주위근" in item:
            neck_root_hint += 1
        if "허리 척추주위근" in item:
            low_back_root_hint += 1

        if item in ["우측 자극 R1", "좌측 자극 R1"]:
            blink_r1_abnormal += 1
        if item in ["우측 자극 R2", "좌측 자극 R2"]:
            blink_r2_abnormal += 1
        if item.startswith("우측 자극"):
            blink_right_stim_abnormal += 1
        if item.startswith("좌측 자극"):
            blink_left_stim_abnormal += 1

        abnormal_items.append({
            "항목": item,
            "신경": a["nerve"],
            "레벨": a["level"],
            "결과": summarize_status(row["left"], row["right"], side)
        })

    total_abnormal = sensory_abnormal + motor_abnormal + muscle_abnormal + reflex_abnormal

    # 신경뿌리병증
    if sensory_abnormal == 0 and muscle_abnormal >= 2 and neck_root_hint >= 1:
        scores["목 신경뿌리병증 (Cervical Radiculopathy)"] += 10
        lesion_tags.add("신경뿌리 수준 (Root level)")
        reasons.append("감각신경 보존과 목 척추주위근 침범이 함께 보여 목 신경뿌리병증 가능성이 높습니다.")
        suggestions.add("목 자기공명영상(MRI)을 고려하세요.")

    if sensory_abnormal == 0 and muscle_abnormal >= 2 and low_back_root_hint >= 1:
        scores["허리 신경뿌리병증 (Lumbar Radiculopathy)"] += 10
        lesion_tags.add("신경뿌리 수준 (Root level)")
        reasons.append("감각신경 보존과 허리 척추주위근 침범이 함께 보여 허리 신경뿌리병증 가능성이 높습니다.")
        suggestions.add("허리 자기공명영상(MRI)을 고려하세요.")

    # 신경얼기병증
    if sensory_abnormal >= 1 and muscle_abnormal >= 2 and paraspinal_abnormal == 0 and arm_plexus_hint >= 1:
        scores["팔신경얼기병증 (Brachial Plexopathy)"] += 9
        lesion_tags.add("신경얼기 수준 (Plexus level)")
        reasons.append("감각 이상과 다발성 근육 이상이 있으나 척추주위근이 정상이어 팔신경얼기병증 가능성이 있습니다.")

    if sensory_abnormal >= 1 and muscle_abnormal >= 2 and paraspinal_abnormal == 0 and leg_plexus_hint >= 1:
        scores["허리엉치신경얼기병증 (Lumbosacral Plexopathy)"] += 9
        lesion_tags.add("신경얼기 수준 (Plexus level)")
        reasons.append("감각 이상과 다발성 근육 이상이 있으나 척추주위근이 정상이어 허리엉치신경얼기병증 가능성이 있습니다.")

    # 단일신경병증
    if median_related >= 2 and arm_abnormal <= 5:
        scores["정중신경병증/포착신경병증 (Median Neuropathy/Entrapment)"] += 8
        lesion_tags.add("단일 말초신경 수준 (Single peripheral nerve level)")
        reasons.append("정중신경 분포에 이상이 국한되어 정중신경병증 가능성이 높습니다.")
        suggestions.add("손목굴 증후군 감별을 위해 국소 초음파 평가를 고려하세요.")

    if ulnar_related >= 2 and arm_abnormal <= 5:
        scores["자신경병증/포착신경병증 (Ulnar Neuropathy)"] += 8
        lesion_tags.add("단일 말초신경 수준 (Single peripheral nerve level)")
        reasons.append("자신경 분포에 이상이 국한되어 자신경병증 가능성이 높습니다.")

    if radial_related >= 2 and arm_abnormal <= 5:
        scores["노신경병증 (Radial Neuropathy)"] += 6
        lesion_tags.add("단일 말초신경 수준 (Single peripheral nerve level)")
        reasons.append("노신경 분포 이상이 우세하여 노신경병증 가능성이 있습니다.")

    if peroneal_related >= 2 and leg_abnormal <= 6:
        scores["종아리신경병증/포착신경병증 (Peroneal Neuropathy)"] += 9
        lesion_tags.add("단일 말초신경 수준 (Single peripheral nerve level)")
        reasons.append("종아리신경 분포 이상이 뚜렷하여 종아리신경병증 가능성이 높습니다.")
        suggestions.add("종아리뼈 머리 부위 초음파 평가를 고려하세요.")

    if tibial_related >= 2 and leg_abnormal <= 6:
        scores["정강신경병증 (Tibial Neuropathy)"] += 6
        lesion_tags.add("단일 말초신경 수준")
        reasons.append("정강신경 분포 이상이 우세합니다.")

    # 다발신경병증
    if sensory_abnormal >= 3 and motor_abnormal >= 2:
        scores["다발신경병증 (Polyneuropathy)"] += 10
        lesion_tags.add("다발 말초신경 수준 (Multiple peripheral nerves)")
        reasons.append("여러 감각/운동 신경 이상이 양측성으로 보여 다발신경병증 양상입니다.")
        suggestions.add("혈당, 비타민 B12 등 대사/내분비 검사를 고려하세요.")

    if delayed_count >= 3 or no_response_count >= 2:
        scores["말이집탈락성 다발신경병증 (Demyelinating Polyneuropathy)"] += 6
        lesion_tags.add("말이집탈락성 (Demyelinating)")
        reasons.append("잠복기 지연 소견이 두드러져 말이집탈락성 병변 가능성이 높습니다.")

    # 운동신경세포질환
    if muscle_abnormal >= 4 and sensory_abnormal == 0 and spontaneous_count >= 2:
        scores["운동신경세포질환 (Motor Neuron Disease)"] += 8
        lesion_tags.add("운동신경세포 수준 (Motor neuron level)")
        reasons.append("감각신경은 완전히 보존되면서 다발성 근육에 활성 탈신경 전위가 보여 운동신경세포질환을 강하게 시사합니다.")

    # 반사 검사
    h_reflex_abnormal = 0
    h_reflex_hyperactive = 0
    for row in selected_rows:
        vals = [str(row["left"]).lower(), str(row["right"]).lower()]
        if row["item"] in ["H 반사 (좌)", "H 반사 (우)"]:
            if any("지연" in v or "absent" in v for v in vals):
                h_reflex_abnormal += 1
            if any("항진" in v or "hyperactive" in v for v in vals):
                h_reflex_hyperactive += 1

    if h_reflex_abnormal >= 1 and tibial_related >= 1:
        scores["S1 신경뿌리병증 (S1 radiculopathy)"] += 8
        reasons.append("H 반사 지연/소실이 S1 신경뿌리병증을 시사합니다.")

    if h_reflex_hyperactive >= 1:
        scores["중추성 경직 / 상위운동신경원 병변 (Spasticity / UMN Lesion)"] += 8
        lesion_tags.add("척수 반사 흥분성 증가")
        reasons.append("H 반사 항진은 뇌졸중 등 상위운동신경원 병변 후 척수반사 흥분성 증가를 의미합니다.")

    if blink_right_stim_abnormal >= 1 and blink_left_stim_abnormal >= 1:
        scores["뇌줄기 반사경로 병변 (Brainstem Lesion)"] += 8
        lesion_tags.add("뇌신경 반사경로 수준 (Brainstem)")
        reasons.append("양측성 눈깜빡반사 이상은 뇌줄기 병변을 시사합니다.")

    severity = severity_text(total_abnormal, no_response_count)

    if not scores:
        scores["비특이적 이상 또는 추가 평가 필요 (Nonspecific / Further evaluation needed)"] = 1
        reasons.append("현재 선택된 정보만으로는 특정 질환을 명확히 분류하기 어렵습니다.")

    top3 = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:3]

    return {
        "age": age,
        "sex": sex,
        "side": side,
        "final_dx": top3[0][0],
        "top3": top3,
        "severity": severity,
        "lesion_tags": sorted(lesion_tags),
        "reasons": reasons,
        "suggestions": sorted(suggestions),
        "involved_nerves": ", ".join(sorted(involved_nerves)) if involved_nerves else "특이 소견 없음",
        "involved_levels": ", ".join(sorted(involved_levels)) if involved_levels else "특이 소견 없음",
        "abnormal_items": abnormal_items,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

def make_report_text(result):
    lines = []
    lines.append("교육용 근전도 판독 보조 결과")
    lines.append("=" * 50)
    lines.append(f"생성 시각: {result.get('created_at', '')}")
    lines.append(f"최종 유력 진단: {result.get('final_dx', '')}")
    lines.append(f"손상 의심 신경: {result.get('involved_nerves', '')}")
    lines.append(f"신경학적 레벨/분절: {result.get('involved_levels', '')}")
    lines.append(f"중증도: {result.get('severity', '')}")
    lines.append("")

    lines.append("[Top 3 감별진단]")
    for i, (dx, score) in enumerate(result.get("top3", []), 1):
        lines.append(f"{i}. {dx}")
    lines.append("")

    lines.append("[판단 근거]")
    for reason in result.get("reasons", []):
        lines.append(f"- {reason}")
    lines.append("")

    lines.append("[이상 항목 요약]")
    for item in result.get("abnormal_items", []):
        lines.append(f"- {item['항목']} | {item['결과']}")
    lines.append("")
    lines.append("※ 본 결과는 학생 교육용 참고 자료이며 실제 임상 진단을 대체하지 않습니다.")
    return "\n".join(lines)