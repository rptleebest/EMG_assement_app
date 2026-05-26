# app_data.py

# ==========================================
# 상수
# ==========================================
MODE_CASE = "사례 학습"
MODE_DIRECT = "검사 정보 입력 학습"

INPUT_MODES = [
    "체크형 입력 (Checklist Mode)",
    "수치형 입력 (Numeric Mode)"
]

SEX_OPTIONS = ["미선택", "남", "여"]
SIDE_OPTIONS = ["미선택", "좌", "우", "양측"]

# ==========================================
# 항목 정의 (SECTIONS와 ANATOMY 키 완전 일치)
# ==========================================
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
        "뒤넙다리근 (Biceps Femoris)",
        "허리 척추주위근 (Lumbar Paraspinal)"
    ],
    "후기반사검사 (Late responses / H Reflex)": [
        "H 반사 (좌)",
        "H 반사 (우)",
        "H/M 비율",
        "좌우 비교"
    ],
    "눈깜빡반사검사 (Blink reflex)": [
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
    "가쪽아래팔피부신경 감각신경활동전위 (Lateral antebrachial cutaneous SNAP)": {"nerve": "가쪽아래팔피부신경 (Lateral antebrachial cutaneous nerve)", "level": "팔신경얼기/근피신경, C5-C6", "domain": "sensory", "region": "arm"},

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

    "H 반사 (좌)": {"nerve": "정강신경-경골신경 경로 / S1 반사고리", "level": "late response / H reflex, S1", "domain": "reflex", "region": "leg"},
    "H 반사 (우)": {"nerve": "정강신경-경골신경 경로 / S1 반사고리", "level": "late response / H reflex, S1", "domain": "reflex", "region": "leg"},
    "H/M 비율": {"nerve": "척수 반사 흥분성 평가", "level": "late response / H reflex excitability", "domain": "reflex", "region": "leg"},
    "좌우 비교": {"nerve": "좌우 H 반사 비교", "level": "late response / side-to-side comparison", "domain": "reflex", "region": "leg"},
    "우측 자극 R1": {"nerve": "삼차신경-뇌줄기-얼굴신경 반사경로", "level": "blink reflex", "domain": "reflex", "region": "face"},
    "우측 자극 R2": {"nerve": "삼차신경-뇌줄기-얼굴신경 반사경로", "level": "blink reflex", "domain": "reflex", "region": "face"},
    "좌측 자극 R1": {"nerve": "삼차신경-뇌줄기-얼굴신경 반사경로", "level": "blink reflex", "domain": "reflex", "region": "face"},
    "좌측 자극 R2": {"nerve": "삼차신경-뇌줄기-얼굴신경 반사경로", "level": "blink reflex", "domain": "reflex", "region": "face"},
}

# ==========================================
# 사례 라이브러리 (학생 교육 최적화 12선)
# ==========================================
CASE_LIBRARY = {
    "1. 팔저림·손목약화 (C6 radiculopathy)": {
        "patient": {
            "age": 57,
            "sex": "남",
            "side": "우",
            "symptoms": [
                "뒷목에서 오른쪽 어깨와 팔 바깥쪽, 아래팔 노쪽(radial side)으로 뻗치는 방사통과 저림",
                "오른쪽 팔꿈치 굽히기 및 손목 젖히는 힘의 약화"
            ],
            "physical_exam": {
                "근력검사": ["팔꿈치 굽힘(위팔두갈래근) 및 손목 폄 약화 관찰"],
                "감각검사": ["아래팔 노쪽과 엄지 쪽 감각저하"],
                "반사검사": ["위팔두갈래근 반사 및 위팔노근 반사 감소"]
            }
        },
        "findings": {
            "목 척추주위근 (Cervical Paraspinal)": ("정상 (Normal)", "비정상 자발전위 출현 (Abnormal Spontaneous Activity)"),
            "위팔두갈래근 (Biceps Brachii)": ("정상 (Normal)", "비정상 자발전위 출현 (Abnormal Spontaneous Activity)"),
            "위팔노근 (Brachioradialis)": ("정상 (Normal)", "비정상 자발전위 출현 (Abnormal Spontaneous Activity)"),
            "긴노쪽손목폄근/짧은노쪽손목폄근 (Extensor Carpi Radialis Longus/Brevis)": ("정상 (Normal)", "비정상 자발전위 출현 (Abnormal Spontaneous Activity)"),
            "정중신경 감각신경활동전위 (Median SNAP)": ("정상 (Normal)", "정상 (Normal)"),
            "노신경 표재감각신경활동전위 (Superficial Radial SNAP)": ("정상 (Normal)", "정상 (Normal)")
        },
        "teaching": [
            "목에서 팔로 이어지는 방사통과 해당 분절의 근육 약화는 C6 신경뿌리병증을 강력히 시사합니다.",
            "신경뿌리병증(Radiculopathy)에서는 감각신경활동전위(SNAP)가 정상으로 보존되는 것이 말초신경병증과 감별하는 핵심 포인트입니다.",
            "척추주위근(Paraspinal)의 비정상 자발전위 출현 유무를 통해 노신경병증(Radial neuropathy)과 명확히 구분할 수 있습니다."
        ]
    },

    "2. 엄지·검지 저림 (Carpal tunnel syndrome)": {
        "patient": {
            "age": 46,
            "sex": "여",
            "side": "우",
            "symptoms": [
                "오른손 엄지, 검지, 중지의 저림 및 손바닥 통증",
                "야간에 증상이 악화되며, 손을 털면 일시적으로 호전됨"
            ],
            "physical_exam": {
                "근력검사": ["엄지 벌림(짧은엄지벌림근, APB) 약화"],
                "감각검사": ["엄지, 검지, 중지 감각저하"],
                "유발검사": ["팔렌 검사(Phalen test) 및 티넬 징후(Tinel sign) 양성 반응"]
            }
        },
        "findings": {
            "정중신경 감각신경활동전위 (Median SNAP)": ("정상 (Normal)", "잠복기 지연 (Delayed Latency)"),
            "정중신경 복합근육활동전위 (Median CMAP)": ("정상 (Normal)", "잠복기 지연 (Delayed Latency)"),
            "짧은엄지벌림근 (Abductor Pollicis Brevis, APB)": ("정상 (Normal)", "비정상 자발전위 출현 (Abnormal Spontaneous Activity)")
        },
        "teaching": [
            "엄지~중지 저림과 야간 악화는 손목굴증후군의 가장 전형적인 임상 양상입니다.",
            "정중신경의 감각 및 운동 잠복기 지연은 손목굴(carpal tunnel) 부위의 국소적 신경 포착을 의미합니다.",
            "증상이 목에서부터 시작되는 방사통인지, 손목 이하에 국한되는지 문진하여 목 신경뿌리병증과 감별해야 합니다."
        ]
    },

    "3. 손목처짐 (Radial neuropathy)": {
        "patient": {
            "age": 34,
            "sex": "남",
            "side": "우",
            "symptoms": [
                "위팔뼈 골절 이후 오른손목이 떨어지는 손목처짐(Wrist drop) 발생",
                "손목과 손가락 폄이 불가능하며 손등 저림 동반"
            ],
            "physical_exam": {
                "근력검사": ["손목 폄, 손가락 폄, 엄지 폄 근력 0~1등급(약화)"],
                "감각검사": ["손등 노쪽(radial side) 감각저하"],
                "반사검사": ["위팔세갈래근 반사는 골절 위치에 따라 정상 보존됨"]
            }
        },
        "findings": {
            "노신경 감각신경활동전위 (Radial SNAP)": ("정상 (Normal)", "감소 (Reduced)"),
            "노신경 복합근육활동전위 (Radial CMAP)": ("정상 (Normal)", "감소 (Reduced)"),
            "손목폄근 (Extensor Carpi Radialis / Extensor Digitorum)": ("정상 (Normal)", "비정상 자발전위 출현 (Abnormal Spontaneous Activity)"),
            "목 척추주위근 (Cervical Paraspinal)": ("정상 (Normal)", "정상 (Normal)")
        },
        "teaching": [
            "외상 후 발생한 손목처짐은 노신경마비(Radial nerve palsy)를 우선적으로 의심해야 합니다.",
            "손등 감각저하에 따른 SNAP 진폭 감소는 경추 신경뿌리병증이 아닌 말초 노신경 손상임을 강력히 지지합니다.",
            "척추주위근(Paraspinal)이 정상 소견인 것이 C7 신경뿌리병증과의 결정적 감별 포인트입니다."
        ]
    },

    "4. 어깨통증 후 다발약화 (Brachial plexopathy)": {
        "patient": {
            "age": 36,
            "sex": "남",
            "side": "좌",
            "symptoms": [
                "갑작스러운 극심한 왼쪽 어깨 통증 발생 후, 통증이 줄어들며 팔 전체의 힘이 빠짐",
                "특정 단일 신경 영역으로 설명하기 어려운 다발성 팔 근육 약화"
            ],
            "physical_exam": {
                "근력검사": ["어깨 벌림(삼각근) 및 팔꿈치 굽힘(위팔두갈래근) 약화 동반"],
                "감각검사": ["아래팔 가쪽(lateral) 감각저하"],
                "반사검사": ["위팔두갈래근 반사 감소"]
            }
        },
        "findings": {
            "목 척추주위근 (Cervical Paraspinal)": ("정상 (Normal)", "정상 (Normal)"),
            "가쪽아래팔피부신경 감각신경활동전위 (Lateral antebrachial cutaneous SNAP)": ("정상 (Normal)", "감소 (Reduced)"),
            "겨드랑신경 복합근육활동전위 (Axillary CMAP)": ("정상 (Normal)", "감소 (Reduced)"),
            "근피신경 복합근육활동전위 (Musculocutaneous CMAP)": ("정상 (Normal)", "감소 (Reduced)"),
            "삼각근 (Deltoid)": ("정상 (Normal)", "비정상 자발전위 출현 (Abnormal Spontaneous Activity)"),
            "위팔두갈래근 (Biceps Brachii)": ("정상 (Normal)", "비정상 자발전위 출현 (Abnormal Spontaneous Activity)")
        },
        "teaching": [
            "하나의 신경뿌리나 단일 말초신경으로 설명되지 않는 여러 신경 영역의 동시 손상은 신경얼기병증(Plexopathy)을 시사합니다.",
            "감각신경활동전위(SNAP)의 이상은 병변이 신경뿌리결절(DRG)보다 바깥쪽에 위치함(Post-ganglionic)을 의미합니다.",
            "척추주위근이 정상으로 보존되는 점을 통해 다발성 신경뿌리병증과 감별할 수 있습니다."
        ]
    },

    "5. 발처짐 (L5 radiculopathy)": {
        "patient": {
            "age": 61,
            "sex": "여",
            "side": "우",
            "symptoms": [
                "허리에서 오른쪽 엉치, 다리 바깥쪽을 거쳐 발등으로 뻗치는 방사통",
                "오른쪽 발목을 위로 들어 올리기 어려워 걷다가 발끝이 걸리는 발처짐 증상"
            ],
            "physical_exam": {
                "근력검사": ["발목 등굽힘(앞정강근), 엄지발가락 폄(긴엄지폄근) 약화 및 엉덩이 벌림(중간볼기근) 약화 동반"],
                "감각검사": ["다리 바깥쪽 및 발등 감각저하"]
            }
        },
        "findings": {
            "허리 척추주위근 (Lumbar Paraspinal)": ("정상 (Normal)", "비정상 자발전위 출현 (Abnormal Spontaneous Activity)"),
            "앞정강근 (Tibialis Anterior, TA)": ("정상 (Normal)", "비정상 자발전위 출현 (Abnormal Spontaneous Activity)"),
            "중간볼기근 (Gluteus Medius)": ("정상 (Normal)", "비정상 자발전위 출현 (Abnormal Spontaneous Activity)"),
            "얕은종아리신경 감각신경활동전위 (Superficial Peroneal SNAP)": ("정상 (Normal)", "정상 (Normal)")
        },
        "teaching": [
            "발처짐(Foot drop) 환자 평가 시 L5 신경뿌리병증과 온종아리신경병증의 감별이 가장 중요합니다.",
            "중간볼기근(Gluteus medius)과 허리 척추주위근의 이상은 병변이 종아리뼈 머리(fibular head)보다 훨씬 위쪽(근위부)에 있음을 명확히 보여줍니다.",
            "얕은종아리신경 SNAP가 정상으로 보존되는 점이 신경뿌리병증을 확진하는 강력한 감별 단서입니다."
        ]
    },

    "6. 골절 후 발처짐 (Common peroneal neuropathy)": {
        "patient": {
            "age": 31,
            "sex": "남",
            "side": "좌",
            "symptoms": [
                "왼쪽 정강뼈 골절로 인한 장기간의 석고붕대(cast) 치료 후 발처짐 발생",
                "석고붕대 제거 후 발목을 들어 올리지 못함"
            ],
            "physical_exam": {
                "근력검사": [
                    "발목 등굽힘 및 발가락 폄 약화",
                    "발안쪽번짐(Inversion, 뒤정강근)은 정상 근력으로 보존됨"
                ],
                "감각검사": ["종아리 바깥쪽과 발등 감각둔하"]
            }
        },
        "findings": {
            "얕은종아리신경 감각신경활동전위 (Superficial Peroneal SNAP)": ("정상 (Normal)", "감소 (Reduced)"),
            "종아리신경 복합근육활동전위 (Peroneal CMAP)": ("정상 (Normal)", "감소 (Reduced)"),
            "앞정강근 (Tibialis Anterior, TA)": ("정상 (Normal)", "비정상 자발전위 출현 (Abnormal Spontaneous Activity)"),
            "허리 척추주위근 (Lumbar Paraspinal)": ("정상 (Normal)", "정상 (Normal)")
        },
        "teaching": [
            "골절 깁스, 장시간 다리 꼬기, 체중 감소 등에 의한 종아리뼈 머리(fibular head) 부위 압박은 온종아리신경 마비의 흔한 원인입니다.",
            "발안쪽번짐(Inversion) 근력이 보존되고 척추주위근 침근전도가 정상이면 L5 신경뿌리병증을 배제할 수 있습니다.",
            "얕은종아리신경 SNAP 진폭 감소는 병변이 말초신경(신경뿌리결절 외부)에 위치함을 입증합니다."
        ]
    },

    "7. 골반통증 후 다발약화 (Lumbosacral plexopathy)": {
        "patient": {
            "age": 58,
            "sex": "여",
            "side": "좌",
            "symptoms": [
                "원인 모를 왼쪽 골반 및 허벅지 깊은 통증 후 왼쪽 다리 전체의 힘이 빠짐",
                "허리 통증보다는 골반부위 통증이 주 호소임"
            ],
            "physical_exam": {
                "근력검사": ["무릎 폄(넙다리신경), 발목 등굽힘(종아리신경), 발목 바닥굽힘(정강신경) 영역의 다발성 약화"],
                "반사검사": ["무릎반사 및 아킬레스힘줄 반사 모두 감소"]
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
            "서로 다른 말초신경(종아리, 정강, 넙다리신경) 분포에 걸친 광범위한 침범은 허리엉치신경얼기병증을 의심하게 합니다.",
            "신경얼기(Plexus) 병변이므로 감각신경(SNAP) 이상이 관찰됩니다.",
            "다발성 다리 약화가 있지만 허리 척추주위근(Paraspinal)이 정상이므로 다발성 신경뿌리병증과 감별됩니다."
        ]
    },

    "8. 양측 발저림 (Axonal polyneuropathy)": {
        "patient": {
            "age": 67,
            "sex": "남",
            "side": "양측",
            "symptoms": [
                "양쪽 발끝부터 시작된 저림과 감각 둔화가 점차 발목 위로 올라오는 양상(Stocking-glove pattern)",
                "수년에 걸쳐 서서히 진행됨"
            ],
            "physical_exam": {
                "근력검사": ["양측 발가락 움직임의 경미한 약화"],
                "감각검사": ["양측 발끝 길이의존성(Length-dependent) 감각 및 진동감각 저하"],
                "반사검사": ["아킬레스힘줄 반사 양측 소실"]
            }
        },
        "findings": {
            "장딴지신경 감각신경활동전위 (Sural SNAP)": ("감소 (Reduced)", "감소 (Reduced)"),
            "얕은종아리신경 감각신경활동전위 (Superficial Peroneal SNAP)": ("감소 (Reduced)", "감소 (Reduced)"),
            "종아리신경 복합근육활동전위 (Peroneal CMAP)": ("감소 (Reduced)", "감소 (Reduced)"),
            "정강신경 복합근육활동전위 (Tibial CMAP)": ("감소 (Reduced)", "감소 (Reduced)")
        },
        "teaching": [
            "발끝부터 대칭적으로 올라오는 감각저하는 다발신경병증(Polyneuropathy)의 전형적인 임상 패턴입니다.",
            "전도 속도 지연보다 '진폭 감소(Reduced amplitude)'가 전반적으로 우세하다면 축삭성(Axonal) 병변을 시사합니다.",
            "당뇨, 알코올 중독, 항암치료 부작용 등이 흔한 원인으로, 물리치료 시 발 보호 및 균형 훈련이 필수적입니다."
        ]
    },

    "9. 양손·양발 저림 (Demyelinating polyneuropathy)": {
        "patient": {
            "age": 55,
            "sex": "여",
            "side": "양측",
            "symptoms": [
                "수주에 걸쳐 양손과 양발이 대칭적으로 저리고, 걷기가 불안정해짐",
                "근위부와 원위부에 걸친 대칭적 근력 약화 호소"
            ],
            "physical_exam": {
                "근력검사": ["팔다리의 대칭적 근력 약화"],
                "감각검사": ["깊은감각(고유수용성감각) 저하로 인한 롬베르그(Romberg) 징후 양성 및 보행 불안정"],
                "반사검사": ["전반적인 깊은힘줄반사(DTR) 무반응"]
            }
        },
        "findings": {
            "정중신경 감각신경활동전위 (Median SNAP)": ("잠복기 지연 (Delayed Latency)", "잠복기 지연 (Delayed Latency)"),
            "자신경 감각신경활동전위 (Ulnar SNAP)": ("잠복기 지연 (Delayed Latency)", "잠복기 지연 (Delayed Latency)"),
            "정중신경 복합근육활동전위 (Median CMAP)": ("잠복기 지연 (Delayed Latency)", "잠복기 지연 (Delayed Latency)"),
            "자신경 복합근육활동전위 (Ulnar CMAP)": ("잠복기 지연 (Delayed Latency)", "잠복기 지연 (Delayed Latency)")
        },
        "teaching": [
            "여러 신경에서 진폭 감소보다 '잠복기 지연(Delayed latency) 및 전도속도 저하'가 뚜렷하다면 말이집탈락성(Demyelinating) 병변을 강력히 의심합니다.",
            "길이의존성 축삭병변과 달리, 비교적 짧은 기간 내에 근위부 약화와 반사 소실이 전반적으로 나타나는 특징이 있습니다.",
            "길랑-바레 증후군(GBS)이나 만성염증탈수초다발신경병증(CIDP) 등을 감별해야 합니다."
        ]
    },

    "10. 감각보존 진행성 약화 (Motor neuron disease)": {
        "patient": {
            "age": 63,
            "sex": "남",
            "side": "양측",
            "symptoms": [
                "양손의 미세 동작이 둔해지고 점차 다리까지 근력이 떨어짐",
                "저림이나 통증 같은 감각 이상은 전혀 호소하지 않음",
                "피부 밑으로 근육이 미세하게 뛰는 현상(Fasciculation) 관찰"
            ],
            "physical_exam": {
                "근력검사": ["비대칭적, 점진적인 사지 근력 약화 및 근위축"],
                "감각검사": ["감각검사(통각, 촉각, 진동각 등) 완전 정상"],
                "반사검사": ["위운동신경세포 병변 징후인 바빈스키 징후(Babinski sign) 양성 및 깊은힘줄반사 항진 동반"]
            }
        },
        "findings": {
            "삼각근 (Deltoid)": ("비정상 자발전위 출현 (Abnormal Spontaneous Activity)", "비정상 자발전위 출현 (Abnormal Spontaneous Activity)"),
            "앞정강근 (Tibialis Anterior, TA)": ("비정상 자발전위 출현 (Abnormal Spontaneous Activity)", "비정상 자발전위 출현 (Abnormal Spontaneous Activity)"),
            "정중신경 감각신경활동전위 (Median SNAP)": ("정상 (Normal)", "정상 (Normal)"),
            "장딴지신경 감각신경활동전위 (Sural SNAP)": ("정상 (Normal)", "정상 (Normal)")
        },
        "teaching": [
            "광범위한 근육의 약화와 위축이 있음에도 감각신경(SNAP)이 완벽히 정상이라면 운동신경세포질환(ALS 등)을 강하게 시사합니다.",
            "서로 다른 세 개 이상의 신체 분절(목, 허리, 뇌신경 등)에서 침근전도상 활성 탈신경 전위가 확인되어야 합니다.",
            "상위운동신경원(반사 항진, 강직)과 하위운동신경원(근위축, 섬유다발수축) 징후가 혼재하는 것이 핵심 임상 소견입니다."
        ]
    },

    "11. 얼굴감각저하 (Blink reflex abnormality)": {
        "patient": {
            "age": 56,
            "sex": "남",
            "side": "우",
            "symptoms": [
                "오른쪽 이마와 눈 주위의 감각 둔화 및 찌릿한 통증 호소",
                "얼굴 근육을 움직이는 데는 문제(안면마비)가 없음"
            ],
            "physical_exam": {
                "감각검사": ["오른쪽 삼차신경 제1지(V1) 영역 감각저하"],
                "운동검사": ["얼굴표정근 근력 정상"],
                "반사검사": ["우측 각막반사(Corneal reflex) 저하"]
            }
        },
        "findings": {
            "우측 자극 R1": ("지연 또는 소실 (Delayed/Absent)", ""),
            "우측 자극 R2": ("양측 지연 또는 소실 (Bilateral delayed/absent)", ""),
            "좌측 자극 R1": ("정상 (Normal)", ""),
            "좌측 자극 R2": ("정상 (Normal)", "")
        },
        "teaching": [
            "눈깜빡반사(Blink reflex)는 삼차신경(감각 입력) - 뇌줄기 - 얼굴신경(운동 출력) 경로를 평가하는 특수 검사입니다.",
            "우측을 자극했을 때만 R1, R2가 모두 비정상이고, 좌측 자극 시에는 양측 R2가 정상이라면, 병변은 입력 경로인 '우측 삼차신경(Trigeminal afferent)'에 있음을 의미합니다.",
            "얼굴의 편측 감각 이상을 감별 진단하는 데 매우 유용합니다."
        ]
    },

    "12. 뇌졸중 후 경직 (H reflex)": {
        "patient": {
            "age": 68,
            "sex": "남",
            "side": "우",
            "symptoms": [
                "좌측 대뇌 뇌경색 발병 6개월 후, 오른쪽 발목의 뻣뻣함(Spasticity)이 심해짐",
                "보행 시 무릎이 펴진 채로 발끝이 끌리며, 발바닥굽힘근의 저항이 강함"
            ],
            "physical_exam": {
                "반사검사": ["우측 아킬레스힘줄 반사 3+ (항진) 및 발목간대경련(Ankle clonus) 3회 이상 관찰"],
                "근긴장검사": ["수정애쉬워스척도(MAS) 2등급: 수동적 발목 등굽힘 시 속도 의존적 저항(Catch) 뚜렷함"]
            }
        },
        "findings": {
            "정강신경 복합근육활동전위 (Tibial CMAP)": ("정상 (Normal)", "정상 (Normal)"),
            "H 반사 (우)": ("항진 또는 역치 감소 (Hyperactive / lower threshold)", ""),
            "H/M 비율": ("증가 가능 (May be increased)", ""),
            "좌우 비교": ("병변측 H 반사 흥분성 증가 가능", "")
        },
        "teaching": [
            "H 반사(H-reflex)는 척수 단일연냅스 반사(Monosynaptic reflex)를 전기생리학적으로 객관화한 검사입니다.",
            "중추신경계 손상에 의한 경직(Spasticity) 발생 시, 하위운동신경원에 대한 상위 억제가 풀리면서 H 반사의 역치가 낮아지고 진폭(H/M ratio)이 증가합니다.",
            "물리치료 시 주관적인 임상 척도(MAS)와 함께 환자의 척수 반사 흥분성 수준을 이해하는 객관적 지표로 활용할 수 있습니다."
        ]
    }
}