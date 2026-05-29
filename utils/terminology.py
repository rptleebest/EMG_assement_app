from data.glossary import GLOSSARY


def term(key, used_terms=None):
    """
    같은 출력 화면에서 용어가 처음 나오면 한글 신용어(영어)를 제시하고,
    이후에는 한글 신용어만 제시하기 위한 함수.
    """
    if used_terms is None:
        used_terms = set()

    item = GLOSSARY.get(key)
    if not item:
        return key

    if key in used_terms:
        return item["short"]

    used_terms.add(key)
    return item["first"]
