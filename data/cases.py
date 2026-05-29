"""
물리치료학과 학생 및 임상물리치료사를 위한 교육용 근전도·신경전도검사 사례 라이브러리.

구성 원칙
1. 실제 진단을 대체하지 않는 교육용 사례입니다.
2. 한글 용어는 가능한 한 신용어를 사용합니다.
3. 각 사례는 증상, 이학적 검사, 전기진단검사 소견, 해석, 감별진단을 포함합니다.
4. 물리치료 관점에서 기능 평가와 임상 추론에 도움이 되도록 구성합니다.
"""

# -----------------------------
# 공통 표현
# -----------------------------

NCS_NORMAL = "정상 범위 또는 보존"
NCS_DELAYED = "잠복기 지연"
NCS_REDUCED = "진폭 감소"
NCS_ABSENT = "반응 소실"
NCS_SLOW = "전도속도 저하"
NCS_BLOCK = "전도차단 의심"

EMG_NORMAL = "휴식 시 전기적 침묵, 수의수축 시 정상 운동단위전위 동원"
EMG_ACTIVE_DENERVATION = "휴식 시 섬유자발전위 및 양성예파 관찰"
EMG_REDUCED_RECRUITMENT = "수의수축 시 운동단위전위 동원 감소"
EMG_NO_MUAP = "수의수축 시 운동단위전위 관찰되지 않음"
EMG_CHRONIC_NEUROGENIC = "크고 긴 지속시간의 운동단위전위 등 만성 신경원성 변화"
EMG_FASCICULATION = "근육다발수축전위 관찰 가능"

FWAVE_DELAYED_ABSENT = "F파 최소잠복기 지연 또는 반응 소실"
H_REFLEX_DELAYED_ABSENT = "H반사 지연 또는 소실"
H_REFLEX_HYPERACTIVE = "H반사 항진 또는 문턱값 감소"
H_M_RATIO_INCREASED = "H/M 비율 증가 가능"

BLINK_DELAYED = "잠복기 지연"
BLINK_DELAYED_ABSENT = "잠복기 지연 또는 반응 소실"


# -----------------------------
# 사례 라이브러리
# -----------------------------

CASE_LIBRARY = {
    # =========================================================
    # 1. 실제 이미지 기반: C5-C6 목 신경뿌리병증
    # =========================================================
    "좌측 어깨-팔 통증과 C5-C6 목 신경뿌리병증": {
        "patient": {
            "age": 52,
            "sex": "여",
            "side": "좌",
            "symptoms": [
                "왼쪽 목에서 어깨와 위팔 가쪽으로 뻗치는 통증",
                "팔을 들어 올리거나 팔꿉관절을 굽힐 때 힘이 빠짐",
                "목 움직임에 따라 팔 증상이 증가"
            ],
            "physical_exam": {
                "감각 검사": [
                    "어깨 가쪽과 위팔 가쪽의 감각 둔화 가능",
                    "손의 정중신경 또는 자신경 분포 감각저하는 뚜렷하지 않음"
                ],
                "맨손 근력검사": [
                    "어깨관절 벌림 약화",
                    "팔꿉관절 굽힘 약화",
                    "위팔노근 기능 약화 가능",
                    "손 자체근 근력은 비교적 보존"
                ],
                "반사 검사": [
                    "위팔두갈래근 반사 감소 가능",
                    "위팔노근 반사 감소 가능",
                    "위팔세갈래근 반사는 비교적 보존"
                ]
            }
        },
        "findings": {
            "정중신경 복합근육활동전위 (Median CMAP)": (NCS_NORMAL, NCS_NORMAL),
            "정중신경 감각신경활동전위 (Median SNAP)": (NCS_NORMAL, NCS_NORMAL),
            "자신경 감각신경활동전위 (Ulnar SNAP)": (NCS_NORMAL, NCS_NORMAL),
            "목 척추주위근 (Cervical Paraspinal)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "삼각근 (Deltoid)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "위팔두갈래근 (Biceps Brachii)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "위팔노근 (Brachioradialis)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "노쪽손목폄근 (Extensor Carpi Radialis)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "위팔세갈래근 (Triceps Brachii)": (EMG_NORMAL, EMG_NORMAL),
            "짧은엄지벌림근 (Abductor Pollicis Brevis, APB)": (EMG_NORMAL, EMG_NORMAL),
            "첫째등쪽뼈사이근 (First Dorsal Interosseous, FDI)": (EMG_NORMAL, EMG_NORMAL)
        },
        "teaching_diagnosis": {
            "summary": "좌측 C5-C6 중심의 목 신경뿌리병증 패턴입니다.",
            "ncs_reason": [
                "정중신경과 자신경의 감각신경전도검사가 보존되어 말초 감각신경병증 가능성은 낮습니다.",
                "운동신경전도검사도 대체로 보존되어 단일 말초신경 포착보다는 신경뿌리 수준 병변을 생각할 수 있습니다."
            ],
            "emg_reason": [
                "목 척추주위근에서 탈신경 소견이 관찰되어 목 신경뿌리병증을 지지합니다.",
                "삼각근, 위팔두갈래근, 위팔노근, 노쪽손목폄근처럼 서로 다른 말초신경 지배를 받지만 C5-C6 분절을 공유하는 근육에서 이상이 모여 있습니다.",
                "C7-T1 관련 근육은 상대적으로 보존되어 병변 분절 추정에 도움이 됩니다."
            ],
            "integration": [
                "감각신경활동전위 보존, 목 척추주위근 이상, C5-C6 분절 근육군의 탈신경 소견을 종합하면 좌측 C5-C6 목 신경뿌리병증이 가장 적절합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "겨드랑신경병증",
                "why_consider": "삼각근 약화와 어깨 가쪽 감각저하가 겹칠 수 있습니다.",
                "how_to_differentiate": "겨드랑신경병증은 목 척추주위근 이상이 없고, C5-C6의 여러 다른 말초신경 지배근 이상이 함께 나타나기 어렵습니다.",
                "practical_tip": "어깨관절 벌림 약화만 보지 말고 위팔두갈래근, 위팔노근, 목 척추주위근을 함께 확인하세요."
            },
            {
                "name": "위팔신경얼기병증",
                "why_consider": "여러 말초신경 지배근 약화가 나타날 수 있습니다.",
                "how_to_differentiate": "위팔신경얼기병증은 감각신경활동전위 감소가 동반될 수 있고 목 척추주위근은 대체로 보존됩니다.",
                "practical_tip": "감각신경활동전위와 목 척추주위근 소견을 함께 보는 것이 중요합니다."
            }
        ]
    },

    # =========================================================
    # 2. C7 목 신경뿌리병증
    # =========================================================
    "팔 뒤쪽 통증과 위팔세갈래근 약화": {
        "patient": {
            "age": 49,
            "sex": "남",
            "side": "우",
            "symptoms": [
                "오른쪽 목에서 팔 뒤쪽과 가운데손가락 쪽으로 뻗치는 통증",
                "팔꿉관절 폄과 손목관절 폄 시 힘이 빠짐"
            ],
            "physical_exam": {
                "감각 검사": [
                    "가운데손가락 주변 감각 둔화 가능"
                ],
                "맨손 근력검사": [
                    "위팔세갈래근 약화",
                    "손목관절 폄 약화 가능",
                    "손 자체근은 비교적 보존"
                ],
                "반사 검사": [
                    "위팔세갈래근 반사 감소"
                ]
            }
        },
        "findings": {
            "노신경 표재감각신경활동전위 (Superficial Radial SNAP)": (NCS_NORMAL, NCS_NORMAL),
            "노신경 복합근육활동전위 (Radial CMAP)": (NCS_NORMAL, NCS_NORMAL),
            "목 척추주위근 (Cervical Paraspinal)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "위팔세갈래근 (Triceps Brachii)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "집게폄근 (Extensor Indicis Proprius, EIP)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "첫째등쪽뼈사이근 (First Dorsal Interosseous, FDI)": (EMG_NORMAL, EMG_NORMAL)
        },
        "teaching_diagnosis": {
            "summary": "우측 C7 목 신경뿌리병증을 의심할 수 있는 패턴입니다.",
            "ncs_reason": [
                "노신경 감각 및 운동반응이 보존되어 말초 노신경병증 가능성은 낮습니다."
            ],
            "emg_reason": [
                "목 척추주위근과 C7 분절 관련 근육에서 탈신경 소견이 관찰됩니다.",
                "자신경 지배 손 자체근이 보존되어 C8-T1 병변 가능성은 낮습니다."
            ],
            "integration": [
                "방사통 방향, 위팔세갈래근 반사 저하, C7 관련 근육 이상을 종합하면 C7 목 신경뿌리병증이 적절합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "노신경병증",
                "why_consider": "손목관절 폄 약화가 겹칠 수 있습니다.",
                "how_to_differentiate": "노신경병증에서는 표재노신경 감각신경활동전위 감소가 나타날 수 있고 목 척추주위근은 정상입니다.",
                "practical_tip": "손목관절 폄 약화만으로 노신경병증으로 판단하지 말고 목 척추주위근과 감각신경활동전위를 확인하세요."
            }
        ]
    },

    # =========================================================
    # 3. 손목굴증후군
    # =========================================================
    "야간 손저림과 엄지손가락 벌림 약화": {
        "patient": {
            "age": 46,
            "sex": "여",
            "side": "우",
            "symptoms": [
                "오른손 엄지, 검지, 가운데손가락 중심의 야간 저림",
                "손을 털면 증상이 일시적으로 완화됨",
                "엄지손가락 벌림 힘이 약해짐"
            ],
            "physical_exam": {
                "감각 검사": [
                    "정중신경 분포 감각 둔화"
                ],
                "맨손 근력검사": [
                    "짧은엄지벌림근 약화"
                ],
                "특수 검사": [
                    "팔렌 검사 양성 가능",
                    "티넬징후 양성 가능"
                ]
            }
        },
        "findings": {
            "정중신경 감각신경활동전위 (Median SNAP)": (NCS_NORMAL, NCS_DELAYED),
            "정중신경 복합근육활동전위 (Median CMAP)": (NCS_NORMAL, NCS_DELAYED),
            "자신경 감각신경활동전위 (Ulnar SNAP)": (NCS_NORMAL, NCS_NORMAL),
            "짧은엄지벌림근 (Abductor Pollicis Brevis, APB)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION)
        },
        "teaching_diagnosis": {
            "summary": "손목굴증후군에 해당하는 정중신경 포착병증 패턴입니다.",
            "ncs_reason": [
                "정중신경 감각 및 운동 잠복기 지연은 손목굴 부위 국소 포착을 시사합니다.",
                "자신경 감각신경전도검사가 보존되어 다발신경병증보다 국소 정중신경병증 가능성이 높습니다."
            ],
            "emg_reason": [
                "짧은엄지벌림근 탈신경 소견은 운동축삭 침범이 동반된 비교적 진행된 손목굴증후군을 시사합니다."
            ],
            "integration": [
                "야간 손저림, 정중신경 분포 감각 이상, 손목 부위 잠복기 지연, 짧은엄지벌림근 이상을 종합하면 손목굴증후군이 적절합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "C6-C7 목 신경뿌리병증",
                "why_consider": "손 저림과 팔 통증이 겹칠 수 있습니다.",
                "how_to_differentiate": "목 신경뿌리병증은 감각신경활동전위가 보존되는 경우가 많고 목 척추주위근 이상이 동반될 수 있습니다.",
                "practical_tip": "야간 악화와 손목 자세 관련 증상이 뚜렷하면 손목굴증후군 가능성이 높습니다."
            }
        ]
    },

    # =========================================================
    # 4. 팔꿈치 부위 자신경병증
    # =========================================================
    "4, 5번째 손가락 저림과 손 자체근 약화": {
        "patient": {
            "age": 42,
            "sex": "남",
            "side": "우",
            "symptoms": [
                "오른손 4, 5번째 손가락 저림",
                "젓가락질과 단추 채우기가 어려움",
                "팔꿈치를 오래 굽히면 증상 증가"
            ],
            "physical_exam": {
                "감각 검사": [
                    "자신경 분포 감각 둔화"
                ],
                "맨손 근력검사": [
                    "손가락 벌림과 모음 약화",
                    "새끼손가락 벌림 약화"
                ],
                "특수 검사": [
                    "팔꿉굴 부위 티넬징후 양성 가능"
                ]
            }
        },
        "findings": {
            "자신경 감각신경활동전위 (Ulnar SNAP)": (NCS_NORMAL, NCS_DELAYED),
            "자신경 복합근육활동전위 (Ulnar CMAP)": (NCS_NORMAL, NCS_DELAYED),
            "새끼벌림근 (Abductor Digiti Minimi, ADM)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "첫째등쪽뼈사이근 (First Dorsal Interosseous, FDI)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "목 척추주위근 (Cervical Paraspinal)": (EMG_NORMAL, EMG_NORMAL)
        },
        "teaching_diagnosis": {
            "summary": "팔꿈치 부위 자신경병증 패턴입니다.",
            "ncs_reason": [
                "자신경 감각 및 운동 잠복기 지연은 팔꿈치 부위 포착을 시사합니다.",
                "감각신경활동전위 이상이 동반되어 말초 자신경 병변 가능성이 높습니다."
            ],
            "emg_reason": [
                "자신경 지배 손 자체근에서 탈신경 소견이 관찰됩니다.",
                "목 척추주위근이 정상이라 C8-T1 신경뿌리병증 가능성은 상대적으로 낮습니다."
            ],
            "integration": [
                "4, 5번째 손가락 저림, 손 자체근 약화, 자신경 전도 지연을 종합하면 팔꿈치 부위 자신경병증이 적절합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "C8-T1 목 신경뿌리병증",
                "why_consider": "손 자체근 약화가 공통으로 나타날 수 있습니다.",
                "how_to_differentiate": "신경뿌리병증은 감각신경활동전위가 보존되는 경우가 많고 목 척추주위근 이상이 동반될 수 있습니다.",
                "practical_tip": "자신경만의 문제인지, C8-T1 분절 문제인지 구분하세요."
            }
        ]
    },

    # =========================================================
    # 5. 노신경병증
    # =========================================================
    "위팔뼈 몸통 골절 후 손목처짐": {
        "patient": {
            "age": 34,
            "sex": "남",
            "side": "우",
            "symptoms": [
                "위팔뼈 몸통 골절 이후 손목처짐 발생",
                "손목과 손가락 폄이 어려움",
                "손등 노쪽 감각 이상 동반"
            ],
            "physical_exam": {
                "감각 검사": [
                    "손등 노쪽 감각 둔화"
                ],
                "맨손 근력검사": [
                    "손목관절 폄 약화",
                    "손가락 폄 약화",
                    "팔꿉관절 폄은 비교적 보존"
                ],
                "반사 검사": [
                    "위팔노근 반사 감소 가능",
                    "위팔세갈래근 반사는 비교적 보존"
                ]
            }
        },
        "findings": {
            "노신경 표재감각신경활동전위 (Superficial Radial SNAP)": (NCS_NORMAL, NCS_REDUCED),
            "노신경 복합근육활동전위 (Radial CMAP)": (NCS_NORMAL, NCS_REDUCED),
            "노쪽손목폄근 (Extensor Carpi Radialis)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "집게폄근 (Extensor Indicis Proprius, EIP)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "위팔세갈래근 (Triceps Brachii)": (EMG_NORMAL, EMG_NORMAL),
            "목 척추주위근 (Cervical Paraspinal)": (EMG_NORMAL, EMG_NORMAL)
        },
        "teaching_diagnosis": {
            "summary": "위팔뼈 나선고랑 부위 노신경병증 패턴입니다.",
            "ncs_reason": [
                "표재노신경 감각신경활동전위 감소는 말초 감각신경 침범을 의미합니다.",
                "노신경 복합근육활동전위 감소는 운동축삭 손상 또는 심한 전도장애 가능성을 시사합니다."
            ],
            "emg_reason": [
                "노신경 지배 원위부 폄근에서 탈신경 소견이 관찰됩니다.",
                "위팔세갈래근과 목 척추주위근이 보존되어 C7 신경뿌리병증이나 더 근위부 노신경병증 가능성은 낮습니다."
            ],
            "integration": [
                "외상 병력, 손목처짐, 표재노신경 감각신경활동전위 감소, 척추주위근 보존을 종합하면 노신경병증이 적절합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "C7 목 신경뿌리병증",
                "why_consider": "손목관절 폄 약화가 겹칠 수 있습니다.",
                "how_to_differentiate": "C7 신경뿌리병증은 감각신경활동전위가 보존되는 경우가 많고 목 척추주위근 이상이 동반될 수 있습니다.",
                "practical_tip": "표재노신경 감각신경활동전위와 목 척추주위근을 함께 보세요."
            }
        ]
    },

    # =========================================================
    # 6. L5 허리 신경뿌리병증
    # =========================================================
    "허리-다리 방사통과 발처짐": {
        "patient": {
            "age": 61,
            "sex": "여",
            "side": "우",
            "symptoms": [
                "허리에서 오른쪽 다리 가쪽과 발등으로 뻗치는 통증",
                "발끝이 끌리는 발처짐",
                "오래 걷거나 허리를 젖힐 때 증상 증가"
            ],
            "physical_exam": {
                "감각 검사": [
                    "종아리 가쪽과 발등 감각 둔화"
                ],
                "맨손 근력검사": [
                    "발목 등굽힘 약화",
                    "엄지발가락 폄 약화",
                    "엉덩관절 벌림 약화",
                    "발목 안쪽번짐 약화 가능"
                ],
                "반사 검사": [
                    "무릎반사와 아킬레스힘줄반사는 비교적 보존 가능"
                ]
            }
        },
        "findings": {
            "얕은종아리신경 감각신경활동전위 (Superficial Peroneal SNAP)": (NCS_NORMAL, NCS_NORMAL),
            "종아리신경 복합근육활동전위 (Peroneal CMAP)": (NCS_NORMAL, NCS_NORMAL),
            "허리 척추주위근 (Lumbar Paraspinal)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "앞정강근 (Tibialis Anterior, TA)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "긴엄지폄근 (Extensor Hallucis Longus, EHL)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "중간볼기근 (Gluteus Medius)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION)
        },
        "teaching_diagnosis": {
            "summary": "우측 L5 허리 신경뿌리병증 패턴입니다.",
            "ncs_reason": [
                "얕은종아리신경 감각신경활동전위가 보존되어 신경뿌리 수준 병변 가능성을 지지합니다.",
                "종아리신경 운동반응이 보존되어 온종아리신경병증 가능성은 상대적으로 낮습니다."
            ],
            "emg_reason": [
                "허리 척추주위근 이상은 허리 신경뿌리병증을 지지합니다.",
                "앞정강근, 긴엄지폄근, 중간볼기근처럼 서로 다른 말초신경 지배를 받지만 L5 분절을 공유하는 근육에서 탈신경 소견이 관찰됩니다."
            ],
            "integration": [
                "L5 분포 방사통, 발처짐, 감각신경활동전위 보존, 척추주위근 이상을 종합하면 L5 허리 신경뿌리병증이 가장 적절합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "온종아리신경병증",
                "why_consider": "발처짐이 공통으로 나타납니다.",
                "how_to_differentiate": "온종아리신경병증은 얕은종아리신경 감각신경활동전위 감소와 허리 척추주위근 보존이 흔합니다.",
                "practical_tip": "엉덩관절 벌림과 발목 안쪽번짐 약화가 있으면 L5 신경뿌리병증 쪽으로 기웁니다."
            }
        ]
    },

    # =========================================================
    # 7. 온종아리신경병증
    # =========================================================
    "석고붕대 후 발처짐과 발등 감각저하": {
        "patient": {
            "age": 31,
            "sex": "남",
            "side": "좌",
            "symptoms": [
                "정강뼈 골절로 석고붕대 후 좌측 발처짐 발생",
                "발등과 종아리 가쪽 감각저하",
                "발목 가쪽번짐이 약해짐"
            ],
            "physical_exam": {
                "감각 검사": [
                    "종아리 가쪽과 발등 감각 둔화"
                ],
                "맨손 근력검사": [
                    "발목 등굽힘 약화",
                    "엄지발가락 폄 약화",
                    "발목 가쪽번짐 약화",
                    "발목 안쪽번짐은 보존"
                ],
                "반사 검사": [
                    "무릎반사와 아킬레스힘줄반사는 대체로 보존"
                ]
            }
        },
        "findings": {
            "얕은종아리신경 감각신경활동전위 (Superficial Peroneal SNAP)": (NCS_NORMAL, NCS_REDUCED),
            "종아리신경 복합근육활동전위 (Peroneal CMAP)": (NCS_NORMAL, NCS_REDUCED),
            "앞정강근 (Tibialis Anterior, TA)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "긴종아리근 (Peroneus Longus)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "허리 척추주위근 (Lumbar Paraspinal)": (EMG_NORMAL, EMG_NORMAL)
        },
        "teaching_diagnosis": {
            "summary": "종아리뼈머리 부위 압박에 의한 온종아리신경병증 패턴입니다.",
            "ncs_reason": [
                "얕은종아리신경 감각신경활동전위 감소는 말초 감각신경 손상을 지지합니다.",
                "종아리신경 복합근육활동전위 감소는 운동섬유 침범을 시사합니다."
            ],
            "emg_reason": [
                "깊은종아리신경과 얕은종아리신경 분지 지배근 모두에서 탈신경 소견이 보입니다.",
                "허리 척추주위근은 정상으로 L5 허리 신경뿌리병증 가능성은 낮습니다."
            ],
            "integration": [
                "석고붕대 압박 병력, 발처짐, 발등 감각저하, 발목 안쪽번짐 보존, 척추주위근 보존을 종합하면 온종아리신경병증이 적절합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "L5 허리 신경뿌리병증",
                "why_consider": "발목 등굽힘과 엄지발가락 폄 약화가 공통으로 나타납니다.",
                "how_to_differentiate": "L5 신경뿌리병증은 감각신경활동전위 보존, 허리 척추주위근 이상, 엉덩관절 벌림 약화를 보일 수 있습니다.",
                "practical_tip": "발목 안쪽번짐 보존은 온종아리신경병증을 지지하는 중요한 단서입니다."
            }
        ]
    },

    # =========================================================
    # 8. 실제 이미지 기반: 허리엉치신경얼기병증
    # =========================================================
    "좌측 다리 광범위 약화와 허리엉치신경얼기병증": {
        "patient": {
            "age": 58,
            "sex": "남",
            "side": "좌",
            "symptoms": [
                "좌측 다리 전반의 근력저하와 보행장애",
                "발처짐과 발목 조절 저하",
                "다리 여러 부위의 감각 둔화"
            ],
            "physical_exam": {
                "감각 검사": [
                    "좌측 발등, 발바닥, 종아리 일부에서 광범위 감각저하 가능"
                ],
                "맨손 근력검사": [
                    "엉덩관절 벌림 약화",
                    "무릎 폄 약화 가능",
                    "발목 등굽힘 현저한 약화",
                    "발목 가쪽번짐 약화",
                    "발목 발바닥굽힘 약화 가능"
                ],
                "반사 검사": [
                    "침범 범위에 따라 무릎반사 또는 아킬레스힘줄반사 저하 가능"
                ]
            }
        },
        "findings": {
            "장딴지신경 감각신경활동전위 (Sural SNAP)": (NCS_NORMAL, NCS_REDUCED),
            "얕은종아리신경 감각신경활동전위 (Superficial Peroneal SNAP)": (NCS_NORMAL, NCS_NORMAL),
            "깊은종아리신경 복합근육활동전위 (Deep Peroneal CMAP)": (NCS_NORMAL, NCS_ABSENT),
            "종아리신경 복합근육활동전위 (Peroneal CMAP)": (NCS_NORMAL, NCS_REDUCED),
            "정강신경 복합근육활동전위 (Tibial CMAP)": (NCS_NORMAL, NCS_NORMAL),
            "허리 척추주위근 (Lumbar Paraspinal)": (EMG_NORMAL, EMG_NORMAL),
            "가쪽넓은근 (Vastus Lateralis)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "엉덩허리근 (Iliopsoas)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "큰볼기근 (Gluteus Maximus)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "중간볼기근 (Gluteus Medius)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "뒤넓적다리근 (Biceps Femoris)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "장딴지근 (Gastrocnemius)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "가자미근 (Soleus)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "앞정강근 (Tibialis Anterior, TA)": (EMG_NORMAL, EMG_NO_MUAP),
            "긴종아리근 (Peroneus Longus)": (EMG_NORMAL, EMG_NO_MUAP),
            "긴엄지폄근 (Extensor Hallucis Longus, EHL)": (EMG_NORMAL, EMG_NO_MUAP)
        },
        "teaching_diagnosis": {
            "summary": "좌측 허리엉치신경얼기병증을 강하게 시사하는 패턴입니다.",
            "ncs_reason": [
                "좌측 장딴지신경 감각신경활동전위가 감소하여 병변이 뒤뿌리신경절보다 원위부에 있을 가능성을 시사합니다.",
                "좌측 깊은종아리신경 또는 종아리신경 운동반응이 심하게 감소하거나 소실되어 운동축삭 침범이 뚜렷합니다.",
                "단일 온종아리신경병증만으로 설명하기에는 침범 범위가 넓습니다."
            ],
            "emg_reason": [
                "넓적다리신경, 위볼기신경, 아래볼기신경, 궁둥신경, 정강신경, 종아리신경 관련 근육들이 광범위하게 침범됩니다.",
                "허리 척추주위근이 정상으로 보존되어 다발 허리 신경뿌리병증보다 허리엉치신경얼기병증 가능성이 높습니다.",
                "일부 원위부 근육에서 수의수축 시 운동단위전위가 관찰되지 않는 것은 심한 운동축삭 손상을 시사합니다."
            ],
            "integration": [
                "감각신경활동전위 감소, 여러 말초신경 영역의 광범위 침범, 허리 척추주위근 보존을 종합하면 좌측 허리엉치신경얼기병증이 가장 적절합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "다발 허리 신경뿌리병증",
                "why_consider": "여러 분절의 근육 약화와 탈신경 소견이 겹칠 수 있습니다.",
                "how_to_differentiate": "다발 신경뿌리병증은 감각신경활동전위가 보존되는 경우가 많고 허리 척추주위근 이상이 동반될 수 있습니다.",
                "practical_tip": "감각신경활동전위 감소와 척추주위근 보존은 신경얼기병증 쪽으로 강하게 기웁니다."
            },
            {
                "name": "궁둥신경병증",
                "why_consider": "뒤넓적다리근과 종아리·정강신경 영역의 약화가 나타날 수 있습니다.",
                "how_to_differentiate": "엉덩허리근이나 넓적다리신경 지배근까지 침범되면 궁둥신경 단독 병변보다 허리엉치신경얼기병증 가능성이 높습니다.",
                "practical_tip": "무릎 폄과 엉덩관절 굽힘까지 함께 약하면 신경얼기 수준을 고려하세요."
            }
        ]
    },

    # =========================================================
    # 9. S1 허리 신경뿌리병증
    # =========================================================
    "종아리 뒤쪽 통증과 발바닥굽힘 약화": {
        "patient": {
            "age": 56,
            "sex": "남",
            "side": "좌",
            "symptoms": [
                "허리에서 좌측 종아리 뒤쪽과 발바닥으로 뻗치는 통증",
                "한발 뒤꿈치 들기가 어려움"
            ],
            "physical_exam": {
                "감각 검사": [
                    "발바닥 또는 발 가쪽 감각 둔화 가능"
                ],
                "맨손 근력검사": [
                    "발목 발바닥굽힘 약화",
                    "발가락 굽힘 약화 가능"
                ],
                "반사 검사": [
                    "아킬레스힘줄반사 감소"
                ]
            }
        },
        "findings": {
            "장딴지신경 감각신경활동전위 (Sural SNAP)": (NCS_NORMAL, NCS_NORMAL),
            "정강신경 복합근육활동전위 (Tibial CMAP)": (NCS_NORMAL, NCS_NORMAL),
            "H 반사 (좌)": (NCS_NORMAL, H_REFLEX_DELAYED_ABSENT),
            "허리 척추주위근 (Lumbar Paraspinal)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "장딴지근 (Gastrocnemius)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "가자미근 (Soleus)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "앞정강근 (Tibialis Anterior, TA)": (EMG_NORMAL, EMG_NORMAL)
        },
        "teaching_diagnosis": {
            "summary": "좌측 S1 허리 신경뿌리병증 패턴입니다.",
            "ncs_reason": [
                "장딴지신경 감각신경활동전위가 보존되어 신경뿌리 수준 병변 가능성을 지지합니다.",
                "좌측 H반사 지연 또는 소실은 S1 경로 이상을 시사합니다."
            ],
            "emg_reason": [
                "허리 척추주위근과 S1 관련 종아리 근육에서 탈신경 소견이 보입니다.",
                "L5 관련 앞정강근은 보존되어 S1 우세 병변으로 해석할 수 있습니다."
            ],
            "integration": [
                "발바닥굽힘 약화, 아킬레스힘줄반사 감소, H반사 이상, S1 관련 근육 이상을 종합하면 S1 허리 신경뿌리병증이 적절합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "정강신경병증",
                "why_consider": "발바닥굽힘 약화와 발바닥 감각 이상이 겹칠 수 있습니다.",
                "how_to_differentiate": "정강신경병증은 정강신경 전도 이상과 말초 감각신경 이상이 더 뚜렷하고 허리 척추주위근은 정상입니다.",
                "practical_tip": "H반사와 허리 척추주위근 소견을 함께 확인하세요."
            }
        ]
    },

    # =========================================================
    # 10. 당뇨병성 축삭성 다발신경병증
    # =========================================================
    "양측 발끝 저림과 균형 저하": {
        "patient": {
            "age": 67,
            "sex": "남",
            "side": "양측",
            "symptoms": [
                "양쪽 발끝부터 시작된 저림",
                "밤에 발이 화끈거리거나 감각이 둔함",
                "어두운 곳에서 균형을 잡기 어려움"
            ],
            "physical_exam": {
                "감각 검사": [
                    "양말형 감각저하",
                    "진동감각과 위치감각 저하 가능"
                ],
                "맨손 근력검사": [
                    "발가락 움직임의 경미한 약화"
                ],
                "반사 검사": [
                    "아킬레스힘줄반사 양측 감소 또는 소실"
                ]
            }
        },
        "findings": {
            "장딴지신경 감각신경활동전위 (Sural SNAP)": (NCS_REDUCED, NCS_REDUCED),
            "얕은종아리신경 감각신경활동전위 (Superficial Peroneal SNAP)": (NCS_REDUCED, NCS_REDUCED),
            "정강신경 복합근육활동전위 (Tibial CMAP)": (NCS_REDUCED, NCS_REDUCED),
            "앞정강근 (Tibialis Anterior, TA)": (EMG_NORMAL, EMG_CHRONIC_NEUROGENIC)
        },
        "teaching_diagnosis": {
            "summary": "길이 의존성 축삭성 다발신경병증 패턴입니다.",
            "ncs_reason": [
                "양측 원위부 감각신경활동전위와 운동반응 진폭이 대칭적으로 감소합니다.",
                "진폭 감소가 두드러지면 축삭성 다발신경병증을 우선 고려합니다."
            ],
            "emg_reason": [
                "원위부 근육에서 만성 신경원성 변화가 동반될 수 있습니다."
            ],
            "integration": [
                "양측 발끝에서 시작되는 감각저하, 아킬레스힘줄반사 감소, 원위부 진폭 감소를 종합하면 길이 의존성 축삭성 다발신경병증이 적절합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "말이집탈락성 다발신경병증",
                "why_consider": "양측성 감각저하와 근력저하가 겹칠 수 있습니다.",
                "how_to_differentiate": "말이집탈락성 병변은 전도속도 저하, 잠복기 지연, F파 이상이 더 두드러질 수 있습니다.",
                "practical_tip": "진폭 감소 우세인지, 전도 지연 우세인지 먼저 구분하세요."
            }
        ]
    },

    # =========================================================
    # 11. 말이집탈락성 다발신경병증 / GBS-CIDP 학습
    # =========================================================
    "대칭성 팔다리 약화와 반사 소실": {
        "patient": {
            "age": 55,
            "sex": "여",
            "side": "양측",
            "symptoms": [
                "양손과 양발의 대칭적 저림",
                "계단 오르기와 보행이 점점 어려움",
                "최근 수주에서 수개월 동안 진행"
            ],
            "physical_exam": {
                "감각 검사": [
                    "상지와 하지 원위부 감각저하"
                ],
                "맨손 근력검사": [
                    "근위부와 원위부 모두 대칭성 약화"
                ],
                "반사 검사": [
                    "깊은힘줄반사 전반적 감소 또는 소실"
                ]
            }
        },
        "findings": {
            "정중신경 F파 (Median F-wave)": (FWAVE_DELAYED_ABSENT, FWAVE_DELAYED_ABSENT),
            "자신경 F파 (Ulnar F-wave)": (FWAVE_DELAYED_ABSENT, FWAVE_DELAYED_ABSENT),
            "정강신경 F파 (Tibial F-wave)": (FWAVE_DELAYED_ABSENT, FWAVE_DELAYED_ABSENT),
            "종아리신경 F파 (Peroneal F-wave)": (FWAVE_DELAYED_ABSENT, FWAVE_DELAYED_ABSENT),
            "정중신경 복합근육활동전위 (Median CMAP)": (NCS_DELAYED, NCS_DELAYED),
            "정강신경 복합근육활동전위 (Tibial CMAP)": (NCS_SLOW, NCS_SLOW)
        },
        "teaching_diagnosis": {
            "summary": "말이집탈락성 다발신경병증을 시사하는 패턴입니다.",
            "ncs_reason": [
                "여러 신경에서 F파 지연 또는 소실이 관찰되어 근위부 전도 이상을 시사합니다.",
                "잠복기 지연과 전도속도 저하가 동반되면 말이집탈락성 변화 가능성이 높습니다."
            ],
            "emg_reason": [
                "초기에는 침근전도 탈신경 소견이 뚜렷하지 않을 수 있습니다.",
                "질환이 진행되면 축삭 손상이 동반되어 탈신경 소견이 나타날 수 있습니다."
            ],
            "integration": [
                "대칭성 팔다리 약화, 반사 소실, 여러 신경의 F파 이상과 전도 지연을 종합하면 말이집탈락성 다발신경병증을 고려합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "기얭-바레증후군",
                "why_consider": "급성 진행성 약화와 반사 소실이 있으면 중요한 감별입니다.",
                "how_to_differentiate": "수일에서 수주 이내 급성 진행, 호흡근 약화, 자율신경 증상이 있으면 즉시 의학적 평가가 필요합니다.",
                "practical_tip": "급성 진행성 양측 약화는 물리치료 전에 의학적 안전 확인이 우선입니다."
            },
            {
                "name": "근육병증",
                "why_consider": "근위부 약화가 두드러지면 혼동될 수 있습니다.",
                "how_to_differentiate": "근육병증은 감각저하와 전반적 반사 소실, F파 이상이 덜 전형적입니다.",
                "practical_tip": "근력만 보지 말고 감각, 반사, 신경전도검사를 함께 해석하세요."
            }
        ]
    },

    # =========================================================
    # 12. 뇌졸중 후 경직 평가
    # =========================================================
    "뇌졸중 후 발목 발바닥굽힘근 경직": {
        "patient": {
            "age": 68,
            "sex": "남",
            "side": "우",
            "symptoms": [
                "뇌졸중 후 우측 발목 경직 증가",
                "보행 시 발끝 끌림과 발꿈치안쪽휜들린발 경향",
                "빠르게 걸을 때 발목 발바닥굽힘근 과긴장 증가"
            ],
            "physical_exam": {
                "감각 검사": [
                    "우측 편마비에 동반된 감각 둔화 가능"
                ],
                "맨손 근력검사": [
                    "우측 발목 등굽힘 약화",
                    "발목 선택적 조절 저하"
                ],
                "반사 검사": [
                    "아킬레스힘줄반사 항진",
                    "발목간대경련 관찰 가능",
                    "수정 애쉬워스척도 증가"
                ]
            }
        },
        "findings": {
            "H 반사 (우)": (NCS_NORMAL, H_REFLEX_HYPERACTIVE),
            "H/M 비율": (NCS_NORMAL, H_M_RATIO_INCREASED)
        },
        "teaching_diagnosis": {
            "summary": "뇌졸중 후 위운동신경세포 손상에 따른 경직 증가 평가 사례입니다.",
            "ncs_reason": [
                "이 사례는 일반 감각·운동신경전도검사보다 H반사와 H/M 비율 해석이 중요합니다.",
                "H반사 항진 또는 H/M 비율 증가는 척수반사 흥분성 증가를 시사할 수 있습니다."
            ],
            "emg_reason": [
                "침근전도검사는 말초 탈신경 확인에 쓰이지만, 이 사례의 핵심은 경직과 반사 흥분성 평가입니다."
            ],
            "integration": [
                "뇌졸중 병력, 반사 항진, 발목간대경련, H반사 항진을 종합하면 중추성 경직 증가와 관련된 소견으로 해석할 수 있습니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "S1 허리 신경뿌리병증",
                "why_consider": "H반사는 S1 경로 평가에도 사용됩니다.",
                "how_to_differentiate": "S1 신경뿌리병증에서는 H반사 지연 또는 소실과 아킬레스힘줄반사 저하가 더 전형적입니다.",
                "practical_tip": "말초 병변은 반사 저하, 중추성 경직은 반사 항진 방향으로 생각해 보세요."
            },
            {
                "name": "발목관절 구축",
                "why_consider": "발목 움직임 제한과 보행 이상이 경직처럼 보일 수 있습니다.",
                "how_to_differentiate": "수동 관절가동범위, 속도 의존성 저항, 근긴장 양상을 함께 평가합니다.",
                "practical_tip": "경직과 구축은 중재 전략이 다르므로 반드시 구분해야 합니다."
            }
        ]
    },

    # =========================================================
    # 13. 얼굴신경/눈깜빡반사
    # =========================================================
    "눈 주위 불편감과 눈깜빡반사 이상": {
        "patient": {
            "age": 62,
            "sex": "여",
            "side": "우",
            "symptoms": [
                "우측 눈 주위 불편감",
                "우측 이마와 눈 주위 감각 둔화",
                "눈깜빡반사 경로 평가 위해 검사 시행"
            ],
            "physical_exam": {
                "감각 검사": [
                    "우측 삼차신경 첫째가지 영역 감각 둔화 가능"
                ],
                "맨손 근력검사": [
                    "눈 감기 근력은 비교적 보존 가능"
                ],
                "반사 검사": [
                    "우측 각막반사 저하 의심"
                ]
            }
        },
        "findings": {
            "우측 자극-우측 R1": (BLINK_DELAYED, ""),
            "우측 자극-우측 R2": (BLINK_DELAYED_ABSENT, ""),
            "우측 자극-좌측 R2": (BLINK_DELAYED_ABSENT, ""),
            "좌측 자극-좌측 R1": (NCS_NORMAL, ""),
            "좌측 자극-좌측 R2": (NCS_NORMAL, ""),
            "좌측 자극-우측 R2": (NCS_NORMAL, "")
        },
        "teaching_diagnosis": {
            "summary": "우측 삼차신경 들신경 경로 이상을 시사하는 눈깜빡반사 패턴입니다.",
            "ncs_reason": [
                "우측 자극 시 양측 반응이 비정상이고 좌측 자극 시 반응은 보존됩니다.",
                "이는 자극을 받아들이는 우측 삼차신경 들신경 경로 이상을 시사합니다."
            ],
            "emg_reason": [
                "이 사례는 침근전도검사보다 반사 회로 해석이 핵심입니다."
            ],
            "integration": [
                "우측 얼굴 감각저하와 우측 자극 시 눈깜빡반사 이상을 종합하면 우측 삼차신경 들신경 경로 이상을 고려합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "우측 얼굴신경병증",
                "why_consider": "눈 감기 약화와 눈 주위 불편감이 겹칠 수 있습니다.",
                "how_to_differentiate": "얼굴신경 날신경 경로 문제라면 좌측 자극 시 우측 R2도 이상해질 수 있습니다.",
                "practical_tip": "어느 쪽을 자극했을 때 어느 쪽 반응이 이상한지 나누어 해석하세요."
            }
        ]
    },

    # =========================================================
    # 14. 운동신경세포질환 red flag 교육 사례
    # =========================================================
    "진행성 근력저하와 근육다발수축": {
        "patient": {
            "age": 59,
            "sex": "남",
            "side": "양측",
            "symptoms": [
                "수개월 동안 진행하는 손과 다리 근력저하",
                "근육이 꿈틀거리는 느낌",
                "감각저하는 뚜렷하지 않음"
            ],
            "physical_exam": {
                "감각 검사": [
                    "객관적 감각저하는 뚜렷하지 않음"
                ],
                "맨손 근력검사": [
                    "상지와 하지 여러 부위의 비대칭적 근력저하",
                    "손 자체근 위축 가능"
                ],
                "반사 검사": [
                    "일부 반사는 항진될 수 있음",
                    "병적반사 확인 필요"
                ]
            }
        },
        "findings": {
            "정중신경 감각신경활동전위 (Median SNAP)": (NCS_NORMAL, NCS_NORMAL),
            "자신경 감각신경활동전위 (Ulnar SNAP)": (NCS_NORMAL, NCS_NORMAL),
            "장딴지신경 감각신경활동전위 (Sural SNAP)": (NCS_NORMAL, NCS_NORMAL),
            "첫째등쪽뼈사이근 (First Dorsal Interosseous, FDI)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "짧은엄지벌림근 (Abductor Pollicis Brevis, APB)": (EMG_NORMAL, EMG_FASCICULATION),
            "앞정강근 (Tibialis Anterior, TA)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "장딴지근 (Gastrocnemius)": (EMG_NORMAL, EMG_CHRONIC_NEUROGENIC)
        },
        "teaching_diagnosis": {
            "summary": "운동신경세포질환 가능성을 반드시 의학적으로 평가해야 하는 red flag 사례입니다.",
            "ncs_reason": [
                "감각신경활동전위가 보존되면서 여러 부위의 운동계 이상이 나타납니다.",
                "감각신경 이상이 뚜렷하지 않은 점은 다발신경병증과 다른 단서가 될 수 있습니다."
            ],
            "emg_reason": [
                "여러 부위에서 활동성 탈신경, 만성 신경원성 변화, 근육다발수축전위가 함께 나타날 수 있습니다.",
                "이러한 소견은 단일 신경뿌리병증이나 단일 말초신경병증으로 설명하기 어렵습니다."
            ],
            "integration": [
                "진행성 근력저하, 감각 보존, 광범위 신경원성 변화, 근육다발수축이 있으면 즉시 전문의 평가가 필요합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "다발 목·허리 신경뿌리병증",
                "why_consider": "여러 부위 근력저하와 탈신경 소견이 겹칠 수 있습니다.",
                "how_to_differentiate": "영상, 임상 경과, 감각 증상, 상위운동신경세포 징후, 침범 분포를 종합해야 합니다.",
                "practical_tip": "물리치료사는 진행성 약화와 근육다발수축을 red flag로 인식하고 의학적 평가를 우선해야 합니다."
            }
        ]
    },
}

from data.case_physical_exam_overrides import apply_physical_exam_overrides
apply_physical_exam_overrides(CASE_LIBRARY)
