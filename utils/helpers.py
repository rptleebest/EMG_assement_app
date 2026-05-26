def safe_index(options, value):
    try:
        return options.index(value)
    except ValueError:
        return 0


def simplify_level_text(level_text):
    if not level_text:
        return "정보 없음"
    return str(level_text).strip()


def normalize_case_item_name(item_name):
    if item_name is None:
        return ""
    return str(item_name).strip()


def get_compact_item_label(item_name):
    return normalize_case_item_name(item_name)


def is_abnormal(value):
    if value is None:
        return False

    text = str(value).strip().lower()
    if text == "":
        return False

    normal_tokens = [
        "정상 (normal)",
        "정상",
    ]
    return text not in normal_tokens


def get_motor_stimulation_labels(domain):
    if domain == "sensory":
        return {"distal": "기본 구간"}
    if domain == "motor":
        return {"distal": "원위부"}
    return {"distal": "기본"}


def get_case_names_for_selection():
    from data.cases import CASE_LIBRARY
    return list(CASE_LIBRARY.keys())