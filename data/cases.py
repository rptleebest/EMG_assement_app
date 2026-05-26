CASE_LIBRARY = {
    "1. 목-팔 통증 증상과 팔 근력 약화": {
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
                    "팔꿉관절 굽힘 (Elbow flexion): Fair (3/5) - 위팔두갈래근(Biceps brachii), 근피신경, C5-C6",
                    "손목관절 폄 (Wrist extension): Fair (3/5) - 긴/짧은노쪽손목폄근(ECRL/B), 노신경, C6-C7"
                ],
                "반사 검사": [
                    "위팔두갈래근힘줄반사 (Biceps jerk): 감소 (1+)",
                    "위팔노근힘줄반사 (Brachioradialis reflex): 감소 (1+)"
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
            "summary": "이 사례는 C6 중심의 목 신경뿌리병증(Cervical radiculopathy) 패턴을 보여줍니다.",
            "ncs_reason": [
                "감각신경활동전위(SNAP)가 정상으로 보존되어 있습니다. 병변이 뒤뿌리신경절(DRG)보다 근위부에 있는 신경뿌리병증에서는 말초 감각신경전도가 정상으로 유지됩니다.",
                "노신경 및 근피신경의 말단 운동신경전도도 정상이어서 말초 단일신경병증의 가능성은 낮습니다."
            ],
            "emg_reason": [
                "침근전도에서 목 척추주위근에 비정상 자발전위가 나타나는 것은 척수신경 앞가지/뒤가지가 분기되기 전의 '신경뿌리' 수준 병변임을 강력히 시사합니다.",
                "서로 다른 말초신경(근피신경, 노신경)의 지배를 받지만 C6 분절을 공유하는 위팔두갈래근과 노쪽손목폄근에 동시 탈신경 소견이 관찰됩니다."
            ],
            "integration": [
                "피부분절에 일치하는 증상, MMT 약화 패턴, 감각신경전도 보존, 척추주위근 침범 소견을 종합할 때 C6 목 신경뿌리병증으로 해석하는 것이 가장 적절합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "노신경병증 (Radial Neuropathy)",
                "why_consider": "손목 폄 약화와 노측 감각 이상이 동반되어 의심할 수 있습니다.",
                "how_to_differentiate": "말초 노신경병증이라면 표재감각신경(SNAP) 진폭 감소나 전도 지연이 나타나야 하며, 척추주위근은 정상이어야 합니다. 본 사례는 SNAP 보존 및 척추주위근 침범이 있어 배제할 수 있습니다.",
                "practical_tip": "신경뿌리병증과 말초신경병증 감별의 핵심은 '감각신경전도의 보존 여부'와 '척추주위근의 침범 여부'입니다."
            }
        ]
    },
    "2. 야간 손저림과 엄지 근력 약화": {
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
                    "엄지손가락 벌림 (Thumb abduction): Good (4/5) - 짧은엄지벌림근(APB), 정중신경, C8-T1"
                ],
                "반사 검사": [
                    "상지 깊은힘줄반사(DTR): 정상 (2+) 대칭적 유지",
                    "특수 검사: 팔렌 검사(Phalen's test) 양성, 손목 티넬 징후(Tinel's sign) 양성"
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
                "정중신경 감각신경 및 운동신경 모두에서 잠복기 지연이 관찰되어 손목굴 부위의 탈수초성 변화(국소 전도 지연)를 의미합니다."
            ],
            "emg_reason": [
                "짧은엄지벌림근(APB)에서 비정상 자발전위가 출현한 것은 신경 포착이 심해져 축삭 손상(탈신경) 단계까지 진행되었음을 시사합니다."
            ],
            "integration": [
                "야간 통증, 정중신경 감각영역 저하, MMT 상 엄지 벌림 약화, 정중신경 특이적 전도 지연을 종합하면 손목굴증후군이 명확합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "근위부 정중신경병증 (Proximal Median Neuropathy)",
                "why_consider": "정중신경 지배 영역의 감각/운동 약화가 동일하게 나타납니다.",
                "how_to_differentiate": "원엎침근(Pronator Teres) 등 손목 상부의 정중신경 지배 근육의 근력(MMT) 및 침근전도 소견이 정상이라는 점으로 손목 수준의 문제임을 감별합니다.",
                "practical_tip": "포착 위치(손목 vs 팔꿈치)를 찾기 위해 침범된 근육 중 가장 몸쪽에 가까운(proximal) 근육이 무엇인지 확인하세요."
            }
        ]
    },
    "3. 위팔뼈 몸통 골절 후 손목처짐": {
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
                    "손목 폄 (Wrist extension): Poor (2/5) - 손목폄근군, 노신경, C6-C7",
                    "손가락 폄 (Finger extension): Poor (2/5) - 손가락폄근군, 노신경, C7-C8",
                    "팔꿉관절 폄 (Elbow extension): Normal (5/5) - 위팔세갈래근, 노신경, C6-C8"
                ],
                "반사 검사": [
                    "위팔세갈래근힘줄반사 (Triceps reflex): 정상 (2+) 유지"
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
            "summary": "위팔뼈 나선홈(Spiral groove) 부위의 노신경 손상(Radial Neuropathy) 패턴입니다.",
            "ncs_reason": [
                "노신경 감각신경(SNAP) 진폭 감소는 병변이 뒤뿌리신경절(DRG) 원위부인 말초 노신경 자체에 있음을 의미합니다.",
                "노신경 운동신경(CMAP) 진폭 감소는 운동 축삭의 심각한 손상 또는 손상 부위의 전도 차단을 의미합니다."
            ],
            "emg_reason": [
                "침근전도에서 손목폄근과 집게폄근에 탈신경 소견이 있으나 목 척추주위근은 정상이므로, C7 신경뿌리병증을 배제할 수 있습니다."
            ],
            "integration": [
                "골절 병력, MMT상 위팔세갈래근은 보존되나 손목/손가락 폄이 약화된 점(나선홈 이하 병변 시사), 말초 신경전도 이상 소견을 종합할 때 노신경병증이 적절합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "뒤뼈사이신경병증 (Posterior Interosseous Neuropathy, PIN)",
                "why_consider": "손가락 폄 및 손목 폄 약화(손목처짐) 양상이 비슷합니다.",
                "how_to_differentiate": "PIN은 순수 운동신경 가지이므로 감각 소실이 없으며 표재감각신경(SNAP)이 정상으로 유지됩니다. 본 사례는 감각 저하와 SNAP 감소가 뚜렷하므로 더 근위부인 나선홈 부위의 노신경 본줄기 손상입니다.",
                "practical_tip": "감각 기능의 보존 여부가 운동 가지 단독 손상(PIN)과 혼합 신경 손상(Radial N. main trunk)을 나누는 결정적 기준입니다."
            }
        ]
    },
    "4. 4, 5번째 손가락 저림과 손가락 근력 약화": {
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
                    "4번째 손가락 자측 절반 및 5번째 손가락, 손 자측면 감각 저하 (자신경 영역)"
                ],
                "맨손 근력검사 (MMT)": [
                    "새끼손가락 벌림 (Little finger abduction): Fair (3/5) - 새끼벌림근(ADM), 자신경, C8-T1",
                    "손가락 벌림/모음 (Finger abduction/adduction): Fair (3/5) - 첫째등쪽뼈사이근(FDI), 자신경, C8-T1"
                ],
                "반사 검사": [
                    "상지 깊은힘줄반사(DTR): 모두 정상 (2+)",
                    "특수 검사: 팔꿉관절 굽힘 검사(Elbow flexion test) 양성, 팔꿈치 자측 티넬 징후 양성"
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
            "summary": "팔꿉관절 터널 증후군(Cubital Tunnel Syndrome)으로 대표되는 팔꿈치 부위 자신경병증입니다.",
            "ncs_reason": [
                "자신경 감각 및 운동 신경전도에서 관찰되는 잠복기 지연은 전형적인 국소 포착에 의한 탈수초성 변화입니다."
            ],
            "emg_reason": [
                "자신경 지배 손 자체기원근육(Intrinsic muscles)인 ADM과 FDI에서 탈신경 소견이 확인되어 운동 축삭 손상이 동반되었음을 알 수 있습니다."
            ],
            "integration": [
                "특정 손가락 감각저하, MMT상 손 내재근 약화, 팔꿈치 스트레스 검사 양성, 자신경 단독 전도 지연을 바탕으로 팔꿈치부 자신경병증으로 진단합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "C8-T1 목 신경뿌리병증 (C8-T1 Radiculopathy)",
                "why_consider": "손 내재근(Intrinsic muscle)의 전반적 약화가 나타날 수 있습니다.",
                "how_to_differentiate": "신경뿌리병증은 말초 감각신경(SNAP)이 정상으로 유지되며, 정중신경 지배 내재근(APB)도 함께 침범되는 경우가 많습니다. 본 사례는 자신경 영역에 국한된 이상이 뚜렷합니다.",
                "practical_tip": "침범된 근육이 동일 신경뿌리 지배인지, 동일 말초신경 지배인지 묶어서 파악하는 훈련이 필요합니다."
            }
        ]
    },
    "5. 허리-다리 통증과 발처짐": {
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
                    "발목 등굽힘 (Ankle dorsiflexion): Fair (3/5) - 앞정강근(TA), 깊은종아리신경, L4-L5",
                    "엄지발가락 폄 (Great toe extension): Poor (2/5) - 긴엄지폄근(EHL), 깊은종아리신경, L5",
                    "엉덩관절 벌림 (Hip abduction): Good (4/5) - 중간볼기근(Gluteus medius), 위볼기신경, L4-S1"
                ],
                "반사 검사": [
                    "무릎반사(Knee jerk): 정상 (2+)",
                    "아킬레스힘줄반사(Ankle jerk): 정상 (2+) 유지"
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
                "다리 감각저하가 있음에도 얕은종아리신경 감각전도(SNAP)가 정상인 것은 병변이 뒤뿌리신경절(DRG) 근위부(척수 신경뿌리)에 위치함을 입증합니다."
            ],
            "emg_reason": [
                "깊은종아리신경(TA, EHL)과 위볼기신경(Gluteus medius) 지배 근육 등 서로 다른 말초신경 영역에서 탈신경 소견이 보이나, 공통적으로 L5 분절의 지배를 받습니다.",
                "허리 척추주위근 탈신경 소견은 병변이 척수신경 앞가지로 갈라지기 전인 신경뿌리 부위임을 확증합니다."
            ],
            "integration": [
                "L5 방사통, 다중 신경 영역 약화(L5 공통 분절), SNAP 보존, 척추주위근 침범을 통해 L5 신경뿌리병증으로 진단합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "종아리신경병증 (Peroneal Neuropathy)",
                "why_consider": "발목 등굽힘 및 발가락 폄 약화(발처짐)의 가장 흔한 말초성 원인입니다.",
                "how_to_differentiate": "종아리신경병증이라면 감각전도(SNAP)가 저하되고, 중간볼기근이나 척추주위근은 정상이어야 합니다. 중간볼기근(Gluteus medius) MMT 약화 및 침근전도 이상 유무가 주요 감별 포인트입니다.",
                "practical_tip": "발처짐 환자 평가 시 엉덩관절 벌림(Hip abduction) MMT를 반드시 확인하여 L5 신경뿌리 손상 여부를 감별해야 합니다."
            }
        ]
    },
    "6. 정강뼈 골절로 석고붕대 후 발처짐과 발등 감각저하": {
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
                    "발목 등굽힘 (Ankle dorsiflexion): Poor (2/5) - 앞정강근, 깊은종아리신경",
                    "엄지발가락 폄 (Great toe extension): Trace (1/5) - 긴엄지폄근, 깊은종아리신경",
                    "발목 가쪽번짐 (Ankle eversion): Poor (2/5) - 긴종아리근, 얕은종아리신경",
                    "발목 안쪽번짐 (Ankle inversion) 및 발바닥굽힘 (Plantarflexion): Normal (5/5) - 정강신경 보존"
                ],
                "반사 검사": [
                    "무릎반사 및 아킬레스힘줄반사: 대칭적 정상 (2+)"
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
            "summary": "종아리뼈머리(Fibular head) 부위 압박으로 인한 온종아리신경 손상(Common Peroneal Neuropathy)입니다.",
            "ncs_reason": [
                "얕은종아리신경 SNAP 진폭 감소는 병변이 척추 수준이 아닌 말초 감각신경 부위에 있음을 명확히 보여줍니다."
            ],
            "emg_reason": [
                "침근전도에서 깊은종아리신경(TA)과 얕은종아리신경(Peroneus longus) 지배 근육 모두 탈신경 소견이 있어 분기 전인 온종아리신경 본줄기 병변임을 알 수 있습니다.",
                "허리 척추주위근이 정상이므로 신경뿌리병증을 배제합니다."
            ],
            "integration": [
                "석고붕대 압박 병력, MMT상 종아리신경 지배 근육에 국한된 약화(발목 안쪽번짐 보존), 감각전도 이상을 종합하여 말초 종아리신경병증으로 확진합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "L5 허리 신경뿌리병증",
                "why_consider": "발목 등굽힘, 발가락 폄 약화(발처짐) 등 주요 임상 증상이 겹칩니다.",
                "how_to_differentiate": "MMT에서 발목 안쪽번짐(Inversion, L4-L5 정강신경 지배)이 보존된 점, 감각전도(SNAP)가 저하된 점, 척추주위근 침근전도가 정상인 점으로 신경뿌리병증을 배제합니다.",
                "practical_tip": "동일하게 발처짐이 있더라도 발목 안쪽번짐(Inversion) 근력이 보존된다면 종아리신경 단독 손상일 확률이 높습니다."
            }
        ]
    },
    "7. 골반 외상 후 다리 전반 근력 약화": {
        "patient": {
            "age": 45,
            "sex": "여",
            "side": "좌",
            "symptoms": [
                "골반 골절(Pelvic bone fracture) 수술 후 좌측 다리 전반의 심한 근력 약화 발생",
                "허벅지부터 종아리, 발등까지 광범위한 감각 둔화와 심각한 보행장애 호소"
            ],
            "physical_exam": {
                "감각 검사": [
                    "허벅지 앞면, 가쪽면, 종아리 앞/뒤, 발등/발바닥 등 여러 피부분절을 넘나드는 광범위 감각 소실"
                ],
                "맨손 근력검사 (MMT)": [
                    "엉덩관절 굽힘 (Hip flexion): Poor (2/5) - 엉덩허리근, 주로 L2-L3",
                    "무릎 폄 (Knee extension): Poor (2/5) - 넓적다리네갈래근, 넓적다리신경, L2-L4",
                    "발목 등굽힘 (Ankle dorsiflexion): Trace (1/5) - 앞정강근, 종아리신경, L4-L5",
                    "발목 발바닥굽힘 (Ankle plantarflexion): Poor (2/5) - 장딴지근, 정강신경, S1-S2"
                ],
                "반사 검사": [
                    "좌측 무릎반사 소실(0), 좌측 아킬레스힘줄반사 소실(0)"
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
            "summary": "외상과 연관된 허리엉치신경얼기병증(Lumbosacral Plexopathy)의 전형적인 다중 신경 침범 패턴입니다.",
            "ncs_reason": [
                "다수의 감각신경(장딴지신경 등) 전도 이상은 신경얼기 이하의 말초 감각 신경세포 손상을 시사합니다.",
                "종아리신경(궁둥신경 분지)과 넓적다리신경(허리신경얼기 분지) CMAP가 모두 감소한 것은 상위 구조의 광범위한 손상을 의미합니다."
            ],
            "emg_reason": [
                "요추 및 천추 분절의 여러 말초신경 지배 근육에 탈신경 소견이 광범위하게 관찰되나, 허리 척추주위근은 정상이어서 다발성 신경뿌리병증을 배제합니다."
            ],
            "integration": [
                "골반 수술력, 다수 피부분절 침범, 여러 말초신경 영역의 심한 MMT 약화, 감각전도 이상 및 척추주위근 보존을 종합하면 신경얼기병증이 확정적입니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "다발 허리 신경뿌리병증 (Multiple Radiculopathy)",
                "why_consider": "다리 전체의 심한 근력 약화와 감각 이상이 나타납니다.",
                "how_to_differentiate": "다발성 신경뿌리병증이라면 임상적 감각 소실이 심해도 말초 감각전도(SNAP)는 유지되는 경우가 많으며, 척추주위근 이상이 동반됩니다. 본 사례는 SNAP 저하와 척추주위근 보존으로 감별됩니다.",
                "practical_tip": "넓은 범위의 손상이 있을 때, 해부학적 교차점(신경얼기)의 외상력을 파악하는 것이 중요합니다."
            }
        ]
    },
    "8. 양측 발끝 저림과 발가락 약화": {
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
                    "양측 발가락 끝부터 발목 상부까지 장갑-양말형(glove-stocking distribution) 대칭적 감각 저하"
                ],
                "맨손 근력검사 (MMT)": [
                    "양측 엄지발가락 폄 (Great toe extension): Good (4/5) - 경미한 원위부 근력 약화",
                    "양측 발목 등굽힘 (Ankle dorsiflexion): Normal (5/5)",
                    "근위부 근력(무릎/엉덩관절): Normal (5/5) 대칭적 보존"
                ],
                "반사 검사": [
                    "양측 아킬레스힘줄반사 소실 (0)",
                    "양측 무릎반사 정상 또는 약간 감소 (1+ ~ 2+)"
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
                "양측 원위부 감각신경(장딴지/얕은종아리) 및 운동신경(정강)에서 대칭적인 진폭 감소가 나타나 축삭 손상을 시사합니다.",
                "전도 속도 저하나 잠복기 지연보다는 '진폭의 저하'가 두드러지는 것이 축삭성 병변의 특징입니다."
            ],
            "emg_reason": [
                "만성 축삭 병변의 경우 발 내재근 등 가장 원위부 근육에서 비정상 자발전위가 보일 수 있으나, 진단은 신경전도검사의 대칭적 진폭 감소 패턴에 더 의존합니다."
            ],
            "integration": [
                "당뇨 병력, 대칭적 원위부 감각/근력 이상, 아킬레스 반사 소실, 대칭성 진폭 감소 패턴은 축삭성 다발신경병증의 교과서적 소견입니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "말이집탈락성 다발신경병증 (Demyelinating Polyneuropathy)",
                "why_consider": "양측성, 대칭성 감각/운동 이상이라는 점에서 다발신경병증의 또 다른 주요 아형입니다.",
                "how_to_differentiate": "말이집탈락성 병변은 진폭 저하보다 잠복기 지연, 전도속도 저하, 전도 차단, F파 지연 등이 주된 소견입니다.",
                "practical_tip": "NCS 결과지를 볼 때 '진폭(Amplitude)'과 '잠복기/속도(Latency/Velocity)' 중 어느 쪽 손상이 주된 패턴인지 먼저 분석하세요."
            }
        ]
    },
    "9. 대칭성 팔다리 근력저하와 보행 저하": {
        "patient": {
            "age": 55,
            "sex": "여",
            "side": "양측",
            "symptoms": [
                "최근 몇 달간 양손과 양발이 대칭적으로 저리고 둔함",
                "계단 오르기(근위부)와 발목 움직임(원위부) 모두에서 진행성 양측 근력 약화 호소"
            ],
            "physical_exam": {
                "감각 검사": [
                    "양측 상/하지 원위부 대칭적 감각 저하"
                ],
                "맨손 근력검사 (MMT)": [
                    "어깨 벌림 (Shoulder abduction): Fair (3/5) - 근위부 약화 동반",
                    "엉덩 굽힘 (Hip flexion): Fair (3/5) - 근위부 약화 동반",
                    "손목 폄 / 발목 등굽힘: Fair (3/5) - 원위부 대칭적 약화"
                ],
                "반사 검사": [
                    "사지 전반의 깊은힘줄반사(DTR) 모두 소실 (0) (Areflexia)"
                ]
            }
        },
        "findings": {
            "정중신경 감각신경활동전위 (Median SNAP)": ("잠복기 지연 (Delayed latency)", "잠복기 지연 (Delayed latency)"),
            "자신경 감각신경활동전위 (Ulnar SNAP)": ("잠복기 지연 (Delayed latency)", "잠복기 지연 (Delayed latency)"),
            "정중신경 복합근육활동전위 (Median CMAP)": ("잠복기 지연 (Delayed latency)", "잠복기 지연 (Delayed latency)"),
            "자신경 복합근육활동전위 (Ulnar CMAP)": ("잠복기 지연 (Delayed latency)", "잠복기 지연 (Delayed latency)"),
            "종아리신경 복합근육활동전위 (Peroneal CMAP)": ("잠복기 지연 (Delayed latency)", "잠복기 지연 (Delayed latency)"),
            "정강신경 F파 (Tibial F-wave)": ("지연 또는 소실 (Delayed/Absent)", "지연 또는 소실 (Delayed/Absent)")
        },
        "teaching_diagnosis": {
            "summary": "만성 염증성 탈수초성 다발신경병증(CIDP) 등을 의심할 수 있는 말이집탈락성 다발신경병증 패턴입니다.",
            "ncs_reason": [
                "다수 감각/운동 신경에서 양측성 잠복기 지연이 나타나 광범위한 탈수초성 변화를 시사합니다.",
                "F파 지연 및 소실은 운동신경 뿌리를 포함한 근위부(Proximal)의 전도 이상을 강력히 뒷받침합니다."
            ],
            "emg_reason": [
                "탈수초성 질환의 초기/중기에는 축삭 손상이 경미하여 침근전도 탈신경 소견이 뚜렷하지 않을 수 있습니다. 후기 반사(F파) 확인이 중요합니다."
            ],
            "integration": [
                "근위부와 원위부를 모두 침범하는 MMT 대칭적 약화, 전신 무반사(Areflexia), 광범위 전도 지연 및 F파 이상을 통해 탈수초성 다발신경병증을 확진합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "근육병증 (Myopathy)",
                "why_consider": "근위부 우세의 양측성 근력 약화 패턴이 근육병증과 유사하게 보일 수 있습니다.",
                "how_to_differentiate": "근육병증은 순수 운동 약화이므로 감각 검사는 정상이며, DTR은 후기까지 보존되는 경우가 많습니다. 본 사례는 심한 감각전도 지연과 반사 소실이 있어 확실한 감별이 가능합니다.",
                "practical_tip": "MMT 양상만 보고 판단하지 말고, 반사 검사 소실 유무와 감각신경전도검사 이상 여부를 반드시 결합하여 해석하세요."
            }
        ]
    },
    "10. 눈꺼풀 떨림과 눈 주위 불편감 지속": {
        "patient": {
            "age": 62,
            "sex": "여",
            "side": "우",
            "symptoms": [
                "우측 눈꺼풀 떨림과 안면의 둔한 느낌이 10일 전 발생하여 지속됨",
                "뇌신경(삼차신경-안면신경) 반사 경로의 무결성 평가를 위해 의뢰됨"
            ],
            "physical_exam": {
                "감각 검사": [
                    "우측 이마 및 눈 주위(삼차신경 V1 영역) 가벼운 터치 감각 둔화 호소"
                ],
                "맨손 근력검사 (MMT)": [
                    "우측 눈둘레근(Orbicularis oculi) 꽉 감기 수축력: Good (4/5) (미세한 약화 보임)",
                    "이마 주름잡기, 입꼬리 올리기: 대칭적 정상 유지"
                ],
                "반사 검사": [
                    "우측 각막반사(Corneal reflex) 지연 또는 약화 의심"
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
            "summary": "눈깜빡반사(Blink reflex)를 통해 삼차신경(구심성)-안면신경(원심성) 회로의 우측 들방향(Afferent) 편측 이상을 찾아내는 사례입니다.",
            "ncs_reason": [
                "우측을 자극했을 때 동측(R1, R2) 및 반대측(좌측 R2) 반응이 모두 지연/소실되었습니다.",
                "반면 좌측을 자극했을 때는 동측(R1, R2) 및 반대측(우측 R2) 반응이 모두 정상이었습니다.",
                "이는 우측에서 신호를 받아들이는 구심성 경로(삼차신경 V1)의 문제임을 시사합니다."
            ],
            "emg_reason": [
                "안면신경 병변의 경우 침근전도를 보조적으로 사용할 수 있으나, 본 사례는 반사 회로 분석 자체가 핵심입니다."
            ],
            "integration": [
                "우측 V1 감각 저하 병력과 우측 자극 시에만 전체 반사가 소실되는 패턴이 완벽히 일치하여, 삼차신경 구심성 경로 편측 손상으로 해석합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "우측 안면신경병증 (Right Facial Neuropathy / Bell's palsy)",
                "why_consider": "눈 감기 약화 등 운동 이상이 관찰될 때 가장 흔한 질환입니다.",
                "how_to_differentiate": "원심성(운동) 경로인 우측 안면신경 문제라면, '좌측 자극 시 우측 R2' 반응도 소실되어야 합니다. 본 사례는 좌측 자극 시 우측 R2가 정상이므로 안면신경(원심성)은 온전함을 입증합니다.",
                "practical_tip": "Blink reflex에서 자극측 문제(Afferent)인지 반응측 문제(Efferent)인지 구분하는 훈련을 반복하세요."
            }
        ]
    },
    "11. 뇌졸중 후 발목 발바닥굽힘근 경직 평가": {
        "patient": {
            "age": 68,
            "sex": "남",
            "side": "우",
            "symptoms": [
                "뇌졸중 발병 후 편마비 상태이며, 최근 우측 발목 경직이 심해져 족하수 및 내반족(Equinovarus) 자세 악화",
                "물리치료 전후 경직(Spasticity) 수준 변화의 정량적 모니터링을 위해 의뢰됨"
            ],
            "physical_exam": {
                "감각 검사": [
                    "우측 편마비에 동반된 전반적인 고유수용성 감각 및 표재감각 둔화"
                ],
                "맨손 근력검사 (MMT)": [
                    "우측 발목 등굽힘 (Ankle dorsiflexion): Poor (2/5) - UMN 병변 연관 수의적 조절력 저하",
                    "Modified Ashworth Scale (MAS): 발목 바닥굽힘근 MAS Grade 3"
                ],
                "반사 검사": [
                    "우측 아킬레스힘줄반사: 비정상적 항진 (4+)",
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
            "summary": "위운동신경세포(UMN) 손상에 따른 척수 반사 흥분성 증가(경직)를 H 반사와 H/M 비율로 정량 평가하는 사례입니다.",
            "ncs_reason": [
                "정강신경 말단 운동전도(CMAP)가 정상인 것은 말초 신경-근 접합부 경로 자체는 온전함을 뜻합니다."
            ],
            "emg_reason": [
                "H 반사가 낮은 자극 강도에서 쉽게 유발(항진)되며, M파 최대 진폭 대비 H파 최대 진폭의 비율(H/M ratio)이 0.60 이상으로 비정상적으로 높게 나타납니다."
            ],
            "integration": [
                "뇌졸중 병력, MAS 3등급의 심한 경직, DTR 항진/간대경련 소견과 전기생리학적 H/M 비율 증가 소견이 완벽히 일치하여 중추성 척수반사 흥분성 증가 상태를 증명합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "말초 S1 신경뿌리병증 (Peripheral S1 Radiculopathy)",
                "why_consider": "H 반사를 이용해 평가하는 대표적인 또 다른 질환입니다.",
                "how_to_differentiate": "S1 신경뿌리병증은 말초 신경 압박이므로 H 반사의 '잠복기 지연' 또는 '소실'이 발생하며 임상적으로 반사 저하(Hyporeflexia)가 동반됩니다. 본 사례는 정반대인 '항진' 소견입니다.",
                "practical_tip": "H 반사는 하위운동신경(말초) 손상 시에는 소실/지연되고, 상위운동신경(중추) 손상 시에는 항진됨을 기억하세요."
            }
        ]
    },
    "12. 급성 양측 다리 근력 약화": {
        "patient": {
            "age": 35,
            "sex": "남",
            "side": "양측",
            "symptoms": [
                "2주 전 장염을 심하게 앓음",
                "3일 전부터 다리가 무겁더니, 현재 의자에서 혼자 일어서기 힘들 정도로 급격히 진행하는 양측 근력저하 호소"
            ],
            "physical_exam": {
                "감각 검사": [
                    "발끝 부위의 경미한 이상감각 호소, 뚜렷한 감각 소실은 아직 불분명함"
                ],
                "맨손 근력검사 (MMT)": [
                    "양측 엉덩관절 굽힘 (Hip flexion): Poor (2/5) - 상행성 근력 약화 양상",
                    "양측 무릎 폄 (Knee extension): Fair (3/5)",
                    "양측 발목 등굽힘 (Ankle dorsiflexion): Fair (3/5)"
                ],
                "반사 검사": [
                    "양측 무릎반사 및 아킬레스힘줄반사 완전 소실 (0) (Areflexia)"
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
            "summary": "급성 염증성 다발신경병증(초기 길랭-바레 증후군, GBS)의 전형적인 초기 전기생리적 단서(F파 이상)를 보여줍니다.",
            "ncs_reason": [
                "GBS 발병 1주 이내의 초기에는 원위부 운동신경전도(CMAP) 및 감각신경전도가 정상으로 나타나는 경우가 흔합니다.",
                "그러나 운동 신경뿌리를 포함한 근위부 전도 경로를 평가하는 F파가 조기에 지연되거나 소실되는 것이 질환을 인지하는 결정적 힌트가 됩니다."
            ],
            "emg_reason": [
                "급성기(발병 수일 내)에는 아직 근육의 탈신경(Wallerian degeneration)이 충분히 진행되지 않아 침근전도에서 비정상 자발전위가 보이지 않습니다."
            ],
            "integration": [
                "선행 감염력, 급성 상행성 이완성 마비, 전신 심부건반사 소실(Areflexia), F파 조기 이상을 종합하여 초기 GBS를 강하게 의심합니다."
            ]
        },
        "differential_diagnosis": [
            {
                "name": "급성 중증 근육병증 (Acute Severe Myopathy)",
                "why_consider": "급격한 양측 근력저하 양상 때문에 혼동될 수 있습니다.",
                "how_to_differentiate": "근육병증 환자는 근력 약화가 심해도 깊은힘줄반사(DTR)가 상대적으로 보존되는 경향이 있으며, F파 전도 이상 같은 근위부 신경 이상 소견이 동반되지 않습니다.",
                "practical_tip": "급성 마비 환자에서 DTR이 0(소실)이라면 신경 병변을 우선 고려하고, 전기생리적으로 'F파'를 먼저 확인하는 습관을 들이세요."
            }
        ]
    }
}