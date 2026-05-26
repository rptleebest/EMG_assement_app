import streamlit as st


def apply_global_styles():
    st.markdown("""
    <style>
    .block-container {
        padding-top: 2.8rem;
        padding-bottom: 1.0rem;
        max-width: 960px;
    }

    .main-title {
        font-size: 1.34rem;
        font-weight: 700;
        margin-top: 0.2rem;
        margin-bottom: 0.35rem;
        line-height: 1.28;
        color: #0f172a;
        letter-spacing: -0.01em;
        word-break: keep-all;
    }

    .subtle {
        color: #475569;
        font-size: 0.95rem;
        margin-bottom: 0.9rem;
        line-height: 1.62;
    }

    .section-card,
    .result-card,
    .warn-card {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 12px;
        padding: 12px 12px 14px 12px;
        margin-bottom: 14px;
    }

    .result-card {
        background: #f8fffb;
        border: 1px solid #d1fae5;
    }

    .warn-card {
        background: #fffaf3;
        border: 1px solid #fed7aa;
    }

    .input-title {
        font-weight: 650;
        font-size: 0.96rem;
        margin-bottom: 4px;
        color: #0f172a;
        line-height: 1.45;
        word-break: keep-all;
    }

    .input-meta {
        font-size: 0.84rem;
        color: #64748b;
        margin-bottom: 8px;
        line-height: 1.52;
    }

    .big-section-title {
        font-size: 0.95rem;
        font-weight: 700;
        color: #0f172a;
        background: #f8fafc;
        border: 1px solid #dbeafe;
        border-left: 4px solid #3b82f6;
        border-radius: 10px;
        padding: 9px 10px;
        margin-top: 12px;
        margin-bottom: 10px;
        line-height: 1.4;
    }

    .section-hint {
        font-size: 0.9rem;
        color: #334155;
        background: #f8fafc;
        border-left: 4px solid #22c55e;
        padding: 10px 11px;
        border-radius: 10px;
        margin-top: 8px;
        margin-bottom: 12px;
        line-height: 1.62;
    }

    .case-title-mobile {
        font-size: 1.02rem;
        font-weight: 700;
        line-height: 1.4;
        color: #0f172a;
        margin-bottom: 8px;
        word-break: keep-all;
    }

    .case-subtitle-mobile {
        font-size: 0.86rem;
        color: #475569;
        margin-bottom: 10px;
        line-height: 1.58;
    }

    .case-section-label {
        font-size: 0.95rem;
        font-weight: 700;
        color: #0f172a;
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-left: 4px solid #60a5fa;
        border-radius: 10px;
        padding: 9px 10px;
        margin-top: 14px;
        margin-bottom: 10px;
        line-height: 1.42;
    }

    .case-subheading {
        font-size: 0.92rem;
        font-weight: 700;
        color: #0f172a;
        margin-top: 14px;
        margin-bottom: 8px;
        line-height: 1.45;
    }

    .case-bullet {
        font-size: 0.9rem;
        line-height: 1.68;
        color: #1f2937;
        margin-bottom: 7px;
        word-break: keep-all;
    }

    .case-text-block {
        background: #fcfcfd;
        border-left: 4px solid #e2e8f0;
        border-radius: 9px;
        padding: 10px 11px;
        margin-bottom: 10px;
    }

    .finding-item-title {
        font-size: 0.9rem;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 6px;
        line-height: 1.5;
    }

    .finding-subtext {
        font-size: 0.88rem;
        color: #334155;
        line-height: 1.68;
        margin-bottom: 7px;
    }

    .mobile-note {
        font-size: 0.86rem;
        color: #475569;
        line-height: 1.58;
        margin-bottom: 6px;
    }

    .result-title {
        font-size: 0.98rem;
        font-weight: 700;
        color: #065f46;
        line-height: 1.4;
        margin-bottom: 6px;
    }

    .result-label {
        font-size: 0.9rem;
        font-weight: 700;
        color: #0f172a;
        background: #f8fafc;
        border-left: 4px solid #86efac;
        border-radius: 8px;
        padding: 8px 9px;
        margin-top: 12px;
        margin-bottom: 10px;
        line-height: 1.42;
    }

    .result-text {
        font-size: 0.88rem;
        color: #1f2937;
        line-height: 1.64;
        margin-bottom: 7px;
    }

    .result-small {
        font-size: 0.84rem;
        color: #475569;
        line-height: 1.58;
    }

    .group-check-box {
        padding: 6px 8px;
        border: 1px solid #e5e7eb;
        border-radius: 8px;
        background: #fafafa;
        margin-bottom: 6px;
    }

    div[data-testid="stButton"] button {
        font-weight: 700 !important;
        border-radius: 10px !important;
    }
    </style>
    """, unsafe_allow_html=True)