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
    padding-top: 4.4rem;
    padding-bottom: 1.8rem;
    max-width: 1180px;
}

.main-title {
    font-size: 2.15rem;
    font-weight: 900;
    margin-top: 0.6rem;
    margin-bottom: 0.35rem;
    line-height: 1.34;
    color: #0f172a;
    word-break: keep-all;
}

.subtle {
    color: #475569;
    font-size: 0.97rem;
    margin-bottom: 0.95rem;
    line-height: 1.55;
}

.section-card {
    background: #ffffff;
    border: 1px solid #e5e7eb;
    border-radius: 14px;
    padding: 14px;
    margin-bottom: 12px;
}

.result-card {
    background: #f8fffb;
    border: 1px solid #d1fae5;
    border-radius: 14px;
    padding: 14px;
    margin-bottom: 12px;
}

.warn-card {
    background: #fffaf3;
    border: 1px solid #fed7aa;
    border-radius: 14px;
    padding: 14px;
    margin-bottom: 12px;
}

.input-row {
    background: transparent;
    border: none;
    border-radius: 0;
    padding: 10px 0 6px 0;
    margin-bottom: 0;
}

.input-title {
    font-weight: 800;
    font-size: 0.99rem;
    margin-bottom: 4px;
    color: #0f172a;
    line-height: 1.45;
}

.input-meta {
    font-size: 0.87rem;
    color: #475569;
    margin-bottom: 8px;
    line-height: 1.48;
}

.big-section-title {
    font-size: 1.02rem;
    font-weight: 800;
    color: #111827;
    border-left: 4px solid #93c5fd;
    padding: 5px 0 5px 10px;
    margin-top: 8px;
    margin-bottom: 6px;
    line-height: 1.45;
}

.section-hint {
    font-size: 0.93rem;
    color: #334155;
    background: #f8fafc;
    border-left: 4px solid #22c55e;
    padding: 10px 12px;
    border-radius: 10px;
    margin-bottom: 10px;
    line-height: 1.52;
}

.mode-box-green {
    border: 1px solid #d9ead3;
    border-radius: 12px;
    padding: 14px 16px;
    background-color: #f6fff2;
    margin-top: 10px;
    margin-bottom: 14px;
}

.mode-box-blue {
    border: 1px solid #cfe2f3;
    border-radius: 12px;
    padding: 14px 16px;
    background-color: #f8fbff;
    margin-top: 10px;
    margin-bottom: 14px;
}

.mode-box-gray {
    border: 1px solid #d1d5db;
    border-radius: 14px;
    padding: 14px;
    background: #fafafa;
    margin-top: 10px;
    margin-bottom: 16px;
}

.mode-title {
    font-size: 1.18rem;
    font-weight: 800;
    margin-bottom: 4px;
    line-height: 1.4;
}

.mode-title-green {
    color: #38761d;
}

.mode-title-blue {
    color: #0b5394;
}

.mode-title-gray {
    color: #666666;
    font-weight: 900;
    font-size: 1.18rem;
}

.mode-desc {
    font-size: 0.95rem;
    color: #444;
    line-height: 1.55;
}

/* 첫 화면 라디오 */
div[role="radiogroup"] label p {
    font-size: 1.08rem !important;
    font-weight: 700 !important;
    color: #0f172a !important;
    line-height: 1.45 !important;
}

div[role="radiogroup"] > label {
    margin-bottom: 0.42rem !important;
}

/* 사례 목록 라디오 */
div[data-testid="stRadio"] > div {
    gap: 0.2rem !important;
}

div[data-testid="stRadio"] label {
    padding-top: 0.35rem !important;
    padding-bottom: 0.35rem !important;
    margin-bottom: 0.1rem !important;
    border-bottom: 1px solid #e5e7eb !important;
}

div[data-testid="stRadio"] label p {
    font-size: 1rem !important;
    font-weight: 700 !important;
    line-height: 1.45 !important;
    word-break: keep-all !important;
    color: #0f172a !important;
}

/* 탭 */
div[data-testid="stTabs"] > div > div > div > div > button {
    font-size: 1rem !important;
    font-weight: 700 !important;
    border: 1.5px solid #e2e8f0 !important;
    border-radius: 8px !important;
    padding: 9px 13px !important;
    margin-right: 5px !important;
    margin-bottom: 10px !important;
    background-color: #ffffff !important;
    color: #475569 !important;
}

div[data-testid="stTabs"] > div > div > div > div > button[aria-selected="true"] {
    border-color: #3b82f6 !important;
    background-color: #eff6ff !important;
    color: #1d4ed8 !important;
    box-shadow: none !important;
}

/* 구분선 */
.item-divider {
    border: none;
    border-top: 1px solid #dbe4ea;
    margin: 10px 0 12px 0;
}

.section-divider {
    border: none;
    border-top: 1px solid #cbd5e1;
    margin: 12px 0 16px 0;
}

.soft-divider {
    border: none;
    border-top: 1px solid #e5e7eb;
    margin: 8px 0 10px 0;
}

.strong-divider {
    border: none;
    border-top: 1.5px solid #cbd5e1;
    margin: 14px 0 18px 0;
}

.top-bottom-nav-space {
    margin-top: 10px;
    margin-bottom: 8px;
}

/* 사례 상세 */
.case-title-mobile {
    font-size: 1.42rem;
    font-weight: 900;
    line-height: 1.4;
    color: #0f172a;
    margin-bottom: 8px;
    word-break: keep-all;
}

.case-subtitle-mobile {
    font-size: 0.95rem;
    color: #475569;
    margin-bottom: 10px;
    line-height: 1.45;
}

.case-section-label {
    font-size: 1rem;
    font-weight: 800;
    color: #0f172a;
    margin-top: 6px;
    margin-bottom: 6px;
    line-height: 1.4;
}

.case-bullet {
    font-size: 0.96rem;
    line-height: 1.56;
    color: #1f2937;
    margin-bottom: 4px;
}

.finding-item-title {
    font-size: 0.98rem;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 5px;
    line-height: 1.45;
}

.finding-subtext {
    font-size: 0.93rem;
    color: #334155;
    line-height: 1.5;
    margin-bottom: 2px;
}

.mobile-note {
    font-size: 0.92rem;
    color: #475569;
    line-height: 1.52;
}

.result-title {
    font-size: 1.12rem;
    font-weight: 900;
    color: #065f46;
    line-height: 1.45;
    margin-bottom: 6px;
}

.result-label {
    font-size: 0.96rem;
    font-weight: 800;
    color: #0f172a;
    margin-top: 4px;
    margin-bottom: 5px;
    line-height: 1.45;
}

.result-text {
    font-size: 0.95rem;
    color: #1f2937;
    line-height: 1.54;
    margin-bottom: 4px;
}

.result-small {
    font-size: 0.9rem;
    color: #475569;
    line-height: 1.5;
}

@media (max-width: 768px) {
    .block-container {
        padding-top: 4.0rem;
        padding-bottom: 1.3rem;
    }

    .main-title {
        font-size: 1.82rem;
        line-height: 1.32;
    }

    .section-card,
    .result-card,
    .warn-card,
    .mode-box-green,
    .mode-box-blue,
    .mode-box-gray {
        padding: 12px;
    }

    div[data-testid="stRadio"] label p {
        font-size: 0.97rem !important;
        line-height: 1.42 !important;
    }

    .case-title-mobile {
        font-size: 1.16rem;
        line-height: 1.44;
    }

    .case-subtitle-mobile {
        font-size: 0.9rem;
    }

    .case-section-label {
        font-size: 0.98rem;
    }

    .case-bullet {
        font-size: 0.94rem;
        line-height: 1.52;
    }

    .finding-item-title {
        font-size: 0.95rem;
    }

    .finding-subtext,
    .mobile-note,
    .result-text,
    .result-small {
        font-size: 0.9rem;
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
        "넙다리신경 복합근육활동전위 (Femoral CMAP)"
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
    "후기반사 및 경직평가 (Late responses / Spasticity evaluation)": [
        "H 반사 (좌)",
        "H 반사 (우)",
        "H/M 비율",
        "정중신경 F파 (Median F-wave)",
        "자신경 F파 (Ulnar F-wave)",
        "정강신경 F파 (Tibial F-wave)",
        "종아리신경 F파 (Peroneal F-wave)"
    ],
    "눈깜빡반사검사 (Blink reflex)": [
        "우측 자극 R1",
        "우측 자극 R2",
        "좌측 자극 R1",
        "좌측 자극 R2"
    ]
}

ANATOMY = {
    "정중신경 감각신경활동전위 (Median SNAP)": {
        "nerve": "정중신경 (Median nerve)",
        "level": "손목/아래팔, C6-T1",
        "domain": "sensory",
        "region": "arm"
    },
    "자신경 감각신경활동전위 (Ulnar SNAP)": {
        "nerve": "자신경 (Ulnar nerve)",
        "level": "손목/팔꿉, C8-T1",
        "domain": "sensory",
        "region": "arm"
    },
    "노신경 감각신경활동전위 (Radial SNAP)": {
        "nerve": "노신경 (Radial nerve)",
        "level": "아래팔/손등, C5-C8",
        "domain": "sensory",
        "region": "arm"
    },
    "노신경 표재감각신경활동전위 (Superficial Radial SNAP)": {
        "nerve": "노신경 표재감각분지 (Superficial radial sensory branch)",
        "level": "아래팔/손등, C6-C8",
        "domain": "sensory",
        "region": "arm"
    },
    "가쪽아래팔피부신경 감각신경활동전위 (Lateral antebrachial cutaneous SNAP)": {
        "nerve": "가쪽아래팔피부신경 (Lateral antebrachial cutaneous nerve)",
        "level": "근피신경 말단 감각분지, C5-C6",
        "domain": "sensory",
        "region": "arm"
    },

    "정중신경 복합근육활동전위 (Median CMAP)": {
        "nerve": "정중신경 (Median nerve)",
        "level": "정중신경 말단운동전도, 관련 신경뿌리 C8-T1",
        "domain": "motor",
        "region": "arm"
    },
    "자신경 복합근육활동전위 (Ulnar CMAP)": {
        "nerve": "자신경 (Ulnar nerve)",
        "level": "말단/팔꿉 구간 운동전도, 관련 신경뿌리 C8-T1",
        "domain": "motor",
        "region": "arm"
    },
    "노신경 복합근육활동전위 (Radial CMAP)": {
        "nerve": "노신경 (Radial nerve)",
        "level": "위팔/아래팔 운동경로, 관련 신경뿌리 C6-C8",
        "domain": "motor",
        "region": "arm"
    },
    "겨드랑신경 복합근육활동전위 (Axillary CMAP)": {
        "nerve": "겨드랑신경 (Axillary nerve)",
        "level": "팔신경얼기 뒤다발, 관련 신경뿌리 C5-C6",
        "domain": "motor",
        "region": "arm"
    },
    "근피신경 복합근육활동전위 (Musculocutaneous CMAP)": {
        "nerve": "근피신경 (Musculocutaneous nerve)",
        "level": "팔신경얼기 가쪽다발, 관련 신경뿌리 C5-C6",
        "domain": "motor",
        "region": "arm"
    },

    "짧은엄지벌림근 (Abductor Pollicis Brevis, APB)": {
        "nerve": "정중신경 (Median nerve)",
        "level": "C8-T1",
        "domain": "muscle",
        "region": "arm"
    },
    "첫째등쪽뼈사이근 (First Dorsal Interosseous, FDI)": {
        "nerve": "자신경 (Ulnar nerve)",
        "level": "C8-T1",
        "domain": "muscle",
        "region": "arm"
    },
    "새끼벌림근 (Abductor Digiti Minimi, ADM)": {
        "nerve": "자신경 (Ulnar nerve)",
        "level": "C8-T1",
        "domain": "muscle",
        "region": "arm"
    },
    "집게폄근 (Extensor Indicis Proprius, EIP)": {
        "nerve": "뒤뼈사이신경/노신경 (Posterior interosseous/Radial nerve)",
        "level": "C7-C8",
        "domain": "muscle",
        "region": "arm"
    },
    "손목폄근 (Extensor Carpi Radialis / Extensor Digitorum)": {
        "nerve": "노신경 (Radial nerve)",
        "level": "C6-C8",
        "domain": "muscle",
        "region": "arm"
    },
    "가시아래근 (Infraspinatus)": {
        "nerve": "어깨위신경 (Suprascapular nerve)",
        "level": "C5-C6",
        "domain": "muscle",
        "region": "arm"
    },
    "삼각근 (Deltoid)": {
        "nerve": "겨드랑신경 (Axillary nerve)",
        "level": "C5-C6",
        "domain": "muscle",
        "region": "arm"
    },
    "위팔두갈래근 (Biceps Brachii)": {
        "nerve": "근피신경 (Musculocutaneous nerve)",
        "level": "C5-C6",
        "domain": "muscle",
        "region": "arm"
    },
    "위팔노근 (Brachioradialis)": {
        "nerve": "노신경 (Radial nerve)",
        "level": "C5-C6",
        "domain": "muscle",
        "region": "arm"
    },
    "긴노쪽손목폄근/짧은노쪽손목폄근 (Extensor Carpi Radialis Longus/Brevis)": {
        "nerve": "노신경 (Radial nerve)",
        "level": "C6-C7",
        "domain": "muscle",
        "region": "arm"
    },
    "원엎침근 (Pronator Teres)": {
        "nerve": "정중신경 (Median nerve)",
        "level": "C6-C7",
        "domain": "muscle",
        "region": "arm"
    },
    "위팔세갈래근 (Triceps Brachii)": {
        "nerve": "노신경 (Radial nerve)",
        "level": "C6-C8 (C7 우세)",
        "domain": "muscle",
        "region": "arm"
    },
    "목 척추주위근 (Cervical Paraspinal)": {
        "nerve": "척수뒤가지 (Posterior primary ramus)",
        "level": "목 신경뿌리 수준",
        "domain": "muscle",
        "region": "arm"
    },

    "장딴지신경 감각신경활동전위 (Sural SNAP)": {
        "nerve": "장딴지신경 (Sural nerve)",
        "level": "S1-S2",
        "domain": "sensory",
        "region": "leg"
    },
    "얕은종아리신경 감각신경활동전위 (Superficial Peroneal SNAP)": {
        "nerve": "얕은종아리신경 (Superficial peroneal nerve)",
        "level": "L5-S1",
        "domain": "sensory",
        "region": "leg"
    },
    "두렁신경 감각신경활동전위 (Saphenous SNAP)": {
        "nerve": "두렁신경 (Saphenous nerve)",
        "level": "L3-L4",
        "domain": "sensory",
        "region": "leg"
    },
    "첫째 발가락사이 감각 (First Dorsal Web Space Sensation)": {
        "nerve": "깊은종아리신경 감각분지 (Deep peroneal sensory branch)",
        "level": "L5",
        "domain": "sensory",
        "region": "leg"
    },

    "종아리신경 복합근육활동전위 (Peroneal CMAP)": {
        "nerve": "온종아리신경-깊은종아리신경 운동경로 (Common/Deep peroneal motor pathway)",
        "level": "종아리뼈머리/종아리 구간, 관련 신경뿌리 L4-S1",
        "domain": "motor",
        "region": "leg"
    },
    "깊은종아리신경 복합근육활동전위 (Deep Peroneal CMAP)": {
        "nerve": "깊은종아리신경 (Deep peroneal nerve)",
        "level": "발목/발등, L5-S1",
        "domain": "motor",
        "region": "leg"
    },
    "정강신경 복합근육활동전위 (Tibial CMAP)": {
        "nerve": "정강신경 (Tibial nerve)",
        "level": "오금/발목, 관련 신경뿌리 L4-S3",
        "domain": "motor",
        "region": "leg"
    },
    "넙다리신경 복합근육활동전위 (Femoral CMAP)": {
        "nerve": "넙다리신경 (Femoral nerve)",
        "level": "L2-L4",
        "domain": "motor",
        "region": "leg"
    },

    "앞정강근 (Tibialis Anterior, TA)": {
        "nerve": "깊은종아리신경 (Deep peroneal nerve)",
        "level": "L4-L5",
        "domain": "muscle",
        "region": "leg"
    },
    "짧은발가락폄근 (Extensor Digitorum Brevis, EDB)": {
        "nerve": "깊은종아리신경 (Deep peroneal nerve)",
        "level": "L5-S1",
        "domain": "muscle",
        "region": "leg"
    },
    "짧은발가락벌림근 (Abductor Digiti Minimi pedis)": {
        "nerve": "가쪽발바닥신경 (Lateral plantar nerve)",
        "level": "S1-S2",
        "domain": "muscle",
        "region": "leg"
    },
    "긴엄지폄근 (Extensor Hallucis Longus, EHL)": {
        "nerve": "깊은종아리신경 (Deep peroneal nerve)",
        "level": "L5",
        "domain": "muscle",
        "region": "leg"
    },
    "긴종아리근 (Peroneus Longus)": {
        "nerve": "얕은종아리신경 (Superficial peroneal nerve)",
        "level": "L5-S1",
        "domain": "muscle",
        "region": "leg"
    },
    "장딴지근 (Gastrocnemius)": {
        "nerve": "정강신경 (Tibial nerve)",
        "level": "S1-S2",
        "domain": "muscle",
        "region": "leg"
    },
    "가자미근 (Soleus)": {
        "nerve": "정강신경 (Tibial nerve)",
        "level": "S1-S2",
        "domain": "muscle",
        "region": "leg"
    },
    "가쪽넓은근 (Vastus Lateralis)": {
        "nerve": "넙다리신경 (Femoral nerve)",
        "level": "L2-L4 (L3-L4 우세)",
        "domain": "muscle",
        "region": "leg"
    },
    "엉덩허리근 (Iliopsoas)": {
        "nerve": "허리신경얼기/넙다리신경 관련 분포",
        "level": "L2-L4 (주로 L2-L3)",
        "domain": "muscle",
        "region": "leg"
    },
    "큰볼기근 (Gluteus Maximus)": {
        "nerve": "아래볼기신경 (Inferior gluteal nerve)",
        "level": "L5-S2",
        "domain": "muscle",
        "region": "leg"
    },
    "중간볼기근 (Gluteus Medius)": {
        "nerve": "위볼기신경 (Superior gluteal nerve)",
        "level": "L4-S1",
        "domain": "muscle",
        "region": "leg"
    },
    "뒤넓적다리근 (Biceps Femoris)": {
        "nerve": "궁둥신경 분포 (Sciatic division)",
        "level": "L5-S2",
        "domain": "muscle",
        "region": "leg"
    },
    "허리 척추주위근 (Lumbar Paraspinal)": {
        "nerve": "척수뒤가지 (Posterior primary ramus)",
        "level": "허리 신경뿌리 수준",
        "domain": "muscle",
        "region": "leg"
    },

    "H 반사 (좌)": {
        "nerve": "정강신경-척수 S1 반사고리",
        "level": "H 반사 경로, 주로 S1",
        "domain": "reflex",
        "region": "leg"
    },
    "H 반사 (우)": {
        "nerve": "정강신경-척수 S1 반사고리",
        "level": "H 반사 경로, 주로 S1",
        "domain": "reflex",
        "region": "leg"
    },
    "H/M 비율": {
        "nerve": "척수 반사 흥분성 평가",
        "level": "H 반사 흥분성 평가",
        "domain": "reflex",
        "region": "leg"
    },
    "정중신경 F파 (Median F-wave)": {
        "nerve": "정중신경 근위부/운동신경뿌리",
        "level": "근위부 경로, 관련 신경뿌리 C8-T1",
        "domain": "reflex",
        "region": "arm"
    },
    "자신경 F파 (Ulnar F-wave)": {
        "nerve": "자신경 근위부/운동신경뿌리",
        "level": "근위부 경로, 관련 신경뿌리 C8-T1",
        "domain": "reflex",
        "region": "arm"
    },
    "정강신경 F파 (Tibial F-wave)": {
        "nerve": "정강신경 근위부/운동신경뿌리",
        "level": "근위부 경로, 관련 신경뿌리 L5-S2",
        "domain": "reflex",
        "region": "leg"
    },
    "종아리신경 F파 (Peroneal F-wave)": {
        "nerve": "종아리신경 근위부/운동신경뿌리",
        "level": "근위부 경로, 관련 신경뿌리 L4-S1",
        "domain": "reflex",
        "region": "leg"
    },

    "우측 자극 R1": {
        "nerve": "삼차신경-뇌줄기-얼굴신경 반사경로",
        "level": "눈깜빡반사 경로",
        "domain": "reflex",
        "region": "face"
    },
    "우측 자극 R2": {
        "nerve": "삼차신경-뇌줄기-얼굴신경 반사경로",
        "level": "눈깜빡반사 경로",
        "domain": "reflex",
        "region": "face"
    },
    "좌측 자극 R1": {
        "nerve": "삼차신경-뇌줄기-얼굴신경 반사경로",
        "level": "눈깜빡반사 경로",
        "domain": "reflex",
        "region": "face"
    },
    "좌측 자극 R2": {
        "nerve": "삼차신경-뇌줄기-얼굴신경 반사경로",
        "level": "눈깜빡반사 경로",
        "domain": "reflex",
        "region": "face"
    }
}

CASE_LIBRARY = {
    "1. 목-팔 방사통과 팔 근력 약화": {
        "patient": {
            "age": 57, "sex": "남", "side": "우",
            "symptoms": [
                "뒷목에서 오른쪽 어깨, 아래팔 노측(Radial side), 엄지 쪽으로 뻗치는 증상이 지속됨",
                "최근 팔꿈치를 굽히는 힘과 손목을 젖히는 힘이 약해져 검사 의뢰됨"
            ],
            "physical_exam": {
                "근력검사": [
                    "팔꿈치 굽힘 약화: 위팔두갈래근(Biceps brachii), 근피신경(Musculocutaneous nerve), 주로 C5-C6",
                    "손목 폄 약화: 긴노쪽손목폄근/짧은노쪽손목폄근(Extensor carpi radialis longus/brevis), 노신경(Radial nerve), 주로 C6-C7"
                ],
                "감각검사": [
                    "아래팔 노측(Radial side)과 엄지 쪽 감각저하: 주로 C6 피부분절(Dermatome)과 연관"
                ],
                "반사검사": [
                    "위팔두갈래근 힘줄반사 감소: 주로 C5-C6",
                    "위팔노근 힘줄반사 감소: 주로 C5-C6"
                ]
            }
        },
        "findings": {
            "정중신경 감각신경활동전위 (Median SNAP)": ("정상 (Normal)", "정상 (Normal)"),
            "노신경 표재감각신경활동전위 (Superficial Radial SNAP)": ("정상 (Normal)", "정상 (Normal)"),
            "근피신경 복합근육활동전위 (Musculocutaneous CMAP)": ("정상 (Normal)", "정상 (Normal)"),
            "노신경 복합근육활동전위 (Radial CMAP)": ("정상 (Normal)", "정상 (Normal)"),
            "목 척추주위근 (Cervical Paraspinal)": ("정상 (Normal)", "비정상 자발전위 출현 (Fibrillation Potential, Positive Sharp Wave 등)"),
            "위팔두갈래근 (Biceps Brachii)": ("정상 (Normal)", "비정상 자발전위 출현 (Fibrillation Potential, Positive Sharp Wave 등)"),
            "긴노쪽손목폄근/짧은노쪽손목폄근 (Extensor Carpi Radialis Longus/Brevis)": ("정상 (Normal)", "비정상 자발전위 출현 (Fibrillation Potential, Positive Sharp Wave 등)")
        },
        "teaching": [
            "목 신경뿌리병증(Cervical radiculopathy)에서는 감각신경활동전위(SNAP)와 말단 운동신경전도는 비교적 정상일 수 있고, 척추주위근과 관련 근육의 침근전도 이상이 진단에 도움이 됩니다.",
            "학생은 말초신경 분포와 피부분절 분포를 구분하고, 정상 SNAP 보존과 척추주위근 이상을 함께 해석하는 연습이 중요합니다."
        ]
    },

    "2. 야간 손저림과 엄지 근력 약화": {
        "patient": {
            "age": 46, "sex": "여", "side": "우",
            "symptoms": [
                "오른손 엄지, 검지, 중지와 반지손가락 노측(Radial side) 부위 저림이 반복됨",
                "야간에 증상이 심하고 최근 엄지 벌림 힘이 약해짐"
            ],
            "physical_exam": {
                "근력검사": [
                    "엄지 벌림 약화: 짧은엄지벌림근(Abductor pollicis brevis), 정중신경(Median nerve), C8-T1"
                ],
                "감각검사": [
                    "엄지, 검지, 중지 및 반지손가락 노측(Radial side) 감각저하: 정중신경(Median nerve) 감각영역"
                ],
                "증상 유발검사": [
                    "팔렌 검사(Phalen test) 양성",
                    "손목 티넬 징후(Tinel sign) 양성"
                ]
            }
        },
        "findings": {
            "정중신경 감각신경활동전위 (Median SNAP)": ("정상 (Normal)", "잠복기 지연 (Delayed latency)"),
            "정중신경 복합근육활동전위 (Median CMAP)": ("정상 (Normal)", "잠복기 지연 (Delayed latency)"),
            "짧은엄지벌림근 (Abductor Pollicis Brevis, APB)": ("정상 (Normal)", "비정상 자발전위 출현 (Fibrillation Potential, Positive Sharp Wave 등)")
        },
        "teaching": [
            "손목굴증후군(Carpal tunnel syndrome)에서는 정중신경 감각신경전도 이상이 먼저 나타나고, 진행되면 운동신경 잠복기 지연과 엄지두덩 근육 침범이 뒤따를 수 있습니다.",
            "학생은 야간 손저림, 정중신경 분포 감각저하, APB 약화와 정중신경 전도지연을 하나의 대표 패턴으로 연결해 이해하는 것이 중요합니다."
        ]
    },

    "3. 상완골 골절 후 손목 및 손가락 폄 약화": {
        "patient": {
            "age": 34, "sex": "남", "side": "우",
            "symptoms": [
                "상완골 몸통골절 이후 손목과 손가락을 들어 올리지 못하는 손목처짐(Wrist drop)이 발생함",
                "손등 노측(Radial side) 감각저하와 함께 손목 및 손가락 폄 약화가 뚜렷함"
            ],
            "physical_exam": {
                "근력검사": [
                    "손목 폄 약화: 손목폄근군(Extensor carpi radialis / extensor digitorum), 노신경(Radial nerve), C6-C7",
                    "손가락 폄 약화: 손가락폄근군, 노신경(Radial nerve), C7-C8"
                ],
                "감각검사": [
                    "손등 노측(Radial side) 감각저하: 노신경 표재감각분지(Superficial radial sensory branch) 영역과 연관"
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
        "teaching": [
            "감각신경활동전위가 감소하면 병변이 신경뿌리보다 원위부의 말초신경에 있을 가능성이 높습니다.",
            "학생은 손목처짐에서 노신경병증(Radial neuropathy), 뒤뼈사이신경병증(Posterior interosseous neuropathy), 목 신경뿌리병증을 함께 감별하는 연습이 필요합니다."
        ]
    },

    "4. 4·5지 저림과 손 intrinsic 근력 약화": {
        "patient": {
            "age": 42, "sex": "남", "side": "우",
            "symptoms": [
                "오른쪽 4번째, 5번째 손가락 저림과 손의 자측(Ulnar side) 불편감이 있음",
                "최근 세밀한 손동작과 손가락 벌림/모음에서 힘이 빠지는 느낌이 생김"
            ],
            "physical_exam": {
                "근력검사": [
                    "새끼손가락 벌림 약화: 새끼벌림근(Abductor digiti minimi), 자신경(Ulnar nerve), C8-T1",
                    "손가락 벌림 약화: 첫째등쪽뼈사이근(First dorsal interosseous), 자신경(Ulnar nerve), C8-T1"
                ],
                "감각검사": [
                    "4번째, 5번째 손가락과 손의 자측(Ulnar side) 감각저하: 자신경(Ulnar nerve) 감각영역"
                ],
                "증상 유발검사": [
                    "팔꿈치 굽힘 검사(Elbow flexion test) 양성"
                ]
            }
        },
        "findings": {
            "자신경 감각신경활동전위 (Ulnar SNAP)": ("정상 (Normal)", "잠복기 지연 (Delayed latency)"),
            "자신경 복합근육활동전위 (Ulnar CMAP)": ("정상 (Normal)", "잠복기 지연 (Delayed latency)"),
            "새끼벌림근 (Abductor Digiti Minimi, ADM)": ("정상 (Normal)", "비정상 자발전위 출현 (Fibrillation Potential, Positive Sharp Wave 등)"),
            "첫째등쪽뼈사이근 (First Dorsal Interosseous, FDI)": ("정상 (Normal)", "비정상 자발전위 출현 (Fibrillation Potential, Positive Sharp Wave 등)")
        },
        "teaching": [
            "팔꿈치부 자신경병증(Ulnar neuropathy at elbow)에서는 4·5지 저림과 손 intrinsic 근육 약화가 대표적이며, 자신경 전도 이상과 ADM/FDI 침근전도 이상이 함께 나타날 수 있습니다.",
            "학생은 C8-T1 신경뿌리병증과 감별하기 위해 감각신경전도 이상 유무와 척추주위근 침범 여부를 함께 보는 연습이 필요합니다."
        ]
    },

    "5. 허리-다리 증상과 발처짐": {
        "patient": {
            "age": 61, "sex": "여", "side": "우",
            "symptoms": [
                "허리에서 우측 엉치와 종아리 가쪽, 발등 쪽으로 증상이 뻗침",
                "최근 걷다가 발끝이 걸리는 우측 발처짐(Foot drop)이 심해짐"
            ],
            "physical_exam": {
                "근력검사": [
                    "발목 등굽힘 약화: 앞정강근(Tibialis anterior), 깊은종아리신경(Deep peroneal nerve), 주로 L4-L5",
                    "엄지발가락 폄 약화: 긴엄지폄근(Extensor hallucis longus), 깊은종아리신경(Deep peroneal nerve), 주로 L5"
                ],
                "감각검사": [
                    "종아리 가쪽과 발등 감각저하: 주로 L5 피부분절(Dermatome)과 연관"
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
        "teaching": [
            "L5 신경뿌리병증(L5 radiculopathy)에서는 발처짐이 나타날 수 있으며, 감각신경전도와 원위 운동신경전도가 비교적 정상인데 척추주위근과 L5 관련 근육의 침근전도 이상이 동반될 수 있습니다.",
            "학생은 종아리신경병증(Peroneal neuropathy)과 감별할 때 SNAP 보존, 척추주위근 이상, 중간볼기근 및 긴엄지폄근 침범을 함께 해석하는 연습이 중요합니다."
        ]
    },

    "6. 압박 후 발처짐과 발등 감각저하": {
        "patient": {
            "age": 31, "sex": "남", "side": "좌",
            "symptoms": [
                "하퇴 골절 후 석고붕대를 제거한 뒤 발목을 위로 들기 어려워짐",
                "좌측 발처짐(Foot drop)과 발등 감각저하가 비교적 갑자기 나타남"
            ],
            "physical_exam": {
                "근력검사": [
                    "발목 등굽힘 약화: 앞정강근(Tibialis anterior), 깊은종아리신경(Deep peroneal nerve), L4-L5",
                    "엄지발가락 폄 약화: 긴엄지폄근(Extensor hallucis longus), 깊은종아리신경(Deep peroneal nerve), L5",
                    "발가쪽번짐(외번) 약화 가능: 긴종아리근(Peroneus longus), 얕은종아리신경(Superficial peroneal nerve), L5-S1",
                    "발안쪽번짐(내번)은 비교적 보존: 뒤정강근(Tibialis posterior), 정강신경(Tibial nerve), L4-L5"
                ],
                "감각검사": [
                    "종아리 가쪽과 발등 감각저하: 얕은종아리신경 감각영역과 연관"
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
        "teaching": [
            "종아리뼈머리 부위 압박이나 손상 뒤 발처짐이 생기고 superficial peroneal SNAP 감소가 있으면 종아리신경병증(Peroneal neuropathy) 가능성이 높습니다.",
            "학생은 발안쪽번짐 보존, 감각신경전도 감소, 척추주위근 정상 소견을 통해 L5 신경뿌리병증과 감별하는 연습이 필요합니다."
        ]
    },

    "7. 골반 외상 후 다리 전반의 근력 약화": {
        "patient": {
            "age": 45, "sex": "여", "side": "좌",
            "symptoms": [
                "골반 골절 수술 후 좌측 다리 전반의 근력 약화가 생김",
                "허벅지와 종아리의 넓은 범위 감각 둔화와 보행장애가 동반됨"
            ],
            "physical_exam": {
                "근력검사": [
                    "무릎 폄 약화: 가쪽넓은근(Vastus lateralis), 넙다리신경(Femoral nerve), L2-L4",
                    "발목 등굽힘 약화: 앞정강근(Tibialis anterior), 깊은종아리신경(Deep peroneal nerve), L4-L5"
                ],
                "감각검사": [
                    "허벅지와 종아리의 넓은 범위 감각저하: 여러 말초신경 분포가 함께 침범된 양상"
                ]
            }
        },
        "findings": {
            "허리 척추주위근 (Lumbar Paraspinal)": ("정상 (Normal)", "정상 (Normal)"),
            "장딴지신경 감각신경활동전위 (Sural SNAP)": ("정상 (Normal)", "감소 (Reduced)"),
            "종아리신경 복합근육활동전위 (Peroneal CMAP)": ("정상 (Normal)", "감소 (Reduced)"),
            "넙다리신경 복합근육활동전위 (Femoral CMAP)": ("정상 (Normal)", "감소 (Reduced)"),
            "가쪽넓은근 (Vastus Lateralis)": ("정상 (Normal)", "비정상 자발전위 출현 (Fibrillation Potential, Positive Sharp Wave 등)"),
            "앞정강근 (Tibialis Anterior, TA)": ("정상 (Normal)", "비정상 자발전위 출현 (Fibrillation Potential, Positive Sharp Wave 등)")
        },
        "teaching": [
            "골반 외상 이후 하나의 신경이나 하나의 신경뿌리로 설명하기 어려운 다영역 운동·감각 침범이 있으면 허리엉치신경얼기병증(Lumbosacral plexopathy)을 생각할 수 있습니다.",
            "학생은 감각신경 이상이 있으면서 척추주위근이 정상이면 신경뿌리병증보다 신경얼기병증 가능성이 높아진다는 점을 익히는 것이 중요합니다."
        ]
    },

    "8. 양측 발끝 저림과 발가락 근력 약화": {
        "patient": {
            "age": 67, "sex": "남", "side": "양측",
            "symptoms": [
                "당뇨병 병력이 오래되었고 양쪽 발끝 저림이 서서히 진행함",
                "최근 발가락 힘이 약해지고 보행 시 발의 감각이 둔해짐"
            ],
            "physical_exam": {
                "근력검사": [
                    "발가락 움직임 약화: 발 자체기원근육 및 발가락 폄/굽힘 관련 근육, 종아리신경/정강신경(Peroneal/Tibial nerve), 주로 L5-S1"
                ],
                "감각검사": [
                    "양측 발끝부터 시작되는 감각저하: 길이의존성(Length-dependent) 말초신경 침범 양상"
                ],
                "반사검사": [
                    "아킬레스 힘줄반사 양측 감소 또는 소실: 정강신경(Tibial nerve), S1-S2"
                ]
            }
        },
        "findings": {
            "장딴지신경 감각신경활동전위 (Sural SNAP)": ("감소 (Reduced)", "감소 (Reduced)"),
            "얕은종아리신경 감각신경활동전위 (Superficial Peroneal SNAP)": ("감소 (Reduced)", "감소 (Reduced)"),
            "정강신경 복합근육활동전위 (Tibial CMAP)": ("감소 (Reduced)", "감소 (Reduced)")
        },
        "teaching": [
            "양측 발끝부터 시작하는 감각저하와 여러 신경의 진폭 감소는 축삭성 다발신경병증(Axonal polyneuropathy) 패턴을 이해하는 데 좋은 예입니다.",
            "학생은 대칭성, 원위부 우세, 감각신경과 운동신경의 다발성 진폭 감소를 다발신경병증의 대표 소견으로 익히면 좋습니다."
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
                "근력검사": [
                    "원위부와 일부 근위부를 포함한 대칭적 근력저하가 관찰됨"
                ],
                "감각검사": [
                    "양손과 양발의 대칭적 감각저하: 여러 말초신경 감각영역 침범 양상"
                ],
                "반사검사": [
                    "깊은힘줄반사 전반적 감소 또는 소실"
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
        "teaching": [
            "여러 감각·운동 신경에서 양측성 잠복기 지연이 반복되고 F파 이상이 동반되면 말이집탈락성 다발신경병증(Demyelinating polyneuropathy) 패턴을 생각할 수 있습니다.",
            "학생은 축삭성 다발신경병증의 진폭 감소 패턴과, 말이집탈락성 신경병증의 잠복기 지연·후기반사 이상 패턴을 구분하는 연습이 중요합니다."
        ]
    },

    "10. 눈꺼풀 떨림과 눈 주위 불편감 지속": {
        "patient": {
            "age": 62, "sex": "여", "side": "우",
            "symptoms": [
                "우측 눈꺼풀 떨림과 눈 주위 불편감이 10일 이상 지속됨",
                "눈 주변 반사경로와 얼굴신경 기능 평가를 위해 검사함"
            ],
            "physical_exam": {
                "얼굴근육 움직임 평가": [
                    "우측 눈둘레근(Orbicularis oculi) 주변 움직임이 다소 둔하고 불편감을 호소함"
                ],
                "감각검사": [
                    "우측 눈 주위 감각 이상 또는 불편감: 삼차신경(Trigeminal nerve) V1 영역과 연관 가능"
                ]
            }
        },
        "findings": {
            "우측 자극 R1": ("지연 또는 소실 (Delayed/Absent)", ""),
            "우측 자극 R2": ("지연 또는 소실 (Delayed/Absent)", ""),
            "좌측 자극 R1": ("정상 (Normal)", ""),
            "좌측 자극 R2": ("정상 (Normal)", "")
        },
        "teaching": [
            "눈깜빡반사(Blink reflex)는 삼차신경(Trigeminal nerve), 뇌줄기(Brainstem), 얼굴신경(Facial nerve)이 함께 관여하는 반사검사입니다.",
            "학생은 눈꺼풀 떨림, 눈 주위 불편감, 반사경로 이상 가능성을 함께 연결해 이해하고, 한쪽 자극에서 이상이 두드러질 때 편측 반사경로 이상 가능성을 생각하는 연습이 필요합니다."
        ]
    },

    "11. 뇌졸중 후 발목 발바닥굽힘근 경직(Spasticity) 평가": {
        "patient": {
            "age": 68, "sex": "남", "side": "우",
            "symptoms": [
                "뇌졸중 이후 우측 발목이 뻣뻣해지고 보행 시 발끝이 바닥에 잘 걸림",
                "치료 전후 발목 발바닥굽힘근 경직(Spasticity) 변화를 정량적으로 평가하기 위해 검사함"
            ],
            "physical_exam": {
                "근긴장검사": [
                    "발목 발바닥굽힘근의 경직(Spasticity) 증가: 장딴지근(Gastrocnemius), 가자미근(Soleus), 정강신경(Tibial nerve), S1-S2"
                ],
                "반사검사": [
                    "아킬레스 힘줄반사 항진 및 발목간대경련(Ankle clonus) 관찰"
                ],
                "보행관찰": [
                    "우측 하지의 경직성 보행(Spastic gait) 양상 관찰"
                ]
            }
        },
        "findings": {
            "정강신경 복합근육활동전위 (Tibial CMAP)": ("정상 (Normal)", "정상 (Normal)"),
            "H 반사 (우)": ("항진 또는 문턱값 감소 (Hyperactive / lower threshold)", ""),
            "H/M 비율": ("증가 가능 (May be increased)", "")
        },
        "teaching": [
            "이 사례에서 H 반사는 질환 진단보다 발목 발바닥굽힘근 경직(Spasticity)과 관련된 척수 반사 흥분성을 정량적으로 추적하는 교육용 지표로 이해하는 것이 더 적절합니다.",
            "학생은 치료 전후 H 반사 변화와 H/M 비율 변화를 임상적 경직 변화, 보행 변화, 기능 변화와 함께 연결해 해석하는 연습을 할 수 있습니다."
        ]
    },

    "12. 급성 양측 다리 근력 약화": {
        "patient": {
            "age": 35, "sex": "남", "side": "양측",
            "symptoms": [
                "장염 이후 갑자기 양쪽 다리 힘이 빠져 앉았다 일어서기가 어려워짐",
                "빠르게 진행하는 양측 하지 근력저하로 검사 의뢰됨"
            ],
            "physical_exam": {
                "근력검사": [
                    "엉덩관절 굽힘 약화: 엉덩허리근(Iliopsoas), 주로 L2-L3",
                    "무릎 폄 약화: 가쪽넓은근(Vastus lateralis), 넙다리신경(Femoral nerve), L2-L4"
                ],
                "감각검사": [
                    "원위부 감각저하는 뚜렷하지 않거나 경미할 수 있음"
                ],
                "반사검사": [
                    "깊은힘줄반사 감소 또는 소실 가능"
                ]
            }
        },
        "findings": {
            "정강신경 복합근육활동전위 (Tibial CMAP)": ("정상 (Normal)", "정상 (Normal)"),
            "종아리신경 복합근육활동전위 (Peroneal CMAP)": ("정상 (Normal)", "정상 (Normal)"),
            "정강신경 F파 (Tibial F-wave)": ("지연 또는 소실 (Delayed/Absent)", "지연 또는 소실 (Delayed/Absent)"),
            "종아리신경 F파 (Peroneal F-wave)": ("지연 또는 소실 (Delayed/Absent)", "지연 또는 소실 (Delayed/Absent)")
        },
        "teaching": [
            "초기 급성 염증성 다발신경병증(Acute inflammatory polyneuropathy)에서는 원위부 운동신경전도가 비교적 정상이어도 F파 이상이 먼저 나타날 수 있습니다.",
            "학생은 빠르게 진행하는 대칭성 약화, 반사저하, 후기반사 이상을 함께 묶어 초기 길랭-바레 증후군(Guillain-Barré syndrome, GBS) 가능성을 떠올리는 연습이 필요합니다."
        ]
    }
}

def normalize_case_item_name(item_name):
    mapping = {
        "짧은엄지벌림근 (Abductor Pollicis Brevis, Abductor Pollics Brevis)": "짧은엄지벌림근 (Abductor Pollicis Brevis, APB)",
        "H 반사 (우측)": "H 반사 (우)",
        "H 반사 (좌측)": "H 반사 (좌)",
        "가쪽넓은근 (Vastus Lateralis)": "가쪽넓은근 (Vastus Lateralis)",
    }
    return mapping.get(item_name, item_name)

def compose_ncs_result(distal_amp, distal_lat, proximal_amp=None, proximal_lat=None, conduction=None):
    tags = []
    for amp, lat, label in [
        (distal_amp, distal_lat, "원위부"),
        (proximal_amp, proximal_lat, "근위부")
    ]:
        if amp is None and lat is None:
            continue

        if amp == "무반응 (No response)":
            tags.append(f"{label} 무반응")
            continue

        sub = []
        if amp == "감소 (Reduced)":
            sub.append("진폭 감소")
        if lat == "잠복기 지연 (Delayed latency)":
            sub.append("잠복기 지연")
        if sub:
            tags.append(f"{label} " + " 및 ".join(sub))

    if conduction and conduction != "정상 (Normal)":
        tags.append(conduction)

    return "정상 (Normal)" if not tags else " / ".join(tags)

def text_has_any(value, keywords):
    v = str(value).lower()
    return any(k.lower() in v for k in keywords)

# ==========================================
# 3. 보조 및 유틸리티 함수
# ==========================================
def classify_finding_domain(item_name):
    """
    사례 상세 화면에서 전기생리 소견을
    - 신경전도검사
    - 침근전도검사
    - 반사검사
    로 분류하기 위한 함수
    """
    normalized = normalize_case_item_name(item_name)
    anatomy = ANATOMY.get(normalized)

    if not anatomy:
        return "other"

    domain = anatomy.get("domain")

    if domain in ["sensory", "motor"]:
        return "ncs"
    if domain == "muscle":
        return "needle"
    if domain == "reflex":
        return "reflex"

    return "other"

def get_side_labels(side):
    if side == "좌":
        return {"normal_side": "우측", "lesion_side": "좌측"}
    if side == "우":
        return {"normal_side": "좌측", "lesion_side": "우측"}
    return {"normal_side": "반대측", "lesion_side": "병변측"}

def get_domain_options(domain, item=None):
    if domain in ["sensory", "motor"]:
        return ["정상 (Normal)", "감소 (Reduced)", "잠복기 지연 (Delayed latency)", "무반응 (No response)"]

    if domain == "muscle":
        return [
            "정상 (Normal)",
            "비정상 자발전위 (Fibrillation, Positive sharp wave 등) 출현",
            "무반응 / 전기적 침묵 (Electrical silence)"
        ]

    if domain == "reflex":
        if item in ["H 반사 (좌)", "H 반사 (우)"]:
            return ["정상 (Normal)", "지연 또는 소실 (Delayed/Absent)", "항진 또는 문턱값 감소 (Hyperactive / lower threshold)"]
        if item == "H/M 비율":
            return ["정상 (Normal)", "증가 가능 (May be increased)"]
        return ["정상 (Normal)", "지연 (Delayed)", "지연 또는 소실 (Delayed/Absent)", "양측 지연 또는 소실 (Bilateral delayed/absent)"]

    return ["정상 (Normal)"]

def is_abnormal(value):
    if value is None:
        return False
    value = str(value).strip().lower()
    if value == "" or value == "미선택":
        return False
    normal_aliases = {"정상", "normal", "정상 (normal)"}
    return value not in {x.lower() for x in normal_aliases}

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

def find_section_for_item(item_name):
    for section, items in SECTIONS.items():
        if item_name in items:
            return section
    return None

def safe_index(options, value, default=0):
    return options.index(value) if value in options else default

def get_case_names_for_selection():
    return list(CASE_LIBRARY.keys())

def simplify_level_text(level_text):
    if not level_text:
        return ""
    replacements = {
        "정중신경 말단운동전도, 관련 신경뿌리 C8-T1": "정중신경 말단운동전도, C8-T1",
        "말단/팔꿉 구간 운동전도, 관련 신경뿌리 C8-T1": "말단/팔꿉 구간 운동전도, C8-T1",
        "위팔/아래팔 운동경로, 관련 신경뿌리 C6-C8": "위팔/아래팔 운동경로, C6-C8",
        "오금/발목, 관련 신경뿌리 L4-S3": "오금/발목, L4-S3",
        "종아리뼈머리/종아리 구간, 관련 신경뿌리 L4-S1": "종아리뼈머리/종아리 구간, L4-S1",
        "근위부 경로, 관련 신경뿌리 C8-T1": "근위부 경로, C8-T1",
        "근위부 경로, 관련 신경뿌리 L5-S2": "근위부 경로, L5-S2",
        "근위부 경로, 관련 신경뿌리 L4-S1": "근위부 경로, L4-S1",
    }
    for old, new in replacements.items():
        level_text = level_text.replace(old, new)
    return level_text

def build_diff_dx_details(dx_name):
    detail_map = {
        "손목굴증후군 포함 정중신경 포착병증 (Median Entrapment Neuropathy)":
            "정중신경 관련 검사에서 잠복기 지연이 중심이면 손목굴 부위 정중신경 포착병증 가능성이 높습니다. 목 신경뿌리병증과 감별할 때는 목 척추주위근 이상 여부를 함께 봅니다.",
        "정중신경병증 (Median Neuropathy)":
            "이상이 정중신경 관련 항목에 모여 있으면 정중신경병증을 생각합니다. 손목 수준인지 그보다 위쪽인지 임상 증상과 함께 판단합니다.",
        "자신경병증 (Ulnar Neuropathy)":
            "이상이 자신경 관련 항목에 모여 있으면 자신경병증을 생각합니다. 4, 5번째 손가락 저림과 자체기원근육 약화가 함께 있는지 확인합니다.",
        "팔꿈치부 자신경병증 (Ulnar Neuropathy at Elbow)":
            "자신경 관련 검사 이상과 손의 자체기원근육 이상이 함께 있으면 팔꿈치부 자신경병증 가능성이 높습니다.",
        "노신경병증 (Radial Neuropathy)":
            "노신경 관련 검사 이상과 손목 폄 약화가 함께 있으면 노신경병증 가능성이 높습니다. 목 신경뿌리병증과 감별할 때는 목 척추주위근 이상 여부가 도움이 됩니다.",
        "종아리신경병증 (Peroneal Neuropathy)":
            "종아리신경 관련 검사 이상과 발처짐이 함께 있으면 종아리신경병증 가능성이 높습니다. L5 신경뿌리병증과 감별할 때는 허리 척추주위근 이상 여부를 함께 봅니다.",
        "정강신경병증 (Tibial Neuropathy)":
            "정강신경 관련 검사 이상이 모여 있으면 정강신경병증을 생각합니다.",
        "목 신경뿌리병증 (Cervical Radiculopathy)":
            "감각신경전도 이상은 뚜렷하지 않은데 목 척추주위근과 관련 근육에서 비정상 자발전위가 보이면 목 신경뿌리병증 가능성이 높습니다.",
        "허리 신경뿌리병증 (Lumbar Radiculopathy)":
            "감각신경전도 이상은 뚜렷하지 않은데 허리 척추주위근과 관련 다리 근육에서 비정상 자발전위가 보이면 허리 신경뿌리병증 가능성이 높습니다.",
        "팔신경얼기병증 (Brachial Plexopathy)":
            "여러 팔 신경에 걸친 이상이 있지만 목 척추주위근 이상이 뚜렷하지 않으면 팔신경얼기병증을 생각할 수 있습니다.",
        "허리엉치신경얼기병증 (Lumbosacral Plexopathy)":
            "여러 다리 신경에 걸친 이상이 있지만 허리 척추주위근 이상이 뚜렷하지 않으면 허리엉치신경얼기병증을 생각할 수 있습니다.",
        "다발신경병증 (Polyneuropathy)":
            "여러 감각신경과 운동신경에서 양측성 이상이 보이면 다발신경병증 패턴에 가깝습니다.",
        "축삭성 다발신경병증 (Axonal Polyneuropathy)":
            "여러 신경에서 진폭 감소가 중심이면 축삭성 다발신경병증 가능성이 높습니다.",
        "말이집탈락성 다발신경병증 (Demyelinating Polyneuropathy)":
            "여러 신경에서 잠복기 지연이 반복되면 말이집탈락 신경병증 가능성을 생각합니다.",
        "운동신경세포질환 가능성 (Motor Neuron Disease, correlate clinically)":
            "감각신경 이상은 뚜렷하지 않은데 여러 근육에서 비정상 자발전위가 보이면 운동신경세포질환도 감별해야 합니다. 다만 임상 진찰과 함께 매우 신중히 해석해야 합니다.",
        "S1 신경뿌리/근위부 정강신경 경로 이상 가능성":
            "H 반사 지연 또는 소실이 보이면 S1 신경뿌리 또는 근위부 정강신경 경로 이상 가능성을 생각합니다.",
        "중추성 경직 / 상위운동신경세포 병변 (Spasticity / UMN Lesion)":
            "H 반사 항진 또는 H/M 비율 증가가 보이면 상위운동신경세포 병변과 관련된 반사 흥분성 증가를 생각할 수 있습니다.",
        "근위부 말이집탈락 신경병증 / 초기 GBS 가능성":
            "여러 F파에서 지연 또는 소실이 보이면 근위부 말이집탈락 신경병증이나 초기 GBS 가능성을 생각할 수 있습니다.",
        "뇌줄기 반사경로 이상 가능성 (Brainstem reflex pathway involvement)":
            "양쪽 자극에서 눈깜빡반사 이상이 보이면 뇌줄기 반사경로 이상 가능성을 생각합니다.",
        "삼차-뇌줄기-안면신경 반사경로의 편측 이상 가능성":
            "한쪽 자극에서 눈깜빡반사 이상이 두드러지면 해당 쪽 반사경로 이상 가능성을 생각합니다.",
        "비특이적 이상 또는 추가 평가 필요 (Nonspecific)":
            "현재 입력된 정보만으로는 한 가지 질환으로 좁히기 어렵습니다. 더 많은 검사 항목과 임상소견이 필요합니다."
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
    if result.get("suggestions"):
        lines.append("[추가 참고]")
        for s in result.get("suggestions", []):
            lines.append(f"- {s}")

    lines.append("")
    lines.append("※ 본 결과는 학생 교육용 참고 자료이며 실제 임상 진단을 대체하지 않습니다.")
    return "\\n".join(lines)

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
        elif a["domain"] == "reflex":
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
        if "넙다리신경" in item or "넓적다리신경" in item or "가쪽넓은근" in item or "엉덩허리근" in item:
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
        reasons.append("감각신경전도 이상은 뚜렷하지 않은데 목 척추주위근과 관련 근육에서 비정상 자발전위가 보여 목 신경뿌리병증 가능성이 높습니다.")
        suggestions.add("목 MRI 및 신경학적 진찰과 함께 해석하면 도움이 됩니다.")

    if sensory_abnormal == 0 and muscle_abnormal >= 2 and low_back_root_hint >= 1:
        scores["허리 신경뿌리병증 (Lumbar Radiculopathy)"] += 10
        lesion_tags.add("신경뿌리 수준")
        reasons.append("감각신경전도 이상은 뚜렷하지 않은데 허리 척추주위근과 관련 다리 근육에서 비정상 자발전위가 보여 허리 신경뿌리병증 가능성이 높습니다.")
        suggestions.add("허리 MRI 및 분절별 근력검사와 함께 해석하면 도움이 됩니다.")

    if sensory_abnormal >= 1 and muscle_abnormal >= 2 and paraspinal_abnormal == 0 and arm_plexus_hint >= 1:
        scores["팔신경얼기병증 (Brachial Plexopathy)"] += 9
        lesion_tags.add("신경얼기 수준")
        reasons.append("여러 팔 신경에 걸쳐 이상이 있지만 목 척추주위근 이상이 뚜렷하지 않아 팔신경얼기병증 가능성을 생각할 수 있습니다.")

    if sensory_abnormal >= 1 and muscle_abnormal >= 2 and paraspinal_abnormal == 0 and leg_plexus_hint >= 1:
        scores["허리엉치신경얼기병증 (Lumbosacral Plexopathy)"] += 9
        lesion_tags.add("신경얼기 수준")
        reasons.append("여러 다리 신경에 걸쳐 이상이 있지만 허리 척추주위근 이상이 뚜렷하지 않아 허리엉치신경얼기병증 가능성을 생각할 수 있습니다.")

    if median_related >= 2 and arm_abnormal <= 6:
        scores["정중신경병증 (Median Neuropathy)"] += 7
        lesion_tags.add("단일 말초신경 수준")
        reasons.append("이상이 정중신경 관련 항목에 모여 있습니다.")

    if ulnar_related >= 2 and arm_abnormal <= 6:
        scores["자신경병증 (Ulnar Neuropathy)"] += 7
        lesion_tags.add("단일 말초신경 수준")
        reasons.append("이상이 자신경 관련 항목에 모여 있습니다.")

    if radial_related >= 2 and arm_abnormal <= 6:
        scores["노신경병증 (Radial Neuropathy)"] += 7
        lesion_tags.add("단일 말초신경 수준")
        reasons.append("이상이 노신경 관련 항목에 모여 있습니다.")

    if peroneal_related >= 2 and leg_abnormal <= 7:
        scores["종아리신경병증 (Peroneal Neuropathy)"] += 8
        lesion_tags.add("단일 말초신경 수준")
        reasons.append("이상이 종아리신경 관련 항목에 모여 있습니다.")

    if tibial_related >= 2 and leg_abnormal <= 7:
        scores["정강신경병증 (Tibial Neuropathy)"] += 6
        lesion_tags.add("단일 말초신경 수준")
        reasons.append("이상이 정강신경 관련 항목에 모여 있습니다.")

    if median_related >= 2 and delayed_count >= 1:
        scores["손목굴증후군 포함 정중신경 포착병증 (Median Entrapment Neuropathy)"] += 8
        reasons.append("정중신경 관련 검사에서 잠복기 지연이 보여 손목굴 부위 정중신경 포착병증 가능성을 생각할 수 있습니다.")

    if ulnar_related >= 2 and delayed_count >= 1:
        scores["팔꿈치부 자신경병증 (Ulnar Neuropathy at Elbow)"] += 7
        reasons.append("자신경 관련 검사에서 잠복기 지연이 보여 팔꿈치부 자신경병증 가능성을 생각할 수 있습니다.")

    if sensory_abnormal >= 2 and (motor_abnormal >= 1 or side == "양측"):
        scores["다발신경병증 (Polyneuropathy)"] += 10
        lesion_tags.add("다발 말초신경 수준")
        reasons.append("여러 감각신경과 운동신경에서 양측성 이상이 보여 다발신경병증 패턴에 가깝습니다.")

    if delayed_count >= 3 and reduced_count <= delayed_count:
        scores["말이집탈락성 다발신경병증 (Demyelinating Polyneuropathy)"] += 7
        lesion_tags.add("말이집탈락 신경병증 패턴")
        reasons.append("여러 신경에서 잠복기 지연이 반복되어 말이집탈락 신경병증 가능성을 생각할 수 있습니다.")

    if reduced_count >= 3 and sensory_abnormal >= 2:
        scores["축삭성 다발신경병증 (Axonal Polyneuropathy)"] += 6
        reasons.append("여러 신경에서 진폭 감소가 중심이어서 축삭성 다발신경병증 가능성을 생각할 수 있습니다.")

    if muscle_abnormal >= 4 and sensory_abnormal == 0 and spontaneous_count >= 3 and paraspinal_abnormal == 0:
        scores["운동신경세포질환 가능성 (Motor Neuron Disease, correlate clinically)"] += 4
        lesion_tags.add("운동신경세포 수준 가능성")
        reasons.append("감각신경 이상은 뚜렷하지 않은데 여러 근육에서 비정상 자발전위가 보여 운동신경세포질환도 감별해야 합니다. 다만 매우 신중한 해석이 필요합니다.")

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

        if "f-wave" in normalized_item.lower() and ("지연" in combined or "소실" in combined or "absent" in combined):
            f_wave_abnormal += 1

    if h_reflex_abnormal >= 1 and tibial_related >= 1:
        scores["S1 신경뿌리/근위부 정강신경 경로 이상 가능성"] += 5
        reasons.append("H 반사 지연 또는 소실이 보여 S1 신경뿌리 또는 근위부 정강신경 경로 이상 가능성을 생각할 수 있습니다.")

    if h_reflex_hyperactive >= 1 or hm_ratio_increased >= 1:
        scores["중추성 경직 / 상위운동신경세포 병변 (Spasticity / UMN Lesion)"] += 8
        lesion_tags.add("척수 반사 흥분성 증가")
        reasons.append("H 반사 항진 또는 H/M 비율 증가가 보여 경직(Spasticity)과 관련된 척수 반사 흥분성 증가를 생각할 수 있습니다.")

    if f_wave_abnormal >= 2:
        scores["근위부 말이집탈락 신경병증 / 초기 GBS 가능성"] += 7
        reasons.append("여러 F파에서 지연 또는 소실이 보여 근위부 말이집탈락 신경병증이나 초기 GBS 가능성을 생각할 수 있습니다.")

    if blink_right_stim_abnormal >= 1 and blink_left_stim_abnormal >= 1:
        scores["뇌줄기 반사경로 이상 가능성 (Brainstem reflex pathway involvement)"] += 5
        reasons.append("양쪽 자극에서 눈깜빡반사 이상이 보여 뇌줄기 반사경로 이상 가능성을 생각할 수 있습니다.")
    elif blink_right_stim_abnormal >= 1 or blink_left_stim_abnormal >= 1:
        scores["삼차-뇌줄기-안면신경 반사경로의 편측 이상 가능성"] += 4
        reasons.append("한쪽 자극에서 눈깜빡반사 이상이 두드러져 해당 쪽 반사경로 이상 가능성을 생각할 수 있습니다.")

    if not scores:
        scores["비특이적 이상 또는 추가 평가 필요 (Nonspecific)"] = 1
        reasons.append("현재 입력된 검사 정보만으로는 병변 위치를 한 가지로 명확히 좁히기 어렵습니다.")

    top3 = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:3]
    for dx, score in top3:
        top3_details.append({
            "name": dx,
            "how_to_differentiate": build_diff_dx_details(dx)
        })

    return {
        "age": age,
        "sex": sex,
        "side": side,
        "final_dx": top3[0][0],
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
        if st.button(f"🏠 처음으로_{position}", use_container_width=True):
            st.session_state["current_screen"] = "home"
            st.session_state["confirmed_case"] = None
            clear_result()
            st.rerun()

    with c2:
        if st.button(f"⬅️ 이전으로_{position}", use_container_width=True):
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

def render_basic_info(disabled=False, title="기본 정보 입력"):
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown(f"### {title}")
    c1, c2, c3 = st.columns(3)
    age = c1.number_input("나이", min_value=0, max_value=120, value=st.session_state.get("age", 50), step=1, disabled=disabled)
    sex = c2.selectbox("성별", SEX_OPTIONS, index=safe_index(SEX_OPTIONS, st.session_state.get("sex", "미선택")), disabled=disabled)
    side = c3.selectbox("병변쪽/증상측", SIDE_OPTIONS, index=safe_index(SIDE_OPTIONS, st.session_state.get("side", "미선택")), disabled=disabled)
    st.markdown("</div>", unsafe_allow_html=True)
    return age, sex, side

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
    st.markdown("### 진행할 학습 모드를 선택하세요")
    selected_mode = st.radio(
        "진행할 학습 모드를 선택하세요",
        [MODE_CASE, MODE_DIRECT],
        label_visibility="collapsed"
    )

    if selected_mode == MODE_CASE:
        st.markdown('<div class="mobile-note">대표 임상사례를 보고 증상, 신체검사, 전기생리 소견을 함께 연결하는 모드입니다.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="mobile-note">학생이 이상 소견만 직접 입력하고 자동 분석 결과와 비교하는 모드입니다.</div>', unsafe_allow_html=True)

    if st.button("확인", type="primary", use_container_width=True):
        st.session_state["app_mode"] = selected_mode
        st.session_state["current_screen"] = "mode"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

def render_case_selector_only():
    case_options = get_case_names_for_selection()

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("### 📖 대표 사례 선택")
    st.markdown("모바일에서도 읽기 쉽도록 짧은 제목으로 정리했습니다. 학습할 사례를 선택하세요.")
    case_name = st.radio("사례 목록", case_options, label_visibility="collapsed")

    if st.button("사례 학습 시작", type="primary", use_container_width=True):
        st.session_state["confirmed_case"] = case_name
        st.session_state["current_screen"] = "case_detail"
        patient = CASE_LIBRARY[case_name].get("patient", {})
        st.session_state["age"] = patient.get("age", 50)
        st.session_state["sex"] = patient.get("sex", "미선택")
        st.session_state["side"] = patient.get("side", "미선택")
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

def render_direct_entry_start():
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("### 🧾 검사 입력 학습 시작")
    st.markdown('<div class="mobile-note">학생이 판독지의 이상 소견만 선택하여 병변 위치와 질환을 추론하는 학습 모드입니다.</div>', unsafe_allow_html=True)

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
    st.markdown("**1) 기본 정보 입력**")

    age = st.number_input("나이", min_value=1, max_value=120, value=int(st.session_state.get("age", 50)), step=1)
    sex = st.selectbox("성별", SEX_OPTIONS, index=safe_index(SEX_OPTIONS, st.session_state.get("sex", "미선택")))
    side = st.selectbox("병변측", SIDE_OPTIONS, index=safe_index(SIDE_OPTIONS, st.session_state.get("side", "미선택")))

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
    st.markdown("**2) 학습 안내**")
    st.markdown('<div class="case-bullet">• 이상 소견이 있는 항목만 체크해서 입력합니다.</div>', unsafe_allow_html=True)
    st.markdown('<div class="case-bullet">• 체크하지 않은 항목은 정상으로 처리됩니다.</div>', unsafe_allow_html=True)
    st.markdown('<div class="case-bullet">• 결과 해석은 현재 학생이 입력한 항목을 바탕으로 설명됩니다.</div>', unsafe_allow_html=True)
    st.markdown('<div class="case-bullet">• 현재 앱은 학생 교육용이므로 이해하기 쉬운 대표 해석 중심으로 결과를 제공합니다.</div>', unsafe_allow_html=True)

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
    c1, c2 = st.columns(2)

    with c1:
        if st.button("입력 화면으로 이동", type="primary", use_container_width=True):
            if sex == "미선택" or side == "미선택":
                st.warning("성별과 병변측을 선택하세요.")
            else:
                st.session_state["age"] = age
                st.session_state["sex"] = sex
                st.session_state["side"] = side
                st.session_state["current_screen"] = "direct_input"
                clear_result()
                st.rerun()

    with c2:
        if st.button("초기화", use_container_width=True):
            st.session_state["age"] = 50
            st.session_state["sex"] = "미선택"
            st.session_state["side"] = "미선택"
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
    teaching = case.get("teaching", [])
    physical_exam = patient.get("physical_exam", {})

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown(f'<div class="case-title-mobile">📘 {case_name}</div>', unsafe_allow_html=True)
    st.markdown(
        f'<div class="case-subtitle-mobile">연령: {patient.get("age", "-")}세 | 성별: {patient.get("sex", "-")} | 병변측: {patient.get("side", "-")}</div>',
        unsafe_allow_html=True
    )

    st.markdown('<hr class="strong-divider">', unsafe_allow_html=True)
    st.markdown('<div class="case-section-label">🗣️ 주요 증상</div>', unsafe_allow_html=True)
    for s in patient.get("symptoms", []):
        st.markdown(f'<div class="case-bullet">• {s}</div>', unsafe_allow_html=True)

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
    st.markdown('<div class="case-section-label">🧪 신체검사</div>', unsafe_allow_html=True)
    for exam_name, exam_items in physical_exam.items():
        st.markdown(f"**{exam_name}**")
        for item in exam_items:
            st.markdown(f'<div class="case-bullet">- {item}</div>', unsafe_allow_html=True)
        st.markdown('<hr class="soft-divider">', unsafe_allow_html=True)

    sensory_ncs_items = []
    motor_ncs_items = []
    needle_items = []
    reflex_items = []

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
        elif domain == "reflex":
            reflex_items.append((normalized_name, values))

    def render_finding_block(title, items):
        if not items:
            return

        st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
        st.markdown(f'<div class="case-section-label">{title}</div>', unsafe_allow_html=True)

        for item_name, values in items:
            left_val = values[0] if len(values) > 0 else ""
            right_val = values[1] if len(values) > 1 else ""

            st.markdown(f'<div class="finding-item-title">{item_name}</div>', unsafe_allow_html=True)

            if patient.get("side") == "양측":
                st.markdown(f'<div class="finding-subtext">좌측: {normalize_result_text(left_val)}</div>', unsafe_allow_html=True)
                if str(right_val).strip() != "":
                    st.markdown(f'<div class="finding-subtext">우측: {normalize_result_text(right_val)}</div>', unsafe_allow_html=True)

            elif str(right_val).strip() != "":
                side = patient.get("side", "병변")
                if side == "우":
                    st.markdown(f'<div class="finding-subtext">좌측(정상측): {normalize_result_text(left_val)}</div>', unsafe_allow_html=True)
                    st.markdown(f'<div class="finding-subtext">우측(병변측): {normalize_result_text(right_val)}</div>', unsafe_allow_html=True)
                elif side == "좌":
                    st.markdown(f'<div class="finding-subtext">좌측(병변측): {normalize_result_text(left_val)}</div>', unsafe_allow_html=True)
                    st.markdown(f'<div class="finding-subtext">우측(정상측): {normalize_result_text(right_val)}</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="finding-subtext">반대측: {normalize_result_text(left_val)}</div>', unsafe_allow_html=True)
                    st.markdown(f'<div class="finding-subtext">병변측: {normalize_result_text(right_val)}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="finding-subtext">결과: {normalize_result_text(left_val)}</div>', unsafe_allow_html=True)

            st.markdown('<hr class="item-divider">', unsafe_allow_html=True)

    render_finding_block("⚡ 감각신경전도검사 소견", sensory_ncs_items)
    render_finding_block("⚡ 운동신경전도검사 소견", motor_ncs_items)
    render_finding_block("🪡 침근전도검사 소견", needle_items)

    if reflex_items:
        render_finding_block("🔁 반사검사 소견", reflex_items)

    st.markdown('<div class="case-section-label">💡 핵심 학습 포인트</div>', unsafe_allow_html=True)
    for t in teaching:
        st.markdown(f'<div class="case-bullet">• {t}</div>', unsafe_allow_html=True)

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
    st.markdown('<div class="mobile-note">이 사례는 임상 증상, 근력·감각·반사 소견, 전기생리 결과를 함께 연결하는 연습을 위한 학생 교육용 자료입니다.</div>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

def render_item_card_header(item, a):
    st.markdown('<div class="input-row">', unsafe_allow_html=True)
    st.markdown(f'<div class="input-title">{item}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="input-meta">관련 신경: {a["nerve"]} | 관련 레벨: {simplify_level_text(a["level"])}</div>', unsafe_allow_html=True)

def render_check_item(section, item, side, disabled=False):
    a = ANATOMY.get(item)
    if not a:
        return None

    rv = st.session_state.get("input_reset_version", 0)
    check_key = f"chk_{rv}_{section}_{item}"
    render_item_card_header(item, a)

    use_item = st.checkbox("이 검사 항목에 이상 소견 입력하기", key=check_key, disabled=disabled)
    row = None

    if use_item:
        options = get_domain_options(a["domain"], item)

        if a["domain"] == "reflex":
            st.caption("입력 가이드: 반사검사는 해당 항목의 결과만 선택하면 됩니다.")
            res = st.selectbox("검사 결과", options, key=f"res_{rv}_{item}", disabled=disabled)
            row = {"section": section, "item": item, "left": res, "right": ""}

        elif side == "양측":
            st.caption("입력 가이드: 양측 병변이므로 좌측과 우측 결과를 각각 선택하세요.")
            c1, c2 = st.columns(2)
            left = c1.selectbox("좌측 소견", options, key=f"l_{rv}_{item}", disabled=disabled)
            right = c2.selectbox("우측 소견", options, key=f"r_{rv}_{item}", disabled=disabled)
            row = {"section": section, "item": item, "left": left, "right": right}

        else:
            if a["domain"] in ["sensory", "motor"]:
                st.caption(f"입력 가이드: 반대측은 정상으로 자동 반영됩니다. 병변측({side}측) 소견만 선택하세요.")
                c3, c4 = st.columns(2)

                amp = c3.selectbox(
                    "진폭",
                    ["정상 (Normal)", "감소 (Reduced)", "무반응 (No response)"],
                    key=f"amp_{rv}_{item}",
                    disabled=disabled
                )
                lat = c4.selectbox(
                    "잠복기",
                    ["정상 (Normal)", "잠복기 지연 (Delayed latency)"],
                    key=f"lat_{rv}_{item}",
                    disabled=disabled
                )

                if amp == "무반응 (No response)":
                    lesion_res = "무반응 (No response)"
                elif amp == "감소 (Reduced)" and lat == "잠복기 지연 (Delayed latency)":
                    lesion_res = "감소 (Reduced) 및 잠복기 지연 (Delayed latency)"
                elif amp == "감소 (Reduced)":
                    lesion_res = "감소 (Reduced)"
                elif lat == "잠복기 지연 (Delayed latency)":
                    lesion_res = "잠복기 지연 (Delayed latency)"
                else:
                    lesion_res = "정상 (Normal)"

            elif a["domain"] == "muscle":
                st.caption("입력 가이드: 침근전도에서는 비정상 자발전위 출현 여부를 중심으로 선택하세요.")
                lesion_res = st.selectbox(
                    "침근전도 소견",
                    options,
                    key=f"emg_{rv}_{item}",
                    disabled=disabled
                )
            else:
                lesion_res = "정상 (Normal)"

            if side == "좌":
                row = {"section": section, "item": item, "left": lesion_res, "right": "정상 (Normal)"}
            else:
                row = {"section": section, "item": item, "left": "정상 (Normal)", "right": lesion_res}

    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown('<hr class="item-divider">', unsafe_allow_html=True)
    return row

def render_input_sections_for_side(side):
    rows = []

    with st.expander("💡 [필독] 입력 가이드", expanded=True):
        st.markdown("""
현재 앱에서는 **학생이 실제로 체크할 수 있는 항목만** 입력하면 됩니다.

**1. 감각/운동 신경전도검사**
- **정상:** 이상 소견이 없으면 체크하지 않아도 됩니다.
- **진폭 감소:** 반응 크기가 줄어든 경우
- **잠복기 지연:** 반응이 정상보다 늦게 시작하는 경우
- **무반응:** 반응이 기록되지 않는 경우

**2. 침근전도검사**
- **비정상 자발전위 출현:** 휴식 시 fibrillation, positive sharp wave 등이 보이는 경우
- **전기적 침묵:** 반응이 거의 없는 경우

**3. 반사검사**
- H 반사, F파, 눈깜빡반사는 각 항목에서 보이는 결과만 선택하면 됩니다.

**중요**
- 체크하지 않은 항목은 모두 정상으로 처리됩니다.
- 현재 앱은 학생 교육용이므로, 입력한 항목 범위 안에서 이해하기 쉬운 설명을 제공합니다.
        """)

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("### 📋 검사 그룹 선택")
    st.markdown('<div class="mobile-note">이상 소견이 있는 항목만 체크하세요. 모바일에서는 항목을 순서대로 내려가며 확인하는 방식이 가장 읽기 쉽습니다.</div>', unsafe_allow_html=True)
    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

    tabs = st.tabs([
        "팔 신경전도",
        "팔 침근전도",
        "다리 신경전도",
        "다리 침근전도",
        "H 반사",
        "눈깜빡 반사"
    ])

    section_groups = [
        ["팔 감각신경전도검사 (arm sensory NCS)", "팔 운동신경전도검사 (arm motor NCS)"],
        ["팔 침근전도검사 근육 (arm needle EMG muscles)"],
        ["다리 감각신경전도검사 (leg sensory NCS)", "다리 운동신경전도검사 (leg motor NCS)"],
        ["다리 침근전도검사 근육 (leg needle EMG muscles)"],
        ["후기반사검사 (Late responses / H Reflex)"],
        ["눈깜빡반사검사 (Blink reflex)"]
    ]

    for tab, sections in zip(tabs, section_groups):
        with tab:
            st.info("이상 소견이 있는 항목만 체크해서 입력하세요. 체크하지 않은 항목은 정상으로 처리됩니다.")
            st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

            for sec in sections:
                st.markdown(f'<div class="big-section-title">{sec}</div>', unsafe_allow_html=True)
                st.markdown('<hr class="soft-divider">', unsafe_allow_html=True)

                for item in SECTIONS[sec]:
                    row = render_check_item(sec, item, side)
                    if row:
                        rows.append(row)

    st.markdown("</div>", unsafe_allow_html=True)
    return rows

def render_result_view(result):
    st.markdown('<div class="result-card">', unsafe_allow_html=True)
    st.markdown('<div class="result-title">📊 자동 분석 결과</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="result-text"><b>최종 유력 진단:</b> {result["final_dx"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="result-text"><b>손상 의심 신경:</b> {result["involved_nerves"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="result-text"><b>신경학적 레벨/분절:</b> {result["involved_levels"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="result-text"><b>중증도:</b> {result["severity"]}</div>', unsafe_allow_html=True)

    if result.get("lesion_tags"):
        st.markdown(f'<div class="result-text"><b>병변 해석 태그:</b> {", ".join(result["lesion_tags"])}</div>', unsafe_allow_html=True)

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
    st.markdown('<div class="result-label">🧠 판단 근거</div>', unsafe_allow_html=True)
    for reason in result.get("reasons", []):
        st.markdown(f'<div class="case-bullet">• {reason}</div>', unsafe_allow_html=True)

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
    st.markdown('<div class="result-label">🔍 Top 3 감별진단</div>', unsafe_allow_html=True)
    for i, item in enumerate(result.get("top3_details", []), 1):
        st.markdown(f'<div class="finding-item-title">{i}. {item["name"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="finding-subtext">감별 포인트: {item["how_to_differentiate"]}</div>', unsafe_allow_html=True)
        st.markdown('<hr class="soft-divider">', unsafe_allow_html=True)

    st.markdown('<div class="result-label">📌 입력된 이상 소견</div>', unsafe_allow_html=True)
    if result.get("abnormal_items"):
        for item in result["abnormal_items"]:
            st.markdown(f'<div class="finding-item-title">{item["항목"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="finding-subtext">{item["결과"]}</div>', unsafe_allow_html=True)
            st.markdown('<hr class="soft-divider">', unsafe_allow_html=True)
    else:
        st.markdown('<div class="result-small">입력된 이상 소견 없음</div>', unsafe_allow_html=True)

    st.markdown('<div class="result-label">✅ 추가 권고</div>', unsafe_allow_html=True)
    if result.get("suggestions"):
        for s in result["suggestions"]:
            st.markdown(f'<div class="case-bullet">• {s}</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="result-small">추가 권고 없음</div>', unsafe_allow_html=True)

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
    st.markdown('<div class="result-small">현재 입력된 결과를 바탕으로 한 학생 교육용 자동 해석이며, 실제 임상 진단을 대체하지 않습니다.</div>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# 7. 메인 애플리케이션 실행 흐름
# ==========================================
init_app_state()
current_screen = st.session_state["current_screen"]

if current_screen == "home":
    render_home_screen()

else:
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

    render_navigation_controls(position="bottom")    
