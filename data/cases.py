# data/cases.py

"""
물리치료학과 학생 교육용 대표 전기진단 사례 라이브러리.

주의:
- 본 자료는 교육용 예시입니다.
- 신경전도검사 정상범위는 장비, 검사실, 피부온도, 나이, 키, 팔다리 길이,
  자극/기록 위치에 따라 달라질 수 있습니다.
- 실제 임상 판단은 환자의 병력, 진찰, 영상검사, 검사실 기준을
  종합하여 전문 의료진의 판단하에 이루어져야 합니다.
"""

EMG_NORMAL = "휴식 시 전기적 침묵(no motor unit action potential, MUAP), 수의수축 시 정상 운동단위전위(MUAP) 동원"

EMG_ACTIVE_DENERVATION = "휴식 시 섬유자발전위(fibrillation potential) 및 양성예파(positive sharp wave) 관찰, 수의수축 시 운동단위전위(MUAP) 동원 감소 가능"

EMG_PARASPINAL_DENERVATION = "휴식 시 섬유자발전위(fibrillation potential) 및 양성예파(positive sharp wave) 관찰"

EMG_FASCICULATION = "휴식 시 근육다발수축전위(fasciculation potential) 관찰 가능"

NCS_NORMAL = "정상 범위(within normal limits)"
NCS_DELAYED = "잠복기 지연(delayed latency)"
NCS_REDUCED = "진폭 감소(reduced amplitude)"
NCS_ABSENT = "반응 소실(absent response)"
FWAVE_DELAYED_ABSENT = "F파 최소잠복기 지연 또는 소실(delayed or absent F-wave)"
H_REFLEX_HYPERACTIVE = "H-반사 항진 또는 문턱값 감소(hyperactive H-reflex / lower threshold)"
H_M_RATIO_INCREASED = "H/M 비율 증가 가능(increased H/M ratio possible)"
BLINK_DELAYED = "잠복기 지연(delayed latency)"
BLINK_DELAYED_ABSENT = "잠복기 지연 또는 반응 소실(delayed or absent response)"


CASE_LIBRARY = {
    "목-팔 통증 증상과 팔 근력 약화": {
        "patient": {
            "age": 57,
            "sex": "남",
            "side": "우",
            "symptoms": [
                "뒷목에서 오른쪽 어깨와 아래팔 노쪽(radial side), 엄지 쪽으로 뻗치는 통증과 저림이 지속됨",
                "최근 팔꿉관절 굽힘과 손목관절 폄 동작 시 힘이 빠지는 현상 발생"
            ],
            "physical_exam": {
                "감각 검사": [
                    "아래팔 노쪽 및 엄지/검지 쪽 감각 저하. C6 피부분절(dermatome) 분포와 잘 맞음"
                ],
                "맨손 근력검사(MMT)": [
                    "팔꿉관절 굽힘(Elbow flexion): Fair (3/5) - 위팔두갈래근(Biceps brachii), 근육피부신경(Musculocutaneous nerve), C5-C6 우세",
                    "손목관절 폄(Wrist extension): Fair (3/5) - 긴/짧은노쪽손목폄근(Extensor carpi radialis longus/brevis), 노신경(Radial nerve), C6 우세",
                    "팔꿉관절 폄(Elbow extension): Normal (5/5) - 위팔세갈래근(Triceps brachii), 노신경(Radial nerve), C7 우세 보존"
                ],
                "반사 검사": [
                    "위팔노근 반사(Brachioradialis reflex, C6): 감소(DRT 1+)",
                    "위팔두갈래근 반사(Biceps reflex, C5): 정상(DRT 2+) 또는 경미한 감소",
                    "위팔세갈래근 반사(Triceps reflex, C7): 정상(DRT 2+)"
                ]
            }
        },
        "findings": {
            "노신경 표재감각신경활동전위 (Superficial Radial SNAP)": (NCS_NORMAL, NCS_NORMAL),
            "가쪽아래팔피부신경 감각신경활동전위 (Lateral Antebrachial Cutaneous SNAP)": (NCS_NORMAL, NCS_NORMAL),
            "근육피부신경 복합근육활동전위 (Musculocutaneous CMAP)": (NCS_NORMAL, NCS_NORMAL),
            "노신경 복합근육활동전위 (Radial CMAP)": (NCS_NORMAL, NCS_NORMAL),
            "목 척추주위근 (Cervical Paraspinal)": (EMG_NORMAL, EMG_PARASPINAL_DENERVATION),
            "위팔두갈래근 (Biceps Brachii)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "노쪽손목폄근 (Extensor Carpi Radialis)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION)
        },
        "teaching_diagnosis": {
            "summary": "C6 중심의 목 신경뿌리병증(cervical radiculopathy) 패턴입니다.",
            "ncs_reason": [
                "감각신경활동전위(SNAP)가 정상 범위로 보존됩니다. 신경뿌리병증은 병변이 뒤뿌리신경절(dorsal root ganglion, DRG)보다 몸쪽에 있어 말초 감각신경전도가 정상 범위일 수 있습니다.",
                "노신경(radial nerve)과 근육피부신경(musculocutaneous nerve)의 말단 운동신경전도(CMAP)가 정상 범위이므로 말초 단일신경병증(mononeuropathy) 가능성은 낮습니다."
            ],
            "emg_reason": [
                "목 척추주위근(cervical paraspinal muscle)에서 섬유자발전위(fibrillation potential)와 양성예파(positive sharp wave)가 관찰되면 신경뿌리 수준 병변을 강하게 시사합니다.",
                "서로 다른 말초신경 지배를 받지만 C6 분절을 공유하는 근육에서 탈신경근(denervated muscle) 소견이 함께 나타납니다.",
                "섬유자발전위와 양성예파는 비정상 자발전위(abnormal spontaneous activity)로, 축삭 손상(axonal injury) 또는 진행된 신경뿌리 손상을 시사합니다."
            ],
            "integration": [
                "C6 피부분절 증상, C6 우세 근력 약화, 위팔노근 반사 저하, 척추주위근 침범을 종합하면 C6 목 신경뿌리병증으로 해석하는 것이 적절합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "노신경병증(Radial neuropathy)",
                "why_consider": "손목관절 폄 약화와 노쪽 감각 이상이 동반되어 혼동될 수 있습니다.",
                "how_to_differentiate": "말초 노신경병증이라면 표재노신경 감각신경전도(SNAP) 진폭 감소가 나타날 수 있고 척추주위근은 정상이어야 합니다. 본 사례는 감각신경전도 (SNAP) 보존과 척추주위근 탈신경 소견이 있어 신경뿌리병증에 가깝습니다.",
                "practical_tip": "손목 폄 약화가 있더라도 감각신경전도 (SNAP) 보존 여부와 척추주위근 침범 여부를 함께 확인하세요."
            }
        ]
    },

    "야간 손저림과 엄지 근력 약화": {
        "patient": {
            "age": 46,
            "sex": "여",
            "side": "우",
            "symptoms": [
                "오른손 1, 2, 3번째 손가락 중심의 저림이 야간에 특히 심함",
                "최근 병을 따거나 물건을 쥘 때 엄지손가락의 힘이 부족함을 느낌"
            ],
            "physical_exam": {
                "감각 검사": [
                    "엄지, 검지, 중지 및 반지손가락 노쪽 절반의 손바닥쪽 감각 둔화. 정중신경(median nerve) 분포와 일치"
                ],
                "맨손 근력검사(MMT)": [
                    "엄지손가락 벌림(Thumb abduction): Good (4/5) - 짧은엄지벌림근(Abductor pollicis brevis), 정중신경(Median nerve), T1 우세"
                ],
                "반사 검사": [
                    "위팔두갈래근(C5), 위팔노근(C6), 위팔세갈래근(C7) 반사: 모두 대칭적 정상(DRT 2+)",
                    "특수 검사: 팔렌 검사(Phalen test), 손목 티넬징후(Tinel sign) 양성"
                ]
            }
        },
        "findings": {
            "정중신경 감각신경활동전위 (Median SNAP)": (NCS_NORMAL, NCS_DELAYED),
            "정중신경 복합근육활동전위 (Median CMAP)": (NCS_NORMAL, NCS_DELAYED),
            "짧은엄지벌림근 (Abductor Pollicis Brevis, APB)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION)
        },
        "teaching_diagnosis": {
            "summary": "손목굴증후군(carpal tunnel syndrome)을 시사하는 정중신경 포착병증(median entrapment neuropathy)입니다.",
            "ncs_reason": [
                "정중신경 감각신경전도(SNAP)와 운동신경전도(CMAP)에서 잠복기 지연이 관찰되어 손목굴(carpal tunnel) 부위의 국소 전도 지연을 시사합니다.",
                "잠복기 지연은 일반적으로 말이집탈락성 변화(demyelinating change) 또는 국소 포착에 의한 전도 지연을 반영합니다."
            ],
            "emg_reason": [
                "짧은엄지벌림근(APB)에서 섬유자발전위와 양성예파가 관찰되면 단순 전도 지연을 넘어 운동축삭 손상(axonal injury)이 동반되었을 가능성을 시사합니다.",
                "침근전도에서 휴식 시 비정상 자발전위가 보이면 탈신경근 소견으로 해석합니다."
            ],
            "integration": [
                "야간 손저림, 정중신경 분포 감각저하, 엄지 벌림 약화, 정중신경 특이적 잠복기 지연을 종합하면 손목굴증후군으로 판단할 수 있습니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "근위부 정중신경병증(Proximal median neuropathy)",
                "why_consider": "정중신경 지배 영역의 감각 이상과 엄지 근력 약화가 비슷하게 나타날 수 있습니다.",
                "how_to_differentiate": "원엎침근(pronator teres) 등 손목보다 몸쪽의 정중신경 지배근이 보존되면 손목굴 수준 병변 가능성이 높습니다.",
                "practical_tip": "정중신경병증에서는 어느 지점보다 먼쪽 근육부터 침범되는지 확인해 포착 위치를 추정하세요."
            }
        ]
    },

    "위팔뼈 몸통 골절 후 손목처짐": {
        "patient": {
            "age": 34,
            "sex": "남",
            "side": "우",
            "symptoms": [
                "위팔뼈 몸통 골절(humeral shaft fracture) 병력",
                "이후 손목과 손가락을 들어 올리지 못하는 손목처짐(wrist drop) 발생"
            ],
            "physical_exam": {
                "감각 검사": [
                    "손등 노쪽 부위 감각 소실. 표재노신경(superficial radial nerve) 분포"
                ],
                "맨손 근력검사(MMT)": [
                    "손목관절 폄(Wrist extension): Poor (2/5) - 노쪽손목폄근(Extensor carpi radialis), 노신경(Radial nerve), C6 우세",
                    "손가락 폄(Finger extension): Poor (2/5) - 손가락폄근(Extensor digitorum), 노신경(Radial nerve), C7 우세",
                    "팔꿉관절 폄(Elbow extension): Normal (5/5) - 위팔세갈래근(Triceps brachii), 노신경(Radial nerve), C7 우세 보존"
                ],
                "반사 검사": [
                    "위팔세갈래근 반사(Triceps reflex, C7): 정상(DRT 2+)",
                    "위팔노근 반사(Brachioradialis reflex, C6): 감소(DRT 1+)"
                ]
            }
        },
        "findings": {
            "노신경 표재감각신경활동전위 (Superficial Radial SNAP)": (NCS_NORMAL, NCS_REDUCED),
            "노신경 복합근육활동전위 (Radial CMAP)": (NCS_NORMAL, NCS_REDUCED),
            "노쪽손목폄근 (Extensor Carpi Radialis)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "집게폄근 (Extensor Indicis Proprius, EIP)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "목 척추주위근 (Cervical Paraspinal)": (EMG_NORMAL, EMG_NORMAL)
        },
        "teaching_diagnosis": {
            "summary": "위팔뼈 나선고랑(spiral groove) 부위 노신경병증(radial neuropathy) 패턴입니다.",
            "ncs_reason": [
                "표재노신경 감각신경전도(SNAP) 진폭 감소는 말초 감각신경이 병변에 포함되었음을 의미합니다.",
                "노신경 운동신경전도 (CMAP) 진폭 감소는 운동축삭 손상 또는 심한 전도차단 가능성을 시사합니다."
            ],
            "emg_reason": [
                "노신경 지배 원위부 근육에서 섬유자발전위와 양성예파가 관찰되므로 탈신경근 소견이 있습니다.",
                "목 척추주위근이 정상 범위이므로 C7 신경뿌리병증보다는 말초 노신경병증에 가깝습니다."
            ],
            "integration": [
                "위팔뼈 골절 병력, 위팔세갈래근 보존, 손목/손가락 폄 약화, 표재노신경 감각신경전도(SNAP) 감소를 종합하면 나선고랑 부위 노신경병증이 적절합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "뒤뼈사이신경병증(Posterior interosseous neuropathy, PIN)",
                "why_consider": "손목과 손가락 폄 약화가 비슷하게 보일 수 있습니다.",
                "how_to_differentiate": "뒤뼈사이신경은 주로 운동가지이므로 감각 소실과 표재노신경 감각신경전도 (SNAP) 감소가 없어야 합니다. 본 사례는 감각 이상과 감각신경전도 (SNAP) 감소가 있어 노신경 본줄기 손상입니다.",
                "practical_tip": "손목처짐 환자에서 감각 이상이 있으면 운동가지 단독 손상보다 혼합신경 손상을 먼저 고려하세요."
            }
        ]
    },

    "4, 5번째 손가락 저림과 손가락 근력 약화": {
        "patient": {
            "age": 42,
            "sex": "남",
            "side": "우",
            "symptoms": [
                "오른쪽 4번째, 5번째 손가락 저림과 손날쪽 불편감",
                "젓가락질 등 세밀한 손동작에서 손가락을 모으기 어렵고 힘이 빠짐"
            ],
            "physical_exam": {
                "감각 검사": [
                    "반지손가락 자쪽 절반 및 새끼손가락 감각 저하. 자신경(ulnar nerve) 영역"
                ],
                "맨손 근력검사(MMT)": [
                    "새끼손가락 벌림(Little finger abduction): Fair (3/5) - 새끼벌림근(Abductor digiti minimi), 자신경(Ulnar nerve), T1 우세",
                    "손가락 벌림/모음(Finger abduction/adduction): Fair (3/5) - 뼈사이근(Interossei), 자신경(Ulnar nerve), T1 우세"
                ],
                "반사 검사": [
                    "위팔두갈래근(C5), 위팔노근(C6), 위팔세갈래근(C7) 반사: 대칭적 정상(DRT 2+)",
                    "특수 검사: 팔꿉관절 굽힘 검사 양성, 팔꿈치 자쪽 티넬징후 양성"
                ]
            }
        },
        "findings": {
            "자신경 감각신경활동전위 (Ulnar SNAP)": (NCS_NORMAL, NCS_DELAYED),
            "자신경 복합근육활동전위 (Ulnar CMAP)": (NCS_NORMAL, NCS_DELAYED),
            "새끼벌림근 (Abductor Digiti Minimi, ADM)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "첫째등쪽뼈사이근 (First Dorsal Interosseous, FDI)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION)
        },
        "teaching_diagnosis": {
            "summary": "팔꿉굴증후군(cubital tunnel syndrome)으로 대표되는 팔꿈치 부위 자신경병증(ulnar neuropathy)입니다.",
            "ncs_reason": [
                "자신경 감각신경전도 (SNAP)와 운동신경전도 (CMAP)에서 잠복기 지연이 나타나 팔꿈치 부위 국소 포착성 전도 지연을 시사합니다.",
                "감각신경 이상이 동반되어 C8-T1 신경뿌리병증보다 말초 자신경병증에 더 가깝습니다."
            ],
            "emg_reason": [
                "새끼벌림근과 첫째등쪽뼈사이근에서 섬유자발전위와 양성예파가 관찰되면 자신경 지배 손 자체기원근의 탈신경근 소견입니다.",
                "이는 포착이 심해져 운동축삭 손상이 동반되었을 가능성을 시사합니다."
            ],
            "integration": [
                "자신경 감각 영역 저림, 손 자체기원근 약화, 자신경 전도 지연, 자신경 지배근 탈신경 소견을 종합하면 팔꿈치 부위 자신경병증이 적절합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "C8-T1 목 신경뿌리병증(C8-T1 cervical radiculopathy)",
                "why_consider": "손 자체기원근 약화가 공통적으로 나타날 수 있습니다.",
                "how_to_differentiate": "신경뿌리병증은 감각신경전도 (SNAP)가 보존되는 경우가 많고, 정중신경 지배근도 함께 침범될 수 있습니다. 본 사례는 자신경 영역에 국한된 감각신경전도/운동신경전도(SNAP/CMAP) 이상이 핵심입니다.",
                "practical_tip": "같은 T1 분절인지, 같은 자신경 지배인지 구분하여 근육을 묶어 해석하세요."
            }
        ]
    },

    "허리-다리 통증과 발처짐": {
        "patient": {
            "age": 61,
            "sex": "여",
            "side": "우",
            "symptoms": [
                "허리에서 우측 엉치, 종아리 가쪽, 발등으로 뻗치는 방사통과 저림",
                "최근 보행 시 발끝이 바닥에 끌리는 발처짐(foot drop) 발생"
            ],
            "physical_exam": {
                "감각 검사": [
                    "종아리 가쪽 및 발등 중앙 부위 감각 둔화. L5 피부분절 분포"
                ],
                "맨손 근력검사(MMT)": [
                    "발목관절 등굽힘(Ankle dorsiflexion): Fair (3/5) - 앞정강근(Tibialis anterior), 깊은종아리신경(Deep peroneal nerve), L4-L5",
                    "엄지발가락 폄(Great toe extension): Poor (2/5) - 긴엄지폄근(Extensor hallucis longus), 깊은종아리신경(Deep peroneal nerve), L5 우세",
                    "엉덩관절 벌림(Hip abduction): Good (4/5) - 중간볼기근(Gluteus medius), 위볼기신경(Superior gluteal nerve), L5 우세"
                ],
                "반사 검사": [
                    "무릎반사(Patellar reflex, L4): 정상(DRT 2+)",
                    "아킬레스힘줄반사(Achilles tendon reflex, S1): 정상(DRT 2+)"
                ]
            }
        },
        "findings": {
            "얕은종아리신경 감각신경활동전위 (Superficial Peroneal SNAP)": (NCS_NORMAL, NCS_NORMAL),
            "종아리신경 복합근육활동전위 (Peroneal CMAP)": (NCS_NORMAL, NCS_NORMAL),
            "허리 척추주위근 (Lumbar Paraspinal)": (EMG_NORMAL, EMG_PARASPINAL_DENERVATION),
            "앞정강근 (Tibialis Anterior, TA)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "긴엄지폄근 (Extensor Hallucis Longus, EHL)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "중간볼기근 (Gluteus Medius)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION)
        },
        "teaching_diagnosis": {
            "summary": "발처짐을 동반한 L5 허리 신경뿌리병증(L5 lumbar radiculopathy) 패턴입니다.",
            "ncs_reason": [
                "얕은종아리신경 SNAP가 정상 범위이면 병변이 말초 감각신경보다 몸쪽, 즉 신경뿌리 수준일 가능성을 지지합니다.",
                "종아리신경 운동신경전도 (CMAP)가 정상 범위이므로 온종아리신경병증보다는 L5 신경뿌리병증을 우선 고려합니다."
            ],
            "emg_reason": [
                "앞정강근, 긴엄지폄근, 중간볼기근은 서로 다른 말초신경 지배를 받지만 L5 분절을 공유합니다.",
                "허리 척추주위근 탈신경 소견은 신경뿌리병증을 지지하는 중요한 단서입니다.",
                "섬유자발전위와 양성예파는 탈신경근 소견으로 축삭 손상을 동반한 신경뿌리 침범을 시사합니다."
            ],
            "integration": [
                "L5 방사통, L5 우세 근력 약화, 감각신경전도 (SNAP) 보존, 척추주위근 침범을 종합하면 L5 허리 신경뿌리병증이 적절합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "온종아리신경병증(Common peroneal neuropathy)",
                "why_consider": "발목 등굽힘 약화와 발처짐(foot drop)이 공통적으로 나타납니다.",
                "how_to_differentiate": "온종아리신경병증에서는 얕은종아리신경 감각신경전도 (SNAP) 감소, 종아리신경 운동신경전도 (CMAP) 감소가 흔하며 중간볼기근과 척추주위근은 정상이어야 합니다.",
                "practical_tip": "발처짐 환자는 엉덩관절 벌림과 발목 안쪽번짐(inversion)을 함께 평가하여 L5 신경뿌리병증과 종아리신경병증을 구분하세요."
            }
        ]
    },

    "정강뼈 골절로 석고붕대 후 발처짐과 발등 감각저하": {
        "patient": {
            "age": 31,
            "sex": "남",
            "side": "좌",
            "symptoms": [
                "정강뼈 골절(tibial fracture) 후 석고붕대 유지",
                "석고붕대 제거 직후 좌측 발처짐과 발등 감각 소실 발견"
            ],
            "physical_exam": {
                "감각 검사": [
                    "종아리 가쪽 및 발등 부위 감각 소실. 얕은/깊은종아리신경 분포"
                ],
                "맨손 근력검사(MMT)": [
                    "발목관절 등굽힘(Ankle dorsiflexion): Poor (2/5) - 앞정강근(Tibialis anterior), 깊은종아리신경(Deep peroneal nerve), L4-L5",
                    "엄지발가락 폄(Great toe extension): Trace (1/5) - 긴엄지폄근(Extensor hallucis longus), 깊은종아리신경(Deep peroneal nerve), L5 우세",
                    "발목관절 가쪽번짐(Ankle eversion): Poor (2/5) - 긴종아리근(Peroneus longus), 얕은종아리신경(Superficial peroneal nerve), L5 우세",
                    "발목관절 안쪽번짐(Ankle inversion): Normal (5/5) - 뒤정강근(Tibialis posterior), 정강신경(Tibial nerve), L5 지배 보존"
                ],
                "반사 검사": [
                    "무릎반사(Patellar reflex, L4): 대칭적 정상(DRT 2+)",
                    "아킬레스힘줄반사(Achilles tendon reflex, S1): 대칭적 정상(DRT 2+)"
                ]
            }
        },
        "findings": {
            "얕은종아리신경 감각신경활동전위 (Superficial Peroneal SNAP)": (NCS_NORMAL, NCS_REDUCED),
            "종아리신경 복합근육활동전위 (Peroneal 운동신경전도 (CMAP))": (NCS_NORMAL, NCS_REDUCED),
            "앞정강근 (Tibialis Anterior, TA)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "긴종아리근 (Peroneus Longus)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "허리 척추주위근 (Lumbar Paraspinal)": (EMG_NORMAL, EMG_NORMAL)
        },
        "teaching_diagnosis": {
            "summary": "종아리뼈머리 부위 압박으로 인한 온종아리신경병증(common peroneal neuropathy)입니다.",
            "ncs_reason": [
                "얕은종아리신경 감각신경전도 (SNAP) 진폭 감소는 말초 감각신경 손상을 의미합니다.",
                "종아리신경 운동신경전도 (CMAP) 진폭 감소는 운동축삭 손상 또는 심한 압박성 전도장애를 시사합니다."
            ],
            "emg_reason": [
                "앞정강근과 긴종아리근 모두에서 섬유자발전위와 양성예파가 관찰되므로 깊은/얕은종아리신경 분기 전 병변을 시사합니다.",
                "허리 척추주위근이 정상 범위이므로 L5 신경뿌리병증 가능성은 낮습니다."
            ],
            "integration": [
                "석고붕대 압박 병력, 종아리신경 지배근 약화, 발목 안쪽번짐 보존, 감각신경전도/운동신경전도(SNAP/CMAP) 감소를 종합하면 온종아리신경병증이 적절합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "L5 허리 신경뿌리병증(L5 lumbar radiculopathy)",
                "why_consider": "발처짐과 L5 관련 근력 약화가 비슷합니다.",
                "how_to_differentiate": "L5 신경뿌리병증은 감각신경전도 (SNAP)가 보존되고 척추주위근 침범이 나타날 수 있습니다. 본 사례는 감각신경전도 (SNAP) 감소와 척추주위근 정상 소견이 핵심입니다.",
                "practical_tip": "발처짐에서 발목 안쪽번짐(inversion)이 정상이라면 종아리신경병증 가능성을 강하게 고려하세요."
            }
        ]
    },

    "골반 외상 후 다리 전반 근력 약화": {
        "patient": {
            "age": 45,
            "sex": "여",
            "side": "좌",
            "symptoms": [
                "골반 골절(pelvic fracture) 수술 후 좌측 다리 전반의 심한 근력 약화 발생",
                "허벅지부터 종아리, 발등까지 광범위한 감각 둔화와 보행장애 호소"
            ],
            "physical_exam": {
                "감각 검사": [
                    "허벅지, 종아리, 발등 등 여러 피부분절을 넘는 광범위 감각 소실"
                ],
                "맨손 근력검사(MMT)": [
                    "엉덩관절 굽힘(Hip flexion): Poor (2/5) - 엉덩허리근(Iliopsoas), 넙다리신경(Femoral nerve), L2 우세",
                    "무릎관절 폄(Knee extension): Poor (2/5) - 넙다리네갈래근(Quadriceps femoris), 넙다리신경(Femoral nerve), L3-L4",
                    "발목관절 등굽힘(Ankle dorsiflexion): Trace (1/5) - 앞정강근(Tibialis anterior), 깊은종아리신경(Deep peroneal nerve), L4-L5",
                    "발목관절 발바닥굽힘(Ankle plantarflexion): Poor (2/5) - 장딴지근(Gastrocnemius), 정강신경(Tibial nerve), S1 우세"
                ],
                "반사 검사": [
                    "무릎반사(Patellar reflex, L4): 좌측 완전 소실(DRT 0)",
                    "아킬레스힘줄반사(Achilles tendon reflex, S1): 좌측 완전 소실(DRT 0)"
                ]
            }
        },
        "findings": {
            "허리 척추주위근 (Lumbar Paraspinal)": (EMG_NORMAL, EMG_NORMAL),
            "장딴지신경 감각신경활동전위 (Sural SNAP)": (NCS_NORMAL, NCS_REDUCED),
            "종아리신경 복합근육활동전위 (Peroneal CMAP)": (NCS_NORMAL, NCS_REDUCED),
            "넙다리신경 복합근육활동전위 (Femoral CMAP)": (NCS_NORMAL, NCS_REDUCED),
            "가쪽넓은근 (Vastus Lateralis)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION),
            "앞정강근 (Tibialis Anterior, TA)": (EMG_NORMAL, EMG_ACTIVE_DENERVATION)
        },
        "teaching_diagnosis": {
            "summary": "외상과 관련된 허리엉치신경얼기병증(lumbosacral plexopathy) 패턴입니다.",
            "ncs_reason": [
                "장딴지신경 감각신경전도 (SNAP), 종아리신경 운동신경전도 (CMAP), 넙다리신경 운동신경전도 (CMAP) 등 여러 말초신경에서 진폭 감소가 관찰됩니다.",
                "감각신경활동전위 감소는 병변이 뒤뿌리신경절보다 먼쪽, 즉 신경얼기 또는 말초신경 수준임을 시사합니다."
            ],
            "emg_reason": [
                "넙다리신경 지배근과 종아리신경 지배근에서 탈신경근 소견이 함께 나타납니다.",
                "허리 척추주위근이 정상 범위이면 다발 신경뿌리병증보다 신경얼기병증 가능성이 높습니다.",
                "섬유자발전위(fibrillation potential)와 양성예파(positive sharp wave)는 축삭 손상을 동반한 신경얼기 손상을 시사합니다."
            ],
            "integration": [
                "골반 외상 병력, 여러 말초신경 영역의 광범위 약화, 간각신경/운동신경전도(SNAP/CMAP) 감소, 척추주위근 보존을 종합하면 허리엉치신경얼기병증이 적절합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "다발 허리 신경뿌리병증(Multiple lumbar radiculopathy)",
                "why_consider": "여러 분절의 근력 약화와 반사 소실이 나타날 수 있습니다.",
                "how_to_differentiate": "다발 신경뿌리병증은 감각신경전도 (SNAP)가 보존되고 척추주위근 이상이 동반되는 경우가 많습니다. 본 사례는 감각신경전도 (SNAP) 감소와 척추주위근 보존이 핵심입니다.",
                "practical_tip": "광범위 다리 약화에서는 감각신경전도 (SNAP)와 척추주위근 침범 여부가 신경뿌리와 신경얼기 감별에 중요합니다."
            }
        ]
    },

    "양측 발끝 저림과 발가락 약화": {
        "patient": {
            "age": 67,
            "sex": "남",
            "side": "양측",
            "symptoms": [
                "오랜 기간 당뇨병 병력",
                "양쪽 발끝에서 시작해 발목 위로 서서히 올라오는 대칭성 저림과 감각 둔화"
            ],
            "physical_exam": {
                "감각 검사": [
                    "양측 발가락 끝부터 발목 상부까지 장갑-양말형(glove-stocking distribution) 대칭성 감각 저하"
                ],
                "맨손 근력검사(MMT)": [
                    "양측 엄지발가락 폄(Great toe extension): Good (4/5) - 긴엄지폄근(Extensor hallucis longus), 깊은종아리신경(Deep peroneal nerve), L5 우세",
                    "양측 발가락 굽힘(Toe flexion): Good (4/5) - 긴발가락굽힘근(Flexor digitorum longus), 정강신경(Tibial nerve), S1 우세",
                    "양측 발목관절 등굽힘(Ankle dorsiflexion): Normal (5/5) - 앞정강근(Tibialis anterior), 깊은종아리신경(Deep peroneal nerve), L4-L5",
                    "양측 무릎관절 폄(Knee extension): Normal (5/5) - 넙다리네갈래근(Quadriceps femoris), 넙다리신경(Femoral nerve), L3-L4",
                    "양측 엉덩관절 굽힘(Hip flexion): Normal (5/5) - 엉덩허리근(Iliopsoas), 넙다리신경(Femoral nerve), L2 우세"
                ],
                "반사 검사": [
                    "아킬레스힘줄반사(Achilles tendon reflex, S1): 양측 소실(DRT 0)",
                    "무릎반사(Patellar reflex, L4): 양측 보존(DRT 1+~2+)"
                ]
            }
        },
        "findings": {
            "장딴지신경 감각신경활동전위 (Sural SNAP)": (NCS_REDUCED, NCS_REDUCED),
            "얕은종아리신경 감각신경활동전위 (Superficial Peroneal SNAP)": (NCS_REDUCED, NCS_REDUCED),
            "정강신경 복합근육활동전위 (Tibial CMAP)": (NCS_REDUCED, NCS_REDUCED)
        },
        "teaching_diagnosis": {
            "summary": "길이 의존성 축삭성 다발신경병증(length-dependent axonal polyneuropathy) 패턴입니다.",
            "ncs_reason": [
                "양측 원위부 감각신경과 운동신경에서 대칭성 진폭 감소가 관찰됩니다.",
                "진폭 감소가 두드러지면 축삭성 병변(axonal neuropathy)을 우선 고려합니다.",
                "길이가 긴 신경의 먼쪽부터 침범되는 양상은 당뇨병성 다발신경병증에서 흔합니다."
            ],
            "emg_reason": [
                "이 사례는 침근전도보다 신경전도검사의 대칭성 진폭 감소 패턴이 진단에 더 중요합니다.",
                "진행된 경우 원위부 근육 침근전도에서 섬유자발전위(fibrillation potential)와 양성예파(positive sharp wave)가 추가로 관찰될 수 있습니다."
            ],
            "integration": [
                "당뇨병 병력, 양측 대칭성 원위부 감각저하, 아킬레스힘줄반사 소실, 감각신경전도/운동신경전도(SNAP/CMAP) 진폭 감소를 종합하면 축삭성 다발신경병증이 적절합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "말이집탈락성 다발신경병증(Demyelinating polyneuropathy)",
                "why_consider": "대칭성 다발신경 침범이라는 점은 유사합니다.",
                "how_to_differentiate": "말이집탈락성 병변은 진폭 감소보다 잠복기 지연, 전도속도 저하, F파 이상이 더 두드러집니다.",
                "practical_tip": "다발신경병증에서는 진폭(amplitude)과 잠복기(latency) 중 어떤 이상이 주된 패턴인지 먼저 구분하세요."
            }
        ]
    },

    "대칭성 팔다리 근력저하와 보행 저하": {
        "patient": {
            "age": 55,
            "sex": "여",
            "side": "양측",
            "symptoms": [
                "몇 달간 양손과 양발이 대칭적으로 저리고 둔함",
                "계단 오르기와 발목 움직임 모두에서 진행성 근력 약화 호소"
            ],
            "physical_exam": {
                "감각 검사": [
                    "양측 상지와 하지 원위부의 대칭성 감각 저하"
                ],
                "맨손 근력검사(MMT)": [
                    "양측 어깨관절 벌림(Shoulder abduction): Fair (3/5) - 어깨세모근(Deltoid), 겨드랑신경(Axillary nerve), C5 우세",
                    "양측 엉덩관절 굽힘(Hip flexion): Fair (3/5) - 엉덩허리근(Iliopsoas), 넙다리신경(Femoral nerve), L2 우세",
                    "양측 손목관절 폄(Wrist extension): Fair (3/5) - 노쪽손목폄근(Extensor carpi radialis), 노신경(Radial nerve), C6 우세",
                    "양측 발목관절 등굽힘(Ankle dorsiflexion): Fair (3/5) - 앞정강근(Tibialis anterior), 깊은종아리신경(Deep peroneal nerve), L4-L5"
                ],
                "반사 검사": [
                    "팔/다리 깊은힘줄반사(C5, C6, C7, L4, S1): 전반적 소실(DRT 0)"
                ]
            }
        },
        "findings": {
            "정중/자신경 감각신경활동전위 (SNAP)": (NCS_DELAYED, NCS_DELAYED),
            "정중/종아리신경 복합근육활동전위 (CMAP)": (NCS_DELAYED, NCS_DELAYED),
            "정강/종아리신경 F파 (F-wave)": (FWAVE_DELAYED_ABSENT, FWAVE_DELAYED_ABSENT)
        },
        "teaching_diagnosis": {
            "summary": "만성 염증성 말이집탈락성 다발신경병증(chronic inflammatory demyelinating polyneuropathy, CIDP) 양상입니다.",
            "ncs_reason": [
                "여러 감각/운동신경에서 양측성 잠복기 지연이 나타나 광범위한 말이집탈락성 변화(demyelination)를 시사합니다.",
                "F파 지연 또는 소실은 근위부 운동신경과 신경뿌리 수준의 전도 이상을 평가하는 데 중요한 단서입니다."
            ],
            "emg_reason": [
                "말이집탈락성 질환에서는 초기 또는 주 병변이 말이집에 있기 때문에 침근전도 탈신경 소견이 뚜렷하지 않을 수 있습니다.",
                "다만 오래 진행되거나 이차 축삭 손상이 생기면 섬유자발전위(fibrillation potential)와 양성예파(positive sharp wave)가 나타날 수 있습니다."
            ],
            "integration": [
                "근위부와 원위부가 함께 약해지고, 전신 반사가 소실되며, 잠복기 지연과 F파 이상이 동반되므로 말이집탈락성 다발신경병증을 우선 고려합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "근육병증(Myopathy)",
                "why_consider": "근위부 근력 약화가 뚜렷하면 근육병증과 혼동될 수 있습니다.",
                "how_to_differentiate": "근육병증은 감각 이상이 없고 깊은힘줄반사가 상대적으로 보존되는 경우가 많습니다. 본 사례는 감각 이상과 전반적 반사 소실이 있어 신경병증(neuropathy)에 가깝습니다.",
                "practical_tip": "근위부 약화만 보지 말고 감각 이상과 반사 소실 여부를 반드시 함께 확인하세요."
            }
        ]
    },

    "눈꺼풀 떨림과 눈 주위 불편감 지속": {
        "patient": {
            "age": 62,
            "sex": "여",
            "side": "우",
            "symptoms": [
                "우측 눈꺼풀 떨림과 얼굴의 둔한 느낌이 지속됨",
                "삼차신경-뇌줄기-얼굴신경 반사 경로 평가를 위해 의뢰됨"
            ],
            "physical_exam": {
                "감각 검사": [
                    "우측 이마 및 눈 주위, 즉 삼차신경 눈신경(Ophthalmic Nerve, V1) 영역의 가벼운 터치 감각 둔화"
                ],
                "맨손 근력검사(MMT)": [
                    "우측 눈 꽉 감기(Eye closure): Good (4/5) - 눈둘레근(Orbicularis oculi), 얼굴신경(Facial nerve)",
                    "이마 주름잡기(Eyebrow elevation): Normal (5/5) - 이마근(Frontalis), 얼굴신경(Facial nerve)",
                    "입꼬리 올리기(Smiling): Normal (5/5) - 큰광대근(Zygomaticus major), 얼굴신경(Facial nerve)"
                ],
                "반사 검사": [
                    "우측 각막반사(corneal reflex) 저하 의심"
                ]
            }
        },
        "findings": {
            "우측 전기자극-우측 R1": (BLINK_DELAYED, ""),
            "우측 전기자극-우측 R2": (BLINK_DELAYED_ABSENT, ""),
            "우측 전기자극-좌측 R2": (BLINK_DELAYED_ABSENT, ""),
            "좌측 전기자극-좌측 R1": (NCS_NORMAL, ""),
            "좌측 전기자극-좌측 R2": (NCS_NORMAL, ""),
            "좌측 전기자극-우측 R2": (NCS_NORMAL, "")
        },
        "teaching_diagnosis": {
            "summary": "눈깜빡반사(blink reflex)를 통해 우측 삼차신경 들신경 경로(afferent pathway) 이상을 확인하는 사례입니다.",
            "ncs_reason": [
                "우측을 자극했을 때 우측 R1, 우측 R2, 좌측 R2가 모두 지연 또는 소실됩니다.",
                "반대로 좌측 자극 시 반응은 보존되어 있으므로 우측 얼굴신경 날신경 경로(efferent pathway)는 상대적으로 보존된 것으로 해석할 수 있습니다."
            ],
            "emg_reason": [
                "이 사례의 핵심은 침근전도보다 반사 회로 분석입니다.",
                "얼굴신경병증이 의심될 때는 얼굴근육 침근전도에서 섬유자발전위(fibrillation potential), 양성예파(positive sharp wave), 운동단위전위 동원 감소 등을 추가로 확인할 수 있습니다."
            ],
            "integration": [
                "우측 삼차신경 눈신경(Ophthalmic Nerve, V1) 감각저하와 우측 자극 시 양측 반응 이상이 일치하므로 우측 삼차신경 들신경 경로 이상으로 해석합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "우측 얼굴신경병증(Right facial neuropathy)",
                "why_consider": "눈 감기 약화와 얼굴 불편감이 있으면 얼굴신경병증을 고려할 수 있습니다.",
                "how_to_differentiate": "우측 얼굴신경 날신경 경로 문제라면 좌측 자극 시 우측 R2도 이상이어야 합니다. 본 사례는 좌측 자극-우측 R2가 정상 범위라 얼굴신경 문제 가능성이 낮습니다.",
                "practical_tip": "눈깜빡반사는 전기자극측 신경문제인지, 반응측 신경문제인지 나누어 해석하는 것이 핵심입니다."
            }
        ]
    },

    "뇌졸중 후 발목 발바닥굽힘근 경직 평가": {
        "patient": {
            "age": 68,
            "sex": "남",
            "side": "우",
            "symptoms": [
                "뇌졸중 후 편마비 상태이며 우측 발목 경직이 심해짐",
                "발꿈치안쪽휜들린발(equinovarus) 악화와 경직 수준의 정량적 모니터링을 위해 의뢰됨"
            ],
            "physical_exam": {
                "감각 검사": [
                    "우측 편마비에 동반된 고유수용성 감각 및 표재감각 둔화"
                ],
                "맨손 근력검사(MMT)": [
                    "우측 발목관절 등굽힘(Ankle dorsiflexion): Poor (2/5) - 앞정강근(Tibialis anterior), 깊은종아리신경(Deep peroneal nerve), L4-L5",
                    "우측 발목관절 발바닥굽힘(Ankle plantarflexion): Poor (2/5) - 장딴지근(Gastrocnemius), 정강신경(Tibial nerve), S1 우세",
                    "근긴장도(Muscle tone): 발목 발바닥굽힘근 수정된 애쉬워스척도(Modified Ashworth Scale, MAS) 3등급"
                ],
                "반사 검사": [
                    "아킬레스힘줄반사(Achilles tendon reflex, S1): 우측 비정상적 항진(DRT 4+)",
                    "우측 발목간대경련(ankle clonus) 3~5회 관찰"
                ]
            }
        },
        "findings": {
            "H 반사 (우)": (H_REFLEX_HYPERACTIVE, ""),
            "H/M 비율": (H_M_RATIO_INCREASED, "")
        },
        "teaching_diagnosis": {
            "summary": "위운동신경세포(upper motor neuron, UMN) 손상에 따른 척수반사 흥분성 증가를 전기생리적으로 정량적 평가를 하는 검사입니다.",
            "emg_reason": [
                "H-반사가 낮은 자극 강도에서 쉽게 유발되거나 H/M 비율이 증가하면 척수반사 흥분성 증가를 의미하므로, 경직 정도가 커집니다. 따라서 치료 후 H/M 비율이 치료 전 보다 감소하면, 경직이 완화된 것으로 평가합니다.",
            ],
            "integration": [
                "뇌졸중 병력, MAS 3등급 경직, 아킬레스힘줄반사 항진, 발목간대경련에 대한 임상적 관찰과 더불어 H/M 비율의 정상범위 "
            ]
        },
        "differential_diagnosis": [
            {
                "name": "말초 S1 신경뿌리병증(Peripheral S1 radiculopathy)",
                "why_consider": "H-반사 검사는 S1 신경뿌리 평가에도 사용됩니다.",
                "how_to_differentiate": "S1 신경뿌리병증에서는 H-반사 지연 또는 소실과 반사 저하가 흔합니다.",
                "practical_tip": "H-반사는 말초 병변에서는 지연/소실, 중추성 경직에서는 항진됩니다."
            }
        ]
    },

    "급성 양측 다리 근력 약화": {
        "patient": {
            "age": 35,
            "sex": "남",
            "side": "양측",
            "symptoms": [
                "2주 전 심한 장염 병력",
                "3일 전부터 다리가 무겁고 급격히 진행하는 양측 근력저하 호소"
            ],
            "physical_exam": {
                "감각 검사": [
                    "발끝 부위 경미한 이상감각. 뚜렷한 감각 소실은 아직 불분명함"
                ],
                "맨손 근력검사(MMT)": [
                    "양측 엉덩관절 굽힘(Hip flexion): Poor (2/5) - 엉덩허리근(Iliopsoas), 넙다리신경(Femoral nerve), L2 우세",
                    "양측 무릎관절 폄(Knee extension): Fair (3/5) - 넙다리네갈래근(Quadriceps femoris), 넙다리신경(Femoral nerve), L3-L4",
                    "양측 발목관절 등굽힘(Ankle dorsiflexion): Fair (3/5) - 앞정강근(Tibialis anterior), 깊은종아리신경(Deep peroneal nerve), L4-L5"
                ],
                "반사 검사": [
                    "무릎반사(L4) 및 아킬레스힘줄반사(S1): 양측 완전 소실(DRT 0)"
                ]
            }
        },
        "findings": {
            "정강/종아리신경 복합근육활동전위 (CMAP)": (NCS_NORMAL, NCS_NORMAL),
            "정강/종아리신경 F파 (F-wave)": (FWAVE_DELAYED_ABSENT, FWAVE_DELAYED_ABSENT)
        },
        "teaching_diagnosis": {
            "summary": "초기 기얭-바레증후군(Guillain-Barre syndrome, GBS)에서 보일 수 있는 F파 이상 중심의 급성 염증성 다발신경병증 패턴입니다.",
            "ncs_reason": [
                "발병 초기에는 원위부 운동신경전도 (CMAP)와 감각신경전도 (SNAP)가 정상 범위일 수 있습니다.",
                "F파 지연 또는 소실은 근위부 운동신경(척수 앞뿔세포에서 신경뿌리 사이), 초기 말이집탈락성 변화를 보여주는 중요한 단서입니다."
            ],
            "emg_reason": [
                "급성기에는 왈러변성(Wallerian degeneration)이 충분히 진행되지 않아 침근전도에서 섬유자발전위(fibrillation potential)나 양성예파(positive sharp wave)가 아직 보이지 않을 수 있습니다.",
                "따라서 초기 기얭-바레증후군(GBS)에서는 침근전도보다 F파와 임상 반사 소실이 더 중요한 단서가 될 수 있습니다."
            ],
            "integration": [
                "선행 감염, 급성 상행성 이완성 근력저하, 양측 깊은힘줄반사 소실, F파 지연 또는 소실을 종합하면 초기 기얭-바레증후군(GBS)을 우선 고려합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "급성 중증 근육병증(Acute severe myopathy)",
                "why_consider": "급격한 양측 근력저하 양상 때문에 혼동될 수 있습니다.",
                "how_to_differentiate": "근육병증은 감각 이상과 전반적 반사 소실이 두드러지지 않는 경우가 많고 F파 이상도 전형적이지 않습니다.",
                "practical_tip": "급성 마비에서 반사 소실이 뚜렷하면 신경병증을 우선 고려하고 F파를 확인하세요."
            }
        ]
    }
}
