from data.diagnostic_rules import DIAGNOSTIC_RULES


def score_rule(rule, selected_codes, selected_region=None):
    selected_codes = set(selected_codes)

    score = 0
    matched_positive = []
    matched_negative = []

    for code in rule.get("positive", []):
        if code in selected_codes:
            score += 2
            matched_positive.append(code)

    for code in rule.get("negative", []):
        if code in selected_codes:
            score -= 2
            matched_negative.append(code)

    if selected_region and rule.get("region") == selected_region:
        score += 2

    max_score = max(1, len(rule.get("positive", [])) * 2 + 2)
    confidence = int(max(0, min(100, (score / max_score) * 100)))

    return {
        "id": rule["id"],
        "name": rule["name"],
        "lesion": rule["lesion"],
        "region": rule["region"],
        "score": score,
        "confidence": confidence,
        "matched_positive": matched_positive,
        "matched_negative": matched_negative,
        "pt_points": rule.get("pt_points", []),
        "teaching": rule.get("teaching", []),
        "differentials": rule.get("differentials", []),
    }


def interpret_findings(selected_codes, selected_region=None):
    results = []

    for rule in DIAGNOSTIC_RULES:
        result = score_rule(rule, selected_codes, selected_region)
        if result["score"] > 0:
            results.append(result)

    results.sort(key=lambda x: (x["confidence"], x["score"]), reverse=True)

    return results[:5]


def summarize_pattern(selected_codes):
    selected_codes = set(selected_codes)
    comments = []

    if "snap_preserved" in selected_codes and "paraspinal_abnormal" in selected_codes:
        comments.append("감각신경활동전위 보존과 척추주위근 이상이 함께 있어 신경뿌리병증 가능성을 올립니다.")

    if "snap_reduced" in selected_codes and "paraspinal_normal" in selected_codes and "multiple_peripheral_nerves" in selected_codes:
        comments.append("감각신경활동전위 감소, 여러 말초신경 분포 침범, 척추주위근 보존은 신경얼기병증을 시사합니다.")

    if "distal_symmetric_pattern" in selected_codes:
        comments.append("양측 원위부 우세의 대칭성 이상은 다발신경병증 패턴과 잘 맞습니다.")

    if "cmap_absent" in selected_codes or "no_muap" in selected_codes:
        comments.append("반응 소실 또는 수의수축 시 운동단위전위 없음은 심한 운동축삭 손상 가능성을 시사합니다.")

    if "conduction_velocity_slow" in selected_codes or "f_wave_delayed_absent" in selected_codes:
        comments.append("전도속도 저하 또는 F파 이상은 말이집탈락성 변화나 근위부 전도 이상을 고려하게 합니다.")

    if "h_reflex_hyperactive" in selected_codes:
        comments.append("H반사 항진 또는 H/M 비율 증가는 중추성 경직 증가와 관련될 수 있습니다.")

    return comments
