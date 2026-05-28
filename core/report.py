from core.formatters import normalize_result_text, educational_result_text


def make_report_text(result):
    """
    교육용 텍스트 보고서 생성.
    물리치료학과 학생이 보기 쉽도록 핵심 진단, 감별 포인트, 검사 해석 원칙을 포함한다.
    """
    lines = []

    lines.append("교육용 근전도/신경전도 판독 보조 결과")
    lines.append("=" * 60)
    lines.append(f"생성 시각: {result.get('created_at', '')}")
    lines.append("")
    lines.append("[핵심 요약]")
    lines.append(f"- 최종 유력 진단: {result.get('final_dx', '')}")
    lines.append(f"- 손상 의심 신경: {result.get('involved_nerves', '')}")
    lines.append(f"- 신경학적 레벨/분절: {result.get('involved_levels', '')}")
    lines.append(f"- 중증도: {result.get('severity', '')}")

    if result.get("lesion_tags"):
        lines.append(f"- 병변 해석 태그: {', '.join(result.get('lesion_tags', []))}")

    lines.append("")
    lines.append("[Top 3 감별진단과 감별 포인트]")
    top3 = result.get("top3_details", [])
    if top3:
        for i, item in enumerate(top3, 1):
            lines.append(f"{i}. {item.get('name', '')}")
            lines.append(f"   - 감별 포인트: {item.get('how_to_differentiate', '')}")
    else:
        lines.append("- 감별진단 정보가 없습니다.")

    lines.append("")
    lines.append("[판단 근거]")
    reasons = result.get("reasons", [])
    if reasons:
        for reason in reasons:
            lines.append(f"- {reason}")
    else:
        lines.append("- 판단 근거 정보가 없습니다.")

    lines.append("")
    lines.append("[이상 항목 요약]")
    abnormal_items = result.get("abnormal_items", [])
    if abnormal_items:
        for item in abnormal_items:
            name = item.get("항목", "")
            raw_result = item.get("결과", "")
            result_text = normalize_result_text(raw_result)
            lines.append(f"- {name}: {result_text}")
    else:
        lines.append("- 뚜렷한 이상 항목이 없습니다.")

    lines.append("")
    lines.append("[학생용 해석 가이드]")
    lines.append("- 신경전도검사에서 '정상'은 절대값이 아니라 해당 검사실 정상범위 내라는 뜻입니다.")
    lines.append("- SNAP 진폭 감소는 말초 감각신경 또는 신경얼기 이후 병변을 시사할 수 있습니다.")
    lines.append("- 신경뿌리병증에서는 뒤뿌리신경절이 보존되어 감각신경활동전위(SNAP)가 정상 범위일 수 있습니다.")
    lines.append("- CMAP 진폭 감소는 운동축삭 손상 또는 심한 전도차단을 시사할 수 있습니다.")
    lines.append("- 잠복기 지연과 전도속도 저하는 말이집탈락성 변화 또는 포착성 병변에서 중요합니다.")
    lines.append("- 침근전도에서 섬유자발전위와 양성예파는 비정상 자발전위이며, 탈신경근 및 축삭 손상을 시사합니다.")
    lines.append("- F파는 근위부 운동신경, 신경뿌리, 다발신경병증 평가에 유용합니다.")

    lines.append("")
    lines.append("[주의]")
    lines.append("- 본 결과는 물리치료학과 학생 교육용 참고 자료입니다.")
    lines.append("- 실제 임상 진단, 치료 결정, 예후 판단은 전문 의료진의 병력청취, 진찰, 영상검사, 검사실 기준을 종합해야 합니다.")
    lines.append("- 전기진단검사의 정상범위는 장비, 검사실, 피부온도, 나이, 키, 사지 길이, 자극/기록 위치에 따라 달라질 수 있습니다.")

    return "\n".join(lines)
