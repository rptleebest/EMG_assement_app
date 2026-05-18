# Part 1

import streamlit as st
from collections import defaultdict
from datetime import datetime

# ==========================================
# 페이지 설정
# ==========================================
st.set_page_config(
    page_title="교육용 근전도 판독 보조",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# 상수
# ==========================================
MODE_CASE = "사례 학습"
MODE_DIRECT = "검사 정보 직접 입력 후 자동 질환 추정 실행"

CHECK_OPTIONS = [
    "미선택",
    "정상 (Normal)",
    "감소 (Reduced)",
    "진폭 감소 (Reduced Amplitude)",
    "잠복기 지연 (Delayed Latency)",
    "무반응 (No Response)",
    "비정상 자발전위 출현 (Abnormal Spontaneous Activity)",
    "지연 (Delayed)",
    "소실 또는 지연 (Absent/Delayed)",
    "지연 또는 소실 (Delayed/Absent)",
    "양측 지연 또는 소실 (Bilateral Delayed/Absent)"
]

INPUT_MODES = [
    "체크형 입력 (Checklist Mode)",
    "수치형 입력 (Numeric Mode)"
]

SEX_OPTIONS = ["미선택", "남", "여"]
SIDE_OPTIONS = ["미선택", "좌", "우", "양측"]

# ==========================================
# 스타일
# ==========================================
st.markdown("""
<style>
.block-container {
    padding-top: 3rem;
    padding-bottom: 2rem;
    max-width: 1200px;
}
.main-title {
    font-size: 2.2rem;
    font-weight: 800;
    margin-top: 0.8rem;
    margin-bottom: 0.4rem;
    line-height: 1.35;
}
.subtle {
    color: #666;
    font-size: 0.98rem;
    margin-bottom: 1rem;
}
.section-card {
    background: #f8fafc;
    border: 1px solid #e5e7eb;
    border-radius: 14px;
    padding: 14px;
    margin-bottom: 12px;
}
.result-card {
    background: #f0fdf4;
    border: 1px solid #bbf7d0;
    border-radius: 14px;
    padding: 16px;
    margin-bottom: 12px;
}
.warn-card {
    background: #fff7ed;
    border: 1px solid #fed7aa;
    border-radius: 14px;
    padding: 14px;
    margin-bottom: 12px;
}
.input-row {
    background: #ffffff;
    border: 1px solid #dbe4ea;
    border-radius: 12px;
    padding: 12px;
    margin-bottom: 10px;
}
.input-title {
    font-weight: 700;
    font-size: 1rem;
    margin-bottom: 4px;
}
.input-meta {
    font-size: 0.86rem;
    color: #556;
    margin-bottom: 8px;
}
.section-help {
    font-size: 0.92rem;
    color: #444;
    margin-bottom: 10px;
}
div[data-testid="stTabs"] button {
    font-size: 0.95rem;
}
hr {
    margin-top: 0.7rem;
    margin-bottom: 0.7rem;
}
.big-section-title {
    font-size: 1.05rem;
    font-weight: 800;
    color: #111827;
    background: #eef6ff;
    border: 1px solid #cfe0ff;
    border-radius: 12px;
    padding: 10px 12px;
    margin-top: 8px;
    margin-bottom: 8px;
}
.section-hint {
    font-size: 0.92rem;
    color: #374151;
    background: #f8fafc;
    border-left: 4px solid #22c55e;
    padding: 10px 12px;
    border-radius: 10px;
    margin-bottom: 10px;
}
.case-symptom-box {
    background: #fffdf5;
    border: 1px solid #f5d78e;
    border-radius: 12px;
    padding: 12px 14px;
    margin-bottom: 12px;
}
.case-teaching-box {
    background: #f6fbff;
    border: 1px solid #cfe2f3;
    border-radius: 12px;
    padding: 12px 14px;
    margin-bottom: 12px;
}
.mode-box-green {
    border: 2px solid #d9ead3;
    border-radius: 12px;
    padding: 14px 16px;
    background-color: #f6fff2;
    margin-top: 10px;
    margin-bottom: 14px;
}
.mode-box-blue {
    border: 2px solid #cfe2f3;
    border-radius: 12px;
    padding: 14px 16px;
    background-color: #f8fbff;
    margin-top: 10px;
    margin-bottom: 14px;
}
.mode-box-gray {
    border: 3px solid #b7b7b7;
    border-radius: 14px;
    padding: 18px;
    background: linear-gradient(180deg, #f8f8f8 0%, #f1f1f1 100%);
    margin-top: 10px;
    margin-bottom: 16px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.03);
}
.mode-title {
    font-size: 1.22rem;
    font-weight: 800;
    margin-bottom: 4px;
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
    font-size: 1.25rem;
}
.mode-desc {
    font-size: 0.96rem;
    color: #444;
    line-height: 1.5;
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# 항목 정의
# ==========================================
SECTIONS = {
    "팔 감각신경전도검사 (Arm Sensory NCS)": [
        "정중신경 감각신경활동전위 (Median SNAP)",
        "자신경 감각신경활동전위 (Ulnar SNAP)",
        "노신경 감각신경활동전위 (Radial SNAP)",
        "노신경 표재감각신경활동전위 (Superficial Radial SNAP)",
        "가쪽아래팔피부신경 감각신경활동전위 (Lateral Antebrachial Cutaneous SNAP)"
    ],
    "팔 운동신경전도검사 (Arm Motor NCS)": [
        "정중신경 복합근육활동전위 (Median CMAP)",
        "자신경 복합근육활동전위 (Ulnar CMAP)",
        "노신경 복합근육활동전위 (Radial CMAP)",
        "겨드랑신경 복합근육활동전위 (Axillary CMAP)",
        "근피신경 복합근육활동전위 (Musculocutaneous CMAP)"
    ],
    "팔 침근전도검사 근육 (Arm Needle EMG Muscles)": [
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
    "다리 감각신경전도검사 (Leg Sensory NCS)": [
        "장딴지신경 감각신경활동전위 (Sural SNAP)",
        "얕은종아리신경 감각신경활동전위 (Superficial Peroneal SNAP)",
        "두렁신경 감각신경활동전위 (Saphenous SNAP)",
        "첫째 발가락사이 감각 (First Dorsal Web Space Sensation)"
    ],
    "다리 운동신경전도검사 (Leg Motor NCS)": [
        "종아리신경 복합근육활동전위 (Peroneal CMAP)",
        "깊은종아리신경 복합근육활동전위 (Deep Peroneal CMAP)",
        "정강신경 복합근육활동전위 (Tibial CMAP)",
        "넙다리신경 복합근육활동전위 (Femoral CMAP)"
    ],
    "다리 침근전도검사 근육 (Leg Needle EMG Muscles)": [
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
        "뒤넙다리근 (Biceps Femoris)",
        "허리 척추주위근 (Lumbar Paraspinal)"
    ],
    "눈깜빡반사검사 (Blink Reflex)": [
        "우측 자극 R1",
        "우측 자극 R2",
        "좌측 자극 R1",
        "좌측 자극 R2"
    ]
}

ANATOMY = {
    "정중신경 감각신경활동전위 (Median SNAP)": {"nerve": "정중신경 (Median nerve)", "level": "손목/아래팔, C6-T1", "domain": "sensory", "region": "arm"},
    "자신경 감각신경활동전위 (Ulnar SNAP)": {"nerve": "자신경 (Ulnar nerve)", "level": "손목/팔꿉, C8-T1", "domain": "sensory", "region": "arm"},
    "노신경 감각신경활동전위 (Radial SNAP)": {"nerve": "노신경 (Radial nerve)", "level": "아래팔, C5-C8", "domain": "sensory", "region": "arm"},
    "노신경 표재감각신경활동전위 (Superficial Radial SNAP)": {"nerve": "노신경 표재감각분지 (Superficial radial sensory branch)", "level": "아래팔/손등, C6-C8", "domain": "sensory", "region": "arm"},
    "가쪽아래팔피부신경 감각신경활동전위 (Lateral Antebrachial Cutaneous SNAP)": {"nerve": "가쪽아래팔피부신경 (Lateral antebrachial cutaneous nerve)", "level": "팔신경얼기/근피신경, C5-C6", "domain": "sensory", "region": "arm"},

    "정중신경 복합근육활동전위 (Median CMAP)": {"nerve": "정중신경 (Median nerve)", "level": "손목/아래팔, C8-T1", "domain": "motor", "region": "arm"},
    "자신경 복합근육활동전위 (Ulnar CMAP)": {"nerve": "자신경 (Ulnar nerve)", "level": "팔꿉/손목, C8-T1", "domain": "motor", "region": "arm"},
    "노신경 복합근육활동전위 (Radial CMAP)": {"nerve": "노신경 (Radial nerve)", "level": "위팔/아래팔, C6-C8", "domain": "motor", "region": "arm"},
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
    "위팔세갈래근 (Triceps Brachii)": {"nerve": "노신경 (Radial nerve)", "level": "C6-C8", "domain": "muscle", "region": "arm"},
    "목 척추주위근 (Cervical Paraspinal)": {"nerve": "척수뒤가지 (Posterior primary ramus)", "level": "목 신경뿌리 수준 (Cervical root level)", "domain": "muscle", "region": "arm"},

    "장딴지신경 감각신경활동전위 (Sural SNAP)": {"nerve": "장딴지신경 (Sural nerve)", "level": "S1-S2", "domain": "sensory", "region": "leg"},
    "얕은종아리신경 감각신경활동전위 (Superficial Peroneal SNAP)": {"nerve": "얕은종아리신경 (Superficial peroneal nerve)", "level": "L5-S1", "domain": "sensory", "region": "leg"},
    "두렁신경 감각신경활동전위 (Saphenous SNAP)": {"nerve": "두렁신경 (Saphenous nerve)", "level": "L3-L4", "domain": "sensory", "region": "leg"},
    "첫째 발가락사이 감각 (First Dorsal Web Space Sensation)": {"nerve": "깊은종아리신경 감각분지", "level": "L5", "domain": "sensory", "region": "leg"},

    "종아리신경 복합근육활동전위 (Peroneal CMAP)": {"nerve": "종아리신경/온종아리신경 분포 (Peroneal/Common peroneal nerve)", "level": "종아리뼈 머리 부위, L4-S1", "domain": "motor", "region": "leg"},
    "깊은종아리신경 복합근육활동전위 (Deep Peroneal CMAP)": {"nerve": "깊은종아리신경 (Deep peroneal nerve)", "level": "발목/발등, L5-S1", "domain": "motor", "region": "leg"},
    "정강신경 복합근육활동전위 (Tibial CMAP)": {"nerve": "정강신경 (Tibial nerve)", "level": "오금/발목, L4-S3", "domain": "motor", "region": "leg"},
    "넙다리신경 복합근육활동전위 (Femoral CMAP)": {"nerve": "넙다리신경 (Femoral nerve)", "level": "L2-L4", "domain": "motor", "region": "leg"},

    "앞정강근 (Tibialis Anterior, TA)": {"nerve": "깊은종아리신경 (Deep peroneal nerve)", "level": "L4-L5", "domain": "muscle", "region": "leg"},
    "짧은발가락폄근 (Extensor Digitorum Brevis, EDB)": {"nerve": "깊은종아리신경 (Deep peroneal nerve)", "level": "L5-S1", "domain": "muscle", "region": "leg"},
    "짧은발가락벌림근 (Abductor Digiti Minimi pedis)": {"nerve": "가쪽발바닥신경 (Lateral plantar nerve)", "level": "S1-S2", "domain": "muscle", "region": "leg"},
    "긴엄지폄근 (Extensor Hallucis Longus, EHL)": {"nerve": "깊은종아리신경 (Deep peroneal nerve)", "level": "L5", "domain": "muscle", "region": "leg"},
    "긴종아리근 (Peroneus Longus)": {"nerve": "얕은종아리신경 (Superficial peroneal nerve)", "level": "L5-S1", "domain": "muscle", "region": "leg"},
    "장딴지근 (Gastrocnemius)": {"nerve": "정강신경 (Tibial nerve)", "level": "S1-S2", "domain": "muscle", "region": "leg"},
    "가자미근 (Soleus)": {"nerve": "정강신경 (Tibial nerve)", "level": "S1-S2", "domain": "muscle", "region": "leg"},
    "가쪽넓은근 (Vastus Lateralis)": {"nerve": "넙다리신경 (Femoral nerve)", "level": "L2-L4", "domain": "muscle", "region": "leg"},
    "엉덩허리근 (Iliopsoas)": {"nerve": "넙다리신경/허리신경얼기 분포", "level": "L2-L4", "domain": "muscle", "region": "leg"},
    "큰볼기근 (Gluteus Maximus)": {"nerve": "아래볼기신경 (Inferior gluteal nerve)", "level": "L5-S2", "domain": "muscle", "region": "leg"},
    "중간볼기근 (Gluteus Medius)": {"nerve": "위볼기신경 (Superior gluteal nerve)", "level": "L4-S1", "domain": "muscle", "region": "leg"},
    "뒤넙다리근 (Biceps Femoris)": {"nerve": "궁둥신경 분포 (Sciatic division)", "level": "L5-S2", "domain": "muscle", "region": "leg"},
    "허리 척추주위근 (Lumbar Paraspinal)": {"nerve": "척수뒤가지 (Posterior primary ramus)", "level": "허리 신경뿌리 수준 (Lumbar root level)", "domain": "muscle", "region": "leg"},

    "우측 자극 R1": {"nerve": "삼차신경-뇌줄기-얼굴신경 반사경로", "level": "Blink reflex", "domain": "reflex", "region": "face"},
    "우측 자극 R2": {"nerve": "삼차신경-뇌줄기-얼굴신경 반사경로", "level": "Blink reflex", "domain": "reflex", "region": "face"},
    "좌측 자극 R1": {"nerve": "삼차신경-뇌줄기-얼굴신경 반사경로", "level": "Blink reflex", "domain": "reflex", "region": "face"},
    "좌측 자극 R2": {"nerve": "삼차신경-뇌줄기-얼굴신경 반사경로", "level": "Blink reflex", "domain": "reflex", "region": "face"},
}

# Part 2


# ==========================================
# 사례 라이브러리
# ==========================================
CASE_LIBRARY = {
    "사례 선택 안 함": {},

    "1. C5 신경뿌리병증 (Cervical Radiculopathy): 뒷목-어깨-위팔 방사통 중심형": {
        "patient": {
            "age": 49,
            "sex": "여",
            "side": "좌",
            "symptoms": [
                "뒷목에서 왼쪽 어깨 바깥쪽과 위팔 가쪽으로 뻗치는 통증이 있음",
                "목을 뒤로 젖히거나 왼쪽으로 돌리면 통증이 심해짐",
                "뚜렷한 근력저하는 없음"
            ],
            "physical_exam": {
                "근력검사": [
                    "어깨 벌림(삼각근) 힘은 대체로 보존됨"
                ],
                "감각검사": [
                    "왼쪽 어깨 가쪽과 위팔 가쪽에 통증 과민 또는 둔한 느낌이 있을 수 있음"
                ],
                "반사검사": [
                    "위팔두갈래근 반사(biceps reflex)는 정상 또는 경미 저하 가능"
                ]
            }
        },
        "findings": {
            "목 척추주위근 (Cervical Paraspinal)": ("정상 (Normal)", "정상 (Normal)"),
            "삼각근 (Deltoid)": ("정상 (Normal)", "정상 (Normal)"),
            "가시아래근 (Infraspinatus)": ("정상 (Normal)", "정상 (Normal)"),
            "위팔두갈래근 (Biceps Brachii)": ("정상 (Normal)", "정상 (Normal)"),
            "정중신경 감각신경활동전위 (Median SNAP)": ("정상 (Normal)", "정상 (Normal)"),
            "자신경 감각신경활동전위 (Ulnar SNAP)": ("정상 (Normal)", "정상 (Normal)")
        },
        "teaching": [
            "C5 신경뿌리병증에서는 목에서 어깨 바깥쪽과 위팔 가쪽으로 퍼지는 통증이 흔합니다.",
            "초기 또는 경미한 신경뿌리병증(radiculopathy)에서는 침근전도와 신경전도검사가 모두 정상일 수 있습니다.",
            "감각신경전도는 대개 정상으로 남아 말초신경병증(peripheral neuropathy)이나 신경얼기병증(plexopathy)과 구분하는 데 도움이 됩니다.",
            "이 경우에는 증상 분포, 자세에 따른 통증 변화, MRI 같은 영상검사가 중요합니다."
        ]
    },

"2. C6 신경뿌리병증 (Cervical Radiculopathy): 뒷목-어깨-팔 통증 및 근력저하형": {
    "patient": {
        "age": 57,
        "sex": "남",
        "side": "우",
        "symptoms": [
            "뒷목에서 오른쪽 어깨와 팔 바깥쪽, 아래팔의 노쪽(radial side), 엄지 쪽으로 뻗치는 통증과 저림이 있음",
            "오른쪽 팔꿈치를 굽히거나 손목을 뒤로 젖히는 힘이 약해짐",
            "팔 전체가 무겁게 느껴지고 물건 들기가 불편함"
        ],
        "physical_exam": {
            "근력검사": [
                "팔꿈치 굽힘(위팔두갈래근) 약화",
                "손목 폄(긴노쪽손목폄근/짧은노쪽손목폄근) 약화",
                "어깨 벌림은 경미 약화되거나 비교적 보존될 수 있음"
            ],
            "감각검사": [
                "아래팔 노쪽과 엄지 쪽 감각저하 또는 저림"
            ],
            "반사검사": [
                "위팔두갈래근 반사(biceps reflex) 감소 가능",
                "위팔노근 반사(brachioradialis reflex) 감소"
            ]
        }
    },
    "findings": {
        "목 척추주위근 (Cervical Paraspinal)": ("정상 (Normal)", "비정상 자발전위 출현 (Abnormal Spontaneous Activity)"),
        "위팔두갈래근 (Biceps Brachii)": ("정상 (Normal)", "비정상 자발전위 출현 (Abnormal Spontaneous Activity)"),
        "위팔노근 (Brachioradialis)": ("정상 (Normal)", "비정상 자발전위 출현 (Abnormal Spontaneous Activity)"),
        "긴노쪽손목폄근/짧은노쪽손목폄근 (Extensor Carpi Radialis Longus/Brevis)": ("정상 (Normal)", "비정상 자발전위 출현 (Abnormal Spontaneous Activity)"),
        "원엎침근 (Pronator Teres)": ("정상 (Normal)", "비정상 자발전위 출현 (Abnormal Spontaneous Activity)"),
        "정중신경 감각신경활동전위 (Median SNAP)": ("정상 (Normal)", "정상 (Normal)"),
        "자신경 감각신경활동전위 (Ulnar SNAP)": ("정상 (Normal)", "정상 (Normal)"),
        "노신경 표재감각신경활동전위 (Superficial Radial SNAP)": ("정상 (Normal)", "정상 (Normal)")
    },
    "teaching": [
        "C6 신경뿌리병증(radiculopathy)에서는 어깨 바깥쪽, 아래팔 노쪽, 엄지 쪽으로 이어지는 통증과 저림이 나타날 수 있습니다.",
        "팔꿈치 굽힘과 손목 폄 약화가 함께 있으면 C6 분절 침범을 더 의심할 수 있습니다.",
        "척추 주변근육과 C6 관련 근육에서 침근전도 이상이 함께 보이면 신경뿌리병증을 강하게 시사합니다.",
        "감각신경전도는 보존되는 경우가 많아 말초신경병증(peripheral neuropathy)이나 신경얼기병증(plexopathy)과 구분하는 데 도움이 됩니다.",
        "노신경병증과 달리 척추주위근 이상이 동반되고 감각신경전도가 보존되면 신경뿌리병증 해석에 도움이 됩니다."
    ]
},

    "3. 손목굴증후군(Carpal Tunnel Syndrome): 정중신경 포착병증(Median Nerve Entrapment Neuropathy) ": {
        "patient": {
            "age": 46,
            "sex": "여",
            "side": "우",
            "symptoms": [
                "오른손 엄지, 검지, 중지의 저림과 손바닥 통증이 있음",
                "밤에 증상이 심해지고 손을 털면 조금 좋아짐",
                "엄지 쪽 집기 힘이 약해지는 느낌이 있음"
            ],
            "physical_exam": {
                "근력검사": [
                    "엄지 벌림(짧은엄지벌림근, APB) 약화 가능"
                ],
                "감각검사": [
                    "엄지, 검지, 중지 및 넷째 손가락 노쪽 절반 감각저하"
                ],
                "반사검사": [
                    "심부건반사는 대개 정상"
                ],
                "유발검사": [
                    "Phalen 검사 양성 가능",
                    "Tinel 징후 양성 가능"
                ]
            }
        },
        "findings": {
            "정중신경 감각신경활동전위 (Median SNAP)": ("정상 (Normal)", "잠복기 지연 (Delayed Latency)"),
            "정중신경 복합근육활동전위 (Median CMAP)": ("정상 (Normal)", "잠복기 지연 (Delayed Latency)"),
            "짧은엄지벌림근 (Abductor Pollicis Brevis, APB)": ("정상 (Normal)", "비정상 자발전위 출현 (Abnormal Spontaneous Activity)")
        },
        "teaching": [
            "엄지, 검지, 중지 저림과 야간 악화는 손목굴증후군의 전형적인 증상입니다.",
            "정중신경 감각 및 운동 잠복기 지연은 손목굴 부위 포착을 시사합니다.",
            "엄지벌림 약화나 짧은엄지벌림근(APB) 침근전도 이상이 있으면 더 진행된 병변을 생각할 수 있습니다.",
            "목에서 내려오는 통증이 주된 경우에는 신경뿌리병증과 감별해야 합니다."
        ]
    },

    "4. 노신경마비: 노신경 손상(Radial Nerve Palsy)으로 인한 손목처짐(wrist drop)": {
        "patient": {
            "age": 34,
            "sex": "남",
            "side": "우",
            "symptoms": [
                "위팔뼈 골절 이후 오른손목이 떨어지는 손목처짐이 생김",
                "손목과 손가락을 뒤로 젖히기 어렵고 손등 저림이 있음"
            ],
            "physical_exam": {
                "근력검사": [
                    "손목 폄 약화",
                    "손가락 폄 약화",
                    "엄지 폄 약화"
                ],
                "감각검사": [
                    "손등 노쪽과 첫째 손등사이(first dorsal web space) 감각저하"
                ],
                "반사검사": [
                    "위팔세갈래근 반사는 병변 위치에 따라 정상 또는 감소 가능"
                ]
            }
        },
        "findings": {
            "노신경 감각신경활동전위 (Radial SNAP)": ("정상 (Normal)", "감소 (Reduced)"),
            "노신경 복합근육활동전위 (Radial CMAP)": ("정상 (Normal)", "감소 (Reduced)"),
            "손목폄근 (Extensor Carpi Radialis / Extensor Digitorum)": ("정상 (Normal)", "비정상 자발전위 출현 (Abnormal Spontaneous Activity)")
        },
        "teaching": [
            "외상 후 손목처짐은 노신경마비를 먼저 생각해야 합니다.",
            "손목과 손가락 폄 약화, 손등 감각저하가 함께 있으면 말초 노신경 병변에 잘 맞습니다.",
            "노신경 감각신경전도 이상은 경추 신경뿌리병증보다 말초신경병증을 더 시사합니다.",
            "병변 위치에 따라 위팔세갈래근 보존 여부가 달라질 수 있습니다."
        ]
    },

    "5. 자신경병증: 팔꿈치 부위 자신경 포착 (Ulnar Neuropathy at Elbow)": {
        "patient": {
            "age": 42,
            "sex": "남",
            "side": "좌",
            "symptoms": [
                "왼손 넷째, 다섯째 손가락 저림이 있음",
                "팔꿈치를 오래 굽히면 증상이 심해짐",
                "손의 세밀한 동작이 불편함"
            ],
            "physical_exam": {
                "근력검사": [
                    "손가락 벌림/모음 약화",
                    "엄지-검지 집기 힘 약화(Froment 징후 가능)"
                ],
                "감각검사": [
                    "넷째와 다섯째 손가락, 손의 자쪽 감각저하"
                ],
                "반사검사": [
                    "깊은힘줄반사(DTR)는 대개 정상"
                ],
                "유발검사": [
                    "팔꿈치 굴곡 유지 시 증상 악화 가능",
                    "팔꿈치 안쪽 티넬(Tinel) 징후 양성 가능"
                ]
            }
        },
        "findings": {
            "자신경 감각신경활동전위 (Ulnar SNAP)": ("정상 (Normal)", "감소 (Reduced)"),
            "자신경 복합근육활동전위 (Ulnar CMAP)": ("정상 (Normal)", "감소 (Reduced)"),
            "첫째등쪽뼈사이근 (First Dorsal Interosseous, FDI)": ("정상 (Normal)", "비정상 자발전위 출현 (Abnormal Spontaneous Activity)"),
            "새끼벌림근 (Abductor Digiti Minimi, ADM)": ("정상 (Normal)", "비정상 자발전위 출현 (Abnormal Spontaneous Activity)")
        },
        "teaching": [
            "넷째, 다섯째 손가락 저림과 팔꿈치 굽힘 시 악화는 자신경 포착의 전형적인 증상입니다.",
            "하나의 말초신경 분포에 국한된 감각저하와 손 자체기원근육(intrinsic) 약화가 핵심입니다.",
            "자신경 감각신경활동전위(Ulnar SNAP) 이상은 신경뿌리병증보다 말초 자신경병증에 더 잘 맞습니다."
        ]
    },

    "6. 위팔 신경얼기병증: 위팔 신경얼기 병변 (Brachial Plexopathy)": {
        "patient": {
            "age": 36,
            "sex": "남",
            "side": "좌",
            "symptoms": [
                "갑작스러운 왼쪽 어깨 통증 후 팔의 힘이 약해짐",
                "한 개의 신경만이 아니라 여러 근육에서 약화가 의심됨",
                "팔 바깥쪽 감각도 둔해진 느낌이 있음"
            ],
            "physical_exam": {
                "근력검사": [
                    "어깨 벌림 약화",
                    "팔꿈치 굽힘 약화",
                    "한 개 말초신경으로 설명되지 않는 여러 근육 약화"
                ],
                "감각검사": [
                    "팔 바깥쪽 또는 아래팔 가쪽 감각저하"
                ],
                "반사검사": [
                    "위팔두갈래근 반사 감소 가능"
                ]
            }
        },
        "findings": {
            "목 척추주위근 (Cervical Paraspinal)": ("정상 (Normal)", "정상 (Normal)"),
            "가쪽아래팔피부신경 감각신경활동전위 (Lateral Antebrachial Cutaneous SNAP)": ("정상 (Normal)", "감소 (Reduced)"),
            "겨드랑신경 복합근육활동전위 (Axillary CMAP)": ("정상 (Normal)", "감소 (Reduced)"),
            "근피신경 복합근육활동전위 (Musculocutaneous CMAP)": ("정상 (Normal)", "감소 (Reduced)"),
            "삼각근 (Deltoid)": ("정상 (Normal)", ""비정상 자발전위 출현(Abnormal Spontaneous Activity)"),
            "위팔두갈래근 (Biceps Brachii)": ("정상 (Normal)", ""비정상 자발전위 출현(Abnormal Spontaneous Activity)")
        },
        "teaching": [
            "여러 말초신경 분포가 함께 침범되면 신경얼기병증을 생각합니다.",
            "감각신경전도 이상이 동반되면 신경뿌리병증보다 신경얼기병증에 더 잘 맞습니다.",
            "척추 주변근육이 정상이면 신경뿌리병증보다 신경얼기병증 가능성이 높아집니다."
        ]
    },

    "7. S1 신경뿌리병증 (Lumbar Radiculopathy): 허리-엉치-종아리 뒤쪽 방사통 중심형: ": {
        "patient": {
            "age": 52,
            "sex": "남",
            "side": "좌",
            "symptoms": [
                "허리에서 왼쪽 엉치와 종아리 뒤쪽, 발 바깥쪽으로 뻗치는 통증이 있음",
                "오래 앉아 있거나 허리를 굽히면 통증이 심해짐",
                "발목을 아래로 미는 힘 저하는 뚜렷하지 않음"
            ],
            "physical_exam": {
                "근력검사": [
                    "발바닥쪽 굽힘(장딴지근) 힘은 대체로 보존됨"
                ],
                "감각검사": [
                    "종아리 뒤쪽과 발 바깥쪽 감각저하 또는 저림 가능"
                ],
                "반사검사": [
                    "아킬레스건 반사(Achilles reflex)는 정상 또는 경미 저하 가능"
                ]
            }
        },
        "findings": {
            "허리 척추주위근 (Lumbar Paraspinal)": ("정상 (Normal)", "정상 (Normal)"),
            "장딴지근 (Gastrocnemius)": ("정상 (Normal)", "정상 (Normal)"),
            "짧은발가락벌림근 (Abductor Digiti Minimi pedis)": ("정상 (Normal)", "정상 (Normal)"),
            "장딴지신경 감각신경활동전위 (Sural SNAP)": ("정상 (Normal)", "정상 (Normal)")
        },
        "teaching": [
            "S1 신경뿌리병증에서는 엉치, 종아리 뒤쪽, 발 바깥쪽으로 이어지는 방사통이 흔합니다.",
            "초기 또는 경미한 경우에는 침근전도와 신경전도검사가 정상일 수 있습니다.",
            "장딴지신경 감각신경활동전위(Sural SNAP)이 정상인 점은 말초 감각신경병증보다 신경뿌리병증 쪽에 더 맞습니다.",
            "증상이 전형적인데 검사 결과가 정상이라면 임상 증상과 MRI를 함께 봐야 합니다."
        ]
    },

    "8. L5 신경뿌리병증 (Lumbar Radiculopathy): 발처짐 및 발목·엄지발가락 들기 약화형": {
        "patient": {
            "age": 61,
            "sex": "여",
            "side": "우",
            "symptoms": [
                "허리에서 오른쪽 엉치와 다리 바깥쪽, 발등 쪽으로 뻗치는 통증이 있음",
                "오른쪽 발목과 엄지발가락을 들어 올리기 어려워 발처짐 양상이 의심됨",
                "오래 앉아 있으면 증상이 악화됨"
            ],
            "physical_exam": {
                "근력검사": [
                    "발목 등굽힘(앞정강근) 약화",
                    "엄지발가락 폄(긴엄지폄근) 약화",
                    "엉덩이 벌림(중간볼기근) 약화 가능"
                ],
                "감각검사": [
                    "다리 바깥쪽과 발등 감각저하 가능"
                ],
                "반사검사": [
                    "깊은힘줄반사(deep tendon reflex)는 뚜렷하지 않을 수 있음",
                    "안쪽 무릎굽힘근(hamstring) 반사 감소 가능"
                ]
            }
        },
        "findings": {
            "허리 척추주위근 (Lumbar Paraspinal)": ("정상 (Normal)", "비정상 자발전위 출현 (Abnormal Spontaneous Activity)"),
            "앞정강근 (Tibialis Anterior, TA)": ("정상 (Normal)", "비정상 자발전위 출현 (Abnormal Spontaneous Activity)"),
            "긴엄지폄근 (Extensor Hallucis Longus, EHL)": ("정상 (Normal)", "비정상 자발전위 출현 (Abnormal Spontaneous Activity)"),
            "중간볼기근 (Gluteus Medius)": ("정상 (Normal)", "비정상 자발전위 출현 (Abnormal Spontaneous Activity)"),
            "장딴지신경 감각신경활동전위 (Sural SNAP)": ("정상 (Normal)", "정상 (Normal)"),
            "얕은종아리신경 감각신경활동전위 (Superficial Peroneal SNAP)": ("정상 (Normal)", "정상 (Normal)")
        },
        "teaching": [
            "발등 쪽 방사통과 발목/엄지발가락 들기 약화는 L5 신경뿌리병증을 의심하게 합니다.",
            "척추 주변근육과 L5 관련 근육에서 침근전도 이상이 보이면 신경뿌리병증을 지지합니다.",
            "감각신경전도는 보존되는 경우가 많아 종아리신경병증과 감별하는 데 도움이 됩니다.",
            "발처짐이 있으면 종아리신경병증과 반드시 감별해야 합니다."
        ]
    },

    "9. 종아리신경병증: 종아리뼈머리 부위 온종아리신경 포착 (Peroneal Neuropathy at Fibular Head)": {
        "patient": {
            "age": 29,
            "sex": "남",
            "side": "우",
            "symptoms": [
                "다리를 꼬고 앉는 습관 후 오른쪽 발처짐이 생김",
                "종아리 바깥쪽과 발등 감각 저하가 있음",
                "발등을 들어 올리기 어렵고 걸을 때 발끝이 끌림"
            ],
            "physical_exam": {
                "근력검사": [
                    "발목 등굽힘 약화",
                    "발가락 폄 약화",
                    "발바깥번짐(eversion) 약화",
                    "발안쪽번짐(inversion)은 비교적 보존됨"
                ],
                "감각검사": [
                    "종아리 바깥쪽과 발등 감각저하"
                ],
                "반사검사": [
                    "아킬레스건 반사는 대개 정상"
                ]
            }
        },
        "findings": {
            "얕은종아리신경 감각신경활동전위 (Superficial Peroneal SNAP)": ("정상 (Normal)", "감소 (Reduced)"),
            "종아리신경 복합근육활동전위 (Peroneal CMAP)": ("정상 (Normal)", "무반응 (No Response)"),
            "앞정강근 (Tibialis Anterior, TA)": ("정상 (Normal)", "비정상 자발전위 출현 (Abnormal Spontaneous Activity)"),
            "짧은발가락폄근 (Extensor Digitorum Brevis, EDB)":  ("정상 (Normal)", "비정상 자발전위 출현 (Abnormal Spontaneous Activity)"),
            "허리 척추주위근 (Lumbar Paraspinal)": ("정상 (Normal)", "정상 (Normal)")
        },
        "teaching": [
            "다리를 꼬고 앉은 뒤 생긴 발처짐은 종아리뼈머리 부위 종아리신경 포착을 의미합니다.",
            "발등 감각저하와 얕은종아리신경 SNAP 감소는 L5 신경뿌리병증보다 말초신경병증에 더 잘 맞습니다.",
            "발안쪽번짐이 비교적 보존되고 척추 주변근육이 정상이면 종아리신경병증 가능성이 더 높습니다."
        ]
    },

       "10. 온종아리신경병증 (Common Peroneal Neuropathy): 종아리뼈머리 부위 외상 후 발처짐형": {
        "patient": {
            "age": 31,
            "sex": "남",
            "side": "좌",
            "symptoms": [
                "왼쪽 종아리뼈 또는 정강뼈 주변 외상 이후 왼쪽 발처짐(foot drop)이 생김",
                "걸을 때 발끝이 끌리고 발목을 들어 올리기 어려움",
                "왼쪽 종아리 바깥쪽과 발등 감각이 둔해짐"
            ],
            "physical_exam": {
                "근력검사": [
                    "발목 등굽힘 약화",
                    "발가락 폄 약화",
                    "발바깥번짐(eversion) 약화",
                    "발안쪽번짐(inversion)은 비교적 보존됨"
                ],
                "감각검사": [
                    "종아리 바깥쪽과 발등 감각저하"
                ],
                "반사검사": [
                    "깊은힘줄반사(deep tendon reflex)는 대개 정상"
                ]
            }
        },
        "findings": {
            "얕은종아리신경 감각신경활동전위 (Superficial Peroneal SNAP)": ("정상 (Normal)", "감소 (Reduced)"),
            "종아리신경 복합근육활동전위 (Peroneal CMAP)": ("정상 (Normal)", "감소 (Reduced)"),
            "앞정강근 (Tibialis Anterior, TA)": ("정상 (Normal)", "비정상 자발전위 출현 (Abnormal Spontaneous Activity)"),
            "짧은발가락폄근 (Extensor Digitorum Brevis, EDB)": ("정상 (Normal)", "비정상 자발전위 출현 (Abnormal Spontaneous Activity)"),
            "허리 척추주위근 (Lumbar Paraspinal)": ("정상 (Normal)", "정상 (Normal)")
        },
        "teaching": [
            "온종아리신경병증은 종아리뼈머리 부위 압박이나 외상 이후 발처짐으로 나타나는 대표적 말초신경병증입니다.",
            "발목 등굽힘 약화와 발바깥번짐 약화가 함께 보이면 온종아리신경 병변을 더 의미합니다.",
            "발안쪽번짐이 비교적 보존되고 허리 척추주위근이 정상이면 L5 신경뿌리병증보다 말초신경 병변 가능성이 높습니다.",
            "얕은종아리 감각신경활동전위(SNAP) 감소는 보다 국소적인 종아리신경 병변을 지지하는 중요한 단서입니다."
        ]
    },

    "11. 허리엉치신경얼기병증: 허리엉치신경얼기 병변 (Lumbosacral Plexopathy)": {
        "patient": {
            "age": 58,
            "sex": "여",
            "side": "좌",
            "symptoms": [
                "왼쪽 골반과 허벅지 통증 후 다리 힘이 약해짐",
                "여러 말초신경 분포에 걸친 감각 저하가 의심됨",
                "한 가지 신경만으로 설명하기 어려운 넓은 분포의 증상이 있음"
            ],
            "physical_exam": {
                "근력검사": [
                    "무릎 폄, 발목 등굽힘, 발목 바닥굽힘 등 여러 근육에서 약화 가능"
                ],
                "감각검사": [
                    "허벅지, 종아리, 발 등 여러 부위에 걸친 감각저하"
                ],
                "반사검사": [
                    "무릎반사 또는 아킬레스건 반사 감소 가능"
                ]
            }
        },
        "findings": {
            "허리 척추주위근 (Lumbar Paraspinal)": ("정상 (Normal)", "정상 (Normal)"),
            "장딴지신경 감각신경활동전위 (Sural SNAP)": ("정상 (Normal)", "감소 (Reduced)"),
            "종아리신경 복합근육활동전위 (Peroneal CMAP)": ("정상 (Normal)", "감소 (Reduced)"),
            "정강신경 복합근육활동전위 (Tibial CMAP)": ("정상 (Normal)", "감소 (Reduced)"),
            "앞정강근 (Tibialis Anterior, TA)": ("정상 (Normal)", "비정상 자발전위 출현 (Abnormal Spontaneous Activity)"),
            "장딴지근 (Gastrocnemius)": ("정상 (Normal)", "비정상 자발전위 출현 (Abnormal Spontaneous Activity)")
        },
        "teaching": [
            "여러 말초신경 분포와 감각신경 이상이 함께 나타나면 허리엉치신경얼기병증을 고려합니다.",
            "척추 주변근육이 정상이면 신경뿌리병증보다 신경얼기병증 쪽에 더 무게가 실립니다.",
            "한 개의 신경뿌리병변이나 단일 신경 손상으로 설명되지 않는 점이 핵심입니다."
        ]
    },

    "12. 축삭성 다발신경병증 (Axonal Polyneuropathy)": {
        "patient": {
            "age": 67,
            "sex": "남",
            "side": "양측",
            "symptoms": [
                "양쪽 발끝부터 시작된 저림이 점차 위로 올라옴",
                "양쪽 발목의 힘이 약해지는 느낌이 있음",
                "증상이 양측 대칭적으로 진행함"
            ],
            "physical_exam": {
                "근력검사": [
                    "원위부, 특히 발목과 발가락 움직임의 약화 가능"
                ],
                "감각검사": [
                    "양측 발끝에서 시작하는 길이의존성 감각저하",
                    "진동감각 저하 가능"
                ],
                "반사검사": [
                    "아킬레스건 반사 감소 또는 소실"
                ]
            }
        },
        "findings": {
            "장딴지신경 감각신경활동전위 (Sural SNAP)": ("감소 (Reduced)", "감소 (Reduced)"),
            "얕은종아리신경 감각신경활동전위 (Superficial Peroneal SNAP)": ("감소 (Reduced)", "감소 (Reduced)"),
            "종아리신경 복합근육활동전위 (Peroneal CMAP)": ("감소 (Reduced)", "감소 (Reduced)"),
            "정강신경 복합근육활동전위 (Tibial CMAP)": ("감소 (Reduced)", "감소 (Reduced)")
        },
        "teaching": [
            "여러 신경에서 진폭 감소가 우세하면 축삭성 다발신경병증을 생각합니다.",
            "증상이 발끝부터 시작해 양측 대칭적으로 올라오는 길이의존성 양상(glove-stocking)이 중요합니다.",
            "반사저하, 특히 아킬레스힘줄 반사 저하는 흔한 이학적 단서입니다."
        ]
    },

    "13. 말이집탈락성 다발신경병증 (Demyelinating Polyneuropathy)": {
        "patient": {
            "age": 55,
            "sex": "여",
            "side": "양측",
            "symptoms": [
                "양손과 양발이 모두 저리고 최근 보행이 불안정해짐",
                "증상이 비교적 대칭적으로 진행함",
                "손과 발의 힘이 전반적으로 떨어진 느낌이 있음"
            ],
            "physical_exam": {
                "근력검사": [
                    "상지와 하지의 대칭적 약화 가능"
                ],
                "감각검사": [
                    "양손과 양발의 감각저하",
                    "깊은감각 저하로 인해 보행 불안정 가능"
                ],
                "반사검사": [
                    "전반적 깊은힘줄반사(DTR) 감소 또는 소실"
                ]
            }
        },
        "findings": {
            "정중신경 감각신경활동전위 (Median SNAP)": ("잠복기 지연 (Delayed Latency)", "잠복기 지연 (Delayed Latency)"),
            "자신경 감각신경활동전위 (Ulnar SNAP)": ("잠복기 지연 (Delayed Latency)", "잠복기 지연 (Delayed Latency)"),
            "정중신경 복합근육활동전위 (Median CMAP)": ("잠복기 지연 (Delayed Latency)", "잠복기 지연 (Delayed Latency)"),
            "자신경 복합근육활동전위 (Ulnar CMAP)": ("잠복기 지연 (Delayed Latency)", "잠복기 지연 (Delayed Latency)")
        },
        "teaching": [
            "여러 신경에서 잠복기 지연이 반복되면 말이집탈락성 병변을 의심합니다.",
            "진폭 감소보다 전도 지연이 더 두드러지는 점이 핵심입니다.",
            "대칭적 약화와 반사저하는 다발신경병증의 중요한 이학적 소견입니다."
        ]
    },

    "14. 운동신경세포질환 (Motor Neuron Disease)": {
        "patient": {
            "age": 63,
            "sex": "남",
            "side": "양측",
            "symptoms": [
                "양손과 양다리의 근력 저하가 서서히 진행함",
                "감각 증상은 뚜렷하지 않음",
                "근육다발수축이 관찰될 수 있음"
            ],
            "physical_exam": {
                "근력검사": [
                    "상지와 하지 여러 근육군의 진행성 약화"
                ],
                "감각검사": [
                    "감각은 대체로 정상"
                ],
                "반사검사": [
                    "심부건반사 항진 가능",
                    "병적 반사(Babinski sign) 가능"
                ],
                "기타": [
                    "근육위축 가능",
                    "근육다발수축(fasciculation) 관찰 가능"
                ]
            }
        },
        "findings": {
            "삼각근 (Deltoid)": ("비정상 자발전위 출현 (Abnormal Spontaneous Activity)", "비정상 자발전위 출현 (Abnormal Spontaneous Activity)"),
            "위팔세갈래근 (Triceps Brachii)": ("비정상 자발전위 출현 (Abnormal Spontaneous Activity)", "비정상 자발전위 출현 (Abnormal Spontaneous Activity)"),
            "앞정강근 (Tibialis Anterior, TA)": ("비정상 자발전위 출현 (Abnormal Spontaneous Activity)", "비정상 자발전위 출현 (Abnormal Spontaneous Activity)"),
            "장딴지근 (Gastrocnemius)": ("비정상 자발전위 출현 (Abnormal Spontaneous Activity)", "비정상 자발전위 출현 (Abnormal Spontaneous Activity)"),
            "정중신경 감각신경활동전위 (Median SNAP)": ("정상 (Normal)", "정상 (Normal)"),
            "장딴지신경 감각신경활동전위 (Sural SNAP)": ("정상 (Normal)", "정상 (Normal)")
        },
        "teaching": [
            "감각 증상은 거의 없는데 여러 분절과 여러 사지 근육에서 침근전도 이상이 보이면 운동신경세포질환을 생각할 수 있습니다.",
            "감각신경전도가 비교적 보존된다는 점이 중요한 단서입니다.",
            "위운동신경세포 징후(반사 항진)와 아래운동신경세포 징후(근위축, 근육다발수축)가 함께 보일 수 있습니다."
        ]
    },

    "15. 눈 깜빡 반사 (Blink Reflex): 삼차신경 들방향 병변 의심": {
        "patient": {
            "age": 56,
            "sex": "남",
            "side": "우",
            "symptoms": [
                "오른쪽 이마와 눈 주위의 감각이 둔함",
                "오른쪽 얼굴 통증 또는 저림을 호소함",
                "얼굴마비는 없음"
            ],
            "physical_exam": {
                "감각검사": [
                    "오른쪽 이마와 눈 주위의 얼굴 감각저하"
                ],
                "운동검사": [
                    "안면근력은 대체로 정상"
                ],
                "반사검사": [
                    "각막반사(corneal reflex) 이상 가능"
                ]
            }
        },
        "findings": {
            "우측 자극 R1": ("지연 또는 소실 (Delayed/Absent)", ""),
            "우측 자극 R2": ("양측 지연 또는 소실 (Bilateral Delayed/Absent)", ""),
            "좌측 자극 R1": ("정상 (Normal)", ""),
            "좌측 자극 R2": ("정상 (Normal)", "")
        },
        "teaching": [
            "오른쪽 자극에서만 R1과 R2가 비정상이면 오른쪽 삼차신경 들방향 병변을 의심할 수 있습니다.",
            "얼굴 감각저하가 함께 있으면 삼차신경 병변 해석이 더 쉬워집니다."
        ]
    },

    "16. 눈 깜빡 반사 (Blink Reflex): 뇌줄기 핵/중간연결 병변 의심": {
        "patient": {
            "age": 62,
            "sex": "여",
            "side": "우",
            "symptoms": [
                "얼굴 감각은 비교적 보존되어 있으나 복시와 어지럼이 동반됨",
                "신경학적 검사에서 뇌줄기 병변이 의심됨"
            ],
            "physical_exam": {
                "감각검사": [
                    "얼굴 감각은 비교적 보존됨"
                ],
                "운동검사": [
                    "눈운동 이상 가능",
                    "안면근력은 정상일 수도 있고 동반 이상이 있을 수도 있음"
                ],
                "기타": [
                    "복시",
                    "어지럼",
                    "뇌줄기 기능 이상을 시사하는 다른 신경학적 징후 가능"
                ]
            }
        },
        "findings": {
            "우측 자극 R1": ("지연 (Delayed)", ""),
            "우측 자극 R2": ("지연 (Delayed)", ""),
            "좌측 자극 R1": ("지연 (Delayed)", ""),
            "좌측 자극 R2": ("지연 (Delayed)", "")
        },
        "teaching": [
            "양측 자극에서 반사 경로 이상이 반복되면 말초 단독 병변보다 뇌줄기 병변을 생각해야 합니다.",
            "복시, 어지럼 같은 뇌줄기 증상이 함께 있으면 해석이 더 쉬워집니다."
        ]
    }
}

# ==========================================
# 보조 함수
# ==========================================
def is_abnormal(value):
    if value is None:
        return False
    value = str(value).strip()
    if value == "" or value == "미선택":
        return False
    return value != "정상 (Normal)"

def summarize_status(left, right):
    if str(right).strip() == "":
        return f"결과: {left}"
    return f"정상쪽: {left} / 병변쪽: {right}"

def severity_text(total_abnormal, no_response_count):
    if no_response_count >= 2 or total_abnormal >= 6:
        return "중등도 이상"
    if total_abnormal >= 3:
        return "경도-중등도"
    if total_abnormal >= 1:
        return "경도"
    return "뚜렷한 이상 없음"

def infer_numeric_status(domain, normal_amp, lesion_amp, normal_latency, lesion_latency, spontaneous=False):
    if domain in ["sensory", "motor"]:
        if lesion_amp == 0:
            return "무반응 (No Response)"
        if normal_latency > 0 and lesion_latency >= normal_latency * 1.2:
            return "잠복기 지연 (Delayed Latency)"
        if normal_amp > 0 and lesion_amp <= normal_amp * 0.6:
            return "감소 (Reduced)"
        return "정상 (Normal)"
    if spontaneous:
        return "비정상 자발전위 출현 (Abnormal Spontaneous Activity)"
    return "정상 (Normal)"

def get_case_names_for_selection():
    return [name for name in CASE_LIBRARY.keys() if name != "사례 선택 안 함"]

def find_section_for_item(item_name):
    for section, items in SECTIONS.items():
        if item_name in items:
            return section
    return None

def get_current_case_data(case_name):
    return CASE_LIBRARY.get(case_name, {}) if case_name else {}

def safe_index(options, value, default=0):
    return options.index(value) if value in options else default

def make_report_text(result):
    lines = []
    lines.append("교육용 근전도 판독 보조 결과")
    lines.append("=" * 50)
    lines.append(f"생성 시각: {result.get('created_at', '')}")
    lines.append(f"최종 유력 진단: {result.get('final_dx', '')}")
    lines.append(f"손상 의심 신경: {result.get('involved_nerves', '')}")
    lines.append(f"신경학적 레벨/분절: {result.get('involved_levels', '')}")
    lines.append(f"중증도: {result.get('severity', '')}")
    lines.append("")

    lines.append("[Top 3 감별진단]")
    for i, (dx, score) in enumerate(result.get("top3", []), 1):
        lines.append(f"{i}. {dx} (점수: {score})")
    lines.append("")

    lines.append("[병변 태그]")
    for tag in result.get("lesion_tags", []):
        lines.append(f"- {tag}")
    lines.append("")

    lines.append("[판단 근거]")
    for reason in result.get("reasons", []):
        lines.append(f"- {reason}")
    lines.append("")

    lines.append("[추가 검사 권고]")
    for suggestion in result.get("suggestions", []):
        lines.append(f"- {suggestion}")
    lines.append("")

    lines.append("[이상 항목 요약]")
    for item in result.get("abnormal_items", []):
        lines.append(
            f"- {item['항목']} | 신경: {item['신경']} | 레벨: {item['레벨']} | {item['결과']}"
        )
    lines.append("")
    lines.append("※ 본 결과는 학생 교육용 참고 자료이며 실제 임상 진단을 대체하지 않습니다.")

    return "\n".join(lines)

# ==========================================
# 상태 관리
# ==========================================
def init_app_state():
    defaults = {
        "app_mode": MODE_CASE,
        "confirmed_case": None,
        "selected_case": get_case_names_for_selection()[0] if get_case_names_for_selection() else None,
        "age": 50,
        "sex": "미선택",
        "side": "미선택",
        "detail_input_mode": INPUT_MODES[0],
        "last_result": None,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

def reset_all_inputs():
    for section, items in SECTIONS.items():
        for item in items:
            st.session_state[f"check_{section}_{item}"] = False
            st.session_state[f"left_{section}_{item}"] = "정상 (Normal)"
            st.session_state[f"right_{section}_{item}"] = "정상 (Normal)"
            st.session_state[f"num_check_{section}_{item}"] = False
            st.session_state[f"na_{section}_{item}"] = 10.0
            st.session_state[f"nl_{section}_{item}"] = 3.0
            st.session_state[f"la_{section}_{item}"] = 10.0
            st.session_state[f"ll_{section}_{item}"] = 3.0
            st.session_state[f"mns_{section}_{item}"] = False
            st.session_state[f"mls_{section}_{item}"] = False
            st.session_state[f"nr_{section}_{item}"] = "정상 (Normal)"

def clear_result():
    st.session_state["last_result"] = None

def init_case_to_session(case_name):
    reset_all_inputs()
    clear_result()

    case_data = CASE_LIBRARY.get(case_name, {})
    patient = case_data.get("patient", {})
    findings = case_data.get("findings", {})

    st.session_state["age"] = patient.get("age", 50)
    st.session_state["sex"] = patient.get("sex", "미선택")
    st.session_state["side"] = patient.get("side", "미선택")

    unmapped_items = []

    for item, vals in findings.items():
        section = find_section_for_item(item)
        if not section:
            unmapped_items.append(item)
            continue

        st.session_state[f"check_{section}_{item}"] = True
        st.session_state[f"left_{section}_{item}"] = vals[0] if len(vals) > 0 and vals[0] != "" else "정상 (Normal)"
        st.session_state[f"right_{section}_{item}"] = vals[1] if len(vals) > 1 and vals[1] != "" else "정상 (Normal)"

    st.session_state["last_unmapped_case_items"] = unmapped_items

def switch_to_case_mode(reset_case_selection=False):
    st.session_state["app_mode"] = MODE_CASE
    st.session_state["confirmed_case"] = None
    clear_result()

    if reset_case_selection:
        options = get_case_names_for_selection()
        st.session_state["selected_case"] = options[0] if options else None

def switch_to_direct_mode():
    st.session_state["app_mode"] = MODE_DIRECT
    st.session_state["confirmed_case"] = None
    clear_result()

# Part 3

# ==========================================
# 규칙 엔진
# ==========================================
def analyze_case(age, sex, side, selected_rows):
    scores = defaultdict(int)
    reasons = []
    suggestions = set()
    lesion_tags = set()
    involved_nerves = set()
    involved_levels = set()

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

    blink_r1_abnormal = 0
    blink_r2_abnormal = 0
    blink_right_stim_abnormal = 0
    blink_left_stim_abnormal = 0

    abnormal_items = []

    for row in selected_rows:
        left = row["left"]
        right = row["right"]

        if not (is_abnormal(left) or is_abnormal(right)):
            continue

        item = row["item"]
        if item not in ANATOMY:
            continue

        a = ANATOMY[item]

        involved_nerves.add(a["nerve"])
        involved_levels.add(a["level"])

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

        vals = [str(left), str(right)]
        if any("감소" in v for v in vals):
            reduced_count += 1
        if any("지연" in v for v in vals):
            delayed_count += 1
        if any("무반응" in v for v in vals):
            no_response_count += 1
        if any("비정상 자발전위" in v for v in vals):
            spontaneous_count += 1

        if "정중신경" in item or "짧은엄지벌림근" in item:
            median_related += 1
        if "자신경" in item or "첫째등쪽뼈사이근" in item or "새끼벌림근" in item:
            ulnar_related += 1
        if "노신경" in item or "뒤뼈사이신경" in item or "집게폄근" in item or "손목폄근" in item or "위팔세갈래근" in item:
            radial_related += 1
        if "종아리신경" in item or "앞정강근" in item or "짧은발가락폄근" in item or "긴종아리근" in item or "깊은종아리신경" in item:
            peroneal_related += 1
        if "정강신경" in item or "장딴지근" in item or "가자미근" in item:
            tibial_related += 1
        if "넙다리신경" in item or "가쪽넓은근" in item or "엉덩허리근" in item:
            femoral_related += 1
        if "가쪽아래팔피부신경" in item or "겨드랑신경" in item or "근피신경" in item:
            arm_plexus_hint += 1
        if "중간볼기근" in item or "큰볼기근" in item or "뒤넙다리근" in item:
            leg_plexus_hint += 1
        if "목 척추주위근" in item:
            neck_root_hint += 1
        if "허리 척추주위근" in item:
            low_back_root_hint += 1

        if item in ["우측 자극 R1", "좌측 자극 R1"]:
            blink_r1_abnormal += 1
        if item in ["우측 자극 R2", "좌측 자극 R2"]:
            blink_r2_abnormal += 1
        if item.startswith("우측 자극"):
            blink_right_stim_abnormal += 1
        if item.startswith("좌측 자극"):
            blink_left_stim_abnormal += 1

        abnormal_items.append({
            "항목": item,
            "신경": a["nerve"],
            "레벨": a["level"],
            "결과": summarize_status(left, right)
        })

    total_abnormal = sensory_abnormal + motor_abnormal + muscle_abnormal + reflex_abnormal

    # 목 신경뿌리병증
    if sensory_abnormal == 0 and muscle_abnormal >= 2 and neck_root_hint >= 1:
        scores["목 신경뿌리병증 (Cervical Radiculopathy)"] += 10
        lesion_tags.add("신경뿌리 수준 (Root level)")
        lesion_tags.add("목 분절 가능 (Cervical segment involvement)")
        reasons.append("감각신경 보존과 목 척추주위근 침범이 함께 보여 목 신경뿌리병증 가능성이 높습니다.")
        suggestions.add("목 자기공명영상(MRI)을 고려하세요.")

    # 허리 신경뿌리병증
    if sensory_abnormal == 0 and muscle_abnormal >= 2 and low_back_root_hint >= 1:
        scores["허리 신경뿌리병증 (Lumbar Radiculopathy)"] += 10
        lesion_tags.add("신경뿌리 수준 (Root level)")
        lesion_tags.add("허리 분절 가능 (Lumbar segment involvement)")
        reasons.append("감각신경 보존과 허리 척추주위근 침범이 함께 보여 허리 신경뿌리병증 가능성이 높습니다.")
        suggestions.add("허리 자기공명영상(MRI)을 고려하세요.")

    # 팔신경얼기병증
    if sensory_abnormal >= 1 and muscle_abnormal >= 2 and paraspinal_abnormal == 0 and arm_plexus_hint >= 1:
        scores["팔신경얼기병증 (Brachial Plexopathy)"] += 9
        lesion_tags.add("신경얼기 수준 (Plexus level)")
        reasons.append("감각신경 이상과 팔의 여러 신경 분포 근육 이상이 함께 있으며 척추주위근 침범이 뚜렷하지 않아 팔신경얼기병증 가능성이 있습니다.")
        suggestions.add("팔신경얼기 MRI 또는 신경초음파를 고려하세요.")

    # 허리엉치신경얼기병증
    if sensory_abnormal >= 1 and muscle_abnormal >= 2 and paraspinal_abnormal == 0 and leg_plexus_hint >= 1:
        scores["허리엉치신경얼기병증 (Lumbosacral Plexopathy)"] += 9
        lesion_tags.add("신경얼기 수준 (Plexus level)")
        reasons.append("감각신경 이상과 다리의 여러 신경 분포 근육 이상이 함께 있으며 척추주위근 침범이 뚜렷하지 않아 허리엉치신경얼기병증 가능성이 있습니다.")
        suggestions.add("허리엉치신경얼기 MRI 또는 신경초음파를 고려하세요.")

    # 단일신경병증
    if median_related >= 2 and arm_abnormal <= 5:
        scores["정중신경병증/포착신경병증 (Median Neuropathy/Entrapment)"] += 8
        lesion_tags.add("단일 말초신경 수준 (Single peripheral nerve level)")
        reasons.append("정중신경 분포 이상이 국소적으로 모여 정중신경병증 가능성이 있습니다.")
        suggestions.add("손목 부위 초음파 또는 국소 평가를 고려하세요.")

    if ulnar_related >= 2 and arm_abnormal <= 5:
        scores["자신경병증/포착신경병증 (Ulnar Neuropathy/Entrapment)"] += 8
        lesion_tags.add("단일 말초신경 수준 (Single peripheral nerve level)")
        reasons.append("자신경 분포 이상이 국소적으로 모여 자신경병증 가능성이 있습니다.")
        suggestions.add("팔꿉 또는 손목 부위 평가를 고려하세요.")

    if radial_related >= 2 and arm_abnormal <= 5:
        scores["노신경병증 (Radial Neuropathy)"] += 6
        lesion_tags.add("단일 말초신경 수준 (Single peripheral nerve level)")
        reasons.append("노신경 분포 이상이 우세하여 노신경병증 가능성이 있습니다.")

    if peroneal_related >= 2 and leg_abnormal <= 6:
        scores["종아리신경병증/포착신경병증 (Peroneal Neuropathy/Entrapment)"] += 9
        lesion_tags.add("단일 말초신경 수준 (Single peripheral nerve level)")
        reasons.append("종아리신경 분포 이상이 우세하여 종아리신경병증 가능성이 높습니다.")
        suggestions.add("종아리뼈 머리 부위 초음파 또는 국소 영상평가를 고려하세요.")

    if tibial_related >= 2 and leg_abnormal <= 6:
        scores["정강신경병증 (Tibial Neuropathy)"] += 6
        lesion_tags.add("단일 말초신경 수준 (Single peripheral nerve level)")
        reasons.append("정강신경 분포 이상이 우세하여 정강신경병증 가능성이 있습니다.")

    if femoral_related >= 2 and leg_abnormal <= 6:
        scores["넙다리신경병증 (Femoral Neuropathy)"] += 6
        lesion_tags.add("단일 말초신경 수준 (Single peripheral nerve level)")
        reasons.append("넙다리신경 분포 이상이 우세하여 넙다리신경병증 가능성이 있습니다.")

    # 다발신경병증
    if sensory_abnormal >= 3 and motor_abnormal >= 2:
        scores["다발신경병증 (Polyneuropathy)"] += 10
        lesion_tags.add("다발 말초신경 수준 (Multiple peripheral nerves)")
        reasons.append("여러 감각신경과 운동신경 이상이 함께 보여 다발신경병증 양상입니다.")
        suggestions.add("혈당, 당화혈색소, 비타민 B12, 갑상샘기능, 혈청단백전기영동 검사를 고려하세요.")

    if reduced_count >= delayed_count + 1 and (sensory_abnormal + motor_abnormal) >= 3:
        scores["축삭성 다발신경병증 (Axonal Polyneuropathy)"] += 6
        lesion_tags.add("축삭성 (Axonal)")
        reasons.append("진폭 감소 소견이 더 우세하여 축삭성 다발신경병증 가능성이 있습니다.")

    if delayed_count >= 3 or no_response_count >= 2:
        scores["말이집탈락성 다발신경병증 (Demyelinating Polyneuropathy)"] += 6
        lesion_tags.add("말이집탈락성 (Demyelinating)")
        reasons.append("잠복기 지연 또는 무반응 소견이 두드러져 말이집탈락성 병변 가능성이 있습니다.")
        suggestions.add("면역매개성 신경병증 감별을 위해 뇌척수액검사를 고려하세요.")

    # 근육병증
    if muscle_abnormal >= 3 and sensory_abnormal == 0 and motor_abnormal == 0 and paraspinal_abnormal == 0:
        scores["근육병증 (Myopathy)"] += 8
        lesion_tags.add("근육 수준 (Muscle level)")
        reasons.append("신경전도 이상 없이 여러 근육의 침근전도 이상이 보여 근육병증 가능성이 있습니다.")
        suggestions.add("CK, 근육 MRI, 근염 관련 항체, 필요 시 근생검을 고려하세요.")

    # 운동신경세포질환
    if muscle_abnormal >= 4 and sensory_abnormal == 0 and spontaneous_count >= 2:
        scores["운동신경세포질환 (Motor Neuron Disease)"] += 8
        lesion_tags.add("운동신경세포 수준 (Motor neuron level)")
        reasons.append("감각신경은 보존되면서 여러 분절 근육에 이상 전위가 보여 운동신경세포질환 가능성을 고려할 수 있습니다.")
        suggestions.add("추가 분절 및 벌바 영역 침근전도검사를 고려하세요.")

    # 눈 깜박 반사(Blink reflex)
    if reflex_abnormal >= 2:
        scores["뇌신경 반사경로 이상 가능성 (Blink Reflex Pathway Abnormality)"] += 7
        lesion_tags.add("뇌신경 반사경로 수준 (Cranial reflex pathway)")
        reasons.append("눈깜빡반사 이상이 있어 삼차신경-뇌줄기-얼굴신경 반사 경로 이상 가능성을 고려합니다.")

    if blink_right_stim_abnormal >= 1 and blink_left_stim_abnormal == 0:
        scores["삼차신경 들방향(afferent) 병변 가능성 (Trigeminal Afferent Lesion)"] += 8
        reasons.append("우측 자극에서만 눈깜빡반사 이상이 보여 우측 삼차신경 들방향 병변 가능성을 시사합니다.")

    if blink_right_stim_abnormal >= 1 and blink_left_stim_abnormal >= 1 and (blink_r1_abnormal + blink_r2_abnormal) >= 2:
        scores["뇌줄기 반사경로 병변 가능성 (Brainstem Reflex Pathway Lesion)"] += 8
        reasons.append("양측 자극에서 반복적인 눈깜빡반사 이상이 보여 뇌줄기 반사경로 병변 가능성을 시사합니다.")
        suggestions.add("뇌 MRI 및 뇌신경 평가를 고려하세요.")

    # 일반검사 정상
    if total_abnormal == 0:
        scores["신경근이음부질환 가능성 포함 (Neuromuscular Junction Disorder)"] += 2
        reasons.append("현재 일반 검사에서 뚜렷한 이상이 없으면 신경근이음부질환은 반복자극검사 등 특수검사가 필요할 수 있습니다.")
        suggestions.add("반복자극검사(RNS), 단일섬유근전도(SFEMG), 아세틸콜린수용체 항체 검사를 고려하세요.")

    if spontaneous_count >= 2:
        lesion_tags.add("활동성 탈신경 변화/아급성-급성 가능")
    if muscle_abnormal >= 2 and spontaneous_count == 0:
        lesion_tags.add("만성 변화 가능 (Chronic change possible)")

    severity = severity_text(total_abnormal, no_response_count)

    if not scores:
        scores["비특이적 이상 또는 추가 평가 필요 (Nonspecific abnormality / Further evaluation needed)"] = 1
        reasons.append("현재 체크 정보만으로 특정 질환군을 명확히 분류하기 어렵습니다.")
        suggestions.add("원시 수치, 좌우 비교, 추가 근육/신경 검사를 보완하세요.")

    top3 = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:3]

    return {
        "age": age,
        "sex": sex,
        "side": side,
        "final_dx": top3[0][0],
        "top3": top3,
        "severity": severity,
        "lesion_tags": sorted(lesion_tags),
        "reasons": reasons,
        "suggestions": sorted(suggestions),
        "involved_nerves": ", ".join(sorted(involved_nerves)) if involved_nerves else "특이 소견 없음",
        "involved_levels": ", ".join(sorted(involved_levels)) if involved_levels else "특이 소견 없음",
        "abnormal_items": abnormal_items,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

# ==========================================
# 입력 수집 함수
# ==========================================
def render_check_item(section, item, disabled=False):
    a = ANATOMY[item]

    st.markdown('<div class="input-row">', unsafe_allow_html=True)
    st.markdown(f'<div class="input-title">{item}</div>', unsafe_allow_html=True)
    st.markdown(
        f'<div class="input-meta">신경: {a["nerve"]} &nbsp;&nbsp;|&nbsp;&nbsp; 레벨: {a["level"]}</div>',
        unsafe_allow_html=True
    )

    use_item = st.checkbox("이 항목 입력하기", key=f"check_{section}_{item}", disabled=disabled)
    row = None

    if use_item:
        if a["domain"] == "reflex":
            left = st.selectbox("결과", CHECK_OPTIONS, key=f"left_{section}_{item}", disabled=disabled)
            right = ""
        else:
            c1, c2 = st.columns(2)
            left = c1.selectbox("정상쪽 결과", CHECK_OPTIONS, key=f"left_{section}_{item}", disabled=disabled)
            right = c2.selectbox("병변쪽 결과", CHECK_OPTIONS, key=f"right_{section}_{item}", disabled=disabled)

        row = {
            "section": section,
            "item": item,
            "left": left,
            "right": right
        }

    st.markdown('</div>', unsafe_allow_html=True)
    return row

def render_numeric_item(section, item, disabled=False):
    a = ANATOMY[item]

    st.markdown('<div class="input-row">', unsafe_allow_html=True)
    st.markdown(f'<div class="input-title">{item}</div>', unsafe_allow_html=True)
    st.markdown(
        f'<div class="input-meta">신경: {a["nerve"]} &nbsp;&nbsp;|&nbsp;&nbsp; 레벨: {a["level"]}</div>',
        unsafe_allow_html=True
    )

    use_item = st.checkbox("이 항목 입력하기", key=f"num_check_{section}_{item}", disabled=disabled)
    row = None

    if use_item:
        if a["domain"] in ["sensory", "motor"]:
            st.markdown(
                '<div class="section-help">정상쪽과 병변쪽 수치를 입력하면 교육용 단순 기준으로 자동 해석합니다.</div>',
                unsafe_allow_html=True
            )

            c1, c2 = st.columns(2)
            with c1:
                st.markdown("**정상쪽 수치**")
                normal_amp = st.number_input("정상쪽 진폭", min_value=0.0, value=10.0, step=0.1, key=f"na_{section}_{item}", disabled=disabled)
                normal_latency = st.number_input("정상쪽 잠복기", min_value=0.0, value=3.0, step=0.1, key=f"nl_{section}_{item}", disabled=disabled)

            with c2:
                st.markdown("**병변쪽 수치**")
                lesion_amp = st.number_input("병변쪽 진폭", min_value=0.0, value=10.0, step=0.1, key=f"la_{section}_{item}", disabled=disabled)
                lesion_latency = st.number_input("병변쪽 잠복기", min_value=0.0, value=3.0, step=0.1, key=f"ll_{section}_{item}", disabled=disabled)

            normal_status = "정상 (Normal)"
            lesion_status = infer_numeric_status(
                a["domain"],
                normal_amp,
                lesion_amp,
                normal_latency,
                lesion_latency,
                spontaneous=False
            )

            st.info(f"자동 해석 결과 → 정상쪽: {normal_status} / 병변쪽: {lesion_status}")

            row = {
                "section": section,
                "item": item,
                "left": normal_status,
                "right": lesion_status
            }

        elif a["domain"] == "muscle":
            st.markdown(
                '<div class="section-help">근육 항목은 비정상 자발전위 출현 여부를 체크합니다.</div>',
                unsafe_allow_html=True
            )

            c1, c2 = st.columns(2)
            with c1:
                normal_spont = st.checkbox("정상쪽 비정상 자발전위 있음", key=f"mns_{section}_{item}", disabled=disabled)
            with c2:
                lesion_spont = st.checkbox("병변쪽 비정상 자발전위 있음", key=f"mls_{section}_{item}", disabled=disabled)

            left_status = "비정상 자발전위 출현 (Abnormal Spontaneous Activity)" if normal_spont else "정상 (Normal)"
            right_status = "비정상 자발전위 출현 (Abnormal Spontaneous Activity)" if lesion_spont else "정상 (Normal)"

            st.info(f"자동 해석 결과 → 정상쪽: {left_status} / 병변쪽: {right_status}")

            row = {
                "section": section,
                "item": item,
                "left": left_status,
                "right": right_status
            }

        elif a["domain"] == "reflex":
            reflex_status = st.selectbox("결과", CHECK_OPTIONS, key=f"nr_{section}_{item}", disabled=disabled)
            st.info(f"자동 해석 결과 → {reflex_status}")
            row = {
                "section": section,
                "item": item,
                "left": reflex_status,
                "right": ""
            }

    st.markdown('</div>', unsafe_allow_html=True)
    return row

# Part 4

# ==========================================
# UI 렌더링 함수
# ==========================================
def render_header():
    st.markdown('<div class="main-title">교육용 근전도 판독 보조 앱</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtle">학생 교육용 규칙 기반 도구입니다. 실제 임상 진단을 대체하지 않습니다.</div>',
        unsafe_allow_html=True
    )

def render_guide():
    st.markdown('<div class="warn-card">', unsafe_allow_html=True)
    st.markdown("### 사용 방법")
    st.write("1. 먼저 학습 방식을 선택합니다.")
    st.write("2. 사례 학습에서는 대표적 사례 예시를 선택하고, 증상·검사·학습 포인트를 확인합니다.")
    st.write("3. 직접 입력 학습에서는 필요한 검사 항목만 선택적으로 입력합니다.")
    st.write("4. 체크형 입력 또는 수치형 입력을 선택할 수 있습니다.")
    st.write("5. 분석 실행을 누르면 최종 진단, 손상 신경, 신경학적 레벨, 감별진단, 추가 검사 권고가 출력됩니다.")
    st.markdown("</div>", unsafe_allow_html=True)

def render_mode_intro_box():
    st.markdown('<div class="mode-box-blue">', unsafe_allow_html=True)
    st.markdown('<div class="mode-title mode-title-blue">학습 모드 선택</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="mode-desc">사례 학습 또는 검사 정보 직접 입력 중 한 가지를 선택하세요. </div>',
        unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

def render_basic_info(disabled=False, title="기본 정보 입력"):
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.subheader(title)

    c1, c2, c3 = st.columns(3)
    age = c1.number_input(
        "나이",
        min_value=0,
        max_value=120,
        value=st.session_state.get("age", 50),
        step=1,
        key="age",
        disabled=disabled
    )
    sex = c2.selectbox(
        "성별",
        SEX_OPTIONS,
        index=safe_index(SEX_OPTIONS, st.session_state.get("sex", "미선택")),
        key="sex",
        disabled=disabled
    )
    side = c3.selectbox(
        "병변쪽/증상측",
        SIDE_OPTIONS,
        index=safe_index(SIDE_OPTIONS, st.session_state.get("side", "미선택")),
        key="side",
        disabled=disabled
    )

    st.markdown("</div>", unsafe_allow_html=True)
    return age, sex, side

def render_navigation_controls():
    app_mode = st.session_state.get("app_mode", MODE_CASE)
    confirmed_case = st.session_state.get("confirmed_case")
    is_first_case_screen = (app_mode == MODE_CASE and not confirmed_case)

    # 첫 화면(사례 선택 화면)에서는 버튼을 숨김
    if is_first_case_screen:
        return

    st.markdown("### 이동")
    c1, c2 = st.columns(2)

    with c1:
        if st.button(
            "처음으로",
            use_container_width=True,
            key=f"nav_home_{app_mode}_{confirmed_case}"
        ):
            switch_to_case_mode(reset_case_selection=True)
            st.rerun()

    with c2:
        # 이전 버튼 동작 정의
        # 1) 사례 상세 화면 -> 사례 선택 화면으로
        # 2) 직접 입력 모드 -> 직전 학습 흐름상 첫 화면(사례 선택 화면)으로
        if st.button(
            "이전으로",
            use_container_width=True,
            key=f"nav_back_{app_mode}_{confirmed_case}"
        ):
            if app_mode == MODE_CASE:
                if confirmed_case:
                    st.session_state["confirmed_case"] = None
                    clear_result()
                else:
                    # 첫 화면이면 이전 동작 없음
                    pass
            elif app_mode == MODE_DIRECT:
                switch_to_case_mode(reset_case_selection=False)
            st.rerun()

def render_mode_selector():
    render_mode_intro_box()

    current_mode = st.session_state.get("app_mode", MODE_CASE)
    mode_options = [MODE_CASE, MODE_DIRECT]
    default_index = mode_options.index(current_mode) if current_mode in mode_options else 0

    selected_mode = st.radio(
        "학습 방식",
        mode_options,
        index=default_index,
        help="사례를 먼저 학습한 뒤 직접 입력으로 넘어가는 교육 흐름을 권장합니다."
    )

    if selected_mode != st.session_state.get("app_mode"):
        st.session_state["app_mode"] = selected_mode
        st.session_state["confirmed_case"] = None
        clear_result()
        st.rerun()

def render_case_selector():
    case_options = get_case_names_for_selection()

    st.markdown('<div class="mode-box-green">', unsafe_allow_html=True)
    st.markdown('<div class="mode-title mode-title-green">1. 사례 선택</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="mode-desc">대표 사례를 하나 선택하고 확인 버튼을 누르세요. </div>',
        unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

    if not case_options:
        st.error("선택 가능한 사례가 없습니다. CASE_LIBRARY 구성을 확인하세요.")
        return

    default_case = st.session_state.get("selected_case")
    if default_case not in case_options:
        default_case = case_options[0]
        st.session_state["selected_case"] = default_case

    case_name = st.radio(
        "대표 사례 선택",
        case_options,
        index=safe_index(case_options, default_case),
        key="selected_case"
    )

    c1, c2 = st.columns(2)
    with c1:
        if st.button("확인", use_container_width=True, key="confirm_case_btn"):
            st.session_state["confirmed_case"] = case_name
            init_case_to_session(case_name)
            st.rerun()
    with c2:
        if st.button("다시 선택", use_container_width=True, key="reset_case_btn"):
            st.session_state["confirmed_case"] = None
            clear_result()
            st.rerun()

def render_case_learning_info(case_name):
    case_data = get_current_case_data(case_name)
    patient = case_data.get("patient", {})
    findings = case_data.get("findings", {})
    teaching = case_data.get("teaching", [])
    symptoms = patient.get("symptoms", [])
    physical_exam = patient.get("physical_exam", {})

    st.success(f"선택한 사례를 불러왔습니다: {case_name}")

    render_basic_info(disabled=True, title="사례 기본 정보")

    if symptoms:
        st.markdown('<div class="case-symptom-box">', unsafe_allow_html=True)
        st.markdown("### 사례 증상 요약")
        for s in symptoms:
            st.write(f"- {s}")
        st.markdown("</div>", unsafe_allow_html=True)

    if physical_exam:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown("### 이학적 검사 요약")

        for exam_title, exam_items in physical_exam.items():
            st.markdown(f"**{exam_title}**")
            if isinstance(exam_items, list):
                for exam_item in exam_items:
                    st.write(f"- {exam_item}")
            else:
                st.write(f"- {exam_items}")

        st.markdown("</div>", unsafe_allow_html=True)

    ncs_items = []
    needle_items = []
    other_items = []

    for item, vals in findings.items():
        domain = ANATOMY.get(item, {}).get("domain", "")
        if domain in ["sensory", "motor", "reflex"]:
            ncs_items.append((item, vals))
        elif domain == "muscle":
            needle_items.append((item, vals))
        else:
            other_items.append((item, vals))

    for title, grouped_items in [
        ("신경전도검사 예시", ncs_items),
        ("침근전도검사 예시", needle_items),
        ("기타 예시", other_items),
    ]:
        if grouped_items:
            st.markdown('<div class="section-card">', unsafe_allow_html=True)
            st.markdown(f"### {title}")

            for item, vals in grouped_items:
                left_val = vals[0] if len(vals) > 0 else ""
                right_val = vals[1] if len(vals) > 1 else ""

                if str(right_val).strip() == "":
                    st.write(f"- **{item}**: {left_val}")
                else:
                    st.write(f"- **{item}**")
                    st.write(f"  - 정상쪽/비병변측: {left_val}")
                    st.write(f"  - 병변쪽/증상측: {right_val}")

            st.markdown("</div>", unsafe_allow_html=True)

    if teaching:
        st.markdown('<div class="case-teaching-box">', unsafe_allow_html=True)
        st.markdown("### 학습 포인트")
        for t in teaching:
            st.write(f"- {t}")
        st.markdown("</div>", unsafe_allow_html=True)

    unmapped_items = st.session_state.get("last_unmapped_case_items", [])
    if unmapped_items:
        st.markdown('<div class="warn-card">', unsafe_allow_html=True)
        st.markdown("### 참고")
        st.write("아래 항목은 현재 직접 입력 섹션의 표준 목록에는 포함되어 있지 않아 사례 설명에만 표시됩니다.")
        for item in unmapped_items:
            st.write(f"- {item}")
        st.markdown("</div>", unsafe_allow_html=True)

def render_case_next_actions():
    st.markdown('<div class="mode-box-blue">', unsafe_allow_html=True)
    st.markdown('<div class="mode-title mode-title-blue">다음 단계 선택</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="mode-desc">사례 학습을 마쳤다면 다른 사례를 다시 선택하거나 직접 입력 모드로 이동할 수 있습니다. </div>',
        unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        if st.button("다른 사례 다시 선택", use_container_width=True, key="choose_another_case_btn"):
            st.session_state["confirmed_case"] = None
            clear_result()
            st.rerun()

    with c2:
        if st.button("검사 정보 직접 입력 모드로 이동", use_container_width=True, key="go_direct_input_btn"):
            switch_to_direct_mode()
            st.rerun()

def render_input_mode_box():
    st.markdown('<div class="mode-box-green">', unsafe_allow_html=True)
    st.markdown('<div class="mode-title mode-title-green">1. 입력 방식</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="mode-desc">체크형 입력 또는 수치형 입력 중 하나를 선택하세요. 선택한 방식의 UI만 보입니다.</div>',
        unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

def render_direct_input_basic_info_box():
    st.markdown('<div class="mode-box-gray">', unsafe_allow_html=True)
    st.markdown('<div class="mode-title mode-title-gray">2. 기본 정보 입력</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="mode-desc">나이, 성별, 병변쪽/증상측을 입력하세요.</div>',
        unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

def render_input_sections():
    rows = []

    render_input_mode_box()

    detail_mode = st.radio(
        "입력 방식",
        INPUT_MODES,
        horizontal=True,
        key="detail_input_mode",
        help="체크형 또는 수치형 입력 방식을 선택합니다."
    )

    tabs = st.tabs(["팔 감각/운동", "팔 침근전도", "다리 감각/운동", "다리 침근전도", "눈깜빡반사"])

    section_groups = [
        ["팔 감각신경전도검사 (Arm Sensory NCS)", "팔 운동신경전도검사 (Arm Motor NCS)"],
        ["팔 침근전도검사 근육 (Arm Needle EMG Muscles)"],
        ["다리 감각신경전도검사 (Leg Sensory NCS)", "다리 운동신경전도검사 (Leg Motor NCS)"],
        ["다리 침근전도검사 근육 (Leg Needle EMG Muscles)"],
        ["눈깜빡반사검사 (Blink Reflex)"]
    ]

    for tab, sections in zip(tabs, section_groups):
        with tab:
            for sec in sections:
                with st.expander(sec, expanded=False):
                    for item in SECTIONS[sec]:
                        if "체크형" in detail_mode:
                            row = render_check_item(sec, item)
                        else:
                            row = render_numeric_item(sec, item)
                        if row:
                            rows.append(row)

    return rows

def render_result(result):
    st.markdown("---")

    st.markdown('<div class="result-card">', unsafe_allow_html=True)
    st.subheader("최종 분석 결과")
    st.success(f"최종 유력 진단: {result['final_dx']}")
    st.write(f"**손상 의심 신경:** {result['involved_nerves']}")
    st.write(f"**신경학적 레벨/분절:** {result['involved_levels']}")
    st.write(f"**중증도:** {result['severity']}")
    if result["lesion_tags"]:
        st.write(f"**병변 해석 태그:** {', '.join(result['lesion_tags'])}")
    st.markdown("</div>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown("### Top 3 감별진단")
        for i, (dx, score) in enumerate(result["top3"], 1):
            st.write(f"{i}. {dx} — 점수 {score}")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown("### 판단 근거")
        for reason in result["reasons"]:
            st.write(f"- {reason}")
        st.markdown("</div>", unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown("### 추가 검사 권고")
        if result["suggestions"]:
            for s in result["suggestions"]:
                st.write(f"- {s}")
        else:
            st.write("- 추가 권고 없음")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown("### 이상 항목 요약")
        if result["abnormal_items"]:
            for item in result["abnormal_items"]:
                st.write(f"- **{item['항목']}**")
                st.write(f"  - 신경: {item['신경']}")
                st.write(f"  - 레벨: {item['레벨']}")
                st.write(f"  - {item['결과']}")
        else:
            st.write("- 입력 항목 중 뚜렷한 이상으로 분류된 항목이 없습니다.")
        st.markdown("</div>", unsafe_allow_html=True)

def render_download_section(result):
    report_text = make_report_text(result)
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("### 결과 다운로드")
    st.download_button(
        label="텍스트 보고서 다운로드 (.txt)",
        data=report_text.encode("utf-8"),
        file_name=f"emg_edu_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
        mime="text/plain",
        use_container_width=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# 메인 실행
# ==========================================
init_app_state()

render_header()
render_guide()
render_navigation_controls()
render_mode_selector()

# ------------------------------------------
# 사례 학습 모드
# ------------------------------------------
if st.session_state["app_mode"] == MODE_CASE:
    confirmed_case = st.session_state.get("confirmed_case")

    if confirmed_case:
        render_case_learning_info(confirmed_case)
        render_case_next_actions()
        st.info("현재는 사례 학습 화면입니다. ")
    else:
        render_case_selector()
        st.info("대표 사례를 선택한 뒤 확인 버튼을 누르면 사례 학습 내용이 표시됩니다.")

# ------------------------------------------
# 직접 입력 모드
# ------------------------------------------
elif st.session_state["app_mode"] == MODE_DIRECT:
    st.session_state["confirmed_case"] = None

    rows = render_input_sections()

    render_direct_input_basic_info_box()
    age, sex, side = render_basic_info(disabled=False, title="기본 정보 입력")

    c1, c2 = st.columns(2)
    with c1:
        analyze_btn = st.button("분석 실행", type="primary", use_container_width=True, key="analyze_btn")
    with c2:
        clear_btn = st.button("입력 초기화", use_container_width=True, key="clear_inputs_btn")

    if clear_btn:
        reset_all_inputs()
        clear_result()
        st.rerun()

    if analyze_btn:
        if not rows:
            st.warning("최소 1개 이상의 항목을 선택하거나 수치를 입력하세요.")
        else:
            result = analyze_case(age, sex, side, rows)
            st.session_state["last_result"] = result

    if st.session_state.get("last_result"):
        render_result(st.session_state["last_result"])
        render_download_section(st.session_state["last_result"])

else:
    st.error("알 수 없는 모드입니다. 처음으로 버튼을 눌러 다시 시작하세요.")
