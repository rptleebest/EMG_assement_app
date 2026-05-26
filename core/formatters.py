def normalize_result_text(value):
    if value is None:
        return ""
    text = str(value).strip()
    mapping = {
        "정상 (Normal)": "정상",
        "감소 (Reduced)": "감소",
        "잠복기 지연 (Delayed latency)": "잠복기 지연",
        "무반응 (No response)": "무반응",
        "비정상 자발전위 출현 (Fibrillation Potential, Positive Sharp Wave 등)": "비정상 자발전위 출현",
        "비정상 자발전위 (Fibrillation, Positive sharp wave 등) 출현": "비정상 자발전위 출현",
        "무반응 / 전기적 침묵 (Electrical silence)": "무반응/전기적 침묵",
        "지연 또는 소실 (Delayed/Absent)": "지연 또는 소실",
        "항진 또는 문턱값 감소 (Hyperactive / lower threshold)": "항진 또는 문턱값 감소",
        "증가 가능 (May be increased)": "증가 가능",
        "지연 (Delayed)": "지연",
        "소실 (Absent)": "소실"
    }
    return mapping.get(text, text)


def summarize_status(left, right, side="미선택"):
    left_disp = normalize_result_text(left)
    right_disp = normalize_result_text(right)

    if str(right).strip() == "":
        return f"결과: {left_disp}"

    if side == "양측":
        return f"좌측: {left_disp} / 우측: {right_disp}"
    if side == "좌":
        return f"좌측(병변측): {left_disp} / 우측(정상측): {right_disp}"
    if side == "우":
        return f"좌측(정상측): {left_disp} / 우측(병변측): {right_disp}"
    return f"좌측: {left_disp} / 우측: {right_disp}"


def severity_text(total_abnormal, no_response_count):
    if no_response_count >= 2 or total_abnormal >= 6:
        return "중등도 이상"
    if total_abnormal >= 3:
        return "경도-중등도"
    if total_abnormal >= 1:
        return "경도"
    return "뚜렷한 이상 없음"