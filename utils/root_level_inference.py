"""
근전도 결과표 예제의 침근전도 소견을 바탕으로 신경뿌리 레벨을 교육용으로 점수화하는 유틸리티.

주의
- 실제 임상 진단 알고리즘이 아니라 교육용 추론 보조 도구입니다.
- 최종 진단은 임상 증상, 이학적 검사, 영상, 검사실 정상범위, 전문의 판독을 종합해야 합니다.
"""


ROOT_ORDER = [
    "C4", "C5", "C6", "C7", "C8", "T1",
    "L3", "L4", "L5", "S1", "S2",
]


MUSCLE_ROOT_WEIGHTS = {
    # 목/팔
    "목 척추주위근": {"C4": 1, "C5": 1, "C6": 1, "C7": 1, "C8": 1, "T1": 1},
    "어깨올림근": {"C3": 1, "C4": 2, "C5": 1},
    "등세모근": {"C3": 1, "C4": 1},
    "삼각근": {"C5": 2, "C6": 1},
    "가시위근": {"C5": 2, "C6": 1},
    "가시밑근": {"C5": 2, "C6": 1},
    "위팔두갈래근": {"C5": 1, "C6": 2},
    "위팔노근": {"C6": 3},
    "노쪽손목폄근": {"C6": 2, "C7": 1},
    "위팔세갈래근": {"C7": 3},
    "손가락폄근": {"C7": 2, "C8": 1},
    "노쪽손목굽힘근": {"C6": 1, "C7": 2},
    "긴엄지굽힘근": {"C8": 2, "T1": 1},
    "짧은엄지벌림근": {"C8": 1, "T1": 2},
    "첫째등쪽뼈사이근": {"C8": 1, "T1": 2},
    "새끼벌림근": {"C8": 1, "T1": 2},

    # 허리/다리
    "허리 척추주위근": {"L3": 1, "L4": 1, "L5": 1, "S1": 1},
    "엉덩허리근": {"L2": 1, "L3": 2, "L4": 1},
    "가쪽넓은근": {"L3": 1, "L4": 2},
    "안쪽넓은근": {"L3": 1, "L4": 2},
    "넙다리곧은근": {"L3": 1, "L4": 2},
    "앞정강근": {"L4": 1, "L5": 3},
    "긴엄지폄근": {"L5": 3},
    "중간볼기근": {"L5": 2, "S1": 1},
    "긴종아리근": {"L5": 2, "S1": 1},
    "뒤정강근": {"L5": 2, "S1": 1},
    "큰볼기근": {"L5": 1, "S1": 2, "S2": 1},
    "뒤넓적다리근": {"L5": 1, "S1": 2, "S2": 1},
    "장딴지근": {"S1": 2, "S2": 1},
    "가자미근": {"S1": 2, "S2": 1},
    "항문조임근": {"S2": 2, "S3": 2, "S4": 1},
}


ABNORMAL_STATES = [
    "섬유자발전위/양성예파",
    "섬유자발전위",
    "양성예파",
    "동원 감소",
    "운동단위전위 없음",
    "만성 신경원성 변화",
    "근육다발수축전위",
    "이상",
]


NORMAL_STATES = [
    "정상",
    "휴식 시 전기적 침묵",
    "silent at rest",
    "normal",
]


def is_abnormal_state(state):
    if not state:
        return False

    lowered = str(state).lower()

    for keyword in ABNORMAL_STATES:
        if keyword.lower() in lowered:
            return True

    if "fibrillation" in lowered:
        return True
    if "positive sharp" in lowered:
        return True
    if "no muap" in lowered:
        return True
    if "reduced recruitment" in lowered:
        return True
    if "chronic neurogenic" in lowered:
        return True

    return False


def is_normal_state(state):
    if not state:
        return False

    lowered = str(state).lower()

    for keyword in NORMAL_STATES:
        if keyword.lower() in lowered:
            return True

    return False


def infer_root_scores_from_emg(needle_emg):
    """
    needle_emg 예제 데이터에서 이상 근육을 찾아 신경뿌리 점수를 계산합니다.
    """
    scores = {root: 0 for root in ROOT_ORDER}
    abnormal_muscles = []
    normal_muscles = []

    for row in needle_emg:
        muscle = row.get("muscle", "")
        state = row.get("state", "")

        weights = MUSCLE_ROOT_WEIGHTS.get(muscle, {})

        if is_abnormal_state(state):
            abnormal_muscles.append(muscle)
            for root, weight in weights.items():
                if root not in scores:
                    scores[root] = 0
                scores[root] += weight

        elif is_normal_state(state):
            normal_muscles.append(muscle)

    # 정상 근육은 해당 레벨 가능성을 약간 낮춥니다.
    # 단, 과도한 감점은 피합니다.
    for muscle in normal_muscles:
        weights = MUSCLE_ROOT_WEIGHTS.get(muscle, {})
        for root, weight in weights.items():
            if root in scores and scores[root] > 0:
                scores[root] = max(0, scores[root] - 0.5)

    return scores, abnormal_muscles, normal_muscles


def summarize_top_roots(scores, limit=3):
    sorted_items = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    sorted_items = [(root, score) for root, score in sorted_items if score > 0]
    return sorted_items[:limit]


def root_score_to_percent(scores):
    max_score = max(scores.values()) if scores else 0

    if max_score <= 0:
        return {root: 0 for root in scores}

    return {
        root: int(round((score / max_score) * 100))
        for root, score in scores.items()
    }


def infer_lesion_hint(report):
    """
    감각신경활동전위와 척추주위근 소견을 조합해
    신경뿌리병증/신경얼기병증/말초신경병증 힌트를 생성합니다.
    """
    sensory_rows = report.get("sensory_ncs", [])
    needle_rows = report.get("needle_emg", [])

    sensory_reduced = False
    sensory_preserved = False
    paraspinal_abnormal = False
    paraspinal_normal = False

    for row in sensory_rows:
        interpretation = str(row.get("interpretation", "")).lower()
        amp_text = str(row.get("amplitude", "")).lower()

        if "reduced" in interpretation or "감소" in interpretation or "low" in interpretation:
            sensory_reduced = True
        elif "normal" in interpretation or "정상" in interpretation or "보존" in interpretation:
            sensory_preserved = True

        if "no response" in interpretation or "소실" in interpretation:
            sensory_reduced = True

    for row in needle_rows:
        muscle = row.get("muscle", "")
        state = row.get("state", "")

        if "척추주위근" in muscle:
            if is_abnormal_state(state):
                paraspinal_abnormal = True
            elif is_normal_state(state):
                paraspinal_normal = True

    if sensory_preserved and paraspinal_abnormal:
        return "감각신경활동전위 보존 + 척추주위근 이상 → 신경뿌리병증을 지지합니다."

    if sensory_reduced and paraspinal_normal:
        return "감각신경활동전위 감소 + 척추주위근 보존 → 신경얼기병증 또는 말초신경병증을 더 의심합니다."

    if sensory_reduced:
        return "감각신경활동전위 감소 → 병변이 뒤뿌리신경절보다 원위부일 가능성을 고려합니다."

    if paraspinal_abnormal:
        return "척추주위근 이상 → 신경뿌리병증 가능성을 고려합니다."

    return "신경전도검사와 침근전도검사 패턴을 함께 해석해야 합니다."
