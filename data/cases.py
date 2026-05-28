CASE_LIBRARY = {
    "목-팔 통증 증상과 팔 근력 약화": {
        "patient": {
            "age": 57,
            "sex": "남",
            "side": "우",
            "symptoms": [
                "뒷목에서 오른쪽 어깨와 아래팔 노측(radial side), 엄지 쪽으로 뻗치는 통증과 저림이 지속됨",
                "최근 팔꿉관절 굽힘과 손목 폄 동작 시 힘이 빠지는 현상 발생"
            ],
            "physical_exam": {
                "감각 검사": [
                    "아래팔 노측 및 엄지/검지 쪽 감각 저하 (C6 피부분절 지배 영역)"
                ],
                "맨손 근력검사 (MMT)": [
                    "팔꿉관절 굽힘 (Elbow flexion): Fair (3/5) - 위팔두갈래근(Biceps brachii), 근육피부신경(Musculocutaneous nerve), C5-C6 우세",
                    "손목관절 폄 (Wrist extension): Fair (3/5) - 긴/짧은노쪽손목폄근(Extensor carpi radialis longus/brevis), 노신경(Radial nerve), C6 우세 포함",
                    "팔꿉관절 폄 (Elbow extension): Normal (5/5) - 위팔세갈래근(Triceps brachii), 노신경(Radial nerve), C7 우세 보존"
                ],
                "반사 검사": [
                    "위팔노근 반사 (Brachioradialis reflex, C6 지배): 감소 (DRT 1+)",
                    "위팔두갈래근 반사 (Biceps reflex, C5 지배): 정상 (DRT 2+) 또는 경미한 감소",
                    "세갈래근 반사 (Triceps reflex, C7 지배): 정상 (DRT 2+)"
                ]
            }
        },
        "findings": {
            "노신경 표재감각신경활동전위 (Superficial Radial SNAP)": ("정상 (Normal)", "정상 (Normal)"),
            "가쪽아래팔피부신경 감각신경활동전위 (Lateral antebrachial cutaneous SNAP)": ("정상 (Normal)", "정상 (Normal)"),
            "근육피부신경 복합근육활동전위 (Musculocutaneous CMAP)": ("정상 (Normal)", "정상 (Normal)"),
            "노신경 복합근육활동전위 (Radial CMAP)": ("정상 (Normal)", "정상 (Normal)"),
            "목 척추주위근 (Cervical Paraspinal)": ("정상 (Normal)", "비정상 자발전위 출현 (Fibrillation Potential, Positive Sharp Wave 등)"),
            "위팔두갈래근 (Biceps Brachii)": ("정상 (Normal)", "비정상 자발전위 출현 (Fibrillation Potential, Positive Sharp Wave 등)"),
            "노쪽손목폄근 (Extensor Carpi Radialis)": ("정상 (Normal)", "비정상 자발전위 출현 (Fibrillation Potential, Positive Sharp Wave 등)")
        },
        "teaching_diagnosis": {
            "summary": "이 사례는 C6 중심의 목 신경뿌리병증(Cervical radiculopathy) 패턴을 보여줍니다.",
            "ncs_reason": [
                "감각신경활동전위(SNAP)가 정상으로 보존되어 있습니다. 병변이 뒤뿌리신경절(DRG)보다 근위부에 있는 신경뿌리병증(radiculopathy)에서는 말초 감각신경전도가 정상으로 유지됩니다.",
                "노신경 및 근육피부신경의 말단 운동신경전도도 정상이어서 말초 단일신경병증(mononeuropathy)의 가능성은 낮습니다."
            ],
            "emg_reason": [
                "침근전도에서 목 척추주위근에 비정상 자발전위가 나타나는 것은 척수신경 앞가지/뒤가지가 분기되기 전의 '신경뿌리(root)' 수준 병변임을 강력히 시사합니다.",
                "서로 다른 말초신경의 지배를 받지만 C6 분절을 공유하는 근육들에 동시 탈신경 소견이 관찰됩니다."
            ],
            "integration": [
                "C6 피부분절 증상, MMT 약화(C6 우세), C6 반사(위팔노근)의 단독 저하, 척추주위근 침범 소견을 종합할 때 C6 신경뿌리병증으로 해석하는 것이 가장 적절합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "노신경병증 (Radial Neuropathy)",
                "why_consider": "손목 폄 약화와 노측 감각 이상이 동반되어 의심할 수 있습니다.",
                "how_to_differentiate": "말초 노신경병증이라면 표재감각신경(SNAP) 진폭 감소가 나타나며, 척추주위근은 정상이어야 합니다. 본 사례는 감각신경(SNAP) 보존 및 척추주위근 침범이 있어 배제됩니다.",
                "practical_tip": "위팔노근 반사(C6)가 떨어졌다면, 반드시 감각신경전도 정상 유무와 목 척추주위근 이상 여부를 확인하여 말초신경인지 척수신경뿌리인지 감별하세요."
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
                    "엄지, 검지, 중지 및 반지손가락 노측 절반의 손바닥 측 감각 둔화 (정중신경 분포)"
                ],
                "맨손 근력검사 (MMT)": [
                    "엄지손가락 벌림 (Thumb abduction): Good (4/5) - 짧은엄지벌림근(Abductor pollicis brevis), 정중신경(Median nerve), T1 우세"
                ],
                "반사 검사": [
                    "위팔두갈래근(C5), 위팔노근(C6), 세갈래근(C7) 반사: 모두 대칭적 정상 (DRT 2+) - 목 척수 분절 이상 없음",
                    "특수 검사: 팔렌 검사(Phalen's test), 손목 티넬 징후(Tinel's sign) 양성"
                ]
            }
        },
        "findings": {
            "정중신경 감각신경활동전위 (Median SNAP)": ("정상 (Normal)", "잠복기 지연 (Delayed latency)"),
            "정중신경 복합근육활동전위 (Median CMAP)": ("정상 (Normal)", "잠복기 지연 (Delayed latency)"),
            "짧은엄지벌림근 (Abductor Pollicis Brevis, APB)": ("정상 (Normal)", "비정상 자발전위 출현 (Fibrillation Potential, Positive Sharp Wave 등)")
        },
        "teaching_diagnosis": {
            "summary": "손목굴증후군(Carpal Tunnel Syndrome)을 시사하는 전형적인 정중신경 포착병증입니다.",
            "ncs_reason": [
                "정중신경 감각신경 및 운동신경 모두에서 잠복기 지연이 관찰되어 손목굴 부위의 국소 전도 지연을 의미합니다."
            ],
            "emg_reason": [
                "짧은엄지벌림근(APB)에서 비정상 자발전위가 출현한 것은 신경 포착이 심해져 축삭 손상 단계까지 진행되었음을 시사합니다."
            ],
            "integration": [
                "야간 통증, 정중신경 영역 감각저하, 엄지 약화(T1), 상위 신경뿌리 반사(C5-C7) 정상, 정중신경 특이적 전도 지연을 종합하면 손목굴증후군이 명확합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "근위부 정중신경병증 (Proximal Median Neuropathy)",
                "why_consider": "정중신경 지배 영역의 감각/운동 약화가 동일하게 나타납니다.",
                "how_to_differentiate": "원엎침근(Pronator teres) 등 손목 상부 근육의 근력(MMT) 및 침근전도가 정상이라는 점으로 손목 수준의 문제임을 감별합니다.",
                "practical_tip": "포착 위치를 찾기 위해 침범된 근육 중 가장 몸쪽(proximal)에 가까운 근육이 무엇인지 확인하세요."
            }
        ]
    },
    "위팔뼈 몸통 골절 후 손목처짐": {
        "patient": {
            "age": 34,
            "sex": "남",
            "side": "우",
            "symptoms": [
                "위팔뼈 몸통 골절(Humeral shaft fracture) 부상 병력",
                "이후 손목과 손가락을 들어 올리지 못하는 손목처짐(Wrist drop) 발생"
            ],
            "physical_exam": {
                "감각 검사": [
                    "손등 노측(Radial dorsum) 부위 감각 소실 (표재 노신경 지배 영역)"
                ],
                "맨손 근력검사 (MMT)": [
                    "손목관절 폄 (Wrist extension): Poor (2/5) - 노쪽손목폄근(Extensor carpi radialis), 노신경(Radial nerve), C6 우세",
                    "손가락 폄 (Finger extension): Poor (2/5) - 손가락폄근(Extensor digitorum), 노신경(Radial nerve), C7 우세",
                    "팔꿉관절 폄 (Elbow extension): Normal (5/5) - 위팔세갈래근(Triceps brachii), 노신경(Radial nerve), C7 우세 보존"
                ],
                "반사 검사": [
                    "세갈래근 반사 (Triceps reflex, C7 지배): 정상 (DRT 2+) - 병변이 나선홈 이하(세갈래근 지배 분지 아래)임을 시사",
                    "위팔노근 반사 (Brachioradialis reflex, C6 지배): 감소 (DRT 1+) - 병변 이하의 반사 저하"
                ]
            }
        },
        "findings": {
            "노신경 표재감각신경활동전위 (Superficial Radial SNAP)": ("정상 (Normal)", "감소 (Reduced)"),
            "노신경 복합근육활동전위 (Radial CMAP)": ("정상 (Normal)", "감소 (Reduced)"),
            "노쪽손목폄근 (Extensor Carpi Radialis)": ("정상 (Normal)", "비정상 자발전위 출현 (Fibrillation Potential, Positive Sharp Wave 등)"),
            "집게폄근 (Extensor Indicis Proprius, EIP)": ("정상 (Normal)", "비정상 자발전위 출현 (Fibrillation Potential, Positive Sharp Wave 등)"),
            "목 척추주위근 (Cervical Paraspinal)": ("정상 (Normal)", "정상 (Normal)")
        },
        "teaching_diagnosis": {
            "summary": "위팔뼈 나선홈(Spiral groove) 부위의 노신경 손상(Radial Neuropathy) 패턴입니다.",
            "ncs_reason": [
                "노신경 감각전도(SNAP) 진폭 감소는 병변이 말초 노신경 자체에 있음을 의미합니다."
            ],
            "emg_reason": [
                "침근전도에서 손목폄근 등 노신경 지배 원위부 근육에 탈신경 소견이 있으나, 목 척추주위근은 정상이므로 C7 신경뿌리병증을 배제합니다."
            ],
            "integration": [
                "골절 병력, C7 지배인 세갈래근 반사/근력이 보존된 점, 말초 신경전도 이상 소견을 종합할 때 나선홈 이하의 노신경병증이 적절합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "뒤뼈사이신경병증 (Posterior Interosseous Neuropathy, PIN)",
                "why_consider": "손가락/손목 폄 약화(손목처짐) 양상이 비슷합니다.",
                "how_to_differentiate": "PIN은 순수 운동신경 가지이므로 감각 소실이 없으며 표재감각신경(SNAP)이 정상입니다. 본 사례는 감각 저하와 SNAP 감소가 뚜렷하므로 본줄기(Main trunk) 손상입니다.",
                "practical_tip": "감각 기능의 보존 여부가 운동 가지 단독 손상(PIN)과 혼합 신경 손상(Main trunk)을 나누는 결정적 기준입니다."
            }
        ]
    },
    "4, 5번째 손가락 저림과 손가락 근력 약화": {
        "patient": {
            "age": 42,
            "sex": "남",
            "side": "우",
            "symptoms": [
                "오른쪽 4번째(반지), 5번째(새끼) 손가락 저림과 손날 쪽 불편감",
                "세밀한 손동작(젓가락질 등) 시 손가락이 잘 모아지지 않고 힘이 빠짐"
            ],
            "physical_exam": {
                "감각 검사": [
                    "4번째 손가락 자측 절반 및 5번째 손가락 감각 저하 (자신경 영역)"
                ],
                "맨손 근력검사 (MMT)": [
                    "새끼손가락 벌림 (Little finger abduction): Fair (3/5) - 새끼벌림근(Abductor digiti minimi), 자신경(Ulnar nerve), T1 우세",
                    "손가락 벌림/모음 (Finger abduction/adduction): Fair (3/5) - 뼈사이근(Interossei), 자신경(Ulnar nerve), T1 우세"
                ],
                "반사 검사": [
                    "위팔두갈래근(C5), 위팔노근(C6), 세갈래근(C7) 반사: 모두 대칭적 정상 (DRT 2+) - 목 척수 분절 보존 확인",
                    "특수 검사: 팔꿉관절 굽힘 검사 양성, 팔꿈치 자측 티넬 징후 양성"
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
            "summary": "팔꿉관절 터널 증후군(Cubital Tunnel Syndrome)으로 대표되는 팔꿈치 부위 자신경병증(Ulnar nerve Neuropathy)입니다.",
            "ncs_reason": [
                "자신경 감각 및 운동 신경전도에서 관찰되는 잠복기 지연은 전형적인 국소 포착에 의한 전도 이상입니다."
            ],
            "emg_reason": [
                "자신경 지배 손 자체기원근육(intrinsic muscles)에서 탈신경 소견이 확인되어 운동 축삭 손상이 동반되었음을 알 수 있습니다."
            ],
            "integration": [
                "특정 손가락 감각저하, MMT에서 T1 우세 근육(손 자체기원근육) 약화, 상위 신경 반사(C5-C7) 정상, 자신경 단독 전도 지연을 바탕으로 팔꿈치부 자신경병증으로 진단합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "C8-T1 목 신경뿌리병증 (C8-T1 Radiculopathy)",
                "why_consider": "손 자체기원근육(Intrinsic muscle)의 전반적 약화가 나타날 수 있습니다.",
                "how_to_differentiate": "신경뿌리병증은 말초 감각신경(SNAP)이 정상으로 유지되며, 정중신경 지배근(APB 등)도 함께 침범됩니다. 본 사례는 자신경 영역 국한 및 SNAP 이상이 관찰됩니다.",
                "practical_tip": "침범된 근육이 동일 신경뿌리(T1) 지배인지, 동일 말초신경(Ulnar) 지배인지 묶어서 파악하는 훈련이 필요합니다."
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
                "최근 보행 시 발끝이 바닥에 끌리는 발처짐(Foot drop) 발생"
            ],
            "physical_exam": {
                "감각 검사": [
                    "종아리 가쪽 및 발등 중앙 부위 감각 둔화 (L5 피부분절)"
                ],
                "맨손 근력검사 (MMT)": [
                    "발목관절 등굽힘 (Ankle dorsiflexion): Fair (3/5) - 앞정강근(Tibialis anterior), 깊은종아리신경(Deep peroneal nerve), L4-L5",
                    "엄지발가락 폄 (Great toe extension): Poor (2/5) - 긴엄지폄근(Extensor hallucis longus), 깊은종아리신경(Deep peroneal nerve), L5 우세",
                    "엉덩관절 벌림 (Hip abduction): Good (4/5) - 중간볼기근(Gluteus medius), 위볼기신경(Superior gluteal nerve), L5 우세"
                ],
                "반사 검사": [
                    "무릎 반사 (Patellar reflex, L4 지배): 정상 (DRT 2+) - L4 병변 배제",
                    "아킬레스힘줄 반사 (Achilles reflex, S1 지배): 정상 (DRT 2+) - S1 병변 배제"
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
            "summary": "발처짐을 동반한 전형적인 L5 허리 신경뿌리병증(L5 Radiculopathy) 패턴입니다.",
            "ncs_reason": [
                "다리 감각저하가 있음에도 SNAP가 정상인 것은 병변이 척수 신경뿌리에 위치함을 입증합니다."
            ],
            "emg_reason": [
                "서로 다른 말초신경 영역이지만 공통적으로 L5 지배를 받는 근육(TA, EHL, Gluteus medius)에 탈신경 소견이 보입니다.",
                "척추주위근 탈신경 소견은 신경뿌리 부위 병변임을 확증합니다."
            ],
            "integration": [
                "L5 방사통, L5 우세 MMT 약화, 무릎(L4)/발목(S1) 반사 정상, 감각전도(SNAP) 보존, 척추주위근 침범을 통해 L5 신경뿌리병증으로 진단합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "종아리신경병증 (Peroneal Neuropathy)",
                "why_consider": "발목 등굽힘 약화(발처짐)의 가장 흔한 말초성 원인입니다.",
                "how_to_differentiate": "종아리신경병증이라면 감각전도(SNAP)가 저하되고, 중간볼기근(L5, 위볼기신경)이나 척추주위근은 정상이어야 합니다.",
                "practical_tip": "발처짐 환자는 엉덩관절 벌림(Hip abduction, L5) 근력과 무릎(L4)/아킬레스(S1) 반사를 확인하여 L5 신경뿌리 단독 손상인지 감별해야 합니다."
            }
        ]
    },
    "정강뼈 골절로 석고붕대 후 발처짐과 발등 감각저하": {
        "patient": {
            "age": 31,
            "sex": "남",
            "side": "좌",
            "symptoms": [
                "정강이뼈 골절(Tibia fracture) 보존적 치료를 위해 석고붕대 유지 후 제거함",
                "석고붕대 제거 직후 좌측 발처짐과 발등 감각 소실 발견됨"
            ],
            "physical_exam": {
                "감각 검사": [
                    "종아리 가쪽 및 발등 부위 감각 소실 (얕은/깊은 종아리신경 분포 영역)"
                ],
                "맨손 근력검사 (MMT)": [
                    "발목관절 등굽힘 (Ankle dorsiflexion): Poor (2/5) - 앞정강근(Tibialis anterior), 깊은종아리신경(Deep peroneal nerve), L4-L5",
                    "엄지발가락 폄 (Great toe extension): Trace (1/5) - 긴엄지폄근(Extensor hallucis longus), 깊은종아리신경(Deep peroneal nerve), L5 우세",
                    "발목관절 가쪽번짐 (Ankle eversion): Poor (2/5) - 긴종아리근(Peroneus longus), 얕은종아리신경(Superficial peroneal nerve), L5 우세",
                    "발목관절 안쪽번짐 (Ankle inversion): Normal (5/5) - 뒤정강근(Tibialis posterior), 정강신경(Tibial nerve), L5 지배 보존 (중요)"
                ],
                "반사 검사": [
                    "무릎 반사 (Patellar reflex, L4 지배): 대칭적 정상 (DRT 2+)",
                    "아킬레스힘줄 반사 (Achilles reflex, S1 지배): 대칭적 정상 (DRT 2+)"
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
            "summary": "종아리뼈머리 부위 압박으로 인한 온종아리신경 손상(Common Peroneal Neuropathy)입니다.",
            "ncs_reason": [
                "얕은종아리신경 감각전도(SNAP) 감소는 병변이 척추가 아닌 말초 감각신경에 있음을 명확히 보여줍니다."
            ],
            "emg_reason": [
                "침근전도에서 깊은/얕은종아리신경 지배근 모두 탈신경 소견이 있어 분기 전 본줄기 병변임을 알 수 있으며, 허리 척추주위근이 정상이므로 신경뿌리병증을 배제합니다."
            ],
            "integration": [
                "압박 병력, 종아리신경에 국한된 약화(L5 정강신경 지배인 안쪽번짐 보존), 감각전도(SNAP) 이상을 종합하여 말초 종아리신경병증으로 진단합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "L5 허리 신경뿌리병증(L5 Radiculopathy)",
                "why_consider": "발목 등굽힘 약화(발처짐) 등 주요 증상이 겹칩니다.",
                "how_to_differentiate": "MMT에서 발목 안쪽번짐(Inversion, L5 정강신경 지배)이 보존된 점, 감각전도(SNAP) 저하, 척추주위근 정상인 점으로 신경뿌리병증을 배제합니다.",
                "practical_tip": "발처짐 환자에서 발목 안쪽번짐(Inversion) 근력이 정상이라면 척수 병변이 아닌 종아리신경 단독 손상일 확률이 높습니다."
            }
        ]
    },
    "골반 외상 후 다리 전반 근력 약화": {
        "patient": {
            "age": 45,
            "sex": "여",
            "side": "좌",
            "symptoms": [
                "골반 골절(Pelvic bone fracture) 수술 후 좌측 다리 전반의 심한 근력 약화 발생",
                "허벅지부터 종아리, 발등까지 광범위한 감각 둔화와 보행장애 호소"
            ],
            "physical_exam": {
                "감각 검사": [
                    "허벅지, 종아리, 발등 등 여러 피부분절을 넘나드는 광범위 감각 소실"
                ],
                "맨손 근력검사 (MMT)": [
                    "엉덩관절 굽힘 (Hip flexion): Poor (2/5) - 엉덩허리근(Iliopsoas), 넓적다리신경(Femoral nerve), L2 우세",
                    "무릎관절 폄 (Knee extension): Poor (2/5) - 넓적다리네갈래근(Quadriceps femoris), 넓적다리신경(Femoral nerve), L3-L4",
                    "발목관절 등굽힘 (Ankle dorsiflexion): Trace (1/5) - 앞정강근(Tibialis anterior), 깊은종아리신경(Deep peroneal nerve), L4-L5",
                    "발목관절 발바닥굽힘 (Ankle plantarflexion): Poor (2/5) - 장딴지근(Gastrocnemius), 정강신경(Tibial nerve), S1 우세"
                ],
                "반사 검사": [
                    "무릎 반사 (Patellar reflex, L4 지배): 좌측 완전 소실 (DRT 0)",
                    "아킬레스힘줄 반사 (Achilles reflex, S1 지배): 좌측 완전 소실 (DRT 0)"
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
            "summary": "외상과 연관된 허리엉치신경얼기병증(Lumbosacral Plexopathy) 패턴입니다.",
            "ncs_reason": [
                "다수의 말초 감각/운동 신경전도(CMAP, SNAP)가 모두 감소한 것은 상위 구조(신경얼기)의 광범위한 손상을 의미합니다."
            ],
            "emg_reason": [
                "여러 말초신경 지배 근육에 탈신경 소견이 광범위하게 관찰되나, 허리 척추주위근은 정상이어서 신경뿌리병증을 배제합니다."
            ],
            "integration": [
                "다수 피부분절 및 L2~S1 MMT의 광범위 약화, L4/S1 반사 동시 소실, 감각전도 이상 및 척추주위근 보존을 종합하면 신경얼기병증이 확정적입니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "다발 허리 신경뿌리병증 (Multiple Radiculopathy)",
                "why_consider": "다리 전체의 심한 근력 약화와 감각 이상이 나타납니다.",
                "how_to_differentiate": "다발성 신경뿌리병증은 말초 감각전도(SNAP)가 유지되며 척추주위근 이상이 동반됩니다. 본 사례는 감각전도(SNAP)와 척추주위근 보존으로 감별됩니다.",
                "practical_tip": "넓은 범위의 손상이 있을 때, 무릎(L4)과 아킬레스힘줄(S1) 반사가 모두 소실되었다면 신경얼기 수준의 대형 병변을 의심하세요."
            }
        ]
    },
    "양측 발끝 저림과 발가락 약화": {
        "patient": {
            "age": 67,
            "sex": "남",
            "side": "양측",
            "symptoms": [
                "오랜 기간 앓아온 당뇨병 병력",
                "양쪽 발끝에서 시작되어 발목 위로 서서히 올라오는 양측성 저림과 감각 둔화"
            ],
            "physical_exam": {
                "감각 검사": [
                    "양측 발가락 끝부터 발목 상부까지 장갑-양말형(Glove-stocking distribution) 대칭적 감각 저하"
                ],
                "맨손 근력검사 (MMT)": [
                    "양측 엄지발가락 폄 (Great toe extension): Good (4/5) - 긴엄지폄근(Extensor hallucis longus), 깊은종아리신경(Deep peroneal nerve), L5 우세 (원위부 약화)",
                    "양측 발가락 굽힘 (Toe flexion): Good (4/5) - 긴발가락굽힘근(Flexor digitorum longus), 정강신경(Tibial nerve), S1 우세 (원위부 약화)",
                    "양측 발목관절 등굽힘 (Ankle dorsiflexion): Normal (5/5) - 앞정강근(Tibialis anterior), 깊은종아리신경(Deep peroneal nerve), L4-L5",
                    "양측 무릎관절 폄 (Knee extension): Normal (5/5) - 넓적다리네갈래근(Quadriceps femoris), 넓적다리신경(Femoral nerve), L3-L4 대칭적 보존",
                    "양측 엉덩관절 굽힘 (Hip flexion): Normal (5/5) - 엉덩허리근(Iliopsoas), 넓적다리신경(Femoral nerve), L2 우세 대칭적 보존"
                ],
                "반사 검사": [
                    "아킬레스힘줄 반사 (Achilles reflex, S1 지배): 양측 소실 (DRT 0) - 원위부 긴 신경 침범 시사",
                    "무릎 반사 (Patellar reflex, L4 지배): 양측 보존 (DRT 1+ ~ 2+) - 상대적 근위부 신경 보존"
                ]
            }
        },
        "findings": {
            "장딴지신경 감각신경활동전위 (Sural SNAP)": ("감소 (Reduced)", "감소 (Reduced)"),
            "얕은종아리신경 감각신경활동전위 (Superficial Peroneal SNAP)": ("감소 (Reduced)", "감소 (Reduced)"),
            "정강신경 복합근육활동전위 (Tibial CMAP)": ("감소 (Reduced)", "감소 (Reduced)")
        },
        "teaching_diagnosis": {
            "summary": "길이 의존성(Length-dependent) 패턴을 보이는 축삭성 다발신경병증(Axonal Polyneuropathy)입니다.",
            "ncs_reason": [
                "원위부 감각/운동 신경에서 대칭적 진폭 감소가 나타나며, 전도 속도보다 '진폭 저하'가 두드러지는 것이 축삭성 병변의 특징입니다."
            ],
            "emg_reason": [
                "진단은 침근전도보다 신경전도검사의 대칭적 진폭 감소 패턴에 더 의존합니다."
            ],
            "integration": [
                "당뇨 병력, 대칭적 원위부 감각/근력 이상, S1 반사(아킬레스) 단독 소실, 대칭성 진폭 감소 패턴은 축삭성 다발신경병증의 교과서적 소견입니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "말이집탈락성 다발신경병증 (Demyelinating Polyneuropathy)",
                "why_consider": "양측 대칭성 이상이라는 점에서 다발신경병증의 또 다른 아형입니다.",
                "how_to_differentiate": "말이집탈락성 병변은 진폭 저하보다 잠복기 지연, 전도속도 저하 등이 주된 소견입니다.",
                "practical_tip": "신경전도검사 결과지를 볼 때 '진폭(Amplitude)'과 '잠복기(Latency)' 중 어느 쪽 손상이 주된 패턴인지 분석하세요."
            }
        ]
    },
    "대칭성 팔다리 근력저하와 보행 저하": {
        "patient": {
            "age": 55,
            "sex": "여",
            "side": "양측",
            "symptoms": [
                "최근 몇 달간 양손과 양발이 대칭적으로 저리고 둔함",
                "계단 오르기(근위부)와 발목 움직임(원위부) 모두에서 진행성 근력 약화 호소"
            ],
            "physical_exam": {
                "감각 검사": [
                    "양측 상/하지 원위부 대칭적 감각 저하"
                ],
                "맨손 근력검사 (MMT)": [
                    "양측 어깨관절 벌림 (Shoulder abduction): Fair (3/5) - 어깨세모근(Deltoid), 겨드랑신경(Axillary nerve), C5 우세 (근위부 약화 뚜렷)",
                    "양측 엉덩관절 굽힘 (Hip flexion): Fair (3/5) - 엉덩허리근(Iliopsoas), 넓적다리신경(Femoral nerve), L2 우세 (근위부 약화 뚜렷)",
                    "양측 손목관절 폄 (Wrist extension): Fair (3/5) - 노쪽손목폄근(Extensor carpi radialis), 노신경(Radial nerve), C6 우세 (원위부 동시 약화)",
                    "양측 발목관절 등굽힘 (Ankle dorsiflexion): Fair (3/5) - 앞정강근(Tibialis anterior), 깊은종아리신경(Deep peroneal nerve), L4-L5 (원위부 동시 약화)"
                ],
                "반사 검사": [
                    "팔/다리 깊은힘줄반사 (C5, C6, C7, L4, S1 전체): 완전 소실 (DRT 0)"
                ]
            }
        },
        "findings": {
            "정중/자신경 감각신경활동전위 (SNAP)": ("잠복기 지연 (Delayed latency)", "잠복기 지연 (Delayed latency)"),
            "정중/종아리신경 복합근육활동전위 (CMAP)": ("잠복기 지연 (Delayed latency)", "잠복기 지연 (Delayed latency)"),
            "정강/종아리신경 F파 (F-wave)": ("지연 또는 소실 (Delayed/Absent)", "지연 또는 소실 (Delayed/Absent)")
        },
        "teaching_diagnosis": {
            "summary": "만성 염증성 말이집탈락성 다발신경병증(Demyelinating Polyneuropathy) 패턴입니다.",
            "ncs_reason": [
                "다수 감각/운동 신경에서 양측성 잠복기 지연이 나타나 광범위한 말이집탈락성 변화를 시사합니다.",
                "F파 지연 및 소실은 운동신경 뿌리를 포함한 근위부 전도 이상을 강력히 뒷받침합니다."
            ],
            "emg_reason": [
                "말이집탈락성 질환은 축삭 손상이 경미하여 침근전도 탈신경 소견이 뚜렷하지 않을 수 있습니다. 근위부 평가를 위한 반사(F파) 확인이 중요합니다."
            ],
            "integration": [
                "근위/원위부 MMT 대칭적 약화, 전신 반사 소실, 광범위 전도 지연 및 F파 이상을 통해 다발신경병증을 진단합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "근육병증 (Myopathy)",
                "why_consider": "근위부 우세의 양측성 근력 약화 패턴이 근육병증과 유사하게 보입니다.",
                "how_to_differentiate": "근육병증은 순수 운동 약화이므로 감각이 정상이며, 반사(DTR)가 유지됩니다. 본 사례는 전신 반사 소실과 심한 감각 지연이 있어 감별됩니다.",
                "practical_tip": "MMT 양상만 보지 말고, 전체 DTR 소실 유무와 감각 이상 여부를 반드시 결합하여 해석하세요."
            }
        ]
    },
    "눈꺼풀 떨림과 눈 주위 불편감 지속": {
        "patient": {
            "age": 62,
            "sex": "여",
            "side": "우",
            "symptoms": [
                "우측 눈꺼풀 떨림과 얼굴의 둔한 느낌이 발생하여 지속됨",
                "뇌신경(삼차신경-뇌줄기-얼굴신경) 반사 경로 평가를 위해 의뢰됨"
            ],
            "physical_exam": {
                "감각 검사": [
                    "우측 이마 및 눈 주위(삼차신경 V1 영역) 가벼운 터치 감각 둔화"
                ],
                "맨손 근력검사 (MMT)": [
                    "우측 눈 꽉 감기 (Eye closure): Good (4/5) - 눈둘레근(Orbicularis oculi), 얼굴신경(Facial nerve), 뇌신경 7번 (미세 약화)",
                    "이마 주름잡기 (Eyebrow elevation): Normal (5/5) - 이마근(Frontalis), 얼굴신경(Facial nerve), 뇌신경 7번 대칭적 정상",
                    "입꼬리 올리기 (Smiling): Normal (5/5) - 큰광대근(Zygomaticus major), 얼굴신경(Facial nerve), 뇌신경 7번 대칭적 정상"
                ],
                "반사 검사": [
                    "우측 각막반사(Corneal reflex) 저하 의심"
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
            "summary": "눈깜빡반사(Blink reflex)를 통해 삼차신경 들방향(afferent) 편측 이상을 찾아내는 사례입니다.",
            "ncs_reason": [
                "우측 자극 시에만 동/반대측 반응이 모두 지연/소실되었습니다.",
                "이는 우측에서 신호를 받아들이는 들방향 경로(삼차신경 V1)의 문제임을 시사합니다."
            ],
            "emg_reason": [
                "얼굴신경 병변의 경우 침근전도를 보조적으로 사용하나, 본 사례는 반사 회로 분석이 핵심입니다."
            ],
            "integration": [
                "우측 삼차신경 감각 저하와 우측 자극 시 전체 반사 소실 패턴이 일치하여, 삼차신경 들방향(afferent) 편측 손상으로 해석합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "우측 얼굴신경병증 (Right Facial Neuropathy / Bell's palsy)",
                "why_consider": "얼굴 근육 약화/마비가 관찰될 때 가장 흔한 질환입니다.",
                "how_to_differentiate": "날방향(efferent, 운동) 경로인 우측 얼굴신경 문제라면, '좌측 자극 시 우측 R2' 반응도 소실되어야 합니다. 본 사례는 정상이므로 얼굴신경은 온전합니다.",
                "practical_tip": "자극측 문제(afferent)인지 반응측 문제(efferent)인지 구분하는 훈련을 반복하세요."
            }
        ]
    },
    "뇌졸중 후 발목 발바닥굽힘근 경직 평가": {
        "patient": {
            "age": 68,
            "sex": "남",
            "side": "우",
            "symptoms": [
                "뇌졸중 발병 후 편마비 상태이며, 최근 우측 발목 경직이 심해져 발꿈치안쪽휜들린발(Equinovarus) 악화",
                "경직(Spasticity) 수준 변화의 정량적 모니터링을 위해 의뢰됨"
            ],
            "physical_exam": {
                "감각 검사": [
                    "우측 편마비에 동반된 전반적인 고유수용성 감각 및 표재감각 둔화"
                ],
                "맨손 근력검사 (MMT)": [
                    "우측 발목관절 등굽힘 (Ankle dorsiflexion): Poor (2/5) - 앞정강근(Tibialis anterior), 깊은종아리신경(Deep peroneal nerve), L4-L5 (위운동신경세포 연관 수의적 조절력 저하)",
                    "우측 발목관절 발바닥굽힘 (Ankle plantarflexion): Poor (2/5) - 장딴지근(Gastrocnemius), 정강신경(Tibial nerve), S1 우세",
                    "근육 긴장도 (Muscle tone): 발목 바닥굽힘근 수정된 애쉬워스 척도(Modified Ashworth Scale, MAS) 3등급 (심한 경직)"
                ],
                "반사 검사": [
                    "아킬레스힘줄 반사 (Achilles reflex, S1 지배): 우측 비정상적 항진 (DRT 4+)",
                    "우측 발목간대경련(Ankle clonus) 3~5회 뚜렷하게 관찰됨"
                ]
            }
        },
        "findings": {
            "정강신경 복합근육활동전위 (Tibial CMAP)": ("정상 (Normal)", "정상 (Normal)"),
            "H 반사 (우)": ("항진 또는 문턱값 감소 (Hyperactive / lower threshold)", ""),
            "H/M 비율": ("증가 가능 (May be increased)", "")
        },
        "teaching_diagnosis": {
            "summary": "위운동신경세포(UMN) 손상에 따른 척수 반사 흥분성 증가를 전기생리적으로 정량 평가하는 사례입니다.",
            "ncs_reason": [
                "정강신경 말단 운동전도(CMAP) 정상은 말초 신경-근 접합부 경로 자체가 온전함을 뜻합니다."
            ],
            "emg_reason": [
                "H 반사가 낮은 자극 강도에서 항진되며, H/M 비율이 0.60 이상으로 비정상적으로 높게 나타납니다."
            ],
            "integration": [
                "뇌졸중 병력, MAS 3등급의 심한 경직, S1 반사 항진 및 간대경련과 H/M 비율 증가 소견이 완벽히 일치하여 중추성 척수반사 흥분성 증가를 증명합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "말초 S1 신경뿌리병증 (Peripheral S1 Radiculopathy)",
                "why_consider": "H 반사를 이용해 평가하는 대표적인 말초 질환입니다.",
                "how_to_differentiate": "S1 신경뿌리병증은 말초 신경 압박이므로 H 반사의 '잠복기 지연' 또는 '소실'이 발생하며 임상적으로 반사 저하(Hyporeflexia)가 동반됩니다.",
                "practical_tip": "H 반사는 아래운동신경세포 손상 시 소실/지연되고, 위운동신경세포 손상 시 항진됨을 기억하세요."
            }
        ]
    },
    "급성 양측 다리 근력 약화": {
        "patient": {
            "age": 35,
            "sex": "남",
            "side": "양측",
            "symptoms": [
                "2주 전 장염을 심하게 앓음",
                "3일 전부터 다리가 무겁더니, 급격히 진행하는 양측 근력저하 호소"
            ],
            "physical_exam": {
                "감각 검사": [
                    "발끝 부위 경미한 이상감각, 뚜렷한 감각 소실은 아직 불분명함"
                ],
                "맨손 근력검사 (MMT)": [
                    "양측 엉덩관절 굽힘 (Hip flexion): Poor (2/5) - 엉덩허리근(Iliopsoas), 넓적다리신경(Femoral nerve), L2 우세 (상행성 근력 약화 뚜렷)",
                    "양측 무릎관절 폄 (Knee extension): Fair (3/5) - 넓적다리네갈래근(Quadriceps femoris), 넓적다리신경(Femoral nerve), L3-L4",
                    "양측 발목관절 등굽힘 (Ankle dorsiflexion): Fair (3/5) - 앞정강근(Tibialis anterior), 깊은종아리신경(Deep peroneal nerve), L4-L5"
                ],
                "반사 검사": [
                    "무릎 반사(L4 지배) 및 아킬레스힘줄 반사(S1 지배): 양측 완전 소실 (DRT 0)"
                ]
            }
        },
        "findings": {
            "정강/종아리신경 복합근육활동전위 (CMAP)": ("정상 (Normal)", "정상 (Normal)"),
            "정강/종아리신경 F파 (F-wave)": ("지연 또는 소실 (Delayed/Absent)", "지연 또는 소실 (Delayed/Absent)")
        },
        "teaching_diagnosis": {
            "summary": "급성 염증성 다발신경병증의 전형적인 초기 전기생리적 단서(F파 이상)를 보여줍니다.",
            "ncs_reason": [
                "발병 1주 이내 초기에는 원위부 운동/감각 신경전도가 정상인 경우가 흔합니다.",
                "운동 신경뿌리를 포함한 근위부 전도 경로를 평가하는 F파가 조기에 지연/소실되는 것이 결정적 힌트입니다."
            ],
            "emg_reason": [
                "급성기에는 탈신경(Wallerian degeneration)이 진행되지 않아 침근전도 비정상 자발전위가 보이지 않습니다."
            ],
            "integration": [
                "선행 감염력, 급성 상행성 이완성 마비, 다리 전체 깊은힘줄 반사 소실, F파 조기 이상을 종합하여 초기 기얭-바레증후군(Guillain-Barre syndrome, GBS)을 진단합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "급성 중증 근육병증 (Acute Severe Myopathy)",
                "why_consider": "급격한 양측 근력저하 양상 때문에 혼동될 수 있습니다.",
                "how_to_differentiate": "근육병증 환자는 근력이 약해도 반사(DTR)가 상대적으로 보존되며, 근위부 F파 이상이 동반되지 않습니다.",
                "practical_tip": "급성 마비 환자에서 L4, S1 반사가 소실되었다면 신경 병변을 우선 고려하고, 즉시 'F파'를 확인하세요."
            }
        ]
    }
}
