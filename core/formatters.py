def normalize_result_text(value):
    """
    화면 표시용 결과 문구 정규화.
    기존의 '정상'이라는 단순 표현을 교육용으로 '정상 범위'에 가깝게 바꾼다.
    """
    if value is None:
        return ""

    text = str(value).strip()

    mapping = {
        "정상 (Normal)": "정상 범위",
        "정상": "정상 범위",
        "감소 (Reduced)": "진폭 감소",
        "감소": "진폭 감소",
        "잠복기 지연 (Delayed latency)": "잠복기 지연",
        "잠복기 지연": "잠복기 지연",
        "무반응 (No response)": "무반응",
        "무반응": "무반응",
        "비정상 자발전위 출현 (Fibrillation Potential, Positive Sharp Wave 등)": "비정상 자발전위",
        "비정상 자발전위 (Fibrillation, Positive sharp wave 등) 출현": "비정상 자발전위",
        "비정상 자발전위 출현": "비정상 자발전위",
        "무반응 / 전기적 침묵 (Electrical silence)": "무반응/전기적 침묵",
        "지연 또는 소실 (Delayed/Absent)": "지연 또는 소실",
        "지연 또는 소실": "지연 또는 소실",
        "항진 또는 문턱값 감소 (Hyperactive / lower threshold)": "항진 또는 문턱값 감소",
        "증가 가능 (May be increased)": "증가 가능",
        "지연 (Delayed)": "지연",
        "소실 (Absent)": "소실",
    }

    return mapping.get(text, text)


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
    검사 영역별로 학생 교육용 결과 문구를 보강한다.
    """
    raw = "" if value is None else str(value).strip()
    simple = normalize_result_text(raw)
    domain = domain or ""
    item_name = item_name or ""

    if domain == "muscle":
        if "정상" in raw or "Normal" in raw or simple == "정상 범위":
            return "휴식 시 전기적 침묵, 수의수축 시 정상 운동단위 동원"

        if (
            "비정상 자발전위" in raw
            or "Fibrillation" in raw
            or "Positive Sharp" in raw
            or "Positive sharp" in raw
        ):
            if any(x in item_name for x in ["ADM", "FDI", "APB", "새끼벌림근", "첫째등쪽뼈사이근", "짧은엄지벌림근"]):
                return "휴식 시 섬유자발전위 및 양성예파 관찰, 수의수축 시 동원 감소 가능"
            if any(x in item_name for x in ["척추주위근", "Paraspinal"]):
                return "휴식 시 섬유자발전위 및 양성예파 관찰"
            return "휴식 시 섬유자발전위 및 양성예파 관찰, 수의수축 시 동원 감소 가능"

        if "Fasciculation" in raw or "근육다발" in raw:
            return "휴식 시 근육다발수축전위 관찰"

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
            return "F파 최소잠복기 정상 범위"
        if simple == "지연 또는 소실":
            return "F파 최소잠복기 지연 또는 반응 소실"
        if simple == "지연":
            return "F파 최소잠복기 지연"
        if simple == "소실":
            return "F파 반응 소실"
        return simple

    if domain in ["h_reflex", "h_ratio"]:
        return simple

    if domain == "blink":
        return simple

    return simple


def get_domain_reference(domain, item_name=""):
    """
    검사 영역별 교육용 참고 기준.
    실제 절대 정상값은 검사실마다 다르므로 '교육용 예시'로 제공한다.
    """
    domain = domain or ""
    item_name = item_name or ""

    common_note = "주의: 실제 정상값은 장비, 검사실 기준, 피부온도, 나이, 키, 사지 길이, 자극/기록 위치에 따라 달라집니다."

    if domain == "sensory":
        return {
            "title": "SNAP 감각신경전도 참고",
            "normal": "정상 범위: 원위잠복기, SNAP 진폭, 전도속도가 해당 검사실 정상범위 내",
            "abnormal": "이상 예: 잠복기 지연, SNAP 진폭 감소, 전도속도 저하 또는 무반응",
            "meaning": "SNAP 진폭 감소는 말초 감각신경 또는 신경얼기 이후 병변을 시사합니다. 신경뿌리병증에서는 뒤뿌리신경절이 보존되어 SNAP가 정상일 수 있습니다.",
            "note": common_note,
        }

    if domain == "motor":
        return {
            "title": "CMAP 운동신경전도 참고",
            "normal": "정상 범위: 원위잠복기, CMAP 진폭, 전도속도가 해당 검사실 정상범위 내",
            "abnormal": "이상 예: 원위잠복기 지연, CMAP 진폭 감소, 전도속도 저하, 전도차단, 무반응",
            "meaning": "CMAP 진폭 감소는 운동축삭 손상 또는 심한 전도차단을, 잠복기 지연/전도속도 저하는 말이집탈락성 변화를 시사합니다.",
            "note": common_note,
        }

    if domain == "muscle":
        return {
            "title": "침근전도검사 참고",
            "normal": "정상: 휴식 시 전기적 침묵, 수의수축 시 정상 운동단위전위와 정상 동원 양상",
            "abnormal": "이상 예: 섬유자발전위, 양성예파, 근육다발수축전위, 감소된 동원, 만성 재지배성 운동단위전위",
            "meaning": "섬유자발전위와 양성예파는 비정상 자발전위로, 탈신경근 소견이며 축삭 손상 또는 신경뿌리/말초신경 손상을 시사합니다.",
            "note": "침근전도는 삽입 시 활동, 휴식 시 자발전위, 약한 수의수축 시 운동단위전위, 최대 수축 시 동원 양상을 구분해 해석합니다.",
        }

    if domain == "f_wave":
        return {
            "title": "F파 참고",
            "normal": "정상 범위: F파 최소잠복기와 출현 빈도가 키/사지 길이 및 검사실 기준에 부합",
            "abnormal": "이상 예: 최소잠복기 지연, 출현 빈도 감소, F파 소실",
            "meaning": "F파는 말초 운동신경의 근위부, 신경뿌리, 전반적 말이집탈락성 병변 평가에 유용합니다.",
            "note": common_note,
        }

    if domain in ["h_reflex", "h_ratio"]:
        return {
            "title": "H-반사 참고",
            "normal": "정상 범위: 좌우 잠복기 차이와 H/M 비율이 검사실 기준 내",
            "abnormal": "이상 예: H반사 지연/소실 또는 병적 항진, H/M 비율 증가",
            "meaning": "S1 신경뿌리병증에서는 지연/소실, 위운동신경세포 병변에서는 항진 양상이 나타날 수 있습니다.",
            "note": common_note,
        }

    if domain == "blink":
        return {
            "title": "눈깜빡반사 참고",
            "normal": "정상 범위: R1, R2 잠복기와 좌우 반응 패턴이 검사실 기준 내",
            "abnormal": "이상 예: R1/R2 지연 또는 소실",
            "meaning": "자극측 이상은 삼차신경 들신경 경로, 반응측 이상은 얼굴신경 날신경 경로 감별에 중요합니다.",
            "note": common_note,
        }

    return {
        "title": "검사 참고",
        "normal": "정상 범위: 해당 검사실 정상범위 내",
        "abnormal": "이상 예: 잠복기 지연, 진폭 감소, 전도속도 저하, 소실 등",
        "meaning": "검사 항목과 임상 양상을 함께 해석해야 합니다.",
        "note": common_note,
    }


def summarize_status(left, right, side="미선택", domain=None, item_name=""):
    """
    좌우/정상측/병변측 요약.
    기존 '정상측: 정상' 표현을 '비교측: 정상 범위' 중심으로 개선.
    """
    left_disp = educational_result_text(left, domain=domain, item_name=item_name)
    right_disp = educational_result_text(right, domain=domain, item_name=item_name)

    if str(right).strip() == "":
        return f"결과: {left_disp}"

    if side == "양측":
        return f"좌측: {left_disp} / 우측: {right_disp}"

    if side == "좌":
        return f"좌측(병변측): {left_disp} / 우측(비교측): {right_disp}"

    if side == "우":
        return f"좌측(비교측): {left_disp} / 우측(병변측): {right_disp}"

    return f"좌측: {left_disp} / 우측: {right_disp}"


def severity_text(total_abnormal, no_response_count):
    if no_response_count >= 2 or total_abnormal >= 6:
        return "중등도 이상"
    if total_abnormal >= 3:
        return "경도-중등도"
    if total_abnormal >= 1:
        return "경도"
    return "뚜렷한 이상 없음"
