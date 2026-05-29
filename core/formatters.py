def normalize_result_text(value):
    """
    화면 표시용 결과 문구 정규화.
    학생이 보기에 같은 의미의 표현이 하나로 보이도록 통일한다.
    """
    if value is None:
        return ""

    text = str(value).strip()

    mapping = {
        "정상 (Normal)": "정상 범위",
        "정상": "정상 범위",
        "정상 범위(within normal limits)": "정상 범위",
        "정상 범위 (within normal limits)": "정상 범위",
        "within normal limits": "정상 범위",
        "감소 (Reduced)": "진폭 감소",
        "감소": "진폭 감소",
        "진폭 감소(reduced amplitude)": "진폭 감소",
        "진폭 감소 (reduced amplitude)": "진폭 감소",
        "reduced amplitude": "진폭 감소",
        "잠복기 지연 (Delayed latency)": "잠복기 지연",
        "잠복기 지연": "잠복기 지연",
        "잠복기 지연(delayed latency)": "잠복기 지연",
        "잠복기 지연 (delayed latency)": "잠복기 지연",
        "delayed latency": "잠복기 지연",
        "무반응 (No response)": "무반응",
        "무반응": "무반응",
        "반응 소실(absent response)": "무반응",
        "반응 소실 (absent response)": "무반응",
        "absent response": "무반응",
        "비정상 자발전위 출현 (Fibrillation Potential, Positive Sharp Wave 등)": "비정상 자발전위",
        "비정상 자발전위 (Fibrillation, Positive sharp wave 등) 출현": "비정상 자발전위",
        "비정상 자발전위 출현": "비정상 자발전위",
        "휴식 시 섬유자발전위(fibrillation potential) 및 양성예파(positive sharp wave) 관찰, 수의수축 시 운동단위전위(MUAP) 동원 감소 가능": "비정상 자발전위",
        "휴식 시 섬유자발전위(fibrillation potential) 및 양성예파(positive sharp wave) 관찰": "비정상 자발전위",
        "휴식 시 전기적 침묵(no motor unit action potential, MUAP), 수의수축 시 정상 운동단위전위(MUAP) 동원": "정상 범위",
        "무반응 / 전기적 침묵 (Electrical silence)": "무반응/전기적 침묵",
        "지연 또는 소실 (Delayed/Absent)": "지연 또는 소실",
        "지연 또는 소실": "지연 또는 소실",
        "F파 최소잠복기 지연 또는 소실(delayed or absent F-wave)": "지연 또는 소실",
        "항진 또는 문턱값 감소 (Hyperactive / lower threshold)": "항진 또는 문턱값 감소",
        "H-반사 항진 또는 문턱값 감소(hyperactive H-reflex / lower threshold)": "항진 또는 문턱값 감소",
        "증가 가능 (May be increased)": "증가 가능",
        "H/M 비율 증가 가능(increased H/M ratio possible)": "증가 가능",
        "지연 (Delayed)": "지연",
        "소실 (Absent)": "소실",
        "잠복기 지연 또는 반응 소실(delayed or absent response)": "지연 또는 소실",
    }

    if text in mapping:
        return mapping[text]

    lowered = text.lower()

    if "within normal limits" in lowered:
        return "정상 범위"
    if "reduced amplitude" in lowered:
        return "진폭 감소"
    if "delayed latency" in lowered:
        return "잠복기 지연"
    if "absent response" in lowered:
        return "무반응"
    if "delayed or absent" in lowered:
        return "지연 또는 소실"
    if "fibrillation" in lowered or "positive sharp wave" in lowered:
        return "비정상 자발전위"

    return text


def is_abnormal_result(value):
    """
    결과값이 이상 소견인지 판단.
    화면 색상, 보고서 요약 등에 사용.
    """
    text = normalize_result_text(value)

    abnormal_keywords = [
        "감소",
        "진폭 감소",
        "잠복기 지연",
        "지연",
        "소실",
        "무반응",
        "비정상",
        "자발전위",
        "항진",
        "문턱값 감소",
        "증가 가능",
        "전도차단",
    ]

    normal_keywords = [
        "정상 범위",
        "전기적 침묵",
        "정상 운동단위",
    ]

    if any(k in text for k in abnormal_keywords):
        return True

    if any(k in text for k in normal_keywords):
        return False

    return False


def educational_result_text(value, domain=None, item_name=""):
    """
    검사 영역별 학생 교육용 결과 문구.
    결과 카드에는 검사결과만 간단히 보이도록 통일한다.
    """
    raw = "" if value is None else str(value).strip()
    simple = normalize_result_text(raw)
    domain = domain or ""
    item_name = item_name or ""

    if domain == "muscle":
        if "정상" in raw or "Normal" in raw or simple == "정상 범위":
            return "정상 범위"

        if (
            "비정상 자발전위" in raw
            or "Fibrillation" in raw
            or "fibrillation" in raw
            or "Positive Sharp" in raw
            or "positive sharp" in raw
            or simple == "비정상 자발전위"
        ):
            return "비정상 자발전위"

        if "Fasciculation" in raw or "근육다발" in raw:
            return "근육다발수축전위"

        return simple

    if domain in ["sensory", "motor"]:
        if simple == "정상 범위":
            return "정상 범위"
        if simple == "잠복기 지연":
            return "잠복기 지연"
        if simple == "진폭 감소":
            return "진폭 감소"
        if simple == "무반응":
            return "무반응"
        return simple

    if domain == "f_wave":
        if simple == "정상 범위":
            return "정상 범위"
        if simple == "지연 또는 소실":
            return "지연 또는 소실"
        if simple == "지연":
            return "지연"
        if simple == "소실":
            return "소실"
        return simple

    if domain in ["h_reflex", "h_ratio"]:
        return simple

    if domain == "blink":
        return simple

    return simple


def get_domain_reference(domain, item_name=""):
    """
    검사 영역별 학생 교육용 참고 기준.
    실제 절대 정상값은 검사실마다 다르므로 교육용 예시로 제공한다.
    """
    domain = domain or ""
    item_name = item_name or ""

    common_note = (
        "주의: 아래 수치는 학생 교육용의 대략적 예시입니다. 실제 정상값과 이상 판정 기준은 "
        "장비, 검사실 기준, 피부온도, 나이, 키, 사지 길이, 자극/기록 위치에 따라 달라질 수 있습니다."
    )

    if domain == "sensory":
        return {
            "title": "감각신경전도검사(Sensory NCS, SNAP) 참고",
            "normal": "원위잠복기, 감각신경활동전위(SNAP) 진폭, 전도속도가 해당 검사실 정상범위 내",
            "abnormal": "잠복기 지연(비교측보다 약 10% 이상 느리거나 검사실 정상범위 초과), 진폭 감소(비교측보다 약 20~50% 이상 낮음), 무반응",
            "note": common_note,
        }

    if domain == "motor":
        return {
            "title": "운동신경전도검사(Motor NCS, CMAP) 참고",
            "normal": "원위잠복기, 복합근육활동전위(CMAP) 진폭, 전도속도가 해당 검사실 정상범위 내",
            "abnormal": "잠복기 지연(비교측보다 약 10% 이상 느리거나 검사실 정상범위 초과), 진폭 감소(비교측보다 약 20~50% 이상 낮음), 무반응",
            "note": common_note,
        }

    if domain == "muscle":
        return {
            "title": "침근전도검사(Needle EMG) 참고",
            "normal": "휴식 시 전기적 침묵, 수의수축 시 정상 운동단위전위(MUAP)와 정상 동원",
            "abnormal": "비정상 자발전위 출현(섬유자발전위, 양성예파 등), 동원 감소, 신경원성 운동단위전위 변화",
            "note": "침근전도검사는 삽입활동, 휴식 시 자발전위, 수의수축 시 운동단위전위(MUAP)와 동원 양상을 구분해 해석합니다.",
        }

    if domain == "f_wave":
        return {
            "title": "F파(F-wave) 참고",
            "normal": "F파 최소잠복기와 출현 빈도가 키/사지 길이 및 검사실 기준에 부합",
            "abnormal": "최소잠복기 지연(비교측보다 약 10% 이상 느리거나 검사실 정상범위 초과), 반응 소실",
            "note": common_note,
        }

    if domain in ["h_reflex", "h_ratio"]:
        return {
            "title": "H-반사(H-reflex) 참고",
            "normal": "좌우 잠복기 차이와 H/M 비율이 검사실 기준 내",
            "abnormal": "잠복기 지연 또는 소실, 비정상적 항진, H/M 비율 증가",
            "note": common_note,
        }

    if domain == "blink":
        return {
            "title": "눈깜빡반사검사(Blink reflex) 참고",
            "normal": "R1, R2 잠복기와 좌우 반응 패턴이 검사실 기준 내",
            "abnormal": "R1 또는 R2 잠복기 지연, 반응 소실",
            "note": common_note,
        }

    return {
        "title": "검사 참고",
        "normal": "해당 검사실 정상범위 내",
        "abnormal": "잠복기 지연, 진폭 감소, 무반응 등",
        "note": common_note,
    }


def summarize_status(left, right, side="미선택", domain=None, item_name=""):
    """
    좌우/정상측/병변측 요약.
    학생이 좌우 비교를 쉽게 하도록 표현을 통일한다.
    """
    left_disp = educational_result_text(left, domain=domain, item_name=item_name)
    right_disp = educational_result_text(right, domain=domain, item_name=item_name)

    if str(right).strip() == "":
        return f"결과: {left_disp}"

    if side == "양측":
        return f"좌측: {left_disp} / 우측: {right_disp}"

    if side == "좌":
        return f"비교측(우측): {left_disp} / 병변측(좌측): {right_disp}"

    if side == "우":
        return f"비교측(좌측): {left_disp} / 병변측(우측): {right_disp}"

    return f"좌측: {left_disp} / 우측: {right_disp}"


def severity_text(total_abnormal, no_response_count):
    if no_response_count >= 2 or total_abnormal >= 6:
        return "중등도 이상"
    if total_abnormal >= 3:
        return "경도-중등도"
    if total_abnormal >= 1:
        return "경도"
    return "뚜렷한 이상 없음"
