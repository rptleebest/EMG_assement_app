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
.metric-card {
    background: #eff6ff;
    border: 1px solid #bfdbfe;
    border-radius: 12px;
    padding: 12px;
}
.small-text {
    font-size: 0.85rem;
    color: #555;
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
.expander-box {
    border: 1px solid #dbe4ea;
    border-radius: 12px;
    padding: 6px 10px;
    background: #ffffff;
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
</style>
""", unsafe_allow_html=True)

# ==========================================
# 공통 선택지
# ==========================================
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

# ==========================================
# 항목 정의
# ==========================================
SECTIONS = {
    "팔 감각신경전도검사 (Arm Sensory NCS)": [
        "정중신경 감각신경활동전위 (Median SNAP)",
        "자신경 감각신경활동전위 (Ulnar SNAP)",
        "노신경 감각신경활동전위 (Radial SNAP)",
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
        "삼각근 (Deltoid)",
        "위팔두갈래근 (Biceps Brachii)",
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
    "삼각근 (Deltoid)": {"nerve": "겨드랑신경 (Axillary nerve)", "level": "C5-C6", "domain": "muscle", "region": "arm"},
    "위팔두갈래근 (Biceps Brachii)": {"nerve": "근피신경 (Musculocutaneous nerve)", "level": "C5-C6", "domain": "muscle", "region": "arm"},
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

# ==========================================
# 사례 라이브러리
# ==========================================
CASE_LIBRARY = {
    "사례 선택 안 함": {},

    "1. 목 C5 신경뿌리병증 (Cervical Radiculopathy): 통증/방사통(pain/radiating pain) 중심형": {
        "patient": {
            "age": 49,
            "sex": "여",
            "side": "좌",
            "symptoms": [
                "뒷목에서 왼쪽 어깨 바깥쪽과 위팔 가쪽으로 뻗치는 통증이 있음",
                "목을 뒤로 젖히거나 왼쪽으로 돌리면 통증이 심해짐",
                "뚜렷한 근력저하는 없음"
            ]
        },
        "findings": {
            "목 척추주위근 (Cervical Paraspinal)": ("정상 (Normal)", "정상 (Normal)"),
            "삼각근 (Deltoid)": ("정상 (Normal)", "정상 (Normal)"),
            "위팔두갈래근 (Biceps Brachii)": ("정상 (Normal)", "정상 (Normal)"),
            "정중신경 감각신경활동전위 (Median SNAP)": ("정상 (Normal)", "정상 (Normal)"),
            "자신경 감각신경활동전위 (Ulnar SNAP)": ("정상 (Normal)", "정상 (Normal)")
        },
        "teaching": [
            "C5 분절의 방사통은 목에서 어깨 바깥쪽과 위팔 가쪽으로 퍼지는 통증으로 나타날 수 있습니다.",
            "근력저하가 뚜렷하지 않은 초기 또는 경미한 경우에는 근전도가 정상일 수 있습니다.",
            "감각신경전도는 대개 보존되므로 말초신경병증과 구분하는 데 도움이 됩니다.",
            "추후 목 MRI를 통해 추간판 탈출증(HNP)이나 협착증(stenosis) 여부를 평가할 수 있습니다."
        ]
    },

    "2. 목 C6 신경뿌리병증 (Cervical Radiculopathy): 운동침범형": {
        "patient": {
            "age": 57,
            "sex": "남",
            "side": "우",
            "symptoms": [
                "뒷목에서 오른쪽 어깨와 팔 바깥쪽으로 뻗치는 통증이 있음",
                "오른팔을 들어 올리거나 팔꿈치를 굽히는 힘이 빠짐",
                "팔 전체가 무겁게 느껴지고 물건 들기가 불편함"
            ]
        },
        "findings": {
            "목 척추주위근 (Cervical Paraspinal)": ("비정상 자발전위 출현 (Abnormal Spontaneous Activity)", "정상 (Normal)"),
            "삼각근 (Deltoid)": ("비정상 자발전위 출현 (Abnormal Spontaneous Activity)", "정상 (Normal)"),
            "위팔두갈래근 (Biceps Brachii)": ("비정상 자발전위 출현 (Abnormal Spontaneous Activity)", "정상 (Normal)"),
            "정중신경 감각신경활동전위 (Median SNAP)": ("정상 (Normal)", "정상 (Normal)"),
            "자신경 감각신경활동전위 (Ulnar SNAP)": ("정상 (Normal)", "정상 (Normal)")
        },
        "teaching": [
            "C6 신경뿌리병증에서는 어깨에서 팔 바깥쪽으로 이어지는 통증과 팔꿈치 굽힘 약화가 함께 보일 수 있습니다.",
            "척추주위근과 해당 분절 근육의 이상이 함께 보이면 신경뿌리병증을 강하게 시사합니다.",
            "감각신경전도는 보존되는 경우가 많아 말초신경병증과 구분하는 데 도움이 됩니다."
        ]
    },

    "3. 손목굴증후군: 손목굴 정중신경 포착 (Carpal Tunnel Syndrome)": {
        "patient": {
            "age": 46,
            "sex": "여",
            "side": "우",
            "symptoms": [
                "오른손 엄지, 검지, 중지의 저림과 손바닥 통증이 있음",
                "밤에 증상이 심해지고 손을 털면 조금 좋아짐",
                "엄지 쪽 집기 힘이 약해지는 느낌이 있음"
            ]
        },
        "findings": {
            "정중신경 감각신경활동전위 (Median SNAP)": ("잠복기 지연 (Delayed Latency)", "정상 (Normal)"),
            "정중신경 복합근육활동전위 (Median CMAP)": ("잠복기 지연 (Delayed Latency)", "정상 (Normal)"),
            "짧은엄지벌림근 (Abductor Pollicis Brevis, APB)": ("비정상 자발전위 출현 (Abnormal Spontaneous Activity)", "정상 (Normal)")
        },
        "teaching": [
            "엄지, 검지, 중지 저림과 야간 악화는 손목굴증후군의 전형적 양상입니다.",
            "손목굴에서의 정중신경 포착은 국소 말초신경병증의 대표적인 예입니다.",
            "정중신경 감각/운동 잠복기 지연이 중요한 전기진단 단서입니다."
        ]
    },

    "4. 노신경마비: 팔 부위 노신경 손상 (Radial Nerve Palsy)": {
        "patient": {
            "age": 34,
            "sex": "남",
            "side": "우",
            "symptoms": [
                "위팔뼈 골절 이후 오른손목이 떨어지는 손목처짐(wrist drop)이 생김",
                "손목과 손가락을 뒤로 젖히기 어렵고 손등 저림이 있음"
            ]
        },
        "findings": {
            "노신경 감각신경활동전위 (Radial SNAP)": ("감소 (Reduced)", "정상 (Normal)"),
            "노신경 복합근육활동전위 (Radial CMAP)": ("감소 (Reduced)", "정상 (Normal)"),
            "손목폄근 (Extensor Carpi Radialis / Extensor Digitorum)": ("비정상 자발전위 출현 (Abnormal Spontaneous Activity)", "정상 (Normal)")
        },
        "teaching": [
            "외상 후 손목처짐(wrist drop)은 노신경마비를 먼저 생각해야 합니다.",
            "노신경 분포 감각이상과 손목 폄 약화가 함께 있으면 말초신경 병변에 더 잘 맞습니다.",
            "경추 신경뿌리병증과 감별할 때 감각신경전도 이상이 도움이 됩니다."
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
            ]
        },
        "findings": {
            "자신경 감각신경활동전위 (Ulnar SNAP)": ("감소 (Reduced)", "정상 (Normal)"),
            "자신경 복합근육활동전위 (Ulnar CMAP)": ("잠복기 지연 (Delayed Latency)", "정상 (Normal)"),
            "첫째등쪽뼈사이근 (First Dorsal Interosseous, FDI)": ("비정상 자발전위 출현 (Abnormal Spontaneous Activity)", "정상 (Normal)")
        },
        "teaching": [
            "넷째, 다섯째 손가락 저림과 팔꿈치 굽힘 시 악화는 팔꿈치 자신경 포착을 시사합니다.",
            "하나의 말초신경 분포에 국한된 이상인지 확인하는 것이 중요합니다.",
            "손의 자체기원근육(intrinsic muscle) 침범은 자신경병증 진단에 도움이 됩니다."
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
            ]
        },
        "findings": {
            "가쪽아래팔피부신경 감각신경활동전위 (Lateral Antebrachial Cutaneous SNAP)": ("감소 (Reduced)", "정상 (Normal)"),
            "겨드랑신경 복합근육활동전위 (Axillary CMAP)": ("감소 (Reduced)", "정상 (Normal)"),
            "근피신경 복합근육활동전위 (Musculocutaneous CMAP)": ("감소 (Reduced)", "정상 (Normal)"),
            "삼각근 (Deltoid)": ("비정상 자발전위 출현 (Abnormal Spontaneous Activity)", "정상 (Normal)"),
            "위팔두갈래근 (Biceps Brachii)": ("비정상 자발전위 출현 (Abnormal Spontaneous Activity)", "정상 (Normal)")
        },
        "teaching": [
            "여러 말초신경 분포가 함께 침범되면 신경얼기병증을 생각합니다.",
            "감각신경전도 이상이 동반되면 신경뿌리병증보다 신경얼기병증에 더 잘 맞습니다.",
            "척추주위근 이상이 뚜렷하지 않으면 신경뿌리병변(root lesion)보다 신경얼기병변(plexus lesion) 가능성이 높습니다."
        ]
    },

    "7. 허리 S1 신경뿌리병증 (Lumbar Radiculopathy): 통증/방사통 중심형": {
        "patient": {
            "age": 52,
            "sex": "남",
            "side": "좌",
            "symptoms": [
                "허리에서 왼쪽 엉치와 종아리 뒤쪽, 발 바깥쪽으로 뻗치는 통증이 있음",
                "오래 앉아 있거나 허리를 굽히면 통증이 심해짐",
                "발목을 아래로 미는 힘 저하는 뚜렷하지 않음"
            ]
        },
        "findings": {
            "허리 척추주위근 (Lumbar Paraspinal)": ("정상 (Normal)", "정상 (Normal)"),
            "앞정강근 (Tibialis Anterior, TA)": ("정상 (Normal)", "정상 (Normal)"),
            "중간볼기근 (Gluteus Medius)": ("정상 (Normal)", "정상 (Normal)"),
            "장딴지신경 감각신경활동전위 (Sural SNAP)": ("정상 (Normal)", "정상 (Normal)")
        },
        "teaching": [
            "S1 분포에 가까운 방사통이 전형적이면 신경뿌리병증을 생각할 수 있습니다.",
            "근력저하가 뚜렷하지 않은 초기 또는 경미한 경우에는 근전도가 정상일 수 있습니다.",
            "이 경우에는 임상 증상과 영상검사(MRI)가 진단에 더 중요하며, 추간판 탈출증(HNP)이나 협착증(stenosis) 평가가 필요할 수 있습니다."
        ]
    },

    "8. 허리 L5 신경뿌리병증 (Lumbar Radiculopathy): 운동침범형": {
        "patient": {
            "age": 61,
            "sex": "여",
            "side": "우",
            "symptoms": [
                "허리에서 오른쪽 엉치와 다리 바깥쪽, 발등 쪽으로 뻗치는 통증이 있음",
                "오른쪽 발목과 엄지발가락을 들어 올리기 어려워 발처짐(foot drop) 양상이 의심됨",
                "오래 앉아 있으면 증상이 악화됨"
            ]
        },
        "findings": {
            "허리 척추주위근 (Lumbar Paraspinal)": ("비정상 자발전위 출현 (Abnormal Spontaneous Activity)", "정상 (Normal)"),
            "앞정강근 (Tibialis Anterior, TA)": ("비정상 자발전위 출현 (Abnormal Spontaneous Activity)", "정상 (Normal)"),
            "중간볼기근 (Gluteus Medius)": ("비정상 자발전위 출현 (Abnormal Spontaneous Activity)", "정상 (Normal)"),
            "장딴지신경 감각신경활동전위 (Sural SNAP)": ("정상 (Normal)", "정상 (Normal)"),
            "얕은종아리신경 감각신경활동전위 (Superficial Peroneal SNAP)": ("정상 (Normal)", "정상 (Normal)")
        },
        "teaching": [
            "운동증상이 동반되면 침근전도에서 이상이 더 잘 드러납니다.",
            "감각신경전도는 보존되는 경우가 많아 말초신경병증과 구분하는 데 도움이 됩니다.",
            "척추주위근 이상은 신경뿌리 병변을 지지합니다.",
            "발처짐(foot drop)만으로는 종아리신경병증과 감별이 필요하므로, 척추주위근 이상과 감각신경 보존을 함께 봐야 합니다."
        ]
    },

    "9. 종아리신경병증: 종아리뼈머리 부위 온종아리신경 포착 (Peroneal Neuropathy at Fibular Head)": {
        "patient": {
            "age": 29,
            "sex": "남",
            "side": "우",
            "symptoms": [
                "다리를 꼬고 앉는 습관 후 오른쪽 발처짐(foot drop)이 생김",
                "종아리 바깥쪽과 발등 감각 저하가 있음",
                "발등을 들어 올리기 어렵고 걸을 때 발끝이 끌림"
            ]
        },
        "findings": {
            "얕은종아리신경 감각신경활동전위 (Superficial Peroneal SNAP)": ("감소 (Reduced)", "정상 (Normal)"),
            "종아리신경 복합근육활동전위 (Peroneal CMAP)": ("무반응 (No Response)", "정상 (Normal)"),
            "앞정강근 (Tibialis Anterior, TA)": ("비정상 자발전위 출현 (Abnormal Spontaneous Activity)", "정상 (Normal)"),
            "짧은발가락폄근 (Extensor Digitorum Brevis, EDB)": ("비정상 자발전위 출현 (Abnormal Spontaneous Activity)", "정상 (Normal)")
        },
        "teaching": [
            "종아리뼈머리 부위 온종아리신경(common peroneal nerve) 포착은 발처짐(foot drop)의 흔한 원인입니다.",
            "발등 감각저하와 말초신경전도 이상이 동반되면 L5 신경뿌리병증보다 말초신경병증(peripheral neuropathy)에 더 잘 맞습니다.",
            "L5 신경뿌리병증과의 감별이 교육적으로 중요하며, 임상 양상과 허리 MRI를 함께 해석해야 합니다."
        ]
    },

    "10. 깊은종아리신경병증: 발목 앞쪽 깊은종아리신경 손상 (Deep Peroneal Neuropathy)": {
        "patient": {
            "age": 31,
            "sex": "남",
            "side": "좌",
            "symptoms": [
                "좌측 발등 앞쪽 통증과 함께 발가락을 들어 올리기 어려움이 생김",
                "첫째와 둘째 발가락 사이 감각이 둔함",
                "발목 전체보다 발가락 폄 동작이 더 불편함"
            ]
        },
        "findings": {
            "깊은종아리신경 복합근육활동전위 (Deep Peroneal CMAP)": ("감소 (Reduced)", "정상 (Normal)"),
            "짧은발가락폄근 (Extensor Digitorum Brevis, EDB)": ("비정상 자발전위 출현 (Abnormal Spontaneous Activity)", "정상 (Normal)"),
            "첫째 발가락사이 감각 (First Dorsal Web Space Sensation)": ("감소 (Reduced)", "정상 (Normal)")
        },
        "teaching": [
            "깊은종아리신경병증(deep peroneal nerve neuropathy)은 첫째 발가락사이 감각저하와 발가락 폄 약화가 특징적입니다.",
            "온종아리신경병증이(common peroneal nerve neuropathy)나 L5 신경뿌리병증(radiculopathy)보다 더 국소적인 병변 위치를 생각하게 합니다.",
            "병변 위치를 말초신경 해부학적으로 구분하는 데 도움이 되는 사례입니다."
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
            ]
        },
        "findings": {
            "장딴지신경 감각신경활동전위 (Sural SNAP)": ("감소 (Reduced)", "정상 (Normal)"),
            "종아리신경 복합근육활동전위 (Peroneal CMAP)": ("감소 (Reduced)", "정상 (Normal)"),
            "정강신경 복합근육활동전위 (Tibial CMAP)": ("감소 (Reduced)", "정상 (Normal)"),
            "앞정강근 (Tibialis Anterior, TA)": ("비정상 자발전위 출현 (Abnormal Spontaneous Activity)", "정상 (Normal)"),
            "장딴지근 (Gastrocnemius)": ("비정상 자발전위 출현 (Abnormal Spontaneous Activity)", "정상 (Normal)")
        },
        "teaching": [
            "여러 말초신경 분포와 감각신경 이상이 함께 나타나면 신경얼기병증을 고려합니다.",
            "신경뿌리병증(radiculopahty)과 달리 감각신경전도 이상이 더 분명할 수 있습니다.",
            "한 개의 신경뿌리병변(root lesion)이나 단일 신경 손상병변(single nerve lesion)으로 설명되지 않는 패턴이 핵심입니다."
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
            ]
        },
        "findings": {
            "장딴지신경 감각신경활동전위 (Sural SNAP)": ("감소 (Reduced)", "감소 (Reduced)"),
            "얕은종아리신경 감각신경활동전위 (Superficial Peroneal SNAP)": ("감소 (Reduced)", "감소 (Reduced)"),
            "종아리신경 복합근육활동전위 (Peroneal CMAP)": ("감소 (Reduced)", "감소 (Reduced)"),
            "정강신경 복합근육활동전위 (Tibial CMAP)": ("감소 (Reduced)", "감소 (Reduced)")
        },
        "teaching": [
            "여러 신경에서 진폭 감소가 우세하면 축삭성 다발신경병증을 생각합니다.",
            "좌우 대칭이며, 긴 신경이 가는 먼 부위부터 증상이 시작되는 것이 중요한 단서입니다(glove-stocking type).",
            "국소 포착병증(local entrapment neuropathy)이나 신경뿌리병증(radiculopathy)과 달리 다발성으로 나타납니다."
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
            ]
        },
        "findings": {
            "정중신경 감각신경활동전위 (Median SNAP)": ("잠복기 지연 (Delayed Latency)", "잠복기 지연 (Delayed Latency)"),
            "자신경 감각신경활동전위 (Ulnar SNAP)": ("잠복기 지연 (Delayed Latency)", "잠복기 지연 (Delayed Latency)"),
            "정중신경 복합근육활동전위 (Median CMAP)": ("잠복기 지연 (Delayed Latency)", "잠복기 지연 (Delayed Latency)"),
            "자신경 복합근육활동전위 (Ulnar CMAP)": ("잠복기 지연 (Delayed Latency)", "잠복기 지연 (Delayed Latency)")
        },
        "teaching": [
            "잠복기 지연이 여러 신경에서 반복되면 말이집탈락성 병변(demyelinating lesion) 가능성이 높습니다.",
            "진폭 감소보다 전도 지연이 두드러진다는 점이 축삭성 병변(axonopathy)과의 차이입니다.",
            "대칭성 다발신경병증의 대표적 전기진단 패턴으로 교육하기 좋습니다."
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
                "근육다발수축(fasciculation potential)이 관찰될 수 있음"
            ]
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
            "감각신경은 비교적 보존되면서 여러 분절의 근육에서 비정상 자발활동전위(abnormal spontaneous activity)가 보입니다.",
            "이 패턴은 운동신경세포질환(neuronopathy)을 의심하게 합니다.",
            "다발신경병증과 달리 감각신경전도가 비교적 정상이라는 점이 중요합니다."
        ]
    },

    "15. 눈 깜빡 반사 (Blink Reflex): 정상 반응": {
        "patient": {
            "age": 41,
            "sex": "여",
            "side": "양측",
            "symptoms": [
                "특별한 얼굴 통증, 감각이상, 얼굴마비는 없음"
            ]
        },
        "findings": {
            "우측 자극 R1": ("정상 (Normal)", ""),
            "우측 자극 R2": ("정상 (Normal)", ""),
            "좌측 자극 R1": ("정상 (Normal)", ""),
            "좌측 자극 R2": ("정상 (Normal)", "")
        },
        "teaching": [
            "정상 눈 깜빡 반사(blink reflex)는 삼차신경(trigeminal nerve)-뇌줄기(brain stem)-얼굴신경(facial nerve) 반사 경로가 보존됨을 시사합니다.",
            "R1과 R2가 모두 정상이고 좌우 대칭이면 반사 회로의 큰 이상 가능성은 낮습니다."
        ]
    },

    "16. 눈 깜빡 반사 (Blink Reflex): 삼차신경 들방향(afferent) 병변 의심": {
        "patient": {
            "age": 56,
            "sex": "남",
            "side": "우",
            "symptoms": [
                "오른쪽 이마와 눈 주위의 감각이 둔함",
                "오른쪽 얼굴 통증 또는 저림을 호소함",
                "얼굴마비는 없음"
            ]
        },
        "findings": {
            "우측 자극 R1": ("지연 또는 소실 (Delayed/Absent)", ""),
            "우측 자극 R2": ("양측 지연 또는 소실 (Bilateral Delayed/Absent)", ""),
            "좌측 자극 R1": ("정상 (Normal)", ""),
            "좌측 자극 R2": ("정상 (Normal)", "")
        },
        "teaching": [
            "오른쪽 자극에서만 R1과 R2가 비정상이면 오른쪽 삼차신경 들방향(afferent) 병변을 의심할 수 있습니다.",
            "반대쪽 자극에서 정상 반응이 나오면 출력 경로보다는 입력 경로 이상에 더 잘 맞습니다."
        ]
    },

    "17. 눈 깜빡 반사 (Blink Reflex): 뇌줄기 핵/중간연결 병변 의심": {
        "patient": {
            "age": 62,
            "sex": "여",
            "side": "우",
            "symptoms": [
                "얼굴 감각은 비교적 보존되어 있으나 복시(diplopia)와 어지럼이 동반됨",
                "신경학적 검사에서 뇌줄기 병변이 의심됨"
            ]
        },
        "findings": {
            "우측 자극 R1": ("지연 (Delayed)", ""),
            "우측 자극 R2": ("지연 (Delayed)", ""),
            "좌측 자극 R1": ("지연 (Delayed)", ""),
            "좌측 자극 R2": ("지연 (Delayed)", "")
        },
        "teaching": [
            "양측 자극에서 반사 경로 이상이 반복되면 말초 삼차신경 단독 병변보다 뇌줄기 병변(brain stem lesion)을 생각해야 합니다.",
            "눈 깜빡 반사(blink reflex)는 삼차신경, 얼굴신경, 그리고 뇌줄기 연결 회로를 함께 평가하는 검사입니다."
        ]
    },

    "18. 지속적 눈꺼풀 떨림: 눈 깜박 반사(blink reflex) 정상인 비신경병변": {
        "patient": {
            "age": 38,
            "sex": "여",
            "side": "좌",
            "symptoms": [
                "왼쪽 눈꺼풀 떨림이 2주 이상 지속됨",
                "수면 부족과 스트레스가 심한 시기에 증상이 시작됨",
                "얼굴 감각이상, 얼굴마비, 복시, 말하기 장애는 없음"
            ]
        },
        "findings": {
            "우측 자극 R1": ("정상 (Normal)", ""),
            "우측 자극 R2": ("정상 (Normal)", ""),
            "좌측 자극 R1": ("정상 (Normal)", ""),
            "좌측 자극 R2": ("정상 (Normal)", "")
        },
        "teaching": [
            "눈꺼풀 떨림이 지속되더라도 눈깜박 반사(blink reflex)가 정상이면 삼차신경-뇌줄기-얼굴신경 반사 경로의 중대한 이상 가능성은 낮습니다.",
            "수면 부족, 피로, 스트레스, 카페인 과다와 관련된 양성 눈꺼풀근육잔떨림(eyelid myokymia)을 먼저 생각할 수 있습니다.",
            "다만 얼굴 전체로 퍼지는 경련, 얼굴마비, 감각이상, 다른 뇌신경 증상이 동반되면 추가 평가가 필요합니다."
        ]
    },
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
        suggestions.add("크레아틴인산활성효소(CK), 근육 MRI, 근염 관련 항체, 필요 시 근생검을 고려하세요.")

    # 운동신경세포질환
    if muscle_abnormal >= 4 and sensory_abnormal == 0 and spontaneous_count >= 2:
        scores["운동신경세포질환 (Motor Neuron Disease)"] += 8
        lesion_tags.add("운동신경세포 수준 (Motor neuron level)")
        reasons.append("감각신경은 보존되면서 여러 분절 근육에 이상 전위가 보여 운동신경세포질환 가능성을 고려할 수 있습니다.")
        suggestions.add("추가 분절 및 벌바 영역 침근전도검사를 고려하세요.")

    # blink reflex
    if reflex_abnormal >= 2:
        scores["뇌신경 반사경로 이상 가능성 (Blink Reflex Pathway Abnormality)"] += 7
        lesion_tags.add("뇌신경 반사경로 수준 (Cranial reflex pathway)")
        reasons.append("눈깜빡반사 이상이 있어 삼차신경-뇌줄기-얼굴신경 반사 경로 이상 가능성을 고려합니다.")

    if blink_right_stim_abnormal >= 1 and blink_left_stim_abnormal == 0:
        scores["삼차신경 들방향(afferent) 병변 가능성 (Trigeminal Afferent Lesion)"] += 8
        reasons.append("우측 자극에서만 눈깜빡반사 이상이 보여 우측 삼차신경 들방향(afferent) 병변 가능성을 시사합니다.")

    if blink_right_stim_abnormal >= 1 and blink_left_stim_abnormal >= 1 and (blink_r1_abnormal + blink_r2_abnormal) >= 2:
        scores["뇌줄기 반사경로 병변 가능성 (Brainstem Reflex Pathway Lesion)"] += 8
        reasons.append("양측 자극에서 반복적인 눈깜빡반사 이상이 보여 뇌줄기 반사경로 병변 가능성을 시사합니다.")
        suggestions.add("뇌 MRI 및 뇌신경 평가를 고려하세요.")

    # 신경근이음부질환
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
        "involved_nerves": ", ".join(sorted(involved_nerves)) if involved_nerves else "특정 어려움",
        "involved_levels": ", ".join(sorted(involved_levels)) if involved_levels else "특정 어려움",
        "abnormal_items": abnormal_items,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

# ==========================================
# UI 함수
# ==========================================
def init_case_to_session(case_name):
    case_data = CASE_LIBRARY.get(case_name, {})
    patient = case_data.get("patient", {})
    findings = case_data.get("findings", {})

    st.session_state["age"] = patient.get("age", 50)
    st.session_state["sex"] = patient.get("sex", "미선택")
    st.session_state["side"] = patient.get("side", "미선택")

    for section, items in SECTIONS.items():
        for item in items:
            st.session_state[f"check_{section}_{item}"] = False
            st.session_state[f"left_{section}_{item}"] = "정상 (Normal)"
            st.session_state[f"right_{section}_{item}"] = "정상 (Normal)"
            st.session_state[f"num_check_{section}_{item}"] = False

    for item, vals in findings.items():
        section = find_section_for_item(item)
        if section:
            st.session_state[f"check_{section}_{item}"] = True
            st.session_state[f"left_{section}_{item}"] = vals[0] if len(vals) > 0 and vals[0] != "" else "정상 (Normal)"
            st.session_state[f"right_{section}_{item}"] = vals[1] if len(vals) > 1 and vals[1] != "" else "정상 (Normal)"

def render_header():
    st.markdown('<div class="main-title">교육용 근전도/신경전도 판독 보조 웹앱</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtle">학생 교육용 규칙 기반 도구입니다. 실제 임상 진단을 대체하지 않습니다.</div>', unsafe_allow_html=True)

def render_guide():
    st.markdown('<div class="warn-card">', unsafe_allow_html=True)
    st.markdown("### 사용 방법")
    st.write("1. 먼저 학습 방식을 선택합니다.")
    st.write("2. 사례 학습에서는 대표적 사례 예시 중 하나를 선택하면 관련 검사 정보가 자동으로 입력됩니다.")
    st.write("3. 직접 입력 학습에서는 팔/다리 감각, 운동, 침근전도, 눈깜빡반사 항목 중 필요한 것만 입력합니다.")
    st.write("4. 분석 실행을 누르면 최종 진단, 손상 신경, 신경학적 레벨, 감별진단, 추가 검사 권고가 출력됩니다.")
    st.write("5. 모바일에서는 탭을 하나씩 열어 입력하면 가장 편합니다.")
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
    sex_options = ["미선택", "남", "여"]
    side_options = ["미선택", "좌", "우", "양측"]

    sex = c2.selectbox(
        "성별",
        sex_options,
        index=sex_options.index(st.session_state.get("sex", "미선택"))
        if st.session_state.get("sex", "미선택") in sex_options else 0,
        key="sex",
        disabled=disabled
    )
    side = c3.selectbox(
        "병변쪽/증상측",
        side_options,
        index=side_options.index(st.session_state.get("side", "미선택"))
        if st.session_state.get("side", "미선택") in side_options else 0,
        key="side",
        disabled=disabled
    )
    st.markdown("</div>", unsafe_allow_html=True)
    return age, sex, side

def render_mode_and_case():
    if "go_to_direct_input" not in st.session_state:
        st.session_state["go_to_direct_input"] = False

    if "input_mode" not in st.session_state:
        st.session_state["input_mode"] = "사례 학습"

    if st.session_state["go_to_direct_input"]:
        st.session_state["input_mode"] = "검사 정보 직접 입력 후 자동 질환 추정 실행"
        st.session_state["go_to_direct_input"] = False

    mode = st.radio(
        "학습 방식",
        ["사례 학습", "검사 정보 직접 입력 후 자동 질환 추정 실행"],
        horizontal=False,
        key="input_mode",
        help="처음에는 사례 학습을 먼저 권장합니다."
    )

    case_name = None
    confirmed_case = False
    if mode == "사례 학습":
        st.markdown("""
        <div style="
            border: 3px solid #0b5394;
            border-radius: 14px;
            padding: 18px;
            background: linear-gradient(180deg, #f7fbff 0%, #eef6ff 100%);
            margin-top: 10px;
            margin-bottom: 16px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        ">
            <div style="font-size: 1.35rem; font-weight: 900; color: #0b5394; margin-bottom: 8px;">
                1-1. 사례 선택
            </div>
            <div style="font-size: 1.0rem; color: #333; line-height: 1.5;">
                아래에서 학습할 대표 사례를 선택한 뒤 확인을 누르세요.
            </div>
            <div style="
                display: inline-block;
                font-size: 0.9rem;
                font-weight: 700;
                color: #0b5394;
                background-color: #d9ecff;
                border-radius: 999px;
                padding: 4px 10px;
                margin-top: 8px;
            ">
                학생 추천: 사례부터 학습
            </div>
        </div>
        """, unsafe_allow_html=True)

        case_options = get_case_names_for_selection()
        default_index = 0

        if st.session_state.get("selected_case") in case_options:
            default_index = case_options.index(st.session_state.get("selected_case"))

        confirmed_case = st.session_state.get("confirmed_case")

        if confirmed_case is None:
            case_name = st.radio(
                "대표 사례 선택",
                case_options,
                index=default_index,
                key="selected_case"
            )

            c1, c2 = st.columns([1, 1])
            with c1:
                if st.button("확인", use_container_width=True, key="confirm_selected_case"):
                    st.session_state["confirmed_case"] = case_name
                    init_case_to_session(case_name)
                    st.rerun()

            with c2:
                if st.button("다시 선택", use_container_width=True, key="reset_selected_case"):
                    st.session_state["confirmed_case"] = None
                    st.session_state["selected_case"] = case_options[0]
                    st.rerun()

            confirmed_case = st.session_state.get("confirmed_case")

        else:
            case_name = confirmed_case

            st.info(f"선택된 사례: {confirmed_case}")

            c1, c2 = st.columns([1, 1])
            with c1:
                if st.button("다른 사례 다시 선택", use_container_width=True, key="reselect_case_after_confirm"):
                    st.session_state["confirmed_case"] = None
                    st.rerun()

            with c2:
                if st.button("검사 정보 직접 입력 모드로 이동", use_container_width=True, key="go_direct_input_after_case"):
                    st.session_state["go_to_direct_input"] = True
                    st.session_state["confirmed_case"] = None
                    st.rerun()

            confirmed_case = st.session_state.get("confirmed_case")

    else:
        st.session_state["confirmed_case"] = None

    return mode, case_name, confirmed_case

def render_case_learning_info(case_name):
    case_data = get_current_case_data(case_name)
    patient = case_data.get("patient", {})
    findings = case_data.get("findings", {})
    teaching = case_data.get("teaching", [])

    symptoms = patient.get("symptoms", [])

    if symptoms:
        st.markdown('<div class="case-symptom-box">', unsafe_allow_html=True)
        st.markdown("### 사례 증상 요약")
        for s in symptoms:
            st.write(f"- {s}")
        st.markdown("</div>", unsafe_allow_html=True)

    ncs_items = []
    needle_items = []
    other_items = []

    for item, vals in findings.items():
        anatomy = ANATOMY.get(item, {})
        domain = anatomy.get("domain", "")

        if domain in ["sensory", "motor", "reflex"]:
            ncs_items.append((item, vals))
        elif domain == "muscle":
            needle_items.append((item, vals))
        else:
            other_items.append((item, vals))

    if ncs_items:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown("### 신경전도검사 예시")
        for item, vals in ncs_items:
            left_val = vals[0] if len(vals) > 0 else ""
            right_val = vals[1] if len(vals) > 1 else ""
            if str(right_val).strip() == "":
                st.write(f"- **{item}**: {left_val}")
            else:
                st.write(f"- **{item}**")
                st.write(f"  - 좌/정상측: {left_val}")
                st.write(f"  - 우/병변측: {right_val}")
        st.markdown("</div>", unsafe_allow_html=True)

    if needle_items:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown("### 침근전도검사 예시")
        for item, vals in needle_items:
            left_val = vals[0] if len(vals) > 0 else ""
            right_val = vals[1] if len(vals) > 1 else ""
            if str(right_val).strip() == "":
                st.write(f"- **{item}**: {left_val}")
            else:
                st.write(f"- **{item}**")
                st.write(f"  - 좌/정상측: {left_val}")
                st.write(f"  - 우/병변측: {right_val}")
        st.markdown("</div>", unsafe_allow_html=True)

    if other_items:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown("### 기타 예시")
        for item, vals in other_items:
            left_val = vals[0] if len(vals) > 0 else ""
            right_val = vals[1] if len(vals) > 1 else ""
            if str(right_val).strip() == "":
                st.write(f"- **{item}**: {left_val}")
            else:
                st.write(f"- **{item}**")
                st.write(f"  - 좌/정상측: {left_val}")
                st.write(f"  - 우/병변측: {right_val}")
        st.markdown("</div>", unsafe_allow_html=True)

    if teaching:
        st.markdown('<div class="case-teaching-box">', unsafe_allow_html=True)
        st.markdown("### 학습 포인트")
        for t in teaching:
            st.write(f"- {t}")
        st.markdown("</div>", unsafe_allow_html=True)

def render_check_input_section():
    st.markdown("""
    <div style="
        border: 2px solid #3d85c6;
        border-radius: 12px;
        padding: 16px;
        background-color: #eef6ff;
        margin-bottom: 14px;
    ">
        <div style="font-size: 1.2rem; font-weight: 800; color: #0b5394;">
            체크형 입력
        </div>
        <div style="font-size: 0.97rem; color: #333; margin-top: 6px;">
            각 검사 항목을 정상/이상처럼 쉽게 선택할 수 있습니다.
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_numeric_input_section():
    st.markdown("""
    <div style="
        border: 2px solid #b45f06;
        border-radius: 12px;
        padding: 16px;
        background-color: #fff7ec;
        margin-bottom: 14px;
    ">
        <div style="font-size: 1.2rem; font-weight: 800; color: #7f6000;">
            수치 입력형
        </div>
        <div style="font-size: 0.97rem; color: #333; margin-top: 6px;">
            잠복기, 진폭, 전도 여부 등 기초 수치를 직접 입력할 수 있습니다.
        </div>
    </div>
    """, unsafe_allow_html=True)

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
            st.markdown('<div class="section-help">정상쪽과 병변쪽 수치를 입력하면 교육용 단순 기준으로 자동 해석합니다.</div>', unsafe_allow_html=True)

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
            st.markdown('<div class="section-help">근육 항목은 비정상 자발전위 출현 여부를 체크합니다.</div>', unsafe_allow_html=True)

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

def render_inputs(mode):
    rows = []

    if mode != "검사 정보 직접 입력 후 자동 질환 추정 실행":
        return rows

    detail_mode = st.radio(
        "입력 방식",
        INPUT_MODES,
        horizontal=True,
        key="detail_input_mode",
        help="체크형 또는 수치형 입력 방식을 선택합니다."
    )

    if "체크형" in detail_mode:
        render_check_input_section()
    else:
        render_numeric_input_section()

    st.markdown(
        '<div class="section-hint">'
        '아래의 검사 부위(팔 감각/운동, 팔 침근전도, 다리 감각/운동, 다리 침근전도, 눈깜빡반사)를 먼저 눌러 펼친 뒤, '
        '그 아래에 나타나는 세부 항목을 선택하여 입력하세요.'
        '</div>',
        unsafe_allow_html=True
    )

    tabs = st.tabs([
        "팔 감각/운동",
        "팔 침근전도",
        "다리 감각/운동",
        "다리 침근전도",
        "눈깜빡반사"
    ])

    with tabs[0]:
        st.markdown('<div class="big-section-title">팔 감각신경전도검사 / 팔 운동신경전도검사</div>', unsafe_allow_html=True)
        st.caption("먼저 아래 큰 항목을 눌러 세부 항목을 펼친 뒤 체크하세요.")

        for sec in ["팔 감각신경전도검사 (Arm Sensory NCS)", "팔 운동신경전도검사 (Arm Motor NCS)"]:
            with st.expander(f"▶ {sec}", expanded=False):
                st.markdown(
                    '<div class="section-hint">'
                    '이 항목을 펼친 후, 세부 검사 항목을 선택하세요. 필요한 항목만 체크하면 됩니다.'
                    '</div>',
                    unsafe_allow_html=True
                )
                for item in SECTIONS[sec]:
                    row = render_check_item(sec, item) if "체크형" in detail_mode else render_numeric_item(sec, item)
                    if row:
                        rows.append(row)

    with tabs[1]:
        st.markdown('<div class="big-section-title">팔 침근전도검사 근육</div>', unsafe_allow_html=True)
        st.caption("팔 근육 세부 항목을 선택하려면 아래 박스를 눌러 펼치세요.")

        sec = "팔 침근전도검사 근육 (Arm Needle EMG Muscles)"
        with st.expander(f"▶ {sec}", expanded=False):
            st.markdown(
                '<div class="section-hint">'
                '세부 근육 항목이 아래에 나타납니다. 이 항목들을 하나씩 체크하여 입력하세요.'
                '</div>',
                unsafe_allow_html=True
            )
            for item in SECTIONS[sec]:
                row = render_check_item(sec, item) if "체크형" in detail_mode else render_numeric_item(sec, item)
                if row:
                    rows.append(row)

    with tabs[2]:
        st.markdown('<div class="big-section-title">다리 감각신경전도검사 / 다리 운동신경전도검사</div>', unsafe_allow_html=True)
        st.caption("다리 검사 부위를 누르면 세부 항목이 펼쳐집니다.")

        for sec in ["다리 감각신경전도검사 (Leg Sensory NCS)", "다리 운동신경전도검사 (Leg Motor NCS)"]:
            with st.expander(f"▶ {sec}", expanded=False):
                st.markdown(
                    '<div class="section-hint">'
                    '아래에서 세부 항목을 확인하고 필요한 검사만 선택하세요.'
                    '</div>',
                    unsafe_allow_html=True
                )
                for item in SECTIONS[sec]:
                    row = render_check_item(sec, item) if "체크형" in detail_mode else render_numeric_item(sec, item)
                    if row:
                        rows.append(row)

    with tabs[3]:
        st.markdown('<div class="big-section-title">다리 침근전도검사 근육</div>', unsafe_allow_html=True)
        st.caption("다리 근육 세부 항목을 눌러 체크하세요.")

        sec = "다리 침근전도검사 근육 (Leg Needle EMG Muscles)"
        with st.expander(f"▶ {sec}", expanded=False):
            st.markdown(
                '<div class="section-hint">'
                '세부 근육 항목이 아래에 표시됩니다. 사용할 항목만 체크하여 입력하세요.'
                '</div>',
                unsafe_allow_html=True
            )
            for item in SECTIONS[sec]:
                row = render_check_item(sec, item) if "체크형" in detail_mode else render_numeric_item(sec, item)
                if row:
                    rows.append(row)

    with tabs[4]:
        st.markdown('<div class="big-section-title">눈깜빡반사검사 (Blink Reflex)</div>', unsafe_allow_html=True)
        st.caption("눈 깜빡 반사 항목을 눌러 선택하세요.")

        sec = "눈깜빡반사검사 (Blink Reflex)"
        with st.expander(f"▶ {sec}", expanded=False):
            st.markdown(
                '<div class="section-hint">'
                'R1, R2 항목을 선택하여 입력하세요.'
                '</div>',
                unsafe_allow_html=True
            )
            for item in SECTIONS[sec]:
                row = render_check_item(sec, item) if "체크형" in detail_mode else render_numeric_item(sec, item)
                if row:
                    rows.append(row)

    return rows

def render_navigation_controls(mode, confirmed_case=None):
    st.markdown("""
    <div style="
        border: 1px solid #dbe4ea;
        border-radius: 12px;
        padding: 10px 12px;
        background: #ffffff;
        margin-top: 8px;
        margin-bottom: 14px;
    ">
        <div style="font-size: 0.95rem; font-weight: 700; color: #374151;">
            이동
        </div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:
        if st.button("처음으로", use_container_width=True, key=f"go_home_{mode}_{str(confirmed_case)}"):
            st.session_state["input_mode"] = "사례 학습"
            st.session_state["confirmed_case"] = None
            st.session_state["selected_case"] = get_case_names_for_selection()[0] if get_case_names_for_selection() else None
            st.rerun()

    with c2:
        if st.button("이전으로", use_container_width=True, key=f"go_back_{mode}_{str(confirmed_case)}"):
            if mode == "사례 학습":
                if confirmed_case:
                    st.session_state["confirmed_case"] = None
                else:
                    st.session_state["input_mode"] = "사례 학습"
            else:
                st.session_state["input_mode"] = "사례 학습"
                st.session_state["confirmed_case"] = None
            st.rerun()

def render_result(result):
    st.markdown("---")
    st.markdown('<div class="result-card">', unsafe_allow_html=True)
    st.subheader("최종 분석 결과")
    st.success(f"최종 유력 진단: {result['final_dx']}")
    st.write(f"**손상 의심 신경:** {result['involved_nerves']}")
    st.write(f"**신경학적 레벨/분절:** {result['involved_levels']}")
    st.write(f"**중증도:** {result['severity']}")
    st.markdown("</div>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.subheader("Top 3 감별진단")
        for i, (dx, score) in enumerate(result["top3"], 1):
            st.write(f"{i}. {dx} — 점수 {score}")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.subheader("병변 수준/패턴")
        if result["lesion_tags"]:
            for tag in result["lesion_tags"]:
                st.write(f"- {tag}")
        else:
            st.write("- 특이 패턴 없음")
        st.markdown("</div>", unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.subheader("판단 근거")
        if result["reasons"]:
            for r in result["reasons"]:
                st.write(f"- {r}")
        else:
            st.write("- 판단 근거 없음")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.subheader("추가 검사 권고")
        if result["suggestions"]:
            for s in result["suggestions"]:
                st.write(f"- {s}")
        else:
            st.write("- 추가 권고 없음")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.subheader("이상 항목 상세")
    if result["abnormal_items"]:
        for item in result["abnormal_items"]:
            st.write(f"- **{item['항목']}**")
            st.write(f"  - 신경: {item['신경']}")
            st.write(f"  - 레벨: {item['레벨']}")
            st.write(f"  - 결과: {item['결과']}")
    else:
        st.write("- 이상 항목 없음")
    st.markdown("</div>", unsafe_allow_html=True)

    report_lines = [
        "=== 교육용 근전도/신경전도 판독 결과 ===",
        f"생성 시각: {result['created_at']}",
        f"나이: {result['age']}",
        f"성별: {result['sex']}",
        f"병변쪽/증상측: {result['side']}",
        "",
        f"최종 유력 진단: {result['final_dx']}",
        f"손상 의심 신경: {result['involved_nerves']}",
        f"신경학적 레벨/분절: {result['involved_levels']}",
        f"중증도: {result['severity']}",
        "",
        "Top 3 감별진단"
    ]
    for i, (dx, score) in enumerate(result["top3"], 1):
        report_lines.append(f"{i}. {dx} — 점수 {score}")

    report_lines.extend(["", "병변 수준/패턴"])
    for tag in result["lesion_tags"]:
        report_lines.append(f"- {tag}")

    report_lines.extend(["", "판단 근거"])
    for r in result["reasons"]:
        report_lines.append(f"- {r}")

    report_lines.extend(["", "추가 검사 권고"])
    for s in result["suggestions"]:
        report_lines.append(f"- {s}")

    report_lines.extend(["", "이상 항목 상세"])
    for item in result["abnormal_items"]:
        report_lines.append(f"- {item['항목']}")
        report_lines.append(f"  신경: {item['신경']}")
        report_lines.append(f"  레벨: {item['레벨']}")
        report_lines.append(f"  결과: {item['결과']}")

    report_text = "\n".join(report_lines)

    st.download_button(
        "결과 보고서 다운로드 (.txt)",
        data=report_text,
        file_name="emg_edu_report.txt",
        mime="text/plain"
    )

# ==========================================
# 메인 실행
# ==========================================
render_header()
render_guide()

mode, case_name, confirmed_case = render_mode_and_case()

if mode == "사례 학습":
    render_navigation_controls(mode, confirmed_case)

    if confirmed_case:
        st.success(f"선택한 사례를 불러왔습니다: {confirmed_case}")
        render_case_learning_info(confirmed_case)

        st.markdown("""
        <div style="
            border: 2px dashed #9fc5e8;
            border-radius: 12px;
            padding: 14px 16px;
            background-color: #f8fbff;
            margin-top: 14px;
            margin-bottom: 14px;
        ">
            <div style="font-size: 1.08rem; font-weight: 800; color: #0b5394; margin-bottom: 4px;">
                다음 단계 선택
            </div>
            <div style="font-size: 0.95rem; color: #444; line-height: 1.5;">
                위 사례 내용을 충분히 확인한 뒤, 아래에서 입력을 계속하거나 다른 사례 또는 다른 학습 방식으로 이동할 수 있습니다.
            </div>
        </div>
        """, unsafe_allow_html=True)

        b1, b2 = st.columns(2)
        with b1:
            if st.button("다른 사례 다시 선택", use_container_width=True, key="choose_another_case"):
                st.session_state["confirmed_case"] = None
                st.rerun()
        with b2:
            if st.button("검사 정보 직접 입력 모드로 이동", use_container_width=True):
                st.session_state["go_to_direct_input"] = True
                st.rerun()

        st.markdown("""
        <div style="
            border: 2px solid #d9ead3;
            border-radius: 12px;
            padding: 14px 16px;
            background-color: #f6fff2;
            margin-top: 10px;
            margin-bottom: 14px;
        ">
            <div style="font-size: 1.22rem; font-weight: 800; color: #38761d; margin-bottom: 4px;">
                2. 입력 방식
            </div>
            <div style="font-size: 0.96rem; color: #444; line-height: 1.5;">
                아래에서 체크형 입력 또는 수치형 입력을 선택하여 직접 학습을 이어갈 수 있습니다.
            </div>
        </div>
        """, unsafe_allow_html=True)

        rows = render_inputs(mode)

        st.markdown("""
        <div style="
            border: 2px solid #cfe2f3;
            border-radius: 12px;
            padding: 14px 16px;
            background-color: #f8fbff;
            margin-top: 10px;
            margin-bottom: 14px;
        ">
            <div style="font-size: 1.22rem; font-weight: 800; color: #0b5394; margin-bottom: 4px;">
                3. 기본 설정
            </div>
            <div style="font-size: 0.96rem; color: #444; line-height: 1.5;">
                사례 학습에서는 선택한 사례의 기본 정보가 자동 입력되며, 아래 항목은 확인용으로 표시됩니다.
            </div>
        </div>
        """, unsafe_allow_html=True)

        age, sex, side = render_basic_info(disabled=True, title="기본 설정")

    else:
        st.info("대표 사례를 선택한 뒤 확인 버튼을 눌러 학습 내용을 불러오세요.")
        rows = []
        age = st.session_state.get("age", 50)
        sex = st.session_state.get("sex", "미선택")
        side = st.session_state.get("side", "미선택")

else:
    render_navigation_controls(mode, confirmed_case=None)

    st.markdown("""
    <div style="
        border: 2px solid #d9ead3;
        border-radius: 12px;
        padding: 14px 16px;
        background-color: #f6fff2;
        margin-top: 10px;
        margin-bottom: 14px;
    ">
        <div style="font-size: 1.22rem; font-weight: 800; color: #38761d; margin-bottom: 4px;">
            1. 입력 방식
        </div>
        <div style="font-size: 0.96rem; color: #444; line-height: 1.5;">
            체크형 입력 또는 수치형 입력을 선택하세요.
        </div>
    </div>
    """, unsafe_allow_html=True)

    rows = render_inputs(mode)

    st.markdown("""
    <div style="
        border: 3px solid #b7b7b7;
        border-radius: 14px;
        padding: 18px;
        background: linear-gradient(180deg, #f8f8f8 0%, #f1f1f1 100%);
        margin-top: 10px;
        margin-bottom: 16px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.03);
    ">
        <div style="font-size: 1.25rem; font-weight: 900; color: #666666; margin-bottom: 8px;">
            2. 기본 정보 입력
        </div>
        <div style="font-size: 0.98rem; color: #555; line-height: 1.55;">
            나이, 성별, 병변쪽/증상측을 입력하세요.
        </div>
    </div>
    """, unsafe_allow_html=True)

    age, sex, side = render_basic_info(disabled=False, title="기본 정보 입력")

if mode == "사례 학습":
    st.info("사례 학습에서는 대표 사례 내용을 확인하고 입력 예시를 학습하는 방식입니다. 별도의 분석 실행 버튼은 사용하지 않습니다.")

else:
    c1, c2 = st.columns(2)
    with c1:
        analyze_btn = st.button("분석 실행", type="primary", use_container_width=True)
    with c2:
        st.info("기본 정보와 검사 정보를 입력한 뒤 분석을 실행하세요.")

    if analyze_btn:
        if not rows:
            st.warning("최소 1개 이상의 항목을 선택하거나 수치를 입력하세요.")
        else:
            result = analyze_case(age, sex, side, rows)
            render_result(result)
