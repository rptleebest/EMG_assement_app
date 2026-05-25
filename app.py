import streamlit as st
from collections import defaultdict
from datetime import datetime

# ==========================================
# 1. 페이지 설정 및 스타일
# ==========================================
st.set_page_config(
    page_title="교육용 근전도 판독 보조",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

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

.input-row {
    padding: 0;
    margin-bottom: 0;
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

.item-divider {
    border: none;
    border-top: 1px solid #eef2f7;
    margin: 10px 0 12px 0;
}

.section-divider {
    border: none;
    border-top: 1px solid #e2e8f0;
    margin: 14px 0 16px 0;
}

.soft-divider {
    border: none;
    border-top: 1px solid #f1f5f9;
    margin: 8px 0 10px 0;
}

.strong-divider {
    border: none;
    border-top: 1px solid #cbd5e1;
    margin: 16px 0 18px 0;
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

.case-bullet-strong {
    font-size: 0.9rem;
    line-height: 1.68;
    color: #1f2937;
    margin-bottom: 8px;
    word-break: keep-all;
}

.case-bullet-strong b {
    font-weight: 700;
    color: #0f172a;
}

.case-text-block {
    background: #fcfcfd;
    border-left: 4px solid #e2e8f0;
    border-radius: 9px;
    padding: 10px 11px;
    margin-top: 0;
    margin-bottom: 10px;
}

.finding-item-title {
    font-size: 0.9rem;
    font-weight: 700;
    color: #0f172a;
    margin-top: 0;
    margin-bottom: 6px;
    line-height: 1.5;
    word-break: keep-all;
}

.finding-subtext {
    font-size: 0.88rem;
    color: #334155;
    line-height: 1.68;
    margin-bottom: 7px;
    word-break: keep-all;
}

.finding-subtext b {
    font-weight: 700;
    color: #0f172a;
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

.compact-item {
    padding: 2px 0;
    margin-bottom: 8px;
}

.compact-block {
    margin-bottom: 10px;
}

.compact-divider {
    margin: 10px 0 12px 0 !important;
}

.top-bottom-nav-space {
    height: 4px;
}

div[role="radiogroup"] label p,
div[data-testid="stRadio"] label p,
div[data-testid="stCheckbox"] label p {
    font-size: 0.9rem !important;
    font-weight: 600 !important;
    line-height: 1.45 !important;
    color: #0f172a !important;
    word-break: keep-all !important;
}

label[data-testid="stWidgetLabel"] p {
    font-size: 0.86rem !important;
    font-weight: 600 !important;
    color: #334155 !important;
    line-height: 1.45 !important;
}

div[data-testid="stButton"] button {
    font-weight: 700 !important;
    border-radius: 10px !important;
}

@media (max-width: 768px) {
    .block-container {
        padding-top: 2.4rem;
        padding-bottom: 0.85rem;
        padding-left: 0.7rem;
        padding-right: 0.7rem;
    }

    .main-title {
        font-size: 1.18rem;
        font-weight: 700;
        line-height: 1.3;
        margin-bottom: 0.28rem;
    }

    .subtle {
        font-size: 0.86rem;
        line-height: 1.64;
        margin-bottom: 0.85rem;
    }

    .section-card,
    .result-card,
    .warn-card {
        padding: 10px 10px 12px 10px;
        border-radius: 11px;
        margin-bottom: 12px;
    }

    .case-title-mobile {
        font-size: 0.98rem;
        line-height: 1.42;
        margin-bottom: 7px;
    }

    .case-subtitle-mobile {
        font-size: 0.82rem;
        line-height: 1.56;
        margin-bottom: 9px;
    }

    .case-section-label,
    .big-section-title {
        font-size: 0.9rem;
        font-weight: 700;
        padding: 8px 9px;
        margin-top: 12px;
        margin-bottom: 10px;
        line-height: 1.42;
    }

    .case-subheading {
        font-size: 0.88rem;
        font-weight: 700;
        margin-top: 12px;
        margin-bottom: 7px;
        line-height: 1.46;
    }

    .case-bullet,
    .case-bullet-strong,
    .finding-subtext,
    .mobile-note,
    .result-text,
    .result-small {
        font-size: 0.84rem;
        line-height: 1.72;
        margin-bottom: 8px;
    }

    .finding-item-title {
        font-size: 0.86rem;
        font-weight: 700;
        margin-bottom: 6px;
        line-height: 1.48;
    }

    .input-title {
        font-size: 0.9rem;
        line-height: 1.48;
        margin-bottom: 4px;
    }

    .input-meta {
        font-size: 0.8rem;
        line-height: 1.56;
        margin-bottom: 8px;
    }

    .item-divider {
        margin: 10px 0 12px 0;
    }

    .section-divider {
        margin: 14px 0 16px 0;
    }

    .case-text-block {
        padding: 10px 9px;
        margin-bottom: 10px;
        border-radius: 9px;
    }

    .compact-item {
        margin-bottom: 10px;
    }

    div[role="radiogroup"] label p,
    div[data-testid="stRadio"] label p,
    div[data-testid="stCheckbox"] label p {
        font-size: 0.86rem !important;
        font-weight: 600 !important;
        line-height: 1.46 !important;
    }

    label[data-testid="stWidgetLabel"] p {
        font-size: 0.82rem !important;
        font-weight: 600 !important;
        line-height: 1.42 !important;
    }
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. 시스템 상수 및 데이터
# ==========================================
MODE_CASE = "사례 학습"
MODE_DIRECT = "검사 정보 입력 학습"

SEX_OPTIONS = ["미선택", "남", "여"]
SIDE_OPTIONS = ["미선택", "좌", "우", "양측"]

SECTIONS = {
    "팔 감각신경전도검사 (arm sensory NCS)": [
        "정중신경 감각신경활동전위 (Median SNAP)",
        "자신경 감각신경활동전위 (Ulnar SNAP)",
        "노신경 감각신경활동전위 (Radial SNAP)",
        "노신경 표재감각신경활동전위 (Superficial Radial SNAP)",
        "가쪽아래팔피부신경 감각신경활동전위 (Lateral antebrachial cutaneous SNAP)"
    ],
    "팔 운동신경전도검사 (arm motor NCS)": [
        "정중신경 복합근육활동전위 (Median CMAP)",
        "자신경 복합근육활동전위 (Ulnar CMAP)",
        "노신경 복합근육활동전위 (Radial CMAP)",
        "겨드랑신경 복합근육활동전위 (Axillary CMAP)",
        "근피신경 복합근육활동전위 (Musculocutaneous CMAP)"
    ],
    "팔 침근전도검사 근육 (arm needle EMG muscles)": [
        "짧은엄지벌림근 (Abductor Pollicis Brevis, APB)",
        "첫째등쪽뼈사이근 (First Dorsal Interosseous, FDI)",
        "새끼벌림근 (Abductor Digiti Minimi, ADM)",
        "집게폄근 (Extensor Indicis Proprius, EIP)",
        "손목폄근 (Extensor Carpi Radialis / Extensor Digitorum)",
        "가시아래근 (Infraspinatus)",
        "삼각근 (Deltoid)",
        "위팔두갈래근 (Biceps Brachii)",
        "위팔노근 (Brachioradialis)",
        "긴노쪽손목폄근/짧은노쪽손목폄근 (Extensor Carpi Radialis Longus/Brevis)",
        "원엎침근 (Pronator Teres)",
        "위팔세갈래근 (Triceps Brachii)",
        "목 척추주위근 (Cervical Paraspinal)"
    ],
    "다리 감각신경전도검사 (leg sensory NCS)": [
        "장딴지신경 감각신경활동전위 (Sural SNAP)",
        "얕은종아리신경 감각신경활동전위 (Superficial Peroneal SNAP)",
        "두렁신경 감각신경활동전위 (Saphenous SNAP)",
        "첫째 발가락사이 감각 (First Dorsal Web Space Sensation)"
    ],
    "다리 운동신경전도검사 (leg motor NCS)": [
        "종아리신경 복합근육활동전위 (Peroneal CMAP)",
        "깊은종아리신경 복합근육활동전위 (Deep Peroneal CMAP)",
        "정강신경 복합근육활동전위 (Tibial CMAP)",
        "넓적다리신경 복합근육활동전위 (Femoral CMAP)"
    ],
    "다리 침근전도검사 근육 (leg needle EMG muscles)": [
        "앞정강근 (Tibialis Anterior, TA)",
        "짧은발가락폄근 (Extensor Digitorum Brevis, EDB)",
        "짧은발가락벌림근 (Abductor Digiti Minimi pedis)",
        "긴엄지폄근 (Extensor Hallucis Longus, EHL)",
        "긴종아리근 (Peroneus Longus)",
        "장딴지근 (Gastrocnemius)",
        "가자미근 (Soleus)",
        "가쪽넓은근 (Vastus Lateralis)",
        "엉덩허리근 (Iliopsoas)",
        "큰볼기근 (Gluteus Maximus)",
        "중간볼기근 (Gluteus Medius)",
        "뒤넓적다리근 (Biceps Femoris)",
        "허리 척추주위근 (Lumbar Paraspinal)"
    ],
    "H반사 / 경직 평가 (H-reflex / Spasticity evaluation)": [
        "H 반사 (좌)",
        "H 반사 (우)",
        "H/M 비율"
    ],
    "F파 검사 (F-wave study)": [
        "정중신경 F파 (Median F-wave)",
        "자신경 F파 (Ulnar F-wave)",
        "정강신경 F파 (Tibial F-wave)",
        "종아리신경 F파 (Peroneal F-wave)"
    ],
    "눈깜빡반사검사 (Blink reflex)": [
        "우측 자극-우측 R1",
        "우측 자극-우측 R2",
        "우측 자극-좌측 R2",
        "좌측 자극-좌측 R1",
        "좌측 자극-좌측 R2",
        "좌측 자극-우측 R2"
    ]
}

ANATOMY = {
    "정중신경 감각신경활동전위 (Median SNAP)": {"nerve": "정중신경 (Median nerve)", "level": "손목/아래팔, C6-T1", "domain": "sensory", "region": "arm"},
    "자신경 감각신경활동전위 (Ulnar SNAP)": {"nerve": "자신경 (Ulnar nerve)", "level": "손목/팔꿉, C8-T1", "domain": "sensory", "region": "arm"},
    "노신경 감각신경활동전위 (Radial SNAP)": {"nerve": "노신경 (Radial nerve)", "level": "아래팔/손등, C5-C8", "domain": "sensory", "region": "arm"},
    "노신경 표재감각신경활동전위 (Superficial Radial SNAP)": {"nerve": "노신경 표재감각분지 (Superficial radial sensory branch)", "level": "아래팔/손등, C6-C8", "domain": "sensory", "region": "arm"},
    "가쪽아래팔피부신경 감각신경활동전위 (Lateral antebrachial cutaneous SNAP)": {"nerve": "가쪽아래팔피부신경 (Lateral antebrachial cutaneous nerve)", "level": "근피신경 말단 감각분지, C5-C6", "domain": "sensory", "region": "arm"},

    "정중신경 복합근육활동전위 (Median CMAP)": {"nerve": "정중신경 (Median nerve)", "level": "정중신경 말단운동전도, C8-T1", "domain": "motor", "region": "arm"},
    "자신경 복합근육활동전위 (Ulnar CMAP)": {"nerve": "자신경 (Ulnar nerve)", "level": "말단/팔꿉 구간 운동전도, C8-T1", "domain": "motor", "region": "arm"},
    "노신경 복합근육활동전위 (Radial CMAP)": {"nerve": "노신경 (Radial nerve)", "level": "위팔/아래팔 운동경로, C6-C8", "domain": "motor", "region": "arm"},
    "겨드랑신경 복합근육활동전위 (Axillary CMAP)": {"nerve": "겨드랑신경 (Axillary nerve)", "level": "팔신경얼기 뒤다발, C5-C6", "domain": "motor", "region": "arm"},
    "근피신경 복합근육활동전위 (Musculocutaneous CMAP)": {"nerve": "근피신경 (Musculocutaneous nerve)", "level": "팔신경얼기 가쪽다발, C5-C6", "domain": "motor", "region": "arm"},

    "짧은엄지벌림근 (Abductor Pollicis Brevis, APB)": {"nerve": "정중신경 (Median nerve)", "level": "C8-T1", "domain": "muscle", "region": "arm"},
    "첫째등쪽뼈사이근 (First Dorsal Interosseous, FDI)": {"nerve": "자신경 (Ulnar nerve)", "level": "C8-T1", "domain": "muscle", "region": "arm"},
    "새끼벌림근 (Abductor Digiti Minimi, ADM)": {"nerve": "자신경 (Ulnar nerve)", "level": "C8-T1", "domain": "muscle", "region": "arm"},
    "집게폄근 (Extensor Indicis Proprius, EIP)": {"nerve": "뒤뼈사이신경/노신경 (Posterior interosseous/Radial nerve)", "level": "C7-C8", "domain": "muscle", "region": "arm"},
    "손목폄근 (Extensor Carpi Radialis / Extensor Digitorum)": {"nerve": "노신경 (Radial nerve)", "level": "C6-C8", "domain": "muscle", "region": "arm"},
    "가시아래근 (Infraspinatus)": {"nerve": "어깨위신경 (Suprascapular nerve)", "level": "C5-C6", "domain": "muscle", "region": "arm"},
    "삼각근 (Deltoid)": {"nerve": "겨드랑신경 (Axillary nerve)", "level": "C5-C6", "domain": "muscle", "region": "arm"},
    "위팔두갈래근 (Biceps Brachii)": {"nerve": "근피신경 (Musculocutaneous nerve)", "level": "C5-C6", "domain": "muscle", "region": "arm"},
    "위팔노근 (Brachioradialis)": {"nerve": "노신경 (Radial nerve)", "level": "C5-C6", "domain": "muscle", "region": "arm"},
    "긴노쪽손목폄근/짧은노쪽손목폄근 (Extensor Carpi Radialis Longus/Brevis)": {"nerve": "노신경 (Radial nerve)", "level": "C6-C7", "domain": "muscle", "region": "arm"},
    "원엎침근 (Pronator Teres)": {"nerve": "정중신경 (Median nerve)", "level": "C6-C7", "domain": "muscle", "region": "arm"},
    "위팔세갈래근 (Triceps Brachii)": {"nerve": "노신경 (Radial nerve)", "level": "C6-C8 (C7 우세)", "domain": "muscle", "region": "arm"},
    "목 척추주위근 (Cervical Paraspinal)": {"nerve": "척수뒤가지 (Posterior primary ramus)", "level": "목 신경뿌리 수준", "domain": "muscle", "region": "arm"},

    "장딴지신경 감각신경활동전위 (Sural SNAP)": {"nerve": "장딴지신경 (Sural nerve)", "level": "S1-S2", "domain": "sensory", "region": "leg"},
    "얕은종아리신경 감각신경활동전위 (Superficial Peroneal SNAP)": {"nerve": "얕은종아리신경 (Superficial peroneal nerve)", "level": "L5-S1", "domain": "sensory", "region": "leg"},
    "두렁신경 감각신경활동전위 (Saphenous SNAP)": {"nerve": "두렁신경 (Saphenous nerve)", "level": "L3-L4", "domain": "sensory", "region": "leg"},
    "첫째 발가락사이 감각 (First Dorsal Web Space Sensation)": {"nerve": "깊은종아리신경 감각분지 (Deep peroneal sensory branch)", "level": "L5", "domain": "sensory", "region": "leg"},

    "종아리신경 복합근육활동전위 (Peroneal CMAP)": {"nerve": "온종아리신경-깊은종아리신경 운동경로", "level": "종아리뼈머리/종아리 구간, L4-S1", "domain": "motor", "region": "leg"},
    "깊은종아리신경 복합근육활동전위 (Deep Peroneal CMAP)": {"nerve": "깊은종아리신경 (Deep peroneal nerve)", "level": "발목/발등, L5-S1", "domain": "motor", "region": "leg"},
    "정강신경 복합근육활동전위 (Tibial CMAP)": {"nerve": "정강신경 (Tibial nerve)", "level": "오금/발목, L4-S3", "domain": "motor", "region": "leg"},
    "넓적다리신경 복합근육활동전위 (Femoral CMAP)": {"nerve": "넓적다리신경 (Femoral nerve)", "level": "L2-L4", "domain": "motor", "region": "leg"},

    "앞정강근 (Tibialis Anterior, TA)": {"nerve": "깊은종아리신경 (Deep peroneal nerve)", "level": "L4-L5", "domain": "muscle", "region": "leg"},
    "짧은발가락폄근 (Extensor Digitorum Brevis, EDB)": {"nerve": "깊은종아리신경 (Deep peroneal nerve)", "level": "L5-S1", "domain": "muscle", "region": "leg"},
    "짧은발가락벌림근 (Abductor Digiti Minimi pedis)": {"nerve": "가쪽발바닥신경 (Lateral plantar nerve)", "level": "S1-S2", "domain": "muscle", "region": "leg"},
    "긴엄지폄근 (Extensor Hallucis Longus, EHL)": {"nerve": "깊은종아리신경 (Deep peroneal nerve)", "level": "L5", "domain": "muscle", "region": "leg"},
    "긴종아리근 (Peroneus Longus)": {"nerve": "얕은종아리신경 (Superficial peroneal nerve)", "level": "L5-S1", "domain": "muscle", "region": "leg"},
    "장딴지근 (Gastrocnemius)": {"nerve": "정강신경 (Tibial nerve)", "level": "S1-S2", "domain": "muscle", "region": "leg"},
    "가자미근 (Soleus)": {"nerve": "정강신경 (Tibial nerve)", "level": "S1-S2", "domain": "muscle", "region": "leg"},
    "가쪽넓은근 (Vastus Lateralis)": {"nerve": "넓적다리신경 (Femoral nerve)", "level": "L2-L4", "domain": "muscle", "region": "leg"},
    "엉덩허리근 (Iliopsoas)": {"nerve": "허리신경얼기/넓적다리신경 관련 분포", "level": "L2-L4 (주로 L2-L3)", "domain": "muscle", "region": "leg"},
    "큰볼기근 (Gluteus Maximus)": {"nerve": "아래볼기신경 (Inferior gluteal nerve)", "level": "L5-S2", "domain": "muscle", "region": "leg"},
    "중간볼기근 (Gluteus Medius)": {"nerve": "위볼기신경 (Superior gluteal nerve)", "level": "L4-S1", "domain": "muscle", "region": "leg"},
    "뒤넓적다리근 (Biceps Femoris)": {"nerve": "궁둥신경 분포 (Sciatic division)", "level": "L5-S2", "domain": "muscle", "region": "leg"},
    "허리 척추주위근 (Lumbar Paraspinal)": {"nerve": "척수뒤가지 (Posterior primary ramus)", "level": "허리 신경뿌리 수준", "domain": "muscle", "region": "leg"},

    "H 반사 (좌)": {"nerve": "정강신경-척수 S1 반사고리", "level": "H 반사 경로, 주로 S1", "domain": "h_reflex", "region": "leg"},
    "H 반사 (우)": {"nerve": "정강신경-척수 S1 반사고리", "level": "H 반사 경로, 주로 S1", "domain": "h_reflex", "region": "leg"},
    "H/M 비율": {"nerve": "척수 반사 흥분성 평가", "level": "H 반사 흥분성 평가", "domain": "h_ratio", "region": "leg"},
    "정중신경 F파 (Median F-wave)": {"nerve": "정중신경 근위부/운동신경뿌리", "level": "근위부 경로, C8-T1", "domain": "f_wave", "region": "arm"},
    "자신경 F파 (Ulnar F-wave)": {"nerve": "자신경 근위부/운동신경뿌리", "level": "근위부 경로, C8-T1", "domain": "f_wave", "region": "arm"},
    "정강신경 F파 (Tibial F-wave)": {"nerve": "정강신경 근위부/운동신경뿌리", "level": "근위부 경로, L5-S2", "domain": "f_wave", "region": "leg"},
    "종아리신경 F파 (Peroneal F-wave)": {"nerve": "종아리신경 근위부/운동신경뿌리", "level": "근위부 경로, L4-S1", "domain": "f_wave", "region": "leg"},

    "우측 자극-우측 R1": {
        "nerve": "우측 삼차신경 구심성-뇌줄기-우측 얼굴신경 원심성 반사경로",
        "level": "눈깜빡반사 경로",
        "domain": "blink",
        "region": "face"
    },
    "우측 자극-우측 R2": {
        "nerve": "우측 삼차신경 구심성-뇌줄기-우측 얼굴신경 원심성 반사경로",
        "level": "눈깜빡반사 경로",
        "domain": "blink",
        "region": "face"
    },
    "우측 자극-좌측 R2": {
        "nerve": "우측 삼차신경 구심성-뇌줄기-좌측 얼굴신경 원심성 반사경로",
        "level": "눈깜빡반사 경로",
        "domain": "blink",
        "region": "face"
    },
    "좌측 자극-좌측 R1": {
        "nerve": "좌측 삼차신경 구심성-뇌줄기-좌측 얼굴신경 원심성 반사경로",
        "level": "눈깜빡반사 경로",
        "domain": "blink",
        "region": "face"
    },
    "좌측 자극-좌측 R2": {
        "nerve": "좌측 삼차신경 구심성-뇌줄기-좌측 얼굴신경 원심성 반사경로",
        "level": "눈깜빡반사 경로",
        "domain": "blink",
        "region": "face"
    },
    "좌측 자극-우측 R2": {
        "nerve": "좌측 삼차신경 구심성-뇌줄기-우측 얼굴신경 원심성 반사경로",
        "level": "눈깜빡반사 경로",
        "domain": "blink",
        "region": "face"
    },
}

CASE_LIBRARY = {
    "1. 목-팔 통증 증상과 팔 근력 약화": {
        "patient": {
            "age": 57, "sex": "남", "side": "우",
            "symptoms": [
                "뒷목에서 오른쪽 어깨와 아래팔 노측(radial side), 엄지 쪽으로 뻗치는 통증과 저림이 지속됨",
                "최근 팔꿉관절 굽힘(elbow flexion)과 손목 폄(wrist extension) 힘이 약해져 검사 의뢰됨"
            ],
            "physical_exam": {
                "이학적 검사결과": [
                    "팔꿉관절 굽힘 약화: 위팔두갈래근(biceps brachii), 근피신경(musculocutaneous nerve), 주로 C5-C6 수준",
                    "손목 폄 약화: 긴노쪽손목폄근/짧은노쪽손목폄근(extensor carpi radialis longus/brevis), 노신경(radial nerve), 주로 C6-C7 수준",
                    "아래팔 노측과 엄지 쪽 감각저하: 주로 C6 피부분절(dermatome)과 연관",
                    "위팔두갈래근힘줄반사(biceps tendon reflex) 감소, 위팔노근힘줄반사(brachioradialis reflex) 감소"
                ]
            }
        },
        "findings": {
            "노신경 표재감각신경활동전위 (Superficial Radial SNAP)": ("정상 (Normal)", "정상 (Normal)"),
            "가쪽아래팔피부신경 감각신경활동전위 (Lateral antebrachial cutaneous SNAP)": ("정상 (Normal)", "정상 (Normal)"),
            "근피신경 복합근육활동전위 (Musculocutaneous CMAP)": ("정상 (Normal)", "정상 (Normal)"),
            "노신경 복합근육활동전위 (Radial CMAP)": ("정상 (Normal)", "정상 (Normal)"),
            "목 척추주위근 (Cervical Paraspinal)": ("정상 (Normal)", "비정상 자발전위 출현 (Fibrillation Potential, Positive Sharp Wave 등)"),
            "위팔두갈래근 (Biceps Brachii)": ("정상 (Normal)", "비정상 자발전위 출현 (Fibrillation Potential, Positive Sharp Wave 등)"),
            "긴노쪽손목폄근/짧은노쪽손목폄근 (Extensor Carpi Radialis Longus/Brevis)": ("정상 (Normal)", "비정상 자발전위 출현 (Fibrillation Potential, Positive Sharp Wave 등)")
        },
        "teaching_diagnosis": {
            "summary": "이 사례는 목 신경뿌리병증(cervical radiculopathy), 특히 C6 중심 병변 가능성을 우선 생각하는 패턴입니다.",
            "ncs_reason": [
                "감각신경활동전위(sensory nerve action potential, SNAP)가 보존되어 있습니다. 신경뿌리병증(radiculopathy)에서는 병변이 뒤뿌리신경절(dorsal root ganglion)보다 근위부(proximal)에 있으면 말초 감각신경전도는 정상으로 남을 수 있습니다.",
                "노신경 표재감각분지(superficial radial)와 가쪽아래팔피부신경(lateral antebrachial cutaneous nerve)의 감각신경전도검사가 정상이라는 점은 감각저하가 있더라도 말초 감각신경 자체의 축삭 손상보다는 신경뿌리(root) 수준 병변 가능성을 높입니다.",
                "근피신경(musculocutaneous nerve) 및 노신경(radial nerve)의 말단 운동신경전도검사가 정상이라는 점도 단일신경병증(mononeuropathy)보다는 신경뿌리병증(radiculopathy) 해석에 더 잘 맞습니다."
            ],
            "emg_reason": [
                "목 척추주위근(cervical paraspinal muscle)에서 비정상 자발전위(abnormal spontaneous activity)가 보이는 것은 신경뿌리병증 해석에서 매우 중요한 단서입니다.",
                "위팔두갈래근(biceps brachii)과 노쪽손목폄근(extensor carpi radialis)에서 비정상 자발전위가 보여 C5-C6, C6-C7 분절과 관련된 탈신경(denervation) 변화 가능성을 의미합니다.",
                "여러 말초신경이 지배하는 근육에서 공통 분절 수준 이상이 보이면서 척추주위근까지 침범되면 신경뿌리병증 가능성이 더 높아집니다."
            ],
            "integration": [
                "증상은 C6 피부분절과 유사하고, 감각신경전도는 보존되며, 척추주위근과 관련 근육의 침근전도 이상이 동반됩니다.",
                "따라서 이 사례는 노신경병증(radial neuropathy)보다 C6 중심 목 신경뿌리병증(cervical radiculopathy)으로 해석하는 것이 더 적절합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "노신경병증 (Radial Neuropathy)",
                "why_consider": "손목 폄 약화와 아래팔 노측 불편감이 있어 처음에는 노신경병증을 떠올릴 수 있습니다.",
                "how_to_differentiate": "노신경병증이면 감각신경전도나 운동신경전도 이상과 같은 말초신경전도 이상이 더 잘 나타날 수 있습니다. 이 사례에서는 감각신경전도와 운동신경전도가 보존되고 목 척추주위근 이상이 있어 노신경병증보다 신경뿌리병증이 더 적절합니다.",
                "practical_tip": "노신경 감각지배 분포(radial nerve distribution) 증상과 C6 피부분절(C6 dermatome) 증상이 비슷해 보일 수 있다는 점을 기억해야 합니다."
            },
            {
                "name": "위팔신경얼기병증 (Upper Brachial Plexopathy)",
                "why_consider": "어깨 주변부터 아래팔까지 증상이 있고 근피신경·노신경 관련 근육이 함께 약화되면 위팔신경얼기(Upper brachial plexus) 병변도 생각할 수 있습니다.",
                "how_to_differentiate": "위팔신경얼기병증이면 가쪽아래팔피부신경(lateral antebrachial cutaneous nerve) 등 감각신경전도 이상이 나타날 가능성이 크고, 척추주위근은 보통 정상입니다. 이 사례는 감각신경전도가 보존되고 척추주위근 이상이 있어 신경얼기병증보다는 신경뿌리병증(radiculopathy)이 적절합니다.",
                "practical_tip": "감각신경전도 이상 유무와 척추주위근(paraspinal muscle) 침범 여부를 항상 같이 묶어서 비교해 보세요."
            }
        ]
    },

    "2. 야간 손저림과 엄지 근력 약화": {
        "patient": {
            "age": 46, "sex": "여", "side": "우",
            "symptoms": [
                "오른손 손바닥 쪽 엄지, 검지, 중지 중심의 저림이 반복됨",
                "야간에 증상이 심하며 최근 엄지 벌림(thumb abduction) 힘이 약해짐"
            ],
            "physical_exam": {
                "이학적 검사결과": [
                    "엄지 벌림 약화: 짧은엄지벌림근(abductor pollicis brevis), 정중신경(median nerve), C8-T1",
                    "엄지·검지·중지 및 반지손가락 노측 절반의 손바닥 쪽 감각저하: 정중신경 감각영역",
                    "팔렌검사(Phalen test): 양성반응(positive sign), 손목 티넬징후(Tinel sign): 양성반응(positive sign)"
                ]
            }
        },
        "findings": {
            "정중신경 감각신경활동전위 (Median SNAP)": ("정상 (Normal)", "잠복기 지연 (Delayed latency)"),
            "정중신경 복합근육활동전위 (Median CMAP)": ("정상 (Normal)", "잠복기 지연 (Delayed latency)"),
            "짧은엄지벌림근 (Abductor Pollicis Brevis, APB)": ("정상 (Normal)", "비정상 자발전위 출현 (Fibrillation Potential, Positive Sharp Wave 등)")
        },
        "teaching_diagnosis": {
            "summary": "이 사례는 손목굴증후군(carpal tunnel syndrome)을 우선 생각하는 전형적인 정중신경 포착병증(entrapment neuropathy) 패턴입니다.",
            "ncs_reason": [
                "정중신경 감각신경전도검사에서 잠복기 지연(delayed latency)이 보이는 것은 손목굴(carpal tunnel) 부위 말이집탈락(demyelinating) 변화 또는 국소 전도 지연을 의미합니다.",
                "정중신경 운동신경전도검사에서도 잠복기 지연이 보여 병변이 진행되어 운동섬유까지 영향을 주고 있음을 생각할 수 있습니다.",
                "이상 소견이 정중신경(median nerve)에 국한되어 있다는 점이 중요합니다."
            ],
            "emg_reason": [
                "짧은엄지벌림근(abductor pollicis brevis)에서 비정상 자발전위(abnormal spontaneous activity)가 보이면 손목굴증후군이 진행되어 엄지두덩(thenar eminence) 근육에 탈신경 변화가 생겼음을 의미합니다."
            ],
            "integration": [
                "야간 악화, 정중신경 감각영역 저림, 짧은엄지벌림근 약화, 정중신경 감각 및 운동 잠복기 지연이 함께 있어 손목굴증후군 해석이 가장 적절합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "C6-C7 목 신경뿌리병증 (C6-C7 Cervical Radiculopathy)",
                "why_consider": "손 저림과 엄지 쪽 증상 때문에 목 신경뿌리병증도 감별해야 합니다.",
                "how_to_differentiate": "목 신경뿌리병증이면 정중신경 감각신경전도가 정상일 수 있고, 목 척추주위근이나 근위부(proximal)의 침근전도 이상이 동반됩니다. 반면 이 사례는 정중신경 자체의 전도 지연이 분명하여 말초 포착병증 해석이 적절합니다.",
                "practical_tip": "손 저림만 보고 바로 손목굴증후군으로 단정하지 말고, 감각신경전도가 실제로 비정상인지 반드시 확인하세요."
            },
            {
                "name": "앞뼈사이신경증후군(Anterior Interosseous Syndrome) / 근위부 정중신경병증(Proximal Median Neuropathy)",
                "why_consider": "두 질환 모두 정중신경 관련 병변으로 임상 및 근전도 소견이 겹칠 수 있습니다.",
                "how_to_differentiate": "앞뼈사이신경증후군은 정중신경의 깊은 운동가지로 순수 운동성 병변이므로 보통 감각저하나 감각신경전도 이상이 없습니다. 근전도에서 앞팔(forearm)의 특정 운동근만 이상이 나오면 앞뼈사이신경증후군을 의심합니다. 근위부 정중신경병증은 팔꿈치나 앞팔 수준에서 운동(손목 굽힘근)과 감각이 모두 침범될 수 있어 감각증상과 감각신경전도 이상이 동반될 수 있습니다. 손목굴증후군은 손목에서의 원위부 정중신경병증으로 감각신경전도 지연과 엄지 벌림근의 운동신경전도 이상 또는 근전도 탈신경 소견이 흔합니다. 이 사례는 감각저하와 감각신경전도 이상이 있어 앞뼈사이신경증후군보다는 근위부 정중신경병증 또는 원위부 손목굴증후군이 더 적절합니다.",
                "practical_tip": "간단 규칙: 감각신경전도 이상이 있으면 앞뼈사이신경증후군 가능성은 낮고 근위부 정중신경병증 또는 손목굴증후군을 먼저 고려하세요. 손목굴증후군은 원위부 정중신경병증에 포함됩니다."
            }
        ]
    },

    "3. 위팔뼈 몸통 골절 후 손목처짐": {
        "patient": {
            "age": 34, "sex": "남", "side": "우",
            "symptoms": [
                "위팔뼈(humerus) 몸통(shaft) 골절 이후 손목과 손가락을 들어 올리지 못하는 손목처짐(wrist drop)이 발생함",
                "손등 노측(radial dorsum) 감각저하와 함께 손목 및 손가락 폄 약화가 뚜렷함"
            ],
            "physical_exam": {
                "이학적 검사결과": [
                    "손목 폄 약화: 손목폄근군(extensor carpi radialis / extensor digitorum), 노신경(radial nerve), C6-C7",
                    "손가락 폄 약화: 손가락폄근군(finger extensors), 노신경(radial nerve), C7-C8",
                    "손등 노측 감각저하: 노신경 표재감각분지(superficial radial sensory branch) 영역과 연관"
                ]
            }
        },
        "findings": {
            "노신경 표재감각신경활동전위 (Superficial Radial SNAP)": ("정상 (Normal)", "감소 (Reduced)"),
            "노신경 복합근육활동전위 (Radial CMAP)": ("정상 (Normal)", "감소 (Reduced)"),
            "손목폄근 (Extensor Carpi Radialis / Extensor Digitorum)": ("정상 (Normal)", "비정상 자발전위 출현 (Fibrillation Potential, Positive Sharp Wave 등)"),
            "집게폄근 (Extensor Indicis Proprius, EIP)": ("정상 (Normal)", "비정상 자발전위 출현 (Fibrillation Potential, Positive Sharp Wave 등)"),
            "목 척추주위근 (Cervical Paraspinal)": ("정상 (Normal)", "정상 (Normal)")
        },
        "teaching_diagnosis": {
            "summary": "이 사례는 위팔뼈 몸통 골절 뒤 발생한 노신경병증(radial neuropathy)에 전형적으로 맞습니다.",
            "ncs_reason": [
                "노신경 감각신경전도검사 이상은 병변이 신경뿌리보다 원위부(distal) 말초 노신경에 있음을 의미합니다.",
                "노신경 운동신경전도검사 이상은 운동축삭(motor axon) 손상 또는 의미 있는 전도차단(conduction block) 가능성을 의미합니다."
            ],
            "emg_reason": [
                "손목폄근(extensor carpi radialis)과 집게폄근(extensor indicis proprius)에서 비정상 자발전위가 보이는 것은 노신경 지배 근육의 탈신경 변화를 의미합니다.",
                "목 척추주위근(cervical paraspinal muscle)이 정상이라는 점은 목 신경뿌리병증(cervical radiculopathy)보다 말초 노신경병증(radial neuropathy) 해석에 더 잘 맞습니다."
            ],
            "integration": [
                "위팔뼈 골절 병력, 손목처짐, 노신경 감각영역 저하, 노신경 감각신경활동전위/복합근육활동전위(SNAP/CMAP) 진폭 감소, 노신경 지배 근육 침범이 함께 있어 노신경병증(radial neuropathy)이 가장 적절합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "뒤뼈사이신경병증 (Posterior Interosseous Neuropathy)",
                "why_consider": "손가락 폄 약화와 손목 폄 약화가 있으면 뒤뼈사이신경(posterior interosseous nerve) 병변도 떠올릴 수 있습니다.",
                "how_to_differentiate": "뒤뼈사이신경은 노신경의 주로 깊은 운동가지(deep motor branch)이므로 감각저하가 뚜렷하지 않고 표재감각신경활동전위(SNAP)도 보통 정상입니다. 이 사례는 손등 감각저하와 SNAP 감소가 있어 보다 근위부의 노신경병증이 적절합니다.",
                "practical_tip": "뚜렷한 감각저하가 있으면 뒤뼈사이신경(posterior interosseous nerve) 단독 병변만으로 설명하기 어렵습니다."
            },
            {
                "name": "C7 목 신경뿌리병증 (C7 Cervical Radiculopathy)",
                "why_consider": "손목 및 손가락 폄 약화 때문에 C7 신경뿌리병증을 생각할 수 있습니다.",
                "how_to_differentiate": "신경뿌리병증이면 말초 감각신경전도가 보존되는 경우가 많고, 목 척추주위근 이상이 동반될 수 있습니다. 이 사례는 SNAP가 감소하고 척추주위근이 정상이라 말초 노신경병증이 더 적절합니다.",
                "practical_tip": "감각신경전도 감소 여부와 척추주위근(paraspinal muscle) 침범 여부를 항상 함께 보세요."
            }
        ]
    },

    "4. 4, 5번째 손가락 저림과 손가락 근력 약화": {
        "patient": {
            "age": 42, "sex": "남", "side": "우",
            "symptoms": [
                "오른쪽 4, 5번째 손가락 저림과 손의 자측(ulnar side) 불편감이 있음",
                "최근 세밀한 손동작과 손가락 벌림/모음에서 힘이 빠지는 느낌이 생김"
            ],
            "physical_exam": {
                "이학적 검사결과": [
                    "새끼손가락 벌림 약화: 새끼벌림근(abductor digiti minimi), 자신경(ulnar nerve), C8-T1",
                    "손가락 벌림 약화: 첫째등쪽뼈사이근(first dorsal interosseous), 자신경(ulnar nerve), C8-T1",
                    "4번째, 5번째 손가락 및 손 자측 감각저하: 자신경(ulnar nerve) 감각영역",
                    "팔꿉관절 굽힘 검사(elbow flexion test): 양성반응(positive sign)"
                ]
            }
        },
        "findings": {
            "자신경 감각신경활동전위 (Ulnar SNAP)": ("정상 (Normal)", "잠복기 지연 (Delayed latency)"),
            "자신경 복합근육활동전위 (Ulnar CMAP)": ("정상 (Normal)", "잠복기 지연 (Delayed latency)"),
            "새끼벌림근 (Abductor Digiti Minimi, ADM)": ("정상 (Normal)", "비정상 자발전위 출현 (Fibrillation Potential, Positive Sharp Wave 등)"),
            "첫째등쪽뼈사이근 (First Dorsal Interosseous, FDI)": ("정상 (Normal)", "비정상 자발전위 출현 (Fibrillation Potential, Positive Sharp Wave 등)")
        },
        "teaching_diagnosis": {
            "summary": "이 사례는 팔꿉부 자신경병증(ulnar neuropathy at the elbow)을 우선 생각하는 전형적 패턴입니다.",
            "ncs_reason": [
                "자신경(ulnar nerve) 감각 및 운동 신경전도에서 잠복기 지연(delayed latency)이 보이는 것은 자신경 경로의 국소 전도 이상을 의미합니다.",
                "이상이 자신경에 집중되어 있다는 점이 중요합니다."
            ],
            "emg_reason": [
                "새끼벌림근(ADM)과 첫째등쪽뼈사이근(FDI)은 자신경 지배를 받는 대표적인 손 자체기원근육(intrinsic muscle)입니다.",
                "이 근육들에서 비정상 자발전위가 보이면 자신경병증이 진행되어 운동축삭 침범이 있음을 의미합니다."
            ],
            "integration": [
                "4번째, 5번째 손가락 저림, 자측 감각저하, 손 자체기원근육(intrinsic muscle) 약화, 자신경 전도 이상이 함께 있어 팔꿉부 자신경병증 해석이 가장 적절합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "C8-T1 목 신경뿌리병증 (C8-T1 Cervical Radiculopathy)",
                "why_consider": "손 자체기원근육(intrinsic muscle) 약화는 C8-T1 신경뿌리병증에서도 나타날 수 있습니다.",
                "how_to_differentiate": "목 신경뿌리병증이면 자신경 감각신경전도검사는 정상일 수 있고, 척추주위근 이상이나 자신경 이외의 C8-T1 지배 근육 침범이 중요합니다. 이 사례는 자신경 전도 이상이 명확하여 말초 자신경병증이 적절합니다.",
                "practical_tip": "감각신경전도가 정상인지 비정상인지 확인하는 것이 감별의 핵심입니다."
            },
            {
                "name": "가이온굴 증후군(Guyon's Canal Syndrome) / 손목 수준 자신경병증(Ulnar Neuropathy at Wrist)",
                "why_consider": "자신경병증이라는 점은 같으나 포착(entrapment) 부위가 다를 수 있습니다.",
                "how_to_differentiate": "손목 부위 자신경병증은 손등 감각저하(dorsal ulnar cutaneous nerve 영역)가 보통 나타나지 않습니다. 임상적으로 팔꿉관절 굽힘 검사 양성반응(positive sign), 손등 자측의 감각 침범 여부를 통해 팔꿉부 병변으로 구별할 수 있습니다.",
                "practical_tip": "자신경병증은 '팔꿈치인지 손목인지(elbow vs wrist)' 포착 위치를 추가로 구분해야 합니다."
            }
        ]
    },

    "5. 허리-다리 통증과 발처짐": {
        "patient": {
            "age": 61, "sex": "여", "side": "우",
            "symptoms": [
                "허리에서 우측 엉치, 종아리 가쪽, 발등으로 뻗치는 통증과 저림이 있음",
                "최근 걷다가 발끝이 걸리는 우측 발처짐(foot drop)이 심해짐"
            ],
            "physical_exam": {
                "이학적 검사결과": [
                    "발목 등굽힘(ankle dorsiflexion) 약화: 앞정강근(tibialis anterior), 깊은종아리신경(deep peroneal nerve), 주로 L4-L5",
                    "엄지발가락 폄(great toe extension) 약화: 긴엄지폄근(extensor hallucis longus),  깊은종아리신경(deep peroneal nerve), 주로 L5",
                    "종아리 가쪽과 발등 감각저하: 주로 L5 피부분절(dermatome)과 연관"
                ]
            }
        },
        "findings": {
            "얕은종아리신경 감각신경활동전위 (Superficial Peroneal SNAP)": ("정상 (Normal)", "정상 (Normal)"),
            "종아리신경 복합근육활동전위 (Peroneal CMAP)": ("정상 (Normal)", "정상 (Normal)"),
            "허리 척추주위근 (Lumbar Paraspinal)": ("정상 (Normal)", "비정상 자발전위 출현 (Fibrillation Potential, Positive Sharp Wave 등)"),
            "앞정강근 (Tibialis Anterior, TA)": ("정상 (Normal)", "비정상 자발전위 출현 (Fibrillation Potential, Positive Sharp Wave 등)"),
            "긴엄지폄근 (Extensor Hallucis Longus, EHL)": ("정상 (Normal)", "비정상 자발전위 출현 (Fibrillation Potential, Positive Sharp Wave 등)"),
            "중간볼기근 (Gluteus Medius)": ("정상 (Normal)", "비정상 자발전위 출현 (Fibrillation Potential, Positive Sharp Wave 등)")
        },
        "teaching_diagnosis": {
            "summary": "이 사례는 L5 허리 신경뿌리병증(lumbar radiculopathy, especially L5)을 우선 생각하는 패턴입니다.",
            "ncs_reason": [
                "얕은종아리신경 감각신경전도검사와 종아리신경 운동신경전도검사에서 정상으로 관찰되었습니다.",
                "신경뿌리병증에서는 말초 감각신경전도검사와 원위부 운동신경전도검사가 비교적 정상일 수 있습니다."
            ],
            "emg_reason": [
                "허리 척추주위근(lumbar paraspinal muscle)에서 비정상 자발전위가 보이는 것은 신경뿌리병증 해석에 중요합니다.",
                "앞정강근(tibialis anterior), 긴엄지폄근(extensor hallucis longus), 중간볼기근(gluteus medius)은 L5 신경뿌리의 지배를 받는 근육으로, 이들에서 비정상 자발전위가 보이면 L5 분절 침범을 의미합니다."
            ],
            "integration": [
                "L5 피부분절에 맞는 방사통(radiating pain), 감각신경전도 보존, 척추주위근 및 L5 관련 근육 침범이 함께 있어 L5 신경뿌리병증(L5 radiculopathy) 해석이 가장 적절합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "종아리신경병증 (Peroneal Neuropathy)",
                "why_consider": "발처짐(foot drop)과 발등 감각저하는 종아리신경병증에서도 가장 흔한 증상입니다.",
                "how_to_differentiate": "종아리신경병증이면 얕은종아리신경(감각신경) 전도 이상, 종아리신경(운동신경) 전도 이상이 보이며, 허리 척추주위근과 중간볼기근(gluteus medius)은 정상입니다. 이 사례는 감각신경활동전위/복합근육활동전위(SNAP/CMAP)가 보존되고 척추주위근/중간볼기근 이상이 있어 신경뿌리병증이 더 적절합니다.",
                "practical_tip": "발처짐 환자에서는 L5 신경뿌리병증(L5 radiculopathy)과 말초 종아리신경병증을 항상 감별(differentiation)해야 합니다."
            },
            {
                "name": "허리엉치신경얼기병증 (Lumbosacral Plexopathy)",
                "why_consider": "다리 여러 근육이 침범되면 신경얼기(plexus) 병변도 생각할 수 있습니다.",
                "how_to_differentiate": "신경얼기병증이면 말초 감각신경전도 감소가 나타날 수 있고, 척추주위근은 대체로 정상입니다. 이 사례는 감각신경전도 보존과 척추주위근 침범 때문에 신경뿌리병증이 더 적절합니다.",
                "practical_tip": "감각신경전도가 보존되고 척추주위근(paraspinal muscle)에 이상이 있으면 신경뿌리병증(radiculopathy) 가능성이 큽니다."
            }
        ]
    },

    "6. 정강뼈 골절로 석고붕대 후 발처짐과 발등 감각저하": {
        "patient": {
            "age": 31, "sex": "남", "side": "좌",
            "symptoms": [
                "정강이뼈 골절(tibia fracture) 후 석고붕대(cast)를 제거한 뒤 발목을 위로 들기 어려워짐",
                "좌측 발처짐(foot drop)과 발등 감각저하가 비교적 갑자기 나타남"
            ],
            "physical_exam": {
                "이학적 검사결과": [
                    "발목 등굽힘(ankle dorsiflexion) 약화: 앞정강근(tibialis anterior), 깊은종아리신경(deep peroneal nerve), L4-L5",
                    "엄지발가락 폄(great toe extension) 약화: 긴엄지폄근(extensor hallucis longus),깊은종아리신경(deep peroneal nerve), L5",
                    "발가쪽번짐(ankle eversion) 약화: 긴종아리근(peroneus longus), 얕은종아리신경(superficial peroneal nerve), L5-S1",
                    "종아리 가쪽과 발등 감각저하: 얕은종아리신경(superficial peroneal nerve) 감각영역과 연관"
                ]
            }
        },
        "findings": {
            "얕은종아리신경 감각신경활동전위 (Superficial Peroneal SNAP)": ("정상 (Normal)", "감소 (Reduced)"),
            "종아리신경 복합근육활동전위 (Peroneal CMAP)": ("정상 (Normal)", "감소 (Reduced)"),
            "앞정강근 (Tibialis Anterior, TA)": ("정상 (Normal)", "비정상 자발전위 출현 (Fibrillation Potential, Positive Sharp Wave 등)"),
            "긴종아리근 (Peroneus Longus)": ("정상 (Normal)", "비정상 자발전위 출현 (Fibrillation Potential, Positive Sharp Wave 등)"),
            "허리 척추주위근 (Lumbar Paraspinal)": ("정상 (Normal)", "정상 (Normal)")
        },
        "teaching_diagnosis": {
            "summary": "이 사례는 종아리뼈머리(fibular head) 부위 압박과 연관된 종아리신경병증(peroneal neuropathy)을 우선 생각하는 패턴입니다.",
            "ncs_reason": [
                "얕은종아리신경(감각신경) 전도 이상은 병변이 신경뿌리보다 원위부 말초 감각신경을 침범했음을 의미합니다.",
                "종아리신경(운동신경) 전도 이상은 종아리신경 운동축삭(motor axon) 손상 또는 전도장애를 의미합니다."
            ],
            "emg_reason": [
                "앞정강근(tibialis anterior)과 긴종아리근(peroneus longus)에서 비정상 자발전위가 보여 종아리신경 지배 근육의 탈신경 변화를 의미합니다.",
                "허리 척추주위근(lumbar paraspinal muscle)이 정상이라는 점은 L5 신경뿌리병증보다 종아리신경병증 해석에 더 잘 맞습니다."
            ],
            "integration": [
                "석고붕대 압박 병력, 급성 발처짐, 얕은종아리신경 감각신경전도검사 및 종아리신경 운동신경전도검사 이상, 척추주위근 정상 소견이 함께 있어 종아리신경병증(peroneal neuropathy)이 가장 적절합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "L5 허리 신경뿌리병증 (L5 Lumbar Radiculopathy)",
                "why_consider": "발처짐(foot drop)은 L5 신경뿌리병증에서도 흔히 나타납니다.",
                "how_to_differentiate": "L5 신경뿌리병증이면 감각신경전도가 보존되는 경우가 많고, 허리 척추주위근과 중간볼기근(gluteus medius) 등 다른 L5 지배 근육의 이상이 동반됩니다. 이 사례는 SNAP 감소와 척추주위근 정상 소견이 있어 말초 종아리신경병증이 더 적절합니다.",
                "practical_tip": "발처짐 감별의 핵심은 감각신경전도 감소 여부와 척추주위근(paraspinal muscle) 침범 여부입니다."
            }
        ]
    },

    "7. 골반 외상 후 다리 전반 근력 약화": {
        "patient": {
            "age": 45, "sex": "여", "side": "좌",
            "symptoms": [
                "골반 골절 수술 후 좌측 다리 전반의 근력 약화가 생김",
                "허벅지와 종아리의 넓은 범위 감각 둔화와 보행장애가 동반됨"
            ],
            "physical_exam": {
                "이학적 검사결과": [
                    "무릎 폄(knee extension) 약화: 가쪽넓은근(vastus lateralis), 넓적다리신경(femoral nerve), L2-L4",
                    "발목 등굽힘(ankle dorsiflexion) 약화: 관련근육=앞정강근(tibialis anterior), 깊은종아리신경(deep peroneal nerve), L4-L5",
                    "허벅지와 종아리의 넓은 범위 감각저하: 여러 말초신경 분포가 함께 침범된 양상"
                ]
            }
        },
        "findings": {
            "허리 척추주위근 (Lumbar Paraspinal)": ("정상 (Normal)", "정상 (Normal)"),
            "장딴지신경 감각신경활동전위 (Sural SNAP)": ("정상 (Normal)", "감소 (Reduced)"),
            "종아리신경 복합근육활동전위 (Peroneal CMAP)": ("정상 (Normal)", "감소 (Reduced)"),
            "넓적다리신경 복합근육활동전위 (Femoral CMAP)": ("정상 (Normal)", "감소 (Reduced)"),
            "가쪽넓은근 (Vastus Lateralis)": ("정상 (Normal)", "비정상 자발전위 출현 (Fibrillation Potential, Positive Sharp Wave 등)"),
            "앞정강근 (Tibialis Anterior, TA)": ("정상 (Normal)", "비정상 자발전위 출현 (Fibrillation Potential, Positive Sharp Wave 등)")
        },
        "teaching_diagnosis": {
            "summary": "이 사례는 허리엉치신경얼기병증(lumbosacral plexopathy)을 생각하기 좋은 교육용 패턴입니다.",
            "ncs_reason": [
                "장딴지신경(감각신경) 전도 이상은 감각신경 자체 침범을 시사하므로, 단순 신경뿌리병증(radiculopathy)보다 말초신경 또는 신경얼기(plexus) 수준 병변 가능성을 높입니다.",
                "종아리신경(운동신경) 전도 이상과 넓적다리신경(운동신경) 전도 이상이 함께 감소하는 것은 하나의 단일 말초신경 손상만으로 설명하기 어렵습니다."
            ],
            "emg_reason": [
                "가쪽넓은근(vastus lateralis)과 앞정강근(tibialis anterior)은 서로 다른 말초신경의 지배를 받지만, 이 사례에서는 함께 침범되어 있습니다.",
                "허리 척추주위근(lumbar paraspinal muscle)이 정상이라는 점은 신경뿌리병증보다는 신경얼기병증 해석에 더 잘 맞습니다."
            ],
            "integration": [
                "골반 외상 병력, 넓은 감각저하, 여러 말초신경에 걸친 운동 이상, 감각신경전도 감소, 척추주위근 정상 소견이 함께 있어 허리엉치신경얼기병증(lumbosacral plexopathy) 해석이 가장 적절합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "다발 허리 신경뿌리병증 (Multiple Lumbar Radiculopathies)",
                "why_consider": "다리 여러 분절에 걸친 약화와 감각 이상이 있으면 여러 신경뿌리가 동시에 침범된 다중 신경뿌리병증도 생각할 수 있습니다.",
                "how_to_differentiate": "다중 신경뿌리병증이면 말초 감각신경전도는 비교적 보존될 수 있고, 허리 척추주위근 이상이 나타날 가능성이 있습니다. 이 사례는 SNAP가 감소하고 척추주위근이 정상이라 신경얼기병증이 더 적절합니다.",
                "practical_tip": "감각신경전도 감소와 척추주위근(paraspinal muscle) 정상 소견이 함께 있으면 신경얼기병증(plexopathy)을 더 강하게 고려하세요."
            },
            {
                "name": "복합 다발단일신경병증 (Mononeuropathy Multiplex)",
                "why_consider": "여러 말초신경이 침범되었으므로 다발단일신경병증도 고려할 수 있습니다.",
                "how_to_differentiate": "골반 외상이라는 명확한 국소 손상 병력이 있으므로, 전신적인 원인에 의한 다발단일신경병증보다는 손상 부위인 허리엉치신경얼기(lumbosacral plexus) 병변으로 통합 해석하는 것이 자연스럽습니다.",
                "practical_tip": "여러 신경이 동시에 침범되면 해부학적으로 '공통 상위 구조(common proximal structure)'가 손상되었는지 먼저 확인하세요."
            }
        ]
    },

    "8. 양측 발끝 저림과 발가락 약화": {
        "patient": {
            "age": 67, "sex": "남", "side": "양측",
            "symptoms": [
                "당뇨병 병력이 오래되었고 양쪽 발끝 저림이 서서히 진행함",
                "최근 발가락 힘이 약해지고 보행 시 발의 감각이 둔해짐"
            ],
            "physical_exam": {
                "이학적 검사결과": [
                    "발가락 움직임 약화: 발가락 폄/굽힘 관련 근육 및 발 자체기원근육(intrinsic muscle), 종아리신경(peroneal nerve)/정강신경(tibial nerve), 주로 L5-S1",
                    "양측 발끝부터 시작되는 감각저하: 길이의존성(length-dependent) 말초신경 침범 양상",
                    "아킬레스힘줄반사(Achilles tendon reflex) 양측 감소 또는 소실"
                ]
            }
        },
        "findings": {
            "장딴지신경 감각신경활동전위 (Sural SNAP)": ("감소 (Reduced)", "감소 (Reduced)"),
            "얕은종아리신경 감각신경활동전위 (Superficial Peroneal SNAP)": ("감소 (Reduced)", "감소 (Reduced)"),
            "정강신경 복합근육활동전위 (Tibial CMAP)": ("감소 (Reduced)", "감소 (Reduced)")
        },
        "teaching_diagnosis": {
            "summary": "이 사례는 축삭성 다발신경병증(axonal polyneuropathy), 특히 당뇨병성 다발신경병증 패턴을 이해하기 좋은 예입니다.",
            "ncs_reason": [
                "양측 장딴지신경(sural) 및 얕은종아리신경(superficial peroneal) 감각신경전도 감소는 원위부 감각축삭(sensory axon) 손상을 의미합니다.",
                "양측 정강신경(tibial) 운동신경전도 감소는 운동축삭(motor axon)도 함께 침범되었을 가능성을 의미합니다.",
                "여러 신경에서 대칭적으로 양측성 진폭 감소(amplitude reduction)가 반복된다는 점이 핵심입니다."
            ],
            "emg_reason": [
                "축삭성 다발신경병증(axonal polyneuropathy)에서는 침근전도에서 원위부 근육 위주로 비정상 자발전위가 관찰될 수 있으나, 본 사례는 양측성 다발성 진폭 감소 패턴 자체가 더 핵심적인 교육 포인트입니다."
            ],
            "integration": [
                "대칭성, 원위부(distal) 우세, 감각신경과 운동신경의 양측성 진폭 감소가 함께 있어 축삭성 다발신경병증(axonal polyneuropathy)으로 해석하는 것이 적절합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "말이집탈락성 다발신경병증 (Demyelinating Polyneuropathy)",
                "why_consider": "다발신경병증이라는 큰 범주에서는 말이집탈락성 병변도 감별이 필요합니다.",
                "how_to_differentiate": "말이집탈락성 병변에서는 진폭 감소보다는 잠복기 지연(delayed latency), 전도속도 저하(slowed conduction velocity), F파 지연 등이 더 두드러집니다. 이 사례는 진폭 감소가 중심이어서 축삭성 패턴이 더 적절합니다.",
                "practical_tip": "전도 이상이 진폭 감소(amplitude drop) 중심이면 축삭성(axonal), 잠복기 지연(latency delay) 중심이면 말이집탈락성(demyelinating)으로 먼저 구분해 보세요."
            },
            {
                "name": "양측 허리 신경뿌리병증 (Bilateral Lumbar Radiculopathy)",
                "why_consider": "발의 감각저하와 근력 약화 양상 때문에 신경뿌리병증을 떠올릴 수 있습니다.",
                "how_to_differentiate": "신경뿌리병증은 대개 비대칭적이며, 양측 다발성으로 감각신경전도 감소가 동반되는 패턴으로 나타나기 어렵습니다.",
                "practical_tip": "증상이 '양측성 대칭성'이고 '원위부(glove-stocking 분포)' 패턴이라면 말초 다발신경병증(polyneuropathy)을 먼저 생각하세요."
            }
        ]
    },

    "9. 대칭성 팔다리 근력저하와 보행 저하": {
        "patient": {
            "age": 55, "sex": "여", "side": "양측",
            "symptoms": [
                "최근 양손과 양발이 대칭적으로 저리고 힘이 빠짐",
                "의자에서 일어나기와 계단 오르기가 점점 어려워짐"
            ],
            "physical_exam": {
                "이학적 검사결과": [
                    "원위부(distal)와 근위부(proximal)를 모두 포함한 대칭적 근력저하 관찰됨",
                    "양손과 양발의 대칭적 감각저하",
                    "깊은힘줄반사(deep tendon reflex) 전반적 감소 또는 소실"
                ]
            }
        },
        "findings": {
            "정중신경 감각신경활동전위 (Median SNAP)": ("잠복기 지연 (Delayed latency)", "잠복기 지연 (Delayed latency)"),
            "자신경 감각신경활동전위 (Ulnar SNAP)": ("잠복기 지연 (Delayed latency)", "잠복기 지연 (Delayed latency)"),
            "정중신경 복합근육활동전위 (Median CMAP)": ("정상 (Normal)", "잠복기 지연 (Delayed latency)"),
            "자신경 복합근육활동전위 (Ulnar CMAP)": ("정상 (Normal)", "잠복기 지연 (Delayed latency)"),
            "종아리신경 복합근육활동전위 (Peroneal CMAP)": ("잠복기 지연 (Delayed latency)", "잠복기 지연 (Delayed latency)"),
            "정강신경 F파 (Tibial F-wave)": ("지연 또는 소실 (Delayed/Absent)", "지연 또는 소실 (Delayed/Absent)")
        },
        "teaching_diagnosis": {
            "summary": "이 사례는 말이집탈락성 다발신경병증(demyelinating polyneuropathy) 패턴을 이해하기 좋은 예입니다.",
            "ncs_reason": [
                "여러 감각신경과 운동신경에서 양측성 잠복기 지연(delayed latency)이 반복됩니다.",
                "이상 소견의 중심이 진폭 감소보다는 잠복기 지연이라는 점이 말이집탈락성 패턴 해석에 매우 중요합니다.",
                "정강신경 F파 지연 또는 소실은 척수 인접 신경뿌리(root) 등 근위부 전도 이상을 시사하여 말이집탈락성 병변 가능성을 높입니다."
            ],
            "emg_reason": [
                "이 사례의 핵심은 침근전도 소견보다는 다수 신경의 전도 지연과 후기반사(F파) 이상 패턴에 있습니다."
            ],
            "integration": [
                "대칭성 감각·운동저하, 다수 신경의 양측성 잠복기 지연, F파 이상이 함께 있어 말이집탈락성 다발신경병증(demyelinating polyneuropathy) 해석이 가장 적절합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "축삭성 다발신경병증 (Axonal Polyneuropathy)",
                "why_consider": "다발신경병증 범주 안에서 가장 흔히 감별해야 할 대상입니다.",
                "how_to_differentiate": "축삭성 병변에서는 진폭 감소가 중심이 되는 경우가 많고, 말이집탈락성 병변에서는 잠복기 지연, 전도속도 저하, F파 지연이 더 두드러집니다. 이 사례는 지연 패턴이 중심이므로 말이집탈락성 병변에 가깝습니다.",
                "practical_tip": "신경전도검사에서 '진폭(amplitude) 감소인가, 잠복기(latency) 지연인가?'를 먼저 파악하세요."
            },
            {
                "name": "근육병증 (Myopathy)",
                "why_consider": "근위부를 포함한 대칭성 근력저하 때문에 일부 학생은 근육병증(myopathy)을 떠올릴 수 있습니다.",
                "how_to_differentiate": "근병증은 일차적으로 근육 자체의 병변이므로 감각신경전도 이상이나 심한 신경전도 지연, F파 이상으로 설명되지 않는 경우가 많습니다. 이 사례는 뚜렷한 신경전도 지연과 감각 이상이 있어 신경병증이 적절합니다.",
                "practical_tip": "감각 증상과 감각신경전도 이상이 동반되면 근병증(myopathy) 단독으로는 설명하기 어렵습니다."
            }
        ]
    },

    "10. 눈꺼풀 떨림과 눈 주위 불편감 지속": {
        "patient": {
            "age": 62, "sex": "여", "side": "우",
            "symptoms": [
                "우측 눈꺼풀 떨림과 눈 주위 불편감이 10일 이상 지속됨",
                "삼차신경-뇌줄기-얼굴신경 반사경로(trigeminal-brainstem-facial nerve reflex pathway) 평가를 위해 검사함"
            ],
            "physical_exam": {
                "이학적 검사결과": [
                    "우측 눈둘레근(orbicularis oculi) 주변 불편감 및 미세한 움직임 둔화 호소",
                    "우측 눈 주위 감각 이상 또는 불편감: 삼차신경(trigeminal nerve) V1 영역과 연관 가능"
                ]
            }
        },
        "findings": {
            "우측 자극-우측 R1": ("지연 (Delayed)", ""),
            "우측 자극-우측 R2": ("지연 또는 소실 (Delayed/Absent)", ""),
            "우측 자극-좌측 R2": ("지연 또는 소실 (Delayed/Absent)", ""),
            "좌측 자극-좌측 R1": ("정상 (Normal)", ""),
            "좌측 자극-좌측 R2": ("정상 (Normal)", ""),
            "좌측 자극-우측 R2": ("정상 (Normal)", "")
        },
        "teaching_diagnosis": {
            "summary": "이 사례는 눈깜빡반사(blink reflex) 검사를 통한 편측 반사경로 이상 가능성을 이해하기 위한 교육용 사례입니다.",
            "ncs_reason": [
                "이 사례의 핵심은 일반 사지 신경전도검사가 아닌 뇌신경 반사경로(cranial nerve reflex pathway) 평가입니다.",
                "우측 자극 시 우측 R1과 R2가 지연 또는 소실되고 좌측 자극 시 좌측 R1, R2가 정상인 점은, 자극이 들어가는 우측 들방향 경로(afferent pathway) 또는 뇌줄기 회로 일부의 편측 이상을 의미합니다."
            ],
            "emg_reason": [
                "이 사례는 침근전도보다 얼굴반사경로의 전기생리학적 해석이 핵심입니다."
            ],
            "integration": [
                "우측 눈 주위 증상과 우측 자극 눈깜빡반사(blink reflex) 이상이 일치하여, 삼차신경-뇌줄기-얼굴신경으로 이어지는 반사경로의 우측 편측 이상 가능성을 생각할 수 있습니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "얼굴신경병증 (Facial Neuropathy / Bell's Palsy)",
                "why_consider": "눈둘레근 움직임 이상이나 눈꺼풀 문제는 얼굴신경 병변과 흔히 연관됩니다.",
                "how_to_differentiate": "눈깜빡반사(blink reflex) 해석에서는 감각을 받아들이는 들방향(afferent, 삼차신경), 중추성(뇌줄기), 운동을 지시하는 날방향(efferent, 얼굴신경) 경로를 통합적으로 생각해야 합니다. 특정 반응(R1, R2 동측/반대측)의 소실 패턴에 따라 병변 위치를 세분화합니다.",
                "practical_tip": "눈깜빡반사는 단일 신경 검사가 아니라 반사 회로(reflex arc) 전체를 평가하는 검사라는 점을 기억하세요."
            }
        ]
    },

    "11. 뇌졸중 후 발목 발바닥굽힘근 경직 평가": {
        "patient": {
            "age": 68, "sex": "남", "side": "우",
            "symptoms": [
                "뇌졸중(stroke) 이후 우측 발목이 뻣뻣해지고 보행 시 발끝이 바닥에 잘 걸림",
                "치료 전후 발목 발바닥굽힘근(ankle plantar flexor)의 경직(spasticity) 변화를 정량적으로 평가하기 위해 검사함"
            ],
            "physical_exam": {
                "이학적 검사결과": [
                    "발목 발바닥굽힘근 경직(spasticity) 증가",
                    "아킬레스힘줄반사(Achilles tendon reflex) 항진 및 발목간대경련(ankle clonus) 관찰",
                    "우측 하지의 경직성 보행(spastic gait) 양상 관찰"
                ]
            }
        },
        "findings": {
            "정강신경 복합근육활동전위 (Tibial CMAP)": ("정상 (Normal)", "정상 (Normal)"),
            "H 반사 (우)": ("항진 또는 문턱값 감소 (Hyperactive / lower threshold)", ""),
            "H/M 비율": ("정상 범위보다 증가(0.60 초과, 교육용 기준)", "")
        },
        "teaching_diagnosis": {
            "summary": "이 사례는 질환 진단 목적보다는 중추신경계 손상 후 발생한 경직(spasticity)을 H 반사(H-reflex)와 H/M 비율로 어떻게 평가하는지 이해하는 데 초점이 있습니다.",
            "ncs_reason": [
                "정강신경 복합근육활동전위(tibial CMAP)는 정상으로 보존되어 있어 말초 운동신경 자체의 큰 손상은 없음을 의미합니다."
            ],
            "emg_reason": [
                "이 사례의 핵심은 침근전도보다 H 반사 항진(hyperactive)과 H/M 비율 증가(increased H/M ratio)입니다.",
                "교육용 기준에서 H/M 비율은 대체로 0.30~0.60 범위를 참고할 수 있으며, 0.60 초과는 척수 반사 흥분성 증가를 시사하는 정량적 참고 지표로 해석할 수 있습니다."
            ],
            "integration": [
                "뇌졸중 병력, 우측 다리 경직성 보행(spastic gait), 아킬레스 힘줄 반사 항진, H 반사 항진 및 H/M 비율 증가는 위운동신경세포(upper motor neuron, UMN) 병변으로 인한 척수 반사 흥분성(spinal reflex excitability) 증가를 나타냅니다."
            ]
        },     
    },

    "12. 급성 양측 다리 근력 약화": {
        "patient": {
            "age": 35, "sex": "남", "side": "양측",
            "symptoms": [
                "장염 이후 갑자기 양쪽 다리 힘이 빠져 앉았다 일어서기가 어려워짐",
                "빠르게 진행하는 양측 하지 근력저하로 검사 의뢰됨"
            ],
            "physical_exam": {
                "이학적 검사결과": [
                    "엉덩관절 굽힘(hip flexion) 약화: 엉덩허리근(iliopsoas), 주로 L2-L3",
                    "무릎 폄(knee extension) 약화: 넓적다리네갈래근(quadriceps femoris), 넓적다리신경(femoral nerve), L2-L4",
                    "원위부(distal) 감각저하는 아직 뚜렷하지 않거나 경미함",
                    "깊은힘줄반사(deep tendon reflex) 감소 또는 소실"
                ]
            }
        },
        "findings": {
            "정강신경 복합근육활동전위 (Tibial CMAP)": ("정상 (Normal)", "정상 (Normal)"),
            "종아리신경 복합근육활동전위 (Peroneal CMAP)": ("정상 (Normal)", "정상 (Normal)"),
            "정강신경 F파 (Tibial F-wave)": ("지연 또는 소실 (Delayed/Absent)", "지연 또는 소실 (Delayed/Absent)"),
            "종아리신경 F파 (Peroneal F-wave)": ("지연 또는 소실 (Delayed/Absent)", "지연 또는 소실 (Delayed/Absent)")
        },
        "teaching_diagnosis": {
            "summary": "이 사례는 초기 기엥-바레 증후군(Guillain-Barré syndrome, GBS) 또는 급성 염증성 다발신경병증(acute inflammatory polyneuropathy)을 떠올리게 하는 교육용 패턴입니다.",
            "ncs_reason": [
                "질환의 초기에는 말단 운동신경전도검사(distal CMAP)가 비교적 정상으로 나타날 수 있습니다.",
                "그러나 정강신경과 종아리신경의 F파(F-wave)가 양측에서 지연 또는 소실되면 신경뿌리 등 근위부 전도 이상 또는 초기 말이집탈락성(demyelinating) 병변 가능성을 강력히 의미합니다."
            ],
            "emg_reason": [
                "이 시기(급성기)에는 침근전도에서 비정상 자발전위가 나타나기 전이므로, 후기반사(F파, H 반사) 이상이 병변을 확인하는 데 더 빠르고 중요하게 쓰입니다."
            ],
            "integration": [
                "감염(장염) 후 급성 진행성 양측 근력 약화, 반사 저하, 그리고 양측 F파 이상이 함께 있어 초기 길랭-바레 증후군(GBS) 가능성을 고려하는 것이 적절합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "급성 근육병증 (Acute Myopathy) 또는 전해질 이상 연관 약화",
                "why_consider": "급성 양측 하지 근력 약화는 근육성 원인으로도 발생할 수 있습니다.",
                "how_to_differentiate": "근육병증에서는 깊은힘줄반사가 유지되는 경우가 많고, 특히 F파 지연이나 소실 같은 근위부 신경전도 이상으로 설명하기 어렵습니다. 이 사례는 뚜렷한 F파 이상이 있어 신경병증(neuropathy) 해석에 더 잘 맞습니다.",
                "practical_tip": "급성 대칭성 근력 약화 환자에서 F파 이상은 근위부 신경병증을 확인하게 해주는 매우 유용한 전기생리적 단서입니다."
            }
        ]
    }
}

def normalize_case_item_name(item_name):
    mapping = {
        "짧은엄지벌림근 (Abductor Pollicis Brevis, Abductor Pollics Brevis)": "짧은엄지벌림근 (Abductor Pollicis Brevis, APB)",
        "H 반사 (우측)": "H 반사 (우)",
        "H 반사 (좌측)": "H 반사 (좌)"
    }
    return mapping.get(item_name, item_name)

def compose_ncs_result(distal_amp, distal_lat, proximal_amp=None, proximal_lat=None):
    tags = []

    def build_segment_text(seg_name, amp, lat):
        if amp == "무반응 (No response)":
            return f"{seg_name} 무반응"

        parts = []
        if amp == "감소 (Reduced)":
            parts.append("진폭 감소")
        if lat == "잠복기 지연 (Delayed latency)":
            parts.append("잠복기 지연")

        if parts:
            return f"{seg_name} " + " 및 ".join(parts)
        return ""

    distal_text = build_segment_text("원위부", distal_amp, distal_lat)
    if distal_text:
        tags.append(distal_text)

    if proximal_amp is not None or proximal_lat is not None:
        proximal_text = build_segment_text("근위부", proximal_amp, proximal_lat)
        if proximal_text:
            tags.append(proximal_text)

    return "정상 (Normal)" if not tags else " / ".join(tags)

def compose_fwave_result(latency_status, response_status):
    latency_status = str(latency_status).strip()
    response_status = str(response_status).strip()

    if response_status == "소실 (Absent)":
        return "소실 (Absent)"
    if latency_status == "잠복기 지연 (Delayed latency)":
        return "지연 (Delayed)"
    return "정상 (Normal)"


def compute_hm_ratio_text(hmax, mmax):
    try:
        h = float(hmax)
        m = float(mmax)
        if m <= 0:
            return None, "계산 불가"
        ratio = h / m
        percent = ratio * 100
        return ratio, f"{ratio:.3f} ({percent:.1f}%)"
    except:
        return None, "계산 불가"

def interpret_hm_ratio(ratio):
    if ratio is None:
        return {
            "label": "계산 불가",
            "detail": "M파 최대 진폭(Mmax)이 0이거나 입력되지 않아 H/M 비율을 계산할 수 없습니다.",
            "warning": "※ H/M 비율은 교육용 참고 지표이며 단독으로 경직을 진단하지 않습니다."
        }

    if ratio == 0:
        return {
            "label": "낮음 또는 기록되지 않음",
            "detail": "H반사가 매우 작거나 기록되지 않은 상태일 수 있습니다. 측정 조건과 자극 강도를 함께 확인하세요.",
            "warning": "※ H/M 비율은 교육용 참고 지표이며 단독으로 경직을 진단하지 않습니다."
        }

    if ratio < 0.30:
        return {
            "label": "낮거나 뚜렷한 항진 소견 없음",
            "detail": "교육용 기준에서 H/M 비율이 낮은 편으로, 반사 흥분성 증가를 강하게 시사하지는 않습니다.",
            "warning": "※ 검사 자세, 근긴장도, 자극 강도에 따라 값이 달라질 수 있습니다."
        }

    if ratio <= 0.60:
        return {
            "label": "일반 범위 가능",
            "detail": "교육용 기준에서 일반 범위로 해석할 수 있습니다. 치료 전후 비교 시 동일 조건 유지가 중요합니다.",
            "warning": "※ 단독 수치보다 임상적 경직 소견과 함께 해석해야 합니다."
        }

    return {
        "label": "증가 가능",
        "detail": "교육용 기준에서 H/M 비율 증가 가능 범위로, 척수 반사 흥분성 증가 및 경직 관련 해석을 고려할 수 있습니다.",
        "warning": "※ 단독으로 경직을 확정할 수 없으며, 자세·자극 조건·임상 소견을 함께 봐야 합니다."
    }

def text_has_any(value, keywords):
    v = str(value).lower()
    return any(k.lower() in v for k in keywords)

def get_motor_stimulation_labels(item):
    label_map = {
        "정중신경 복합근육활동전위 (Median CMAP)": {
            "distal": "원위부 (wrist)",
            "proximal": "근위부 (elbow)"
        },
        "자신경 복합근육활동전위 (Ulnar CMAP)": {
            "distal": "원위부 (wrist)",
            "proximal": "근위부 (below elbow / elbow)"
        },
        "노신경 복합근육활동전위 (Radial CMAP)": {
            "distal": "원위부 (forearm)",
            "proximal": "근위부 (above elbow / arm)"
        },
        "겨드랑신경 복합근육활동전위 (Axillary CMAP)": {
            "distal": "원위부 (deltoid point / shoulder)",
            "proximal": "근위부 (Erb's point)"
        },
        "근피신경 복합근육활동전위 (Musculocutaneous CMAP)": {
            "distal": "원위부 (arm)",
            "proximal": "근위부 (Erb's point)"
        },
        "종아리신경 복합근육활동전위 (Peroneal CMAP)": {
            "distal": "원위부 (ankle)",
            "proximal": "근위부 (below fibular head / popliteal fossa)"
        },
        "깊은종아리신경 복합근육활동전위 (Deep Peroneal CMAP)": {
            "distal": "원위부 (ankle / dorsum foot)",
            "proximal": "근위부 (fibular head)"
        },
        "정강신경 복합근육활동전위 (Tibial CMAP)": {
            "distal": "원위부 (ankle)",
            "proximal": "근위부 (popliteal fossa)"
        },
        "넓적다리신경 복합근육활동전위 (Femoral CMAP)": {
            "distal": "원위부 (inguinal region)",
            "proximal": "근위부 (pelvic/upper inguinal course)"
        }
    }

    return label_map.get(item, {
        "distal": "원위부 (distal site)",
        "proximal": "근위부 (proximal site)"
    })

def get_compact_item_label(item):
    compact_map = {
        "정중신경 감각신경활동전위 (Median SNAP)": "정중신경 (Median)",
        "자신경 감각신경활동전위 (Ulnar SNAP)": "자신경 (Ulnar)",
        "노신경 감각신경활동전위 (Radial SNAP)": "노신경 (Radial)",
        "노신경 표재감각신경활동전위 (Superficial Radial SNAP)": "표재노신경 (Superficial Radial)",
        "가쪽아래팔피부신경 감각신경활동전위 (Lateral antebrachial cutaneous SNAP)": "가쪽아래팔피부신경 (Lateral antebrachial cutaneous)",

        "정중신경 복합근육활동전위 (Median CMAP)": "정중신경 (Median)",
        "자신경 복합근육활동전위 (Ulnar CMAP)": "자신경 (Ulnar)",
        "노신경 복합근육활동전위 (Radial CMAP)": "노신경 (Radial)",
        "겨드랑신경 복합근육활동전위 (Axillary CMAP)": "겨드랑신경 (Axillary)",
        "근피신경 복합근육활동전위 (Musculocutaneous CMAP)": "근피신경 (Musculocutaneous)",

        "장딴지신경 감각신경활동전위 (Sural SNAP)": "장딴지신경 (Sural)",
        "얕은종아리신경 감각신경활동전위 (Superficial Peroneal SNAP)": "얕은종아리신경 (Superficial Peroneal)",
        "두렁신경 감각신경활동전위 (Saphenous SNAP)": "두렁신경 (Saphenous)",
        "첫째 발가락사이 감각 (First Dorsal Web Space Sensation)": "첫째 발가락사이 감각 (First Dorsal Web Space)",

        "종아리신경 복합근육활동전위 (Peroneal CMAP)": "종아리신경 (Peroneal)",
        "깊은종아리신경 복합근육활동전위 (Deep Peroneal CMAP)": "깊은종아리신경 (Deep Peroneal)",
        "정강신경 복합근육활동전위 (Tibial CMAP)": "정강신경 (Tibial)",
        "넓적다리신경 복합근육활동전위 (Femoral CMAP)": "넓적다리신경 (Femoral)",

        "짧은엄지벌림근 (Abductor Pollicis Brevis, APB)": "짧은엄지벌림근 (Abductor Pollicis Brevis)",
        "첫째등쪽뼈사이근 (First Dorsal Interosseous, FDI)": "첫째등쪽뼈사이근 (First Dorsal Interosseous)",
        "새끼벌림근 (Abductor Digiti Minimi, ADM)": "새끼벌림근 (Abductor Digiti Minimi)",
        "집게폄근 (Extensor Indicis Proprius, EIP)": "집게폄근 (Extensor Indicis Proprius)",
        "손목폄근 (Extensor Carpi Radialis / Extensor Digitorum)": "손목폄근 (Extensor Carpi Radialis / Extensor Digitorum)",
        "가시아래근 (Infraspinatus)": "가시아래근 (Infraspinatus)",
        "삼각근 (Deltoid)": "삼각근 (Deltoid)",
        "위팔두갈래근 (Biceps Brachii)": "위팔두갈래근 (Biceps Brachii)",
        "위팔노근 (Brachioradialis)": "위팔노근 (Brachioradialis)",
        "긴노쪽손목폄근/짧은노쪽손목폄근 (Extensor Carpi Radialis Longus/Brevis)": "긴노쪽손목폄근/짧은노쪽손목폄근 (Extensor Carpi Radialis Longus/Brevis)",
        "원엎침근 (Pronator Teres)": "원엎침근 (Pronator Teres)",
        "위팔세갈래근 (Triceps Brachii)": "위팔세갈래근 (Triceps Brachii)",
        "목 척추주위근 (Cervical Paraspinal)": "목 척추주위근 (Cervical Paraspinal)",

        "앞정강근 (Tibialis Anterior, TA)": "앞정강근 (Tibialis Anterior)",
        "짧은발가락폄근 (Extensor Digitorum Brevis, EDB)": "짧은발가락폄근 (Extensor Digitorum Brevis)",
        "짧은발가락벌림근 (Abductor Digiti Minimi pedis)": "짧은발가락벌림근 (Abductor Digiti Minimi pedis)",
        "긴엄지폄근 (Extensor Hallucis Longus, EHL)": "긴엄지폄근 (Extensor Hallucis Longus)",
        "긴종아리근 (Peroneus Longus)": "긴종아리근 (Peroneus Longus)",
        "장딴지근 (Gastrocnemius)": "장딴지근 (Gastrocnemius)",
        "가자미근 (Soleus)": "가자미근 (Soleus)",
        "가쪽넓은근 (Vastus Lateralis)": "가쪽넓은근 (Vastus Lateralis)",
        "엉덩허리근 (Iliopsoas)": "엉덩허리근 (Iliopsoas)",
        "큰볼기근 (Gluteus Maximus)": "큰볼기근 (Gluteus Maximus)",
        "중간볼기근 (Gluteus Medius)": "중간볼기근 (Gluteus Medius)",
        "뒤넓적다리근 (Biceps Femoris)": "뒤넓적다리근 (Biceps Femoris)",
        "허리 척추주위근 (Lumbar Paraspinal)": "허리 척추주위근 (Lumbar Paraspinal)",

        "H 반사 (좌)": "H 반사 (좌)",
        "H 반사 (우)": "H 반사 (우)",
        "H/M 비율": "H/M 비율",

        "정중신경 F파 (Median F-wave)": "정중신경 (Median)",
        "자신경 F파 (Ulnar F-wave)": "자신경 (Ulnar)",
        "정강신경 F파 (Tibial F-wave)": "정강신경 (Tibial)",
        "종아리신경 F파 (Peroneal F-wave)": "종아리신경 (Peroneal)",

        "우측 자극-우측 R1": "우측 자극-우측 R1",
        "우측 자극-우측 R2": "우측 자극-우측 R2",
        "우측 자극-좌측 R2": "우측 자극-좌측 R2",
        "좌측 자극-좌측 R1": "좌측 자극-좌측 R1",
        "좌측 자극-좌측 R2": "좌측 자극-좌측 R2",
        "좌측 자극-우측 R2": "좌측 자극-우측 R2",
    }
    return compact_map.get(item, item)

def render_selected_item_detail_input(section, item, side, disabled=False):
    a = ANATOMY.get(item)
    if not a:
        return None

    rv = st.session_state.get("input_reset_version", 0)

    st.markdown(f'<div class="input-title">{get_compact_item_label(item)}</div>', unsafe_allow_html=True)
    st.markdown(
        f'<div class="input-meta">관련 신경: {a["nerve"]} | 관련 레벨: {simplify_level_text(a["level"])}</div>',
        unsafe_allow_html=True
    )

    row = None

    if a["domain"] == "h_reflex":
        c1, c2 = st.columns(2)
        hmax = c1.number_input("Hmax (mV)", min_value=0.0, value=0.0, step=0.1, key=f"hmax_{rv}_{item}", disabled=disabled)
        mmax = c2.number_input("Mmax (mV)", min_value=0.0, value=0.0, step=0.1, key=f"mmax_{rv}_{item}", disabled=disabled)

        ratio, ratio_text = compute_hm_ratio_text(hmax, mmax)
        hm_info = interpret_hm_ratio(ratio)

        st.markdown(f"<div class='mobile-note'>H/M 비율: {ratio_text}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='mobile-note'>{hm_info['label']} - {hm_info['detail']}</div>", unsafe_allow_html=True)

        if ratio is None:
            hm_interpret = "정상 (Normal)"
            h_status = "정상 (Normal)"
        else:
            if ratio > 0.60:
                hm_interpret = "증가 가능 (May be increased)"
                h_status = "항진 또는 문턱값 감소 (Hyperactive / lower threshold)"
            else:
                hm_interpret = "정상 (Normal)"
                h_status = "정상 (Normal)"

        row = {"section": section, "item": item, "left": h_status, "right": ""}
        hm_row = {"section": section, "item": "H/M 비율", "left": f"{hm_interpret} | 자동계산값: {ratio_text}", "right": ""}
        st.markdown('<hr class="item-divider">', unsafe_allow_html=True)
        return [row, hm_row]

    if a["domain"] == "h_ratio":
        return None

    if a["domain"] == "f_wave":
        c1, c2 = st.columns(2)
        latency_status = c1.selectbox(
            "잠복기",
            ["정상 (Normal)", "잠복기 지연 (Delayed latency)"],
            key=f"fw_lat_{rv}_{item}",
            disabled=disabled
        )
        response_status = c2.selectbox(
            "반응",
            ["출현 (Present)", "소실 (Absent)"],
            key=f"fw_resp_{rv}_{item}",
            disabled=disabled
        )
        lesion_res = compose_fwave_result(latency_status, response_status)

        if side == "양측":
            row = {"section": section, "item": item, "left": lesion_res, "right": lesion_res}
        elif side == "좌":
            row = {"section": section, "item": item, "left": lesion_res, "right": "정상 (Normal)"}
        else:
            row = {"section": section, "item": item, "left": "정상 (Normal)", "right": lesion_res}

    elif a["domain"] == "blink":
        res = st.selectbox("반응 결과", get_domain_options(a["domain"], item), key=f"blink_{rv}_{item}", disabled=disabled)
        row = {"section": section, "item": item, "left": res, "right": ""}

    elif a["domain"] == "reflex":
        res = st.selectbox("검사 결과", get_domain_options(a["domain"], item), key=f"res_{rv}_{item}", disabled=disabled)
        row = {"section": section, "item": item, "left": res, "right": ""}

    elif a["domain"] == "sensory":
        if side == "양측":
            st.markdown("**좌측**")
            c1, c2 = st.columns(2)
            left_amp = c1.selectbox("진폭", ["정상 (Normal)", "감소 (Reduced)", "무반응 (No response)"], key=f"sens_l_amp_{rv}_{item}", disabled=disabled)
            left_lat = c2.selectbox("잠복기", ["정상 (Normal)", "잠복기 지연 (Delayed latency)"], key=f"sens_l_lat_{rv}_{item}", disabled=disabled)

            st.markdown("**우측**")
            c3, c4 = st.columns(2)
            right_amp = c3.selectbox("진폭", ["정상 (Normal)", "감소 (Reduced)", "무반응 (No response)"], key=f"sens_r_amp_{rv}_{item}", disabled=disabled)
            right_lat = c4.selectbox("잠복기", ["정상 (Normal)", "잠복기 지연 (Delayed latency)"], key=f"sens_r_lat_{rv}_{item}", disabled=disabled)

            row = {
                "section": section,
                "item": item,
                "left": compose_ncs_result(left_amp, left_lat),
                "right": compose_ncs_result(right_amp, right_lat)
            }
        else:
            c1, c2 = st.columns(2)
            lesion_amp = c1.selectbox("진폭", ["정상 (Normal)", "감소 (Reduced)", "무반응 (No response)"], key=f"sens_amp_{rv}_{item}", disabled=disabled)
            lesion_lat = c2.selectbox("잠복기", ["정상 (Normal)", "잠복기 지연 (Delayed latency)"], key=f"sens_lat_{rv}_{item}", disabled=disabled)
            lesion_res = compose_ncs_result(lesion_amp, lesion_lat)

            if side == "좌":
                row = {"section": section, "item": item, "left": lesion_res, "right": "정상 (Normal)"}
            else:
                row = {"section": section, "item": item, "left": "정상 (Normal)", "right": lesion_res}

    elif a["domain"] == "motor":
        labels = get_motor_stimulation_labels(item)

        if side == "양측":
            c1, c2 = st.columns(2)
            left = c1.selectbox("좌측 결과", get_domain_options(a["domain"], item), key=f"ml_{rv}_{item}", disabled=disabled)
            right = c2.selectbox("우측 결과", get_domain_options(a["domain"], item), key=f"mr_{rv}_{item}", disabled=disabled)
            row = {"section": section, "item": item, "left": left, "right": right}
        else:
            c1, c2 = st.columns(2)
            distal_amp = c1.selectbox(f'{labels["distal"]} 진폭', ["정상 (Normal)", "감소 (Reduced)", "무반응 (No response)"], key=f"da_{rv}_{item}", disabled=disabled)
            distal_lat = c2.selectbox(f'{labels["distal"]} 잠복기', ["정상 (Normal)", "잠복기 지연 (Delayed latency)"], key=f"dl_{rv}_{item}", disabled=disabled)

            c3, c4 = st.columns(2)
            proximal_amp = c3.selectbox(f'{labels["proximal"]} 진폭', ["정상 (Normal)", "감소 (Reduced)", "무반응 (No response)"], key=f"pa_{rv}_{item}", disabled=disabled)
            proximal_lat = c4.selectbox(f'{labels["proximal"]} 잠복기', ["정상 (Normal)", "잠복기 지연 (Delayed latency)"], key=f"pl_{rv}_{item}", disabled=disabled)

            lesion_res = compose_ncs_result(distal_amp, distal_lat, proximal_amp, proximal_lat)

            if side == "좌":
                row = {"section": section, "item": item, "left": lesion_res, "right": "정상 (Normal)"}
            else:
                row = {"section": section, "item": item, "left": "정상 (Normal)", "right": lesion_res}

    elif a["domain"] == "muscle":
        if side == "양측":
            c1, c2 = st.columns(2)
            left = c1.selectbox("좌측 소견", get_domain_options(a["domain"], item), key=f"emg_l_{rv}_{item}", disabled=disabled)
            right = c2.selectbox("우측 소견", get_domain_options(a["domain"], item), key=f"emg_r_{rv}_{item}", disabled=disabled)
            row = {"section": section, "item": item, "left": left, "right": right}
        else:
            lesion_res = st.selectbox("침근전도 소견", get_domain_options(a["domain"], item), key=f"emg_{rv}_{item}", disabled=disabled)
            if side == "좌":
                row = {"section": section, "item": item, "left": lesion_res, "right": "정상 (Normal)"}
            else:
                row = {"section": section, "item": item, "left": "정상 (Normal)", "right": lesion_res}

    st.markdown('<hr class="item-divider">', unsafe_allow_html=True)
    return row

# ==========================================
# 3. 보조 함수
# ==========================================
def classify_finding_domain(item_name):
    normalized = normalize_case_item_name(item_name)
    anatomy = ANATOMY.get(normalized)
    if not anatomy:
        return "other"

    domain = anatomy.get("domain")

    if domain in ["sensory", "motor"]:
        return "ncs"
    if domain == "muscle":
        return "needle"
    if domain in ["reflex", "h_reflex", "h_ratio", "f_wave", "blink"]:
        return "reflex"

    return "other"

def get_domain_options(domain, item=None):
    if domain in ["sensory", "motor"]:
        return ["정상 (Normal)", "감소 (Reduced)", "잠복기 지연 (Delayed latency)", "무반응 (No response)"]

    if domain == "muscle":
        return [
            "정상 (Normal)",
            "비정상 자발전위 (Fibrillation, Positive sharp wave 등) 출현",
            "무반응 / 전기적 침묵 (Electrical silence)"
        ]

    if domain == "h_reflex":
        return ["정상 (Normal)"]

    if domain == "f_wave":
        return ["정상 (Normal)", "지연 (Delayed)", "소실 (Absent)"]

    if domain == "reflex":
        return ["정상 (Normal)", "지연 (Delayed)", "소실 (Absent)"]

    if domain == "blink":
        return ["정상 (Normal)", "지연 (Delayed)", "소실 (Absent)"]

    return ["정상 (Normal)"]

def is_abnormal(value):
    if value is None:
        return False
    value = str(value).strip().lower()
    if value == "" or value == "미선택":
        return False
    return value not in {"정상", "normal", "정상 (normal)"}

def normalize_result_text(value):
    if value is None:
        return ""
    text = str(value).strip()
    mapping = {
        "정상 (Normal)": "정상",
        "감소 (Reduced)": "진폭 감소",
        "잠복기 지연 (Delayed latency)": "잠복기 지연",
        "무반응 (No response)": "무반응",
        "감소 (Reduced) 및 잠복기 지연 (Delayed latency)": "진폭 감소 및 잠복기 지연",
        "비정상 자발전위 출현 (Fibrillation Potential, Positive Sharp Wave 등)": "비정상 자발전위 출현",
        "비정상 자발전위 (Fibrillation, Positive sharp wave 등) 출현": "비정상 자발전위 출현",
        "무반응 / 전기적 침묵 (Electrical silence)": "전기적 침묵",
        "지연 또는 소실 (Delayed/Absent)": "지연 또는 소실",
        "항진 또는 문턱값 감소 (Hyperactive / lower threshold)": "항진 또는 문턱값 감소",
        "증가 가능 (May be increased)": "증가 가능",
        "지연 (Delayed)": "지연",
        "양측 지연 또는 소실 (Bilateral delayed/absent)": "양측 지연 또는 소실"
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

def safe_index(options, value, default=0):
    return options.index(value) if value in options else default

def get_case_names_for_selection():
    return list(CASE_LIBRARY.keys())

def simplify_level_text(level_text):
    return level_text or ""

def build_diff_dx_details(dx_name):
    detail_map = {
        "손목굴증후군 포함 정중신경 포착병증 (Median Entrapment Neuropathy)": "정중신경 관련 감각 및 운동 잠복기 지연이 중심이면 손목굴 부위 정중신경 포착병증 가능성이 높습니다. 감별 시에는 C6-C7 신경뿌리병증처럼 SNAP가 보존되는 패턴인지, 또는 근위부 정중신경병증처럼 전완부 정중신경 지배 근육까지 더 넓게 침범하는지 함께 봐야 합니다.",
        "정중신경병증 (Median Neuropathy)": "이상 소견이 정중신경 관련 항목에 모여 있으면 정중신경병증을 생각합니다. 감별 시에는 C8-T1 신경뿌리병증에서는 SNAP가 보존될 수 있고, 아래팔신경얼기병증에서는 정중신경 외 다른 신경 분포 이상이 함께 나타날 수 있다는 점을 비교하세요.",
        "자신경병증 (Ulnar Neuropathy)": "이상 소견이 자신경 관련 항목에 모여 있으면 자신경병증을 생각합니다. 감별 시에는 C8-T1 신경뿌리병증에서 SNAP가 보존될 수 있고, 아래팔신경얼기병증에서는 자신경 외 정중신경 분포 이상이 함께 나타날 수 있다는 점을 비교하세요.",
        "팔꿈치부 자신경병증 (Ulnar Neuropathy at Elbow)": "자신경 관련 검사 이상과 손 intrinsic muscle 이상이 함께 있으면 팔꿈치부 자신경병증 가능성이 높습니다. 감별 시에는 손목 수준 자신경병증인지, 또는 C8-T1 신경뿌리병증처럼 SNAP 보존 패턴인지 함께 확인해야 합니다.",
        "노신경병증 (Radial Neuropathy)": "이상 소견이 노신경 관련 항목에 모여 있고 손목 또는 손가락 폄 약화가 동반되면 노신경병증 가능성이 높습니다. 감별 시에는 C7 신경뿌리병증처럼 SNAP가 보존되는지, 뒤뼈사이신경병증처럼 감각 이상 없이 운동 이상만 두드러지는지 비교하세요.",
        "종아리신경병증 (Peroneal Neuropathy)": "이상 소견이 종아리신경 관련 항목에 모여 있고 발처짐이 동반되면 종아리신경병증 가능성이 높습니다. 감별 시에는 L5 신경뿌리병증처럼 SNAP가 보존되는지, 허리 척추주위근이나 중간볼기근 침범이 있는지 함께 봐야 합니다.",
        "정강신경병증 (Tibial Neuropathy)": "이상 소견이 정강신경 관련 항목에 모여 있으면 정강신경병증을 생각합니다. 감별 시에는 S1 신경뿌리병증처럼 H반사 지연 또는 소실과 척추주위근 이상이 동반되는지 확인하세요.",
        "목 신경뿌리병증 (Cervical Radiculopathy)": "감각신경전도 이상은 뚜렷하지 않은데 목 척추주위근과 관련 근육에서 비정상 자발전위가 보이면 목 신경뿌리병증 가능성이 높습니다. 말초신경병증과 감별할 때는 SNAP 보존 여부와 척추주위근 침범이 핵심입니다.",
        "허리 신경뿌리병증 (Lumbar Radiculopathy)": "감각신경전도 이상은 뚜렷하지 않은데 허리 척추주위근과 관련 다리 근육에서 비정상 자발전위가 보이면 허리 신경뿌리병증 가능성이 높습니다. 종아리신경병증과 감별할 때는 SNAP 보존 여부, 중간볼기근/척추주위근 침범 여부를 함께 봐야 합니다.",
        "팔신경얼기병증 (Brachial Plexopathy)": "여러 팔 신경에 걸친 이상이 있지만 목 척추주위근 이상이 뚜렷하지 않으면 팔신경얼기병증을 생각할 수 있습니다. 신경뿌리병증과 달리 SNAP 이상이 동반될 수 있고, 단일 말초신경병증보다 더 넓은 분포를 보입니다.",
        "허리엉치신경얼기병증 (Lumbosacral Plexopathy)": "여러 다리 신경에 걸친 이상이 있지만 허리 척추주위근 이상이 뚜렷하지 않으면 허리엉치신경얼기병증을 생각할 수 있습니다. 신경뿌리병증과 달리 SNAP 감소가 동반될 수 있고, 단일 말초신경병증보다 넓은 분포를 보입니다.",
        "다발신경병증 (Polyneuropathy)": "여러 감각신경과 운동신경에서 양측성 이상이 보이면 다발신경병증 패턴에 가깝습니다. 해부학적으로 한 신경뿌리나 단일 말초신경만으로 설명되는지보다 대칭성과 길이의존성 여부가 중요합니다.",
        "축삭성 다발신경병증 (Axonal Polyneuropathy)": "여러 신경에서 진폭 감소가 중심이면 축삭성 다발신경병증 가능성이 높습니다. 감별 시에는 말이집탈락성 병변처럼 잠복기 지연이나 F파 이상이 주된 패턴인지 구분하세요.",
        "말이집탈락성 다발신경병증 (Demyelinating Polyneuropathy)": "여러 신경에서 잠복기 지연이 반복되면 말이집탈락성 신경병증 가능성을 생각합니다. 축삭성 병변보다 잠복기 지연, 전도속도 저하, F파 이상이 더 중요합니다.",
        "운동신경세포질환 가능성 (Motor Neuron Disease, correlate clinically)": "감각신경 이상은 뚜렷하지 않은데 여러 근육에서 비정상 자발전위가 보이면 운동신경세포질환도 감별해야 합니다. 다만 신경뿌리병증이나 다발신경병증과의 분포 차이를 함께 확인해야 합니다.",
        "S1 신경뿌리/근위부 정강신경 경로 이상 가능성": "H 반사 지연 또는 소실이 보이면 S1 신경뿌리 또는 근위부 정강신경 경로 이상 가능성을 생각할 수 있습니다. 중추성 경직처럼 항진이나 H/M 비율 증가가 중심인 경우와 구분해야 합니다.",
        "중추성 경직 / 위운동신경세포 병변 (Spasticity / UMN Lesion)": "H 반사 항진 또는 H/M 비율 증가가 보이면 경직과 관련된 척수 반사 흥분성 증가를 생각할 수 있습니다. 말초 S1 신경뿌리병증처럼 H 반사 지연 또는 소실이 중심인 경우와 구분하세요.",
        "근위부 말이집탈락 신경병증 / 초기 GBS 가능성": "여러 F파에서 지연 또는 소실이 보이면 근위부 말이집탈락 신경병증이나 초기 GBS 가능성을 생각할 수 있습니다. 급성 근육병증이나 전해질 이상은 이런 근위부 신경전도 이상으로 설명하기 어렵습니다.",
        "뇌줄기 반사경로 이상 가능성 (Brainstem reflex pathway involvement)": "양쪽 자극에서 눈깜빡반사 이상이 보이면 뇌줄기 반사경로 이상 가능성을 생각할 수 있습니다. 자극 방향과 반응 측을 함께 해석하여 구심성, 중추성, 원심성 경로를 구분하는 것이 중요합니다.",
        "삼차-뇌줄기-안면신경 반사경로의 편측 이상 가능성": "한쪽 자극에서 눈깜빡반사 이상이 두드러지면 해당 쪽 반사경로 이상 가능성을 생각할 수 있습니다. 자극 방향과 반응 측을 함께 해석하여 병변 위치를 더 세분화합니다.",
        "비특이적 이상 또는 추가 평가 필요 (Nonspecific)": "현재 입력된 정보만으로는 한 가지 질환으로 좁히기 어렵습니다. 병력, 이학적 검사, 추가 신경전도 및 침근전도 소견을 함께 봐야 합니다."
    }
    return detail_map.get(dx_name, "현재 입력된 검사 결과와 임상 정보를 함께 보고 감별해야 합니다.")

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

# ==========================================
# 4. 분석 엔진
# ==========================================
def analyze_case(age, sex, side, selected_rows):
    scores = defaultdict(int)
    reasons = []
    suggestions = set()
    lesion_tags = set()
    involved_nerves = set()
    involved_levels = set()
    top3_details = []

    sensory_abnormal = 0
    motor_abnormal = 0
    muscle_abnormal = 0
    reflex_abnormal = 0
    paraspinal_abnormal = 0

    no_response_count = 0
    delayed_count = 0
    reduced_count = 0
    spontaneous_count = 0

    arm_abnormal = 0
    leg_abnormal = 0
    face_abnormal = 0

    median_related = 0
    ulnar_related = 0
    radial_related = 0
    peroneal_related = 0
    tibial_related = 0
    femoral_related = 0

    arm_plexus_hint = 0
    leg_plexus_hint = 0
    neck_root_hint = 0
    low_back_root_hint = 0

    blink_right_stim_abnormal = 0
    blink_left_stim_abnormal = 0

    abnormal_items = []

    for row in selected_rows:
        item = normalize_case_item_name(row["item"])
        left = row.get("left", "")
        right = row.get("right", "")

        if not (is_abnormal(left) or is_abnormal(right)):
            continue
        if item not in ANATOMY:
            continue

        a = ANATOMY[item]
        involved_nerves.add(a["nerve"])
        involved_levels.add(simplify_level_text(a["level"]))

        if a["region"] == "arm":
            arm_abnormal += 1
        elif a["region"] == "leg":
            leg_abnormal += 1
        elif a["region"] == "face":
            face_abnormal += 1

        if a["domain"] == "sensory":
            sensory_abnormal += 1
        elif a["domain"] == "motor":
            motor_abnormal += 1
        elif a["domain"] == "muscle":
            muscle_abnormal += 1
        elif a["domain"] in ["reflex", "h_reflex", "h_ratio", "f_wave", "blink"]:
            reflex_abnormal += 1

        if "척추주위근" in item:
            paraspinal_abnormal += 1

        vals = [str(left).lower(), str(right).lower()]
        if any("감소" in v or "reduced" in v for v in vals):
            reduced_count += 1
        if any("지연" in v or "delayed" in v for v in vals):
            delayed_count += 1
        if any("무반응" in v or "no response" in v for v in vals):
            no_response_count += 1
        if any("자발전위" in v or "fib" in v or "psw" in v for v in vals):
            spontaneous_count += 1

        if "정중신경" in item or "짧은엄지벌림근" in item:
            median_related += 1
        if "자신경" in item or "첫째등쪽뼈사이근" in item or "새끼벌림근" in item:
            ulnar_related += 1
        if "노신경" in item or "집게폄근" in item or "손목폄근" in item or "위팔세갈래근" in item:
            radial_related += 1
        if "종아리신경" in item or "앞정강근" in item or "짧은발가락폄근" in item or "긴종아리근" in item or "깊은종아리신경" in item:
            peroneal_related += 1
        if "정강신경" in item or "장딴지근" in item or "가자미근" in item:
            tibial_related += 1
        if "넓적다리신경" in item or "가쪽넓은근" in item or "엉덩허리근" in item:
            femoral_related += 1

        if "가쪽아래팔피부신경" in item or "겨드랑신경" in item or "근피신경" in item:
            arm_plexus_hint += 1
        if "중간볼기근" in item or "큰볼기근" in item or "뒤넓적다리근" in item or "가쪽넓은근" in item:
            leg_plexus_hint += 1
        if "목 척추주위근" in item:
            neck_root_hint += 1
        if "허리 척추주위근" in item:
            low_back_root_hint += 1

        if item.startswith("우측 자극"):
            blink_right_stim_abnormal += 1
        if item.startswith("좌측 자극"):
            blink_left_stim_abnormal += 1

        abnormal_items.append({
            "항목": item,
            "신경": a["nerve"],
            "레벨": simplify_level_text(a["level"]),
            "결과": summarize_status(left, right, side)
        })

    total_abnormal = sensory_abnormal + motor_abnormal + muscle_abnormal + reflex_abnormal

    if sensory_abnormal == 0 and muscle_abnormal >= 2 and neck_root_hint >= 1:
        scores["목 신경뿌리병증 (Cervical Radiculopathy)"] += 10
        lesion_tags.add("신경뿌리 수준")
        reasons.append("이상 소견이 목 척추주위근과 관련 상지 근육에 분포하고, 감각신경전도 이상은 뚜렷하지 않아 목 신경뿌리병증 가능성이 높습니다.")
        suggestions.add("목 MRI 및 신경학적 진찰과 함께 해석하면 도움이 됩니다.")

    if sensory_abnormal == 0 and muscle_abnormal >= 2 and low_back_root_hint >= 1:
        scores["허리 신경뿌리병증 (Lumbar Radiculopathy)"] += 10
        lesion_tags.add("신경뿌리 수준")
        reasons.append("이상 소견이 허리 척추주위근과 관련 하지 근육에 분포하고, 감각신경전도 이상은 뚜렷하지 않아 허리 신경뿌리병증 가능성이 높습니다.")
        suggestions.add("허리 MRI 및 분절별 근력검사와 함께 해석하면 도움이 됩니다.")

    if sensory_abnormal >= 1 and muscle_abnormal >= 2 and paraspinal_abnormal == 0 and arm_plexus_hint >= 1:
        scores["팔신경얼기병증 (Brachial Plexopathy)"] += 9
        lesion_tags.add("신경얼기 수준")
        reasons.append("이상 소견이 여러 팔 신경에 걸쳐 있으나 목 척추주위근 이상은 뚜렷하지 않아 팔신경얼기병증 가능성을 생각할 수 있습니다.")

    if sensory_abnormal >= 1 and muscle_abnormal >= 2 and paraspinal_abnormal == 0 and leg_plexus_hint >= 1:
        scores["허리엉치신경얼기병증 (Lumbosacral Plexopathy)"] += 9
        lesion_tags.add("신경얼기 수준")
        reasons.append("이상 소견이 여러 다리 신경에 걸쳐 있으나 허리 척추주위근 이상은 뚜렷하지 않아 허리엉치신경얼기병증 가능성을 생각할 수 있습니다.")

    if median_related >= 2 and arm_abnormal <= 6:
        scores["정중신경병증 (Median Neuropathy)"] += 7
        lesion_tags.add("단일 말초신경 수준")
        reasons.append("이상 소견이 정중신경 관련 항목에 모여 있어 단일 말초신경 수준의 정중신경병증 가능성이 높습니다.")

    if ulnar_related >= 2 and arm_abnormal <= 6:
        scores["자신경병증 (Ulnar Neuropathy)"] += 7
        lesion_tags.add("단일 말초신경 수준")
        reasons.append("이상 소견이 자신경 관련 항목에 모여 있어 단일 말초신경 수준의 자신경병증 가능성이 높습니다.")

    if radial_related >= 2 and arm_abnormal <= 6:
        scores["노신경병증 (Radial Neuropathy)"] += 7
        lesion_tags.add("단일 말초신경 수준")
        reasons.append("이상 소견이 노신경 관련 항목에 모여 있어 단일 말초신경 수준의 노신경병증 가능성이 높습니다.")

    if peroneal_related >= 2 and leg_abnormal <= 7:
        scores["종아리신경병증 (Peroneal Neuropathy)"] += 8
        lesion_tags.add("단일 말초신경 수준")
        reasons.append("이상 소견이 종아리신경 관련 항목에 모여 있어 단일 말초신경 수준의 종아리신경병증 가능성이 높습니다.")

    if tibial_related >= 2 and leg_abnormal <= 7:
        scores["정강신경병증 (Tibial Neuropathy)"] += 6
        lesion_tags.add("단일 말초신경 수준")
        reasons.append("이상 소견이 정강신경 관련 항목에 모여 있어 단일 말초신경 수준의 정강신경병증 가능성이 높습니다.")

    if median_related >= 2 and delayed_count >= 1:
        scores["손목굴증후군 포함 정중신경 포착병증 (Median Entrapment Neuropathy)"] += 8
        reasons.append("이상 소견 중 정중신경 관련 감각 또는 운동 잠복기 지연이 보여 손목굴 부위 정중신경 포착병증 가능성을 생각할 수 있습니다.")

    if ulnar_related >= 2 and delayed_count >= 1:
        scores["팔꿈치부 자신경병증 (Ulnar Neuropathy at Elbow)"] += 7
        reasons.append("이상 소견 중 자신경 관련 잠복기 지연이 보여 팔꿈치부 자신경병증 가능성을 생각할 수 있습니다.")

    if sensory_abnormal >= 2 and (motor_abnormal >= 1 or side == "양측"):
        scores["다발신경병증 (Polyneuropathy)"] += 10
        lesion_tags.add("다발 말초신경 수준")
        reasons.append("이상 소견이 여러 감각신경과 운동신경에 양측성으로 분포하여 다발신경병증 패턴에 가깝습니다.")

    if delayed_count >= 3 and reduced_count <= delayed_count:
        scores["말이집탈락성 다발신경병증 (Demyelinating Polyneuropathy)"] += 7
        lesion_tags.add("말이집탈락 신경병증 패턴")
        reasons.append("이상 소견의 중심이 진폭 감소보다 잠복기 지연이어서 말이집탈락 신경병증 가능성을 생각할 수 있습니다.")

    if reduced_count >= 3 and sensory_abnormal >= 2:
        scores["축삭성 다발신경병증 (Axonal Polyneuropathy)"] += 6
        reasons.append("이상 소견의 중심이 여러 신경의 진폭 감소여서 축삭성 다발신경병증 가능성을 생각할 수 있습니다.")

    h_reflex_abnormal = 0
    h_reflex_hyperactive = 0
    f_wave_abnormal = 0
    hm_ratio_increased = 0

    for row in selected_rows:
        normalized_item = normalize_case_item_name(row["item"])
        left = str(row.get("left", "")).lower()
        right = str(row.get("right", "")).lower()
        combined = left + " " + right

        if normalized_item in ["H 반사 (좌)", "H 반사 (우)"]:
            if "지연" in combined or "소실" in combined or "absent" in combined:
                h_reflex_abnormal += 1
            if "항진" in combined or "문턱값 감소" in combined or "hyperactive" in combined:
                h_reflex_hyperactive += 1

        if normalized_item == "H/M 비율":
            if "증가" in combined:
                hm_ratio_increased += 1

        if "f-wave" in normalized_item.lower():
            if "지연" in combined or "소실" in combined or "absent" in combined or "delayed" in combined:
                f_wave_abnormal += 1

    if h_reflex_abnormal >= 1 and tibial_related >= 1:
        scores["S1 신경뿌리/근위부 정강신경 경로 이상 가능성"] += 5
        reasons.append("이상 소견 중 H 반사 지연 또는 소실이 보여 S1 신경뿌리 또는 근위부 정강신경 경로 이상 가능성을 생각할 수 있습니다.")

    if h_reflex_hyperactive >= 1 or hm_ratio_increased >= 1:
        scores["중추성 경직 / 위운동신경세포 병변 (Spasticity / UMN Lesion)"] += 8
        lesion_tags.add("척수 반사 흥분성 증가")
        reasons.append("이상 소견 중 H 반사 항진 또는 H/M 비율 증가가 보여 경직과 관련된 척수 반사 흥분성 증가를 생각할 수 있습니다.")

    if f_wave_abnormal >= 2:
        scores["근위부 말이집탈락 신경병증 / 초기 GBS 가능성"] += 7
        reasons.append("이상 소견 중 여러 F파의 지연 또는 소실이 보여 근위부 말이집탈락 신경병증이나 초기 GBS 가능성을 생각할 수 있습니다.")

    if blink_right_stim_abnormal >= 1 and blink_left_stim_abnormal >= 1:
        scores["뇌줄기 반사경로 이상 가능성 (Brainstem reflex pathway involvement)"] += 5
        reasons.append("이상 소견이 양쪽 자극의 눈깜빡반사에 걸쳐 있어 뇌줄기 반사경로 이상 가능성을 생각할 수 있습니다.")
    elif blink_right_stim_abnormal >= 1 or blink_left_stim_abnormal >= 1:
        scores["삼차-뇌줄기-안면신경 반사경로의 편측 이상 가능성"] += 4
        reasons.append("이상 소견이 한쪽 자극의 눈깜빡반사에 두드러져 해당 쪽 반사경로 이상 가능성을 생각할 수 있습니다.")

    if not scores:
        scores["비특이적 이상 또는 추가 평가 필요 (Nonspecific)"] = 1
        reasons.append("현재 입력된 검사 정보만으로는 병변 위치를 한 가지로 명확히 좁히기 어렵습니다.")

    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    final_dx = ranked[0][0]

    preferred_diff_map = {
        "정중신경병증 (Median Neuropathy)": [
            "손목굴증후군 포함 정중신경 포착병증 (Median Entrapment Neuropathy)",
            "목 신경뿌리병증 (Cervical Radiculopathy)",
            "팔신경얼기병증 (Brachial Plexopathy)"
        ],
        "손목굴증후군 포함 정중신경 포착병증 (Median Entrapment Neuropathy)": [
            "정중신경병증 (Median Neuropathy)",
            "목 신경뿌리병증 (Cervical Radiculopathy)",
            "팔신경얼기병증 (Brachial Plexopathy)"
        ],
        "자신경병증 (Ulnar Neuropathy)": [
            "팔꿈치부 자신경병증 (Ulnar Neuropathy at Elbow)",
            "목 신경뿌리병증 (Cervical Radiculopathy)",
            "팔신경얼기병증 (Brachial Plexopathy)"
        ],
        "팔꿈치부 자신경병증 (Ulnar Neuropathy at Elbow)": [
            "자신경병증 (Ulnar Neuropathy)",
            "목 신경뿌리병증 (Cervical Radiculopathy)",
            "팔신경얼기병증 (Brachial Plexopathy)"
        ],
        "노신경병증 (Radial Neuropathy)": [
            "목 신경뿌리병증 (Cervical Radiculopathy)",
            "팔신경얼기병증 (Brachial Plexopathy)"
        ],
        "종아리신경병증 (Peroneal Neuropathy)": [
            "허리 신경뿌리병증 (Lumbar Radiculopathy)",
            "허리엉치신경얼기병증 (Lumbosacral Plexopathy)"
        ],
        "정강신경병증 (Tibial Neuropathy)": [
            "허리 신경뿌리병증 (Lumbar Radiculopathy)",
            "S1 신경뿌리/근위부 정강신경 경로 이상 가능성"
        ]
    }

    score_dict = dict(ranked)
    diff_names = []

    for name in preferred_diff_map.get(final_dx, []):
        if name != final_dx and name not in diff_names:
            diff_names.append(name)

    for name, _ in ranked:
        if name != final_dx and name not in diff_names:
            diff_names.append(name)

    top3_names = [final_dx] + diff_names[:2]

    for dx in top3_names:
        top3_details.append({
            "name": dx,
            "how_to_differentiate": build_diff_dx_details(dx)
        })

    top3 = [(dx, score_dict.get(dx, 0)) for dx in top3_names]

    return {
        "age": age,
        "sex": sex,
        "side": side,
        "final_dx": final_dx,
        "top3": top3,
        "top3_details": top3_details,
        "severity": severity_text(total_abnormal, no_response_count),
        "lesion_tags": sorted(lesion_tags),
        "reasons": reasons,
        "suggestions": sorted(suggestions),
        "involved_nerves": ", ".join(sorted(involved_nerves)) if involved_nerves else "특이 소견 없음",
        "involved_levels": ", ".join(sorted(involved_levels)) if involved_levels else "특이 소견 없음",
        "abnormal_items": abnormal_items,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

# ==========================================
# 5. 상태 관리
# ==========================================
def init_app_state():
    defaults = {
        "current_screen": "home",
        "app_mode": MODE_CASE,
        "confirmed_case": None,
        "age": 50,
        "sex": "미선택",
        "side": "미선택",
        "last_result": None,
        "input_reset_version": 0,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

def reset_all_inputs():
    st.session_state["input_reset_version"] += 1
    st.session_state["last_result"] = None

def clear_result():
    st.session_state["last_result"] = None

# ==========================================
# 6. UI 렌더링
# ==========================================
def render_header():
    st.markdown('<div class="main-title">교육용 근전도 판독 보조 앱</div>', unsafe_allow_html=True)

def render_navigation_controls(position="top"):
    current_screen = st.session_state.get("current_screen", "home")
    if current_screen == "home":
        return

    st.markdown('<div class="top-bottom-nav-space"></div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)

    with c1:
        if st.button("🏠 처음으로", key=f"home_btn_{position}", use_container_width=True):
            st.session_state["current_screen"] = "home"
            st.session_state["confirmed_case"] = None
            clear_result()
            st.rerun()

    with c2:
        if st.button("⬅️ 이전으로", key=f"back_btn_{position}", use_container_width=True):
            if current_screen == "case_detail":
                st.session_state["current_screen"] = "mode"
                st.session_state["confirmed_case"] = None
            elif current_screen == "direct_input":
                st.session_state["current_screen"] = "mode"
            elif current_screen == "mode":
                st.session_state["current_screen"] = "home"
            clear_result()
            st.rerun()

    st.markdown("<hr/>", unsafe_allow_html=True)

def render_home_screen():
    render_header()
    st.markdown('<div class="subtle">물리치료학과 학생의 근전도 사례 학습과 기본 해석 훈련을 위한 교육용 앱입니다.</div>', unsafe_allow_html=True)

    st.markdown('<div class="warn-card">', unsafe_allow_html=True)
    st.markdown("### 📌 학습 안내")
    st.markdown('<div class="case-bullet">• 사례 학습: 근력 약화, 감각저하, 보행 문제 등 대표 임상양상과 신경전도·침근전도 소견을 연결하는 훈련을 합니다.</div>', unsafe_allow_html=True)
    st.markdown('<div class="case-bullet">• 검사 정보 입력 학습: 판독지의 이상 소견을 직접 선택하여 병변 위치와 질환을 추론합니다.</div>', unsafe_allow_html=True)
    st.markdown('<div class="case-bullet">• 본 앱은 학생 교육용 시뮬레이터이며 실제 임상 진단을 대체하지 않습니다.</div>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("### 진행할 학습 모드 선택")
    selected_mode = st.radio(
        "진행할 학습 모드를 선택하세요",
        [MODE_CASE, MODE_DIRECT],
        label_visibility="collapsed"
    )

    if selected_mode == MODE_CASE:
        st.markdown("""
        <div class="section-hint">
        <b>사례 학습</b><br>
        증상과 근전도 소견을 바탕으로 진단과 감별 포인트를 익히는 모드입니다.
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="section-hint">
        <b>검사 정보 입력 학습</b><br>
        판독지의 결과를 입력하면, 진단명과 병변 위치 및 감별진단이 자동으로 출력되어 학습하는 모드입니다.
        </div>
        """, unsafe_allow_html=True)

    if st.button("학습시작", type="primary", use_container_width=True):
        st.session_state["app_mode"] = selected_mode
        st.session_state["current_screen"] = "mode"
        clear_result()
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)    

def render_case_selector_only():
    case_options = get_case_names_for_selection()

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="case-section-label">📖 대표 사례 선택</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="mobile-note">증상 분포와 근력 약화를 보고 병변이 신경뿌리인지 말초신경인지 먼저 추론해 보세요.</div>',
        unsafe_allow_html=True
    )

    selected_case = st.radio(
        "대표 사례 선택",
        case_options,
        label_visibility="collapsed"
    )

    if st.button("사례 학습 시작", type="primary", use_container_width=True):
        st.session_state["confirmed_case"] = selected_case
        st.session_state["current_screen"] = "case_detail"
        clear_result()
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

def render_direct_entry_start():
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("### 🧾 검사 입력 학습 시작")
    st.markdown('<div class="mobile-note">학생이 판독지의 이상 소견만 선택하여 병변 위치와 질환을 추론하는 학습 모드입니다.</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="section-hint">
    <b>입력 전 추천 해석 순서</b><br>
    1) 감각신경전도검사에서 감각신경전도 이상이 있는지 본다.<br>
    2) 운동신경전도검사에서 진폭 감소인지 잠복기 지연인지 구분한다.<br>
    3) 침근전도검사에서 비정상 자발전위가 어떤 근육에 있는지 본다.<br>
    4) 척추주위근 이상 여부를 통해 신경뿌리병증 가능성을 생각한다.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
    st.markdown("**1) 기본 정보 입력**")

    age = st.number_input("나이", min_value=1, max_value=120, value=int(st.session_state.get("age", 50)), step=1)
    sex = st.selectbox("성별", SEX_OPTIONS, index=safe_index(SEX_OPTIONS, st.session_state.get("sex", "미선택")))
    side = st.selectbox("병변측", SIDE_OPTIONS, index=safe_index(SIDE_OPTIONS, st.session_state.get("side", "미선택")))

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
    st.markdown("**2) 학습 안내**")
    st.markdown('<div class="case-bullet">• 이상 소견이 있는 항목만 체크해서 입력합니다.</div>', unsafe_allow_html=True)
    st.markdown('<div class="case-bullet">• 체크하지 않은 항목은 정상으로 처리됩니다.</div>', unsafe_allow_html=True)
    st.markdown('<div class="case-bullet">• 운동신경전도는 원위부와 근위부 결과를 함께 입력할 수 있습니다.</div>', unsafe_allow_html=True)
    st.markdown('<div class="case-bullet">• 현재 앱은 학생 교육용이므로 이해하기 쉬운 대표 해석 중심으로 결과를 제공합니다.</div>', unsafe_allow_html=True)

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
    if st.button("세부 입력 화면으로 이동", type="primary", use_container_width=True):
        if sex == "미선택" or side == "미선택":
            st.warning("성별과 병변측을 선택하세요.")
        else:
            st.session_state["age"] = age
            st.session_state["sex"] = sex
            st.session_state["side"] = side
            st.session_state["current_screen"] = "direct_input"
            clear_result()
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

def render_case_learning_info(case_name):
    case = CASE_LIBRARY.get(case_name)
    if not case:
        st.warning("선택한 사례 정보를 찾을 수 없습니다.")
        return

    patient = case.get("patient", {})
    findings = case.get("findings", {})
    physical_exam = patient.get("physical_exam", {})

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown(f'<div class="case-title-mobile">📘 {case_name}</div>', unsafe_allow_html=True)
    st.markdown(
        f'<div class="case-subtitle-mobile">연령: {patient.get("age", "-")}세 | 성별: {patient.get("sex", "-")} | 병변측: {patient.get("side", "-")}</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="warn-card">
        <div class="finding-item-title">학생용 사고 프레임</div>
        <div class="case-bullet">• 증상이 피부분절 분포인지, 말초신경 분포인지 먼저 구분합니다.</div>
        <div class="case-bullet">• 감각신경전도검사가 보존되는지 감소하는지에 따라 신경뿌리병증과 말초신경병증 가능성이 달라집니다.</div>
        <div class="case-bullet">• 침근전도검사에서 어느 근육이 침범되었는지 보면 병변 수준 추론에 도움이 됩니다.</div>
        <div class="case-bullet">• 척추주위근 침범 여부는 신경뿌리병증 감별에 중요합니다.</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<hr class="strong-divider">', unsafe_allow_html=True)

    st.markdown('<div class="case-section-label">🗣️ 주요 증상</div>', unsafe_allow_html=True)
    symptoms_html = "".join(
        [f'<div class="case-bullet">• {s}</div>' for s in patient.get("symptoms", [])]
    )
    st.markdown(f'<div class="case-block compact-block"><div class="case-text-block">{symptoms_html}</div></div>', unsafe_allow_html=True)

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
    st.markdown('<div class="case-section-label">🧪 이학적 검사결과</div>', unsafe_allow_html=True)

    exam_blocks = []
    for _, exam_items in physical_exam.items():
        items_html = "".join([f'<div class="case-bullet">• {item}</div>' for item in exam_items])
        exam_blocks.append(f'<div class="case-text-block">{items_html}</div>')
    st.markdown(f'<div class="case-block compact-block">{"".join(exam_blocks)}</div>', unsafe_allow_html=True)

    sensory_ncs_items, motor_ncs_items, needle_items, reflex_items = [], [], [], []
    for item_name, values in findings.items():
        normalized_name = normalize_case_item_name(item_name)
        anatomy = ANATOMY.get(normalized_name, {})
        domain = anatomy.get("domain")
        if domain == "sensory":
            sensory_ncs_items.append((normalized_name, values))
        elif domain == "motor":
            motor_ncs_items.append((normalized_name, values))
        elif domain == "muscle":
            needle_items.append((normalized_name, values))
        elif domain in ["reflex", "h_reflex", "h_ratio", "f_wave", "blink"]:
            reflex_items.append((normalized_name, values))

    def render_finding_block(title, items):
        if not items:
            return

        st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
        st.markdown(f'<div class="case-section-label">{title}</div>', unsafe_allow_html=True)

        block_parts = []
        for idx, (item_name, values) in enumerate(items):
            left_val = values[0] if len(values) > 0 else ""
            right_val = values[1] if len(values) > 1 else ""

            lines = [f'<div class="finding-item-title">{get_compact_item_label(item_name)}</div>']

            if patient.get("side") == "양측":
                lines.append(f'<div class="finding-subtext">• 좌측: {normalize_result_text(left_val)}</div>')
                if str(right_val).strip() != "":
                    lines.append(f'<div class="finding-subtext">• 우측: {normalize_result_text(right_val)}</div>')
            elif str(right_val).strip() != "":
                side = patient.get("side", "병변")
                if side == "우":
                    lines.append(f'<div class="finding-subtext">• 좌측(정상측): {normalize_result_text(left_val)}</div>')
                    lines.append(f'<div class="finding-subtext">• 우측(병변측): {normalize_result_text(right_val)}</div>')
                elif side == "좌":
                    lines.append(f'<div class="finding-subtext">• 좌측(병변측): {normalize_result_text(left_val)}</div>')
                    lines.append(f'<div class="finding-subtext">• 우측(정상측): {normalize_result_text(right_val)}</div>')
                else:
                    lines.append(f'<div class="finding-subtext">• 반대측: {normalize_result_text(left_val)}</div>')
                    lines.append(f'<div class="finding-subtext">• 병변측: {normalize_result_text(right_val)}</div>')
            else:
                lines.append(f'<div class="finding-subtext">• 결과: {normalize_result_text(left_val)}</div>')

            item_html = f'<div class="compact-item">{"".join(lines)}</div>'
            block_parts.append(item_html)

            if idx < len(items) - 1:
                block_parts.append('<hr class="item-divider compact-divider">')

        st.markdown(
            f'<div class="case-block compact-block"><div class="case-text-block">{"".join(block_parts)}</div></div>',
            unsafe_allow_html=True
        )

    render_finding_block("⚡ 감각신경전도검사 소견", sensory_ncs_items)
    render_finding_block("⚡ 운동신경전도검사 소견", motor_ncs_items)
    render_finding_block("🪡 침근전도검사 소견", needle_items)
    render_finding_block("🔁 반사검사 소견", reflex_items)

    teaching_dx = case.get("teaching_diagnosis", {})
    diff_dx = case.get("differential_diagnosis", [])

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
    st.markdown('<div class="case-section-label">💡 왜 이 질환을 진단하는가?</div>', unsafe_allow_html=True)

    if teaching_dx:
        teaching_parts = []

        if teaching_dx.get("summary"):
            teaching_parts.append(
                f'<div class="case-text-block"><div class="case-bullet">• <b>핵심 요약:</b> {teaching_dx["summary"]}</div></div>'
            )

        if teaching_dx.get("ncs_reason"):
            ncs_html = "".join([f'<div class="case-bullet">• {line}</div>' for line in teaching_dx["ncs_reason"]])
            teaching_parts.append(
                f'<div class="case-subheading">신경전도검사 해석</div><div class="case-text-block">{ncs_html}</div>'
            )

        if teaching_dx.get("emg_reason"):
            emg_html = "".join([f'<div class="case-bullet">• {line}</div>' for line in teaching_dx["emg_reason"]])
            teaching_parts.append(
                f'<div class="case-subheading">침근전도검사 해석</div><div class="case-text-block">{emg_html}</div>'
            )

        if teaching_dx.get("integration"):
            integration_html = "".join([f'<div class="case-bullet">• {line}</div>' for line in teaching_dx["integration"]])
            teaching_parts.append(
                f'<div class="case-subheading">종합 해석</div><div class="case-text-block">{integration_html}</div>'
            )

        st.markdown(f'<div class="case-block compact-block">{"".join(teaching_parts)}</div>', unsafe_allow_html=True)

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
    st.markdown('<div class="case-section-label">🔍 감별진단은 무엇과 어떻게 하는가?</div>', unsafe_allow_html=True)

    if diff_dx:
        diff_parts = []
        for idx, dx_item in enumerate(diff_dx, 1):
            inner = [f'<div class="finding-item-title">{idx}. {dx_item.get("name", "")}</div>']
            if dx_item.get("why_consider"):
                inner.append(
                    f'<div class="finding-subtext">• <b>왜 감별이 필요한가:</b> {dx_item["why_consider"]}</div>'
                )
            if dx_item.get("how_to_differentiate"):
                inner.append(
                    f'<div class="finding-subtext">• <b>구체적 감별 포인트:</b> {dx_item["how_to_differentiate"]}</div>'
                )
            if dx_item.get("practical_tip"):
                inner.append(
                    f'<div class="finding-subtext">• <b>학생용 팁:</b> {dx_item["practical_tip"]}</div>'
                )

            diff_parts.append(f'<div class="compact-item">{"".join(inner)}</div>')
            if idx < len(diff_dx):
                diff_parts.append('<hr class="item-divider compact-divider">')

        st.markdown(
            f'<div class="case-block compact-block"><div class="case-text-block">{"".join(diff_parts)}</div></div>',
            unsafe_allow_html=True
        )

    st.markdown("</div>", unsafe_allow_html=True)

def render_item_card_header(item, a):
    st.markdown('<div class="input-row">', unsafe_allow_html=True)
    st.markdown(f'<div class="input-title">{item}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="input-meta">관련 신경: {a["nerve"]} | 관련 레벨: {simplify_level_text(a["level"])}</div>', unsafe_allow_html=True)

    edu_hint = ""
    if a["domain"] == "motor":
        edu_hint = "운동신경전도는 원위부(distal)와 근위부(proximal)에서 각각 진폭과 잠복기를 나누어 보면 축삭 손상과 탈수초성 전도 이상을 구분하는 데 도움이 됩니다."
    elif a["domain"] == "muscle":
        edu_hint = "침근전도에서 비정상 자발전위는 탈신경 또는 축삭성 병변을 시사할 수 있습니다."
    elif a["domain"] == "h_reflex":
        edu_hint = "H반사는 주로 S1 반사고리와 척수 반사 흥분성을 해석하는 데 도움이 되며, 경직 평가 교육에도 활용할 수 있습니다."
    elif a["domain"] == "h_ratio":
        edu_hint = "H/M 비율은 H파 최대 진폭(Hmax)과 M파 최대 진폭(Mmax)의 비율로 계산되며, 치료 전후 경직 변화를 정량적으로 비교하는 데 도움이 됩니다."
    elif a["domain"] == "f_wave":
        edu_hint = "F파는 근위부 신경전도 및 신경뿌리 수준 이상을 해석하는 데 도움이 되며, 교육용 앱에서는 잠복기와 반응 소실 여부를 우선적으로 학습합니다."
    elif a["domain"] == "blink":
        edu_hint = "눈깜빡반사는 자극 방향과 반응 측을 함께 구분하여 해석해야 합니다."
    elif a["domain"] == "reflex":
        edu_hint = "반사검사는 근위부 전도경로 또는 반사경로 이상 해석에 유용합니다."

    if edu_hint:
        st.markdown(f'<div class="mobile-note">{edu_hint}</div>', unsafe_allow_html=True)

def render_check_item(section, item, side, disabled=False):
    a = ANATOMY.get(item)
    if not a:
        return None

    rv = st.session_state.get("input_reset_version", 0)

    card_key = f"card_{rv}_{section}_{item}"
    check_key = f"chk_{rv}_{section}_{item}"

    st.markdown('<div class="input-row">', unsafe_allow_html=True)
    st.markdown(f'<div class="input-title">{item}</div>', unsafe_allow_html=True)

    use_item = st.checkbox("이 항목 입력", key=check_key, disabled=disabled)

    if not use_item:
        st.markdown('<hr class="item-divider">', unsafe_allow_html=True)
        return None

    st.markdown(
        f'<div class="input-meta">관련 신경: {a["nerve"]} | 관련 레벨: {simplify_level_text(a["level"])}</div>',
        unsafe_allow_html=True
    )

    row = None

    # 1) H 반사
    if a["domain"] == "h_reflex":
        if side in ["좌", "우"]:
            lesion_side_text = "좌측 병변측" if side == "좌" else "우측 병변측"
            st.caption(f"H반사는 {lesion_side_text}의 Hmax와 Mmax만 입력합니다. 반대측은 정상으로 간주합니다.")
        else:
            st.caption("H반사는 각 측의 Hmax와 Mmax를 입력하면 H/M 비율이 자동 계산됩니다.")

        c1, c2 = st.columns(2)
        hmax = c1.number_input(
            "H파 최대 진폭 Hmax (mV)",
            min_value=0.0,
            value=0.0,
            step=0.1,
            key=f"hmax_{rv}_{item}",
            disabled=disabled
        )
        mmax = c2.number_input(
            "M파 최대 진폭 Mmax (mV)",
            min_value=0.0,
            value=0.0,
            step=0.1,
            key=f"mmax_{rv}_{item}",
            disabled=disabled
        )

        ratio, ratio_text = compute_hm_ratio_text(hmax, mmax)
        hm_info = interpret_hm_ratio(ratio)

        st.markdown(f"**자동 계산된 H/M 비율:** {ratio_text}")
        st.markdown(f"**교육용 해석:** {hm_info['label']}")
        st.markdown(f"<div class='mobile-note'>{hm_info['detail']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='mobile-note'>{hm_info['warning']}</div>", unsafe_allow_html=True)

        if ratio is None:
            hm_interpret = "정상 (Normal)"
            h_status = "정상 (Normal)"
        else:
            if ratio > 0.60:
                hm_interpret = "증가 가능 (May be increased)"
                h_status = "항진 또는 문턱값 감소 (Hyperactive / lower threshold)"
            else:
                hm_interpret = "정상 (Normal)"
                h_status = "정상 (Normal)"

        row = {"section": section, "item": item, "left": h_status, "right": ""}
        hm_row = {
            "section": section,
            "item": "H/M 비율",
            "left": f"{hm_interpret} | 자동계산값: {ratio_text}",
            "right": ""
        }

        st.markdown('<hr class="item-divider">', unsafe_allow_html=True)
        return [row, hm_row]

    # 2) H/M 비율 수동 입력 제거
    elif a["domain"] == "h_ratio":
        st.markdown('<hr class="item-divider">', unsafe_allow_html=True)
        return None

    # 3) F파
    elif a["domain"] == "f_wave":
        st.caption("F파는 병변측 기준으로 잠복기 지연 여부와 반응 소실 여부를 입력합니다.")

        c1, c2 = st.columns(2)
        latency_status = c1.selectbox(
            "병변측 잠복기",
            ["정상 (Normal)", "잠복기 지연 (Delayed latency)"],
            key=f"fw_lat_{rv}_{item}",
            disabled=disabled
        )
        response_status = c2.selectbox(
            "병변측 반응",
            ["출현 (Present)", "소실 (Absent)"],
            key=f"fw_resp_{rv}_{item}",
            disabled=disabled
        )

        lesion_res = compose_fwave_result(latency_status, response_status)

        if side == "양측":
            row = {"section": section, "item": item, "left": lesion_res, "right": lesion_res}
        elif side == "좌":
            row = {"section": section, "item": item, "left": lesion_res, "right": "정상 (Normal)"}
        else:
            row = {"section": section, "item": item, "left": "정상 (Normal)", "right": lesion_res}

    # 4) blink
    elif a["domain"] == "blink":
        st.caption("눈깜빡반사는 자극 방향과 반응 측을 구분하여 입력합니다.")
        res = st.selectbox(
            "반응 결과",
            get_domain_options(a["domain"], item),
            key=f"blink_{rv}_{item}",
            disabled=disabled
        )
        row = {"section": section, "item": item, "left": res, "right": ""}

    # 5) reflex
    elif a["domain"] == "reflex":
        st.caption("반사검사는 해당 항목의 결과만 선택합니다.")
        res = st.selectbox(
            "검사 결과",
            get_domain_options(a["domain"], item),
            key=f"res_{rv}_{item}",
            disabled=disabled
        )
        row = {"section": section, "item": item, "left": res, "right": ""}

    # 6) sensory
    elif a["domain"] == "sensory":
        st.caption("감각신경전도는 진폭과 잠복기를 선택합니다.")

        if side == "양측":
            st.markdown("**좌측 결과**")
            c1, c2 = st.columns(2)
            left_amp = c1.selectbox(
                "좌측 진폭",
                ["정상 (Normal)", "감소 (Reduced)", "무반응 (No response)"],
                key=f"sens_l_amp_{rv}_{item}",
                disabled=disabled
            )
            left_lat = c2.selectbox(
                "좌측 잠복기",
                ["정상 (Normal)", "잠복기 지연 (Delayed latency)"],
                key=f"sens_l_lat_{rv}_{item}",
                disabled=disabled
            )

            st.markdown("**우측 결과**")
            c3, c4 = st.columns(2)
            right_amp = c3.selectbox(
                "우측 진폭",
                ["정상 (Normal)", "감소 (Reduced)", "무반응 (No response)"],
                key=f"sens_r_amp_{rv}_{item}",
                disabled=disabled
            )
            right_lat = c4.selectbox(
                "우측 잠복기",
                ["정상 (Normal)", "잠복기 지연 (Delayed latency)"],
                key=f"sens_r_lat_{rv}_{item}",
                disabled=disabled
            )

            left_res = compose_ncs_result(left_amp, left_lat)
            right_res = compose_ncs_result(right_amp, right_lat)
            row = {"section": section, "item": item, "left": left_res, "right": right_res}

        else:
            c1, c2 = st.columns(2)
            lesion_amp = c1.selectbox(
                "병변측 진폭",
                ["정상 (Normal)", "감소 (Reduced)", "무반응 (No response)"],
                key=f"sens_amp_{rv}_{item}",
                disabled=disabled
            )
            lesion_lat = c2.selectbox(
                "병변측 잠복기",
                ["정상 (Normal)", "잠복기 지연 (Delayed latency)"],
                key=f"sens_lat_{rv}_{item}",
                disabled=disabled
            )

            lesion_res = compose_ncs_result(lesion_amp, lesion_lat)

            if side == "좌":
                row = {"section": section, "item": item, "left": lesion_res, "right": "정상 (Normal)"}
            else:
                row = {"section": section, "item": item, "left": "정상 (Normal)", "right": lesion_res}

    # 7) motor
    elif a["domain"] == "motor":
        labels = get_motor_stimulation_labels(item)
        st.caption("운동신경전도는 원위부/근위부 진폭과 잠복기를 입력합니다.")

        if side == "양측":
            c1, c2 = st.columns(2)
            left = c1.selectbox(
                "좌측 대표 결과",
                get_domain_options(a["domain"], item),
                key=f"ml_{rv}_{item}",
                disabled=disabled
            )
            right = c2.selectbox(
                "우측 대표 결과",
                get_domain_options(a["domain"], item),
                key=f"mr_{rv}_{item}",
                disabled=disabled
            )
            row = {"section": section, "item": item, "left": left, "right": right}
        else:
            c1, c2 = st.columns(2)
            distal_amp = c1.selectbox(
                f'{labels["distal"]} 진폭',
                ["정상 (Normal)", "감소 (Reduced)", "무반응 (No response)"],
                key=f"da_{rv}_{item}",
                disabled=disabled
            )
            distal_lat = c2.selectbox(
                f'{labels["distal"]} 잠복기',
                ["정상 (Normal)", "잠복기 지연 (Delayed latency)"],
                key=f"dl_{rv}_{item}",
                disabled=disabled
            )

            c3, c4 = st.columns(2)
            proximal_amp = c3.selectbox(
                f'{labels["proximal"]} 진폭',
                ["정상 (Normal)", "감소 (Reduced)", "무반응 (No response)"],
                key=f"pa_{rv}_{item}",
                disabled=disabled
            )
            proximal_lat = c4.selectbox(
                f'{labels["proximal"]} 잠복기',
                ["정상 (Normal)", "잠복기 지연 (Delayed latency)"],
                key=f"pl_{rv}_{item}",
                disabled=disabled
            )

            lesion_res = compose_ncs_result(distal_amp, distal_lat, proximal_amp, proximal_lat)

            if side == "좌":
                row = {"section": section, "item": item, "left": lesion_res, "right": "정상 (Normal)"}
            else:
                row = {"section": section, "item": item, "left": "정상 (Normal)", "right": lesion_res}

    # 8) muscle
    elif a["domain"] == "muscle":
        st.caption("침근전도는 해당 근육의 이상 여부만 선택합니다.")

        if side == "양측":
            c1, c2 = st.columns(2)
            left = c1.selectbox(
                "좌측 소견",
                get_domain_options(a["domain"], item),
                key=f"emg_l_{rv}_{item}",
                disabled=disabled
            )
            right = c2.selectbox(
                "우측 소견",
                get_domain_options(a["domain"], item),
                key=f"emg_r_{rv}_{item}",
                disabled=disabled
            )
            row = {"section": section, "item": item, "left": left, "right": right}
        else:
            lesion_res = st.selectbox(
                "침근전도 소견",
                get_domain_options(a["domain"], item),
                key=f"emg_{rv}_{item}",
                disabled=disabled
            )
            if side == "좌":
                row = {"section": section, "item": item, "left": lesion_res, "right": "정상 (Normal)"}
            else:
                row = {"section": section, "item": item, "left": "정상 (Normal)", "right": lesion_res}

    st.markdown('<hr class="item-divider">', unsafe_allow_html=True)
    return row

def render_input_sections_for_side(side):
    rows = []

    group_map = {
        "팔 감각신경전도검사": [
            "팔 감각신경전도검사 (arm sensory NCS)"
        ],
        "팔 운동신경전도검사": [
            "팔 운동신경전도검사 (arm motor NCS)"
        ],
        "팔 침근전도검사": [
            "팔 침근전도검사 근육 (arm needle EMG muscles)"
        ],
        "다리 감각신경전도검사": [
            "다리 감각신경전도검사 (leg sensory NCS)"
        ],
        "다리 운동신경전도검사": [
            "다리 운동신경전도검사 (leg motor NCS)"
        ],
        "다리 침근전도검사": [
            "다리 침근전도검사 근육 (leg needle EMG muscles)"
        ],
        "H반사 / 경직 평가": [
            "H반사 / 경직 평가 (H-reflex / Spasticity evaluation)"
        ],
        "F파 검사": [
            "F파 검사 (F-wave study)"
        ],
        "눈깜빡반사검사": [
            "눈깜빡반사검사 (Blink reflex)"
        ]
    }

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("### 📋 검사 종류 선택")
    st.markdown(
        '<div class="mobile-note">검사 종류를 선택한 뒤, 해당 박스 안에서 필요한 항목만 체크하면 바로 아래에 입력창이 나타납니다.</div>',
        unsafe_allow_html=True
    )
    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

    selected_groups = []
    for group_title in group_map.keys():
        if st.checkbox(group_title, key=f"group_{group_title}"):
            selected_groups.append(group_title)

    if not selected_groups:
        st.info("입력할 검사 종류를 하나 이상 선택하세요.")
        st.markdown("</div>", unsafe_allow_html=True)
        return rows

    rv = st.session_state.get("input_reset_version", 0)

    for group_title in selected_groups:
        st.markdown(f'<div class="big-section-title">{group_title}</div>', unsafe_allow_html=True)

        selected_items = []

        for sec in group_map[group_title]:
            items = SECTIONS.get(sec, [])
            if not items:
                continue

            if sec == "H반사 / 경직 평가 (H-reflex / Spasticity evaluation)":
                if side == "우":
                    items = ["H 반사 (우)"]
                elif side == "좌":
                    items = ["H 반사 (좌)"]
                else:
                    items = ["H 반사 (좌)", "H 반사 (우)"]

            for item in items:
                compact_label = get_compact_item_label(item)
                checked = st.checkbox(
                    compact_label,
                    key=f"pick_{rv}_{group_title}_{sec}_{item}"
                )
                if checked:
                    selected_items.append((sec, item))

        if selected_items:
            st.markdown('<hr class="soft-divider">', unsafe_allow_html=True)
            for sec, item in selected_items:
                row = render_selected_item_detail_input(sec, item, side)
                if row:
                    if isinstance(row, list):
                        rows.extend(row)
                    else:
                        rows.append(row)

        st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
    return rows

    rv = st.session_state.get("input_reset_version", 0)

    for group_title in selected_groups:
        st.markdown(f'<div class="big-section-title">{group_title}</div>', unsafe_allow_html=True)

        selected_items = []

        for sec in group_map[group_title]:
            items = SECTIONS.get(sec, [])
            if not items:
                continue

            st.markdown(f'<div class="mobile-note"><b>{sec}</b></div>', unsafe_allow_html=True)

            # H 반사는 단일 항목만 보이도록
            if sec == "H반사 / 경직 평가 (H-reflex / Spasticity evaluation)":
                if side == "우":
                    items = ["H 반사 (우)"]
                elif side == "좌":
                    items = ["H 반사 (좌)"]
                else:
                    items = ["H 반사 (좌)", "H 반사 (우)"]

            for item in items:
                compact_label = get_compact_item_label(item)
                if st.checkbox(compact_label, key=f"pick_{rv}_{group_title}_{sec}_{item}"):
                    selected_items.append((sec, item))

            st.markdown('<hr class="soft-divider">', unsafe_allow_html=True)

        if selected_items:
            if st.button(f"{group_title} 선택 항목 입력 보기", key=f"show_inputs_{rv}_{group_title}", use_container_width=True):
                st.session_state[f"open_inputs_{rv}_{group_title}"] = True

            if st.session_state.get(f"open_inputs_{rv}_{group_title}", False):
                st.markdown(f'<div class="case-section-label">{group_title} 입력</div>', unsafe_allow_html=True)
                for sec, item in selected_items:
                    row = render_selected_item_detail_input(sec, item, side)
                    if row:
                        if isinstance(row, list):
                            rows.extend(row)
                        else:
                            rows.append(row)

    st.markdown("</div>", unsafe_allow_html=True)
    return rows

def render_result_view(result):
    st.markdown('<div class="result-card">', unsafe_allow_html=True)
    st.markdown('<div class="case-title-mobile">📊 자동 분석 결과</div>', unsafe_allow_html=True)

    summary_top = [
        f'<div class="result-text"><b>최종 유력 진단:</b> {result["final_dx"]}</div>',
        f'<div class="result-text"><b>손상 의심 신경:</b> {result["involved_nerves"]}</div>',
        f'<div class="result-text"><b>신경학적 레벨/분절:</b> {result["involved_levels"]}</div>',
        f'<div class="result-text"><b>중증도:</b> {result["severity"]}</div>',
    ]
    if result.get("lesion_tags"):
        summary_top.append(f'<div class="result-text"><b>병변 해석 태그:</b> {", ".join(result["lesion_tags"])}</div>')
    st.markdown(f'<div class="case-text-block compact-block">{"".join(summary_top)}</div>', unsafe_allow_html=True)

    summary_line = ""
    if result["final_dx"] == "목 신경뿌리병증 (Cervical Radiculopathy)":
        summary_line = "감각신경전도검사가 비교적 보존되고, 목 척추주위근과 관련 상지 근육의 침근전도 이상이 핵심 근거입니다."
    elif result["final_dx"] == "허리 신경뿌리병증 (Lumbar Radiculopathy)":
        summary_line = "감각신경전도검사가 비교적 보존되고, 허리 척추주위근과 관련 하지 근육의 침근전도 이상이 핵심 근거입니다."
    elif "손목굴증후군" in result["final_dx"]:
        summary_line = "정중신경 관련 감각 및 운동 잠복기 지연과 엄지두덩 근육 침범이 손목굴증후군 해석에 중요합니다."
    elif "정중신경병증" in result["final_dx"]:
        summary_line = "이상 소견이 정중신경 관련 항목에 집중되어 있고, 다른 신경 분포 이상이 두드러지지 않는 점이 핵심입니다."
    elif "자신경" in result["final_dx"]:
        summary_line = "자신경 분포 감각저하와 ADM/FDI 같은 손 intrinsic muscle 침범이 핵심입니다."
    elif "노신경" in result["final_dx"]:
        summary_line = "노신경 분포의 감각·운동 이상과 손목/손가락 폄 약화가 핵심 해석 포인트입니다."
    elif "종아리신경" in result["final_dx"]:
        summary_line = "발처짐, 발등 감각저하, 종아리신경 관련 전도 이상이 핵심 포인트입니다."
    elif "다발신경병증" in result["final_dx"]:
        summary_line = "양측성, 원위부 우세, 여러 신경의 반복 이상이 다발신경병증 패턴의 핵심입니다."

    if summary_line:
        st.markdown('<div class="case-section-label">🧭 학생용 해석 요약</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="section-hint compact-block">{summary_line}</div>', unsafe_allow_html=True)

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
    st.markdown('<div class="case-section-label">📌 입력된 이상 소견</div>', unsafe_allow_html=True)

    if result.get("abnormal_items"):
        parts = []
        for idx, item in enumerate(result["abnormal_items"]):
            inner = [
                f'<div class="finding-item-title">{item["항목"]}</div>',
                f'<div class="finding-subtext">• <b>결과:</b> {item["결과"]}</div>'
            ]
            if item.get("신경"):
                inner.append(f'<div class="finding-subtext"><b>관련 신경:</b> {item["신경"]}</div>')
            if item.get("레벨"):
                inner.append(f'<div class="finding-subtext"><b>관련 레벨:</b> {item["레벨"]}</div>')
            parts.append(f'<div class="compact-item">{"".join(inner)}</div>')
            if idx < len(result["abnormal_items"]) - 1:
                parts.append('<hr class="item-divider compact-divider">')
        st.markdown(f'<div class="case-block compact-block">{"".join(parts)}</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="case-text-block compact-block"><div class="result-small">입력된 이상 소견 없음</div></div>', unsafe_allow_html=True)

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
    st.markdown('<div class="case-section-label">🧠 판단 근거</div>', unsafe_allow_html=True)

    if result.get("reasons"):
        reasons_html = "".join([f'<div class="case-bullet">• {reason}</div>' for reason in result.get("reasons", [])])
        st.markdown(f'<div class="case-text-block compact-block">{reasons_html}</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="case-text-block compact-block"><div class="result-small">제시할 판단 근거 없음</div></div>', unsafe_allow_html=True)

    if result.get("suggestions"):
        st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
        st.markdown('<div class="case-section-label">🧭 추가로 함께 생각할 점</div>', unsafe_allow_html=True)
        suggestions_html = "".join([f'<div class="case-bullet">• {s}</div>' for s in result["suggestions"]])
        st.markdown(f'<div class="case-text-block compact-block">{suggestions_html}</div>', unsafe_allow_html=True)

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
    st.markdown('<div class="case-section-label">🔍 Top 3 감별진단</div>', unsafe_allow_html=True)

    if result.get("top3_details"):
        parts = []
        for idx, item in enumerate(result.get("top3_details", []), 1):
            title = "최종 유력진단" if idx == 1 else f"감별진단 {idx-1}"
            inner = [
                f'<div class="finding-item-title">{title}: {item["name"]}</div>',
                f'<div class="finding-subtext"><b>감별 포인트:</b> {item["how_to_differentiate"]}</div>'
            ]
            parts.append(f'<div class="compact-item">{"".join(inner)}</div>')
            if idx < len(result["top3_details"]):
                parts.append('<hr class="item-divider compact-divider">')
        st.markdown(f'<div class="case-block compact-block">{"".join(parts)}</div>', unsafe_allow_html=True)

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
    st.markdown(
        '<div class="case-text-block compact-block"><div class="result-small">현재 입력된 결과를 바탕으로 한 학생 교육용 자동 해석이며, 실제 임상 진단을 대체하지 않습니다.</div></div>',
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# 7. 메인 실행
# ==========================================
init_app_state()
current_screen = st.session_state["current_screen"]

if current_screen == "home":
    render_home_screen()
else:
    # [화면 상단] 네비게이션 버튼 렌더링
    render_navigation_controls(position="top")
    
    app_mode = st.session_state.get("app_mode")

    if current_screen == "mode":
        render_header()
        if app_mode == MODE_CASE:
            render_case_selector_only()
        elif app_mode == MODE_DIRECT:
            render_direct_entry_start()

    elif current_screen == "case_detail":
        render_header()
        confirmed_case = st.session_state.get("confirmed_case")
        if confirmed_case:
            render_case_learning_info(confirmed_case)
        else:
            st.warning("선택된 사례가 없습니다.")

    elif current_screen == "direct_input":
        render_header()
        age = st.session_state.get("age", 50)
        sex = st.session_state.get("sex", "미선택")
        side = st.session_state.get("side", "미선택")

        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown(f'<div class="mobile-note"><b>입력 프로필:</b> {age}세 | {sex} | 병변측: {side}</div>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        rows = render_input_sections_for_side(side)

        c1, c2 = st.columns(2)
        with c1:
            if st.button("분석 실행", type="primary", use_container_width=True):
                if not rows:
                    st.warning("최소 1개 이상의 항목에 이상 소견을 입력하세요.")
                else:
                    st.session_state["last_result"] = analyze_case(age, sex, side, rows)

        with c2:
            if st.button("입력 초기화", use_container_width=True):
                reset_all_inputs()
                st.rerun()

        if st.session_state.get("last_result"):
            res = st.session_state["last_result"]
            render_result_view(res)

            st.download_button(
                label="📝 텍스트 보고서 다운로드",
                data=make_report_text(res).encode("utf-8"),
                file_name=f"EMG_Analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                mime="text/plain",
                use_container_width=True
            )

    # ★ 핵심 수정: 아래 코드가 반드시 들여쓰기 4칸으로 위치해야 모든 화면에서 버튼이 나타납니다. ★
    # [화면 하단] 네비게이션 버튼 렌더링
    render_navigation_controls(position="bottom")
