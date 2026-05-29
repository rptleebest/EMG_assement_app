import streamlit as st
from core.formatters import normalize_result_text


def render_result_view(result):
    st.markdown(
        """
        <div class="result-card">
            <div class="result-title">✅ 자동 해석 결과</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="result-text"><b>최종 유력 진단:</b> {result.get("final_dx", "")}</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        f'<div class="result-text"><b>의심 병변 태그:</b> {", ".join(result.get("lesion_tags", [])) if result.get("lesion_tags") else "특이 태그 없음"}</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        f'<div class="result-text"><b>의심 신경:</b> {result.get("involved_nerves", "")}</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        f'<div class="result-text"><b>의심 레벨/분절:</b> {result.get("involved_levels", "")}</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        f'<div class="result-text"><b>중증도:</b> {result.get("severity", "")}</div>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="result-label">Top 3 감별진단</div>', unsafe_allow_html=True)
    for idx, (dx, score) in enumerate(result.get("top3", []), 1):
        st.markdown(
            f'<div class="result-text">{idx}. <b>{dx}</b> <span style="color:#64748b;">(점수: {score})</span></div>',
            unsafe_allow_html=True
        )

    st.markdown('<div class="result-label">감별 포인트</div>', unsafe_allow_html=True)

    top3_details = result.get("top3_details", [])
    total_details_count = len(top3_details)

    for idx, item in enumerate(top3_details, 1):
        if total_details_count == 1:
            detail_title = item.get("name", "")
        else:
            detail_title = f'{idx}. {item.get("name", "")}'

        st.markdown(
            f"""
            <div class="case-text-block">
                <div class="finding-item-title">{detail_title}</div>
                <div class="finding-subtext">{item.get("how_to_differentiate", "")}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown('<div class="result-label">판단 근거</div>', unsafe_allow_html=True)
    for reason in result.get("reasons", []):
        st.markdown(f'<div class="result-text">• {reason}</div>', unsafe_allow_html=True)

    st.markdown('<div class="result-label">이상 항목 요약</div>', unsafe_allow_html=True)
    for item in result.get("abnormal_items", []):
        result_text = normalize_result_text(item.get("결과", ""))
        st.markdown(
            f"""
            <div class="case-text-block">
                <div class="finding-item-title">{item.get("항목", "")}</div>
                <div class="finding-subtext"><b>신경:</b> {item.get("신경", "")}</div>
                <div class="finding-subtext"><b>레벨:</b> {item.get("레벨", "")}</div>
                <div class="finding-subtext"><b>결과:</b> {result_text}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    if result.get("suggestions"):
        st.markdown('<div class="result-label">추가 학습/해석 제안</div>', unsafe_allow_html=True)
        for s in result.get("suggestions", []):
            st.markdown(f'<div class="result-small">• {s}</div>', unsafe_allow_html=True)

    st.markdown(
        '<div class="result-small">※ 본 결과는 학생 교육용 참고 자료이며 실제 임상 진단을 대체하지 않습니다.</div>',
        unsafe_allow_html=True
    )
