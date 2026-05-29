def ko(value):
    """
    현재 앱 전반에서 사용되는 최소 호환 함수.
    문자열/숫자/리스트 등을 안전하게 화면 출력용 문자열로 변환합니다.
    """
    if value is None:
        return ""

    if isinstance(value, (list, tuple, set)):
        return ", ".join(str(v) for v in value if v is not None)

    if isinstance(value, dict):
        return ", ".join(f"{k}: {v}" for k, v in value.items())

    return str(value)
