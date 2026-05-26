def make_report_text(result):
    lines = []
    lines.append("교육용 근전도 판독 보조 결과")
    lines.append("=" * 50)
    lines.append(f"생성 시각: {result.get('created_at', '')}")
    lines.append(f"최종 유력 진단: {result.get('final_dx', '')}")
    lines.append(f"손상 의심 신경: {result.get('involved_nerves', '')}")
    lines.append(f"신경학적 레벨/분절: {result.get('involved_levels', '')}")
    lines.append(f"중증도: {result.get('severity', '')}")

    if result.get("lesion_tags"):
        lines.append(f"병변 해석 태그: {', '.join(result.get('lesion_tags', []))}")

    lines.append("")
    lines.append("[Top 3 감별진단과 감별 포인트]")
    for i, item in enumerate(result.get("top3_details", []), 1):
        lines.append(f"{i}. {item['name']}")
        lines.append(f"   → 감별 포인트: {item['how_to_differentiate']}")

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