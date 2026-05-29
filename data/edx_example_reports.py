"""
근전도·신경전도검사 결과표 판독 학습용 예제 데이터.

목적
- 실제 결과표 형식에 가까운 예제를 불러와 진단 추론을 학습합니다.
- 수치를 일일이 입력하는 방식보다, 대표 패턴을 반복 학습하는 데 초점을 둡니다.
- 신경뿌리 레벨은 C5-C6처럼 넓게 뭉개지지 않도록 우세 레벨을 명시합니다.
"""

EDX_EXAMPLE_REPORTS = {
    # =====================================================
    # 팔 신경뿌리병증
    # =====================================================
    "C4 목 신경뿌리병증 예제": {
        "category": "팔 신경뿌리",
        "diagnosis": "좌측 C4 목 신경뿌리병증 의심",
        "diagnosis_level": "C4",
        "lesion_type": "radiculopathy",
        "side": "좌",
        "difficulty": "어려움",
        "clinical_hint": [
            "목 통증과 어깨 윗부분 통증",
            "팔 원위부 저림이나 손 자체근 약화는 뚜렷하지 않음",
            "C4는 표준 팔 근육 침근전도만으로 특정하기 어려워 임상 양상과 영상 확인이 중요"
        ],
        "motor_ncs": [
            {"nerve": "좌 정중신경", "site": "손목/짧은엄지벌림근", "latency": "정상", "velocity": "정상", "amplitude": "정상", "interpretation": "정상"},
            {"nerve": "좌 자신경", "site": "손목/새끼벌림근", "latency": "정상", "velocity": "정상", "amplitude": "정상", "interpretation": "정상"},
        ],
        "sensory_ncs": [
            {"nerve": "좌 정중신경", "site": "손목/둘째손가락", "latency": "정상", "velocity": "정상", "amplitude": "정상", "interpretation": "정상"},
            {"nerve": "좌 자신경", "site": "손목/다섯째손가락", "latency": "정상", "velocity": "정상", "amplitude": "정상", "interpretation": "정상"},
        ],
        "needle_emg": [
            {"muscle": "목 척추주위근", "nerve": "척수신경 뒤가지", "root": "C3-C5", "state": "섬유자발전위/양성예파"},
            {"muscle": "어깨올림근", "nerve": "등쪽어깨신경", "root": "C3-C5", "state": "섬유자발전위/양성예파"},
            {"muscle": "삼각근", "nerve": "겨드랑신경", "root": "C5-C6", "state": "정상"},
            {"muscle": "위팔두갈래근", "nerve": "근육피부신경", "root": "C5-C6", "state": "정상"},
            {"muscle": "위팔세갈래근", "nerve": "노신경", "root": "C7", "state": "정상"},
        ],
        "expected_root_scores": {"C4": 95, "C5": 35, "C6": 5, "C7": 0, "C8": 0},
        "key_reasoning": [
            "감각신경전도검사가 보존되어 말초 감각신경병증 가능성은 낮습니다.",
            "목 척추주위근과 어깨올림근 이상이 C4 주변 병변을 시사할 수 있습니다.",
            "다만 C4는 표준 팔 근육만으로 확정하기 어려워 임상 증상과 영상 소견이 중요합니다."
        ],
        "differentials": [
            "목성 통증 증후군",
            "위목 신경뿌리병증",
            "어깨관절 질환"
        ],
        "pt_points": [
            "목 움직임과 어깨 윗부분 통증의 관계 확인",
            "감각분절보다 통증 위치와 목 자세 반응을 더 주의 깊게 평가",
            "진행성 신경학적 결손이 있으면 의학적 평가 우선"
        ],
    },

    "C5 목 신경뿌리병증 예제": {
        "category": "팔 신경뿌리",
        "diagnosis": "우측 C5 목 신경뿌리병증",
        "diagnosis_level": "C5",
        "lesion_type": "radiculopathy",
        "side": "우",
        "difficulty": "보통",
        "clinical_hint": [
            "목에서 어깨 가쪽으로 뻗치는 통증",
            "어깨관절 벌림 약화",
            "위팔두갈래근 반사는 정상 또는 경미한 감소"
        ],
        "motor_ncs": [
            {"nerve": "우 정중신경", "site": "손목/짧은엄지벌림근", "latency": "정상", "velocity": "정상", "amplitude": "정상", "interpretation": "정상"},
            {"nerve": "우 자신경", "site": "손목/새끼벌림근", "latency": "정상", "velocity": "정상", "amplitude": "정상", "interpretation": "정상"},
        ],
        "sensory_ncs": [
            {"nerve": "우 정중신경", "site": "손목/둘째손가락", "latency": "정상", "velocity": "정상", "amplitude": "정상", "interpretation": "정상"},
            {"nerve": "우 자신경", "site": "손목/다섯째손가락", "latency": "정상", "velocity": "정상", "amplitude": "정상", "interpretation": "정상"},
        ],
        "needle_emg": [
            {"muscle": "목 척추주위근", "nerve": "척수신경 뒤가지", "root": "C4-T1", "state": "섬유자발전위/양성예파"},
            {"muscle": "삼각근", "nerve": "겨드랑신경", "root": "C5-C6", "state": "섬유자발전위/양성예파"},
            {"muscle": "가시위근", "nerve": "어깨위신경", "root": "C5-C6", "state": "섬유자발전위/양성예파"},
            {"muscle": "위팔두갈래근", "nerve": "근육피부신경", "root": "C5-C6", "state": "정상 또는 경미한 동원 감소"},
            {"muscle": "위팔노근", "nerve": "노신경", "root": "C6", "state": "정상"},
            {"muscle": "위팔세갈래근", "nerve": "노신경", "root": "C7", "state": "정상"},
        ],
        "expected_root_scores": {"C5": 95, "C6": 45, "C7": 0, "C8": 0},
        "key_reasoning": [
            "감각신경활동전위가 보존되고 목 척추주위근 이상이 있어 신경뿌리병증을 지지합니다.",
            "삼각근과 가시위근 침범이 C5 우세 패턴을 형성합니다.",
            "위팔노근과 위팔세갈래근이 보존되어 C6 또는 C7 우세 병변 가능성은 낮아집니다."
        ],
        "differentials": [
            "겨드랑신경병증",
            "어깨위신경병증",
            "위팔신경얼기 위줄기 병변"
        ],
        "pt_points": [
            "어깨관절 벌림 MMT와 통증 억제성 약화를 구분",
            "어깨충돌증후군과 목 신경뿌리병증 감별",
            "스펄링 검사와 목 견인 반응 확인"
        ],
    },

    "C6 목 신경뿌리병증 예제": {
        "category": "팔 신경뿌리",
        "diagnosis": "좌측 C6 우세 목 신경뿌리병증",
        "diagnosis_level": "C6",
        "lesion_type": "radiculopathy",
        "side": "좌",
        "difficulty": "중요",
        "clinical_hint": [
            "목에서 아래팔 노쪽, 엄지/검지 쪽으로 뻗치는 통증",
            "손목관절 폄과 팔꿉관절 굽힘 약화 가능",
            "위팔노근 반사 감소 가능"
        ],
        "motor_ncs": [
            {"nerve": "좌 정중신경", "site": "손목/짧은엄지벌림근", "latency": "3.8 ms", "velocity": "64 m/s", "amplitude": "정상", "interpretation": "정상"},
        ],
        "sensory_ncs": [
            {"nerve": "좌 정중신경", "site": "손목/둘째손가락", "latency": "3.1 ms", "velocity": "정상", "amplitude": "정상", "interpretation": "정상"},
            {"nerve": "좌 정중신경", "site": "손바닥/손목", "latency": "1.8 ms", "velocity": "정상", "amplitude": "정상", "interpretation": "정상"},
            {"nerve": "좌 자신경", "site": "손목/다섯째손가락", "latency": "2.2 ms", "velocity": "정상", "amplitude": "정상", "interpretation": "정상"},
        ],
        "needle_emg": [
            {"muscle": "목 척추주위근", "nerve": "척수신경 뒤가지", "root": "C4-T1", "state": "섬유자발전위/양성예파"},
            {"muscle": "삼각근", "nerve": "겨드랑신경", "root": "C5-C6", "state": "섬유자발전위/양성예파"},
            {"muscle": "위팔두갈래근", "nerve": "근육피부신경", "root": "C5-C6", "state": "섬유자발전위/양성예파"},
            {"muscle": "위팔노근", "nerve": "노신경", "root": "C6", "state": "섬유자발전위/양성예파"},
            {"muscle": "노쪽손목폄근", "nerve": "노신경", "root": "C6-C7", "state": "섬유자발전위/양성예파"},
            {"muscle": "위팔세갈래근", "nerve": "노신경", "root": "C7", "state": "정상"},
            {"muscle": "노쪽손목굽힘근", "nerve": "정중신경", "root": "C6-C7", "state": "정상"},
            {"muscle": "긴엄지굽힘근", "nerve": "정중신경", "root": "C7-T1", "state": "정상"},
            {"muscle": "짧은엄지벌림근", "nerve": "정중신경", "root": "C8-T1", "state": "정상"},
            {"muscle": "첫째등쪽뼈사이근", "nerve": "자신경", "root": "C8-T1", "state": "정상"},
        ],
        "expected_root_scores": {"C5": 55, "C6": 100, "C7": 20, "C8": 0, "T1": 0},
        "key_reasoning": [
            "정중신경과 자신경 감각신경활동전위가 보존되어 말초신경병증보다 신경뿌리병증을 지지합니다.",
            "목 척추주위근 이상은 목 신경뿌리병증 판단에 중요한 단서입니다.",
            "위팔노근은 C6 판단에 매우 중요한 근육이며, 노쪽손목폄근도 C6 기여가 큽니다.",
            "위팔세갈래근과 손 자체근이 보존되어 C7, C8, T1 우세 병변 가능성은 낮습니다.",
            "따라서 C5-C6로 넓게 표현하기보다 C6 우세 목 신경뿌리병증으로 학습하는 것이 적절합니다."
        ],
        "differentials": [
            "겨드랑신경병증",
            "노신경병증",
            "위팔신경얼기 위줄기 병변",
            "손목굴증후군"
        ],
        "pt_points": [
            "C6 피부분절: 아래팔 노쪽, 엄지/검지 쪽 감각 확인",
            "MMT: 팔꿉관절 굽힘, 손목관절 폄, 위팔노근 기능 확인",
            "반사: 위팔노근 반사와 위팔두갈래근 반사 확인",
            "스펄링 검사와 목 견인 검사 반응 확인"
        ],
    },

    "C7 목 신경뿌리병증 예제": {
        "category": "팔 신경뿌리",
        "diagnosis": "우측 C7 목 신경뿌리병증",
        "diagnosis_level": "C7",
        "lesion_type": "radiculopathy",
        "side": "우",
        "difficulty": "보통",
        "clinical_hint": [
            "목에서 팔 뒤쪽과 가운데손가락으로 뻗치는 통증",
            "팔꿉관절 폄과 손가락 폄 약화",
            "위팔세갈래근 반사 감소"
        ],
        "motor_ncs": [
            {"nerve": "우 노신경", "site": "위팔/폄근", "latency": "정상", "velocity": "정상", "amplitude": "정상", "interpretation": "정상"},
        ],
        "sensory_ncs": [
            {"nerve": "우 표재노신경", "site": "아래팔/손등", "latency": "정상", "velocity": "정상", "amplitude": "정상", "interpretation": "정상"},
        ],
        "needle_emg": [
            {"muscle": "목 척추주위근", "nerve": "척수신경 뒤가지", "root": "C4-T1", "state": "섬유자발전위/양성예파"},
            {"muscle": "위팔세갈래근", "nerve": "노신경", "root": "C7", "state": "섬유자발전위/양성예파"},
            {"muscle": "손가락폄근", "nerve": "노신경", "root": "C7-C8", "state": "섬유자발전위/양성예파"},
            {"muscle": "노쪽손목폄근", "nerve": "노신경", "root": "C6-C7", "state": "동원 감소"},
            {"muscle": "위팔두갈래근", "nerve": "근육피부신경", "root": "C5-C6", "state": "정상"},
            {"muscle": "첫째등쪽뼈사이근", "nerve": "자신경", "root": "C8-T1", "state": "정상"},
        ],
        "expected_root_scores": {"C5": 0, "C6": 20, "C7": 100, "C8": 25, "T1": 0},
        "key_reasoning": [
            "감각신경활동전위가 보존되고 목 척추주위근 이상이 있어 신경뿌리병증을 지지합니다.",
            "위팔세갈래근과 손가락폄근 이상이 C7 우세 패턴입니다.",
            "위팔두갈래근과 손 자체근이 보존되어 C5-C6, C8-T1 병변 가능성은 낮습니다."
        ],
        "differentials": [
            "노신경병증",
            "뒤뼈사이신경병증",
            "위팔신경얼기 뒤다발 병변"
        ],
        "pt_points": [
            "위팔세갈래근 반사 확인",
            "팔꿉관절 폄과 손가락 폄 MMT",
            "노신경병증과 구분하기 위해 표재노신경 감각반응과 목 척추주위근 소견 확인"
        ],
    },

    "C8 목 신경뿌리병증 예제": {
        "category": "팔 신경뿌리",
        "diagnosis": "좌측 C8 목 신경뿌리병증",
        "diagnosis_level": "C8",
        "lesion_type": "radiculopathy",
        "side": "좌",
        "difficulty": "보통",
        "clinical_hint": [
            "아래팔 안쪽과 약손가락/새끼손가락 쪽 저림",
            "손가락 굽힘 또는 손 자체근 약화",
            "자신경병증과 감별 필요"
        ],
        "motor_ncs": [
            {"nerve": "좌 자신경", "site": "손목/새끼벌림근", "latency": "정상", "velocity": "정상", "amplitude": "정상", "interpretation": "정상 또는 경미한 감소"},
            {"nerve": "좌 정중신경", "site": "손목/짧은엄지벌림근", "latency": "정상", "velocity": "정상", "amplitude": "정상", "interpretation": "정상"},
        ],
        "sensory_ncs": [
            {"nerve": "좌 자신경", "site": "손목/다섯째손가락", "latency": "정상", "velocity": "정상", "amplitude": "정상", "interpretation": "정상"},
            {"nerve": "좌 정중신경", "site": "손목/둘째손가락", "latency": "정상", "velocity": "정상", "amplitude": "정상", "interpretation": "정상"},
        ],
        "needle_emg": [
            {"muscle": "목 척추주위근", "nerve": "척수신경 뒤가지", "root": "C4-T1", "state": "섬유자발전위/양성예파"},
            {"muscle": "긴엄지굽힘근", "nerve": "앞뼈사이신경", "root": "C8-T1", "state": "섬유자발전위/양성예파"},
            {"muscle": "짧은엄지벌림근", "nerve": "정중신경", "root": "C8-T1", "state": "동원 감소"},
            {"muscle": "첫째등쪽뼈사이근", "nerve": "자신경", "root": "C8-T1", "state": "섬유자발전위/양성예파"},
            {"muscle": "위팔세갈래근", "nerve": "노신경", "root": "C7", "state": "정상"},
            {"muscle": "위팔두갈래근", "nerve": "근육피부신경", "root": "C5-C6", "state": "정상"},
        ],
        "expected_root_scores": {"C6": 0, "C7": 0, "C8": 100, "T1": 75},
        "key_reasoning": [
            "자신경 감각신경활동전위가 보존되면 팔꿈치 자신경병증보다 C8 신경뿌리병증 가능성이 올라갑니다.",
            "정중신경과 자신경 지배 손 근육이 함께 침범되어 단일 자신경병증만으로 설명하기 어렵습니다.",
            "목 척추주위근 이상은 신경뿌리병증을 지지합니다."
        ],
        "differentials": [
            "팔꿈치 부위 자신경병증",
            "아래줄기 위팔신경얼기병증",
            "가슴문증후군"
        ],
        "pt_points": [
            "손가락 굽힘, 엄지손가락 벌림, 손가락 벌림 MMT",
            "자신경 감각분포와 C8 피부분절 비교",
            "목 자세와 팔 증상 변화 확인"
        ],
    },

    "위팔신경얼기 위줄기 병변 예제": {
        "category": "팔 신경얼기",
        "diagnosis": "좌측 위팔신경얼기 위줄기 병변",
        "diagnosis_level": "Upper trunk",
        "lesion_type": "plexopathy",
        "side": "좌",
        "difficulty": "중요",
        "clinical_hint": [
            "어깨와 위팔 가쪽 약화",
            "C5-C6 신경뿌리병증과 유사하게 보일 수 있음",
            "감각신경활동전위 감소와 목 척추주위근 보존이 핵심 감별점"
        ],
        "motor_ncs": [
            {"nerve": "좌 겨드랑신경", "site": "삼각근", "latency": "정상 또는 지연", "velocity": "-", "amplitude": "감소", "interpretation": "진폭 감소"},
            {"nerve": "좌 근육피부신경", "site": "위팔두갈래근", "latency": "정상 또는 지연", "velocity": "-", "amplitude": "감소", "interpretation": "진폭 감소"},
        ],
        "sensory_ncs": [
            {"nerve": "좌 가쪽아래팔피부신경", "site": "아래팔", "latency": "정상", "velocity": "정상", "amplitude": "감소", "interpretation": "진폭 감소"},
            {"nerve": "좌 표재노신경", "site": "손등", "latency": "정상", "velocity": "정상", "amplitude": "정상 또는 감소", "interpretation": "정상 또는 감소"},
        ],
        "needle_emg": [
            {"muscle": "목 척추주위근", "nerve": "척수신경 뒤가지", "root": "C4-T1", "state": "정상"},
            {"muscle": "삼각근", "nerve": "겨드랑신경", "root": "C5-C6", "state": "섬유자발전위/양성예파"},
            {"muscle": "위팔두갈래근", "nerve": "근육피부신경", "root": "C5-C6", "state": "섬유자발전위/양성예파"},
            {"muscle": "위팔노근", "nerve": "노신경", "root": "C6", "state": "동원 감소"},
            {"muscle": "위팔세갈래근", "nerve": "노신경", "root": "C7", "state": "정상"},
            {"muscle": "첫째등쪽뼈사이근", "nerve": "자신경", "root": "C8-T1", "state": "정상"},
        ],
        "expected_root_scores": {"C5": 75, "C6": 90, "C7": 10, "C8": 0, "T1": 0},
        "key_reasoning": [
            "C5-C6 관련 근육 이상은 C6 신경뿌리병증과 비슷하게 보일 수 있습니다.",
            "하지만 목 척추주위근이 정상이고 감각신경활동전위가 감소하면 신경뿌리보다 위팔신경얼기 병변을 더 의심합니다.",
            "위줄기 병변은 C5-C6 근육군을 중심으로 침범합니다."
        ],
        "differentials": [
            "C5 목 신경뿌리병증",
            "C6 목 신경뿌리병증",
            "겨드랑신경병증",
            "어깨위신경병증"
        ],
        "pt_points": [
            "어깨관절 벌림과 가쪽돌림 기능 확인",
            "감각신경활동전위 감소 여부를 신경뿌리병증과 감별에 활용",
            "목 척추주위근 정상 여부 확인"
        ],
    },

    # =====================================================
    # 다리 신경뿌리병증
    # =====================================================
    "L3 허리 신경뿌리병증 예제": {
        "category": "다리 신경뿌리",
        "diagnosis": "좌측 L3 허리 신경뿌리병증",
        "diagnosis_level": "L3",
        "lesion_type": "radiculopathy",
        "side": "좌",
        "difficulty": "보통",
        "clinical_hint": [
            "넓적다리 앞쪽 통증",
            "엉덩관절 굽힘과 무릎관절 폄 약화 가능",
            "무릎반사 저하 가능"
        ],
        "motor_ncs": [
            {"nerve": "좌 넓적다리신경", "site": "넙다리네갈래근", "latency": "정상", "velocity": "-", "amplitude": "정상 또는 경미한 감소", "interpretation": "대체로 보존"},
        ],
        "sensory_ncs": [
            {"nerve": "좌 장딴지신경", "site": "종아리/발목", "latency": "정상", "velocity": "정상", "amplitude": "정상", "interpretation": "정상"},
        ],
        "needle_emg": [
            {"muscle": "허리 척추주위근", "nerve": "척수신경 뒤가지", "root": "L2-S1", "state": "섬유자발전위/양성예파"},
            {"muscle": "엉덩허리근", "nerve": "허리신경얼기", "root": "L2-L4", "state": "섬유자발전위/양성예파"},
            {"muscle": "안쪽넓은근", "nerve": "넓적다리신경", "root": "L3-L4", "state": "동원 감소"},
            {"muscle": "앞정강근", "nerve": "깊은종아리신경", "root": "L4-L5", "state": "정상"},
            {"muscle": "장딴지근", "nerve": "정강신경", "root": "S1-S2", "state": "정상"},
        ],
        "expected_root_scores": {"L3": 95, "L4": 55, "L5": 0, "S1": 0},
        "key_reasoning": [
            "장딴지신경 감각반응이 보존되어 신경뿌리병증을 지지합니다.",
            "엉덩허리근과 넓적다리신경 지배근 이상이 L3-L4 분절을 시사합니다.",
            "앞정강근과 장딴지근이 보존되어 L5/S1 가능성은 낮습니다."
        ],
        "differentials": [
            "넓적다리신경병증",
            "허리신경얼기병증",
            "엉덩관절 질환"
        ],
        "pt_points": [
            "엉덩관절 굽힘과 무릎관절 폄 MMT",
            "무릎반사 확인",
            "넓적다리 앞쪽 감각과 보행 중 무릎 꺾임 확인"
        ],
    },

    "L4 허리 신경뿌리병증 예제": {
        "category": "다리 신경뿌리",
        "diagnosis": "우측 L4 허리 신경뿌리병증",
        "diagnosis_level": "L4",
        "lesion_type": "radiculopathy",
        "side": "우",
        "difficulty": "보통",
        "clinical_hint": [
            "넓적다리 앞쪽에서 정강이 안쪽으로 내려가는 통증",
            "무릎관절 폄과 발목관절 등굽힘 약화 가능",
            "무릎반사 감소"
        ],
        "motor_ncs": [
            {"nerve": "우 종아리신경", "site": "발목/짧은발가락폄근", "latency": "정상", "velocity": "정상", "amplitude": "정상", "interpretation": "정상"},
            {"nerve": "우 정강신경", "site": "발목/엄지벌림근", "latency": "정상", "velocity": "정상", "amplitude": "정상", "interpretation": "정상"},
        ],
        "sensory_ncs": [
            {"nerve": "우 장딴지신경", "site": "종아리/발목", "latency": "정상", "velocity": "정상", "amplitude": "정상", "interpretation": "정상"},
        ],
        "needle_emg": [
            {"muscle": "허리 척추주위근", "nerve": "척수신경 뒤가지", "root": "L2-S1", "state": "섬유자발전위/양성예파"},
            {"muscle": "안쪽넓은근", "nerve": "넓적다리신경", "root": "L3-L4", "state": "섬유자발전위/양성예파"},
            {"muscle": "앞정강근", "nerve": "깊은종아리신경", "root": "L4-L5", "state": "동원 감소"},
            {"muscle": "긴엄지폄근", "nerve": "깊은종아리신경", "root": "L5", "state": "정상"},
            {"muscle": "중간볼기근", "nerve": "위볼기신경", "root": "L5-S1", "state": "정상"},
            {"muscle": "장딴지근", "nerve": "정강신경", "root": "S1-S2", "state": "정상"},
        ],
        "expected_root_scores": {"L3": 30, "L4": 100, "L5": 25, "S1": 0},
        "key_reasoning": [
            "감각신경활동전위가 보존되고 허리 척추주위근 이상이 있어 신경뿌리병증을 지지합니다.",
            "안쪽넓은근과 앞정강근 일부 이상이 L4 우세 패턴입니다.",
            "긴엄지폄근과 중간볼기근 보존은 L5 우세 병변 가능성을 낮춥니다."
        ],
        "differentials": [
            "넓적다리신경병증",
            "L3 신경뿌리병증",
            "L5 신경뿌리병증"
        ],
        "pt_points": [
            "무릎관절 폄 MMT와 무릎반사 확인",
            "정강이 안쪽 감각 확인",
            "계단 내려가기와 무릎 안정성 평가"
        ],
    },

    "L5 허리 신경뿌리병증 예제": {
        "category": "다리 신경뿌리",
        "diagnosis": "우측 L5 허리 신경뿌리병증",
        "diagnosis_level": "L5",
        "lesion_type": "radiculopathy",
        "side": "우",
        "difficulty": "중요",
        "clinical_hint": [
            "허리에서 종아리 가쪽과 발등으로 뻗치는 통증",
            "발처짐",
            "엄지발가락 폄과 엉덩관절 벌림 약화"
        ],
        "motor_ncs": [
            {"nerve": "우 종아리신경", "site": "발목/짧은발가락폄근", "latency": "정상", "velocity": "정상", "amplitude": "정상 또는 경미한 감소", "interpretation": "대체로 보존"},
            {"nerve": "우 정강신경", "site": "발목/엄지벌림근", "latency": "정상", "velocity": "정상", "amplitude": "정상", "interpretation": "정상"},
        ],
        "sensory_ncs": [
            {"nerve": "우 얕은종아리신경", "site": "종아리/발목", "latency": "정상", "velocity": "정상", "amplitude": "정상", "interpretation": "정상"},
            {"nerve": "우 장딴지신경", "site": "종아리/발목", "latency": "정상", "velocity": "정상", "amplitude": "정상", "interpretation": "정상"},
        ],
        "needle_emg": [
            {"muscle": "허리 척추주위근", "nerve": "척수신경 뒤가지", "root": "L2-S1", "state": "섬유자발전위/양성예파"},
            {"muscle": "앞정강근", "nerve": "깊은종아리신경", "root": "L4-L5", "state": "섬유자발전위/양성예파"},
            {"muscle": "긴엄지폄근", "nerve": "깊은종아리신경", "root": "L5", "state": "섬유자발전위/양성예파"},
            {"muscle": "중간볼기근", "nerve": "위볼기신경", "root": "L5-S1", "state": "섬유자발전위/양성예파"},
            {"muscle": "긴종아리근", "nerve": "얕은종아리신경", "root": "L5-S1", "state": "동원 감소"},
            {"muscle": "장딴지근", "nerve": "정강신경", "root": "S1-S2", "state": "정상"},
        ],
        "expected_root_scores": {"L4": 20, "L5": 100, "S1": 35, "S2": 0},
        "key_reasoning": [
            "얕은종아리신경과 장딴지신경 감각반응이 보존되어 신경뿌리병증을 지지합니다.",
            "앞정강근, 긴엄지폄근, 중간볼기근은 서로 다른 말초신경 지배를 받지만 L5 분절을 공유합니다.",
            "장딴지근 보존은 S1 우세 병변 가능성을 낮춥니다."
        ],
        "differentials": [
            "온종아리신경병증",
            "허리엉치신경얼기병증",
            "궁둥신경병증"
        ],
        "pt_points": [
            "발목관절 등굽힘, 엄지발가락 폄, 엉덩관절 벌림 MMT",
            "발목관절 안쪽번짐 보존 여부로 온종아리신경병증과 감별",
            "발처짐 보행과 발목-발 보조기 필요성 확인"
        ],
    },

    "S1 허리 신경뿌리병증 예제": {
        "category": "다리 신경뿌리",
        "diagnosis": "좌측 S1 허리 신경뿌리병증",
        "diagnosis_level": "S1",
        "lesion_type": "radiculopathy",
        "side": "좌",
        "difficulty": "중요",
        "clinical_hint": [
            "종아리 뒤쪽과 발바닥으로 뻗치는 통증",
            "한발 뒤꿈치 들기 어려움",
            "아킬레스힘줄반사 감소"
        ],
        "motor_ncs": [
            {"nerve": "좌 정강신경", "site": "발목/엄지벌림근", "latency": "정상", "velocity": "정상", "amplitude": "정상", "interpretation": "정상"},
        ],
        "sensory_ncs": [
            {"nerve": "좌 장딴지신경", "site": "종아리/발목", "latency": "정상", "velocity": "정상", "amplitude": "정상", "interpretation": "정상"},
        ],
        "special_tests": [
            {"test": "H반사", "side": "좌", "result": "지연 또는 소실", "interpretation": "S1 경로 이상을 시사"}
        ],
        "needle_emg": [
            {"muscle": "허리 척추주위근", "nerve": "척수신경 뒤가지", "root": "L2-S1", "state": "섬유자발전위/양성예파"},
            {"muscle": "장딴지근", "nerve": "정강신경", "root": "S1-S2", "state": "섬유자발전위/양성예파"},
            {"muscle": "가자미근", "nerve": "정강신경", "root": "S1-S2", "state": "동원 감소"},
            {"muscle": "큰볼기근", "nerve": "아래볼기신경", "root": "L5-S2", "state": "동원 감소"},
            {"muscle": "앞정강근", "nerve": "깊은종아리신경", "root": "L4-L5", "state": "정상"},
        ],
        "expected_root_scores": {"L4": 0, "L5": 15, "S1": 100, "S2": 45},
        "key_reasoning": [
            "장딴지신경 감각반응이 보존되어 S1 신경뿌리병증을 지지합니다.",
            "장딴지근, 가자미근, 큰볼기근 이상이 S1 우세 패턴입니다.",
            "H반사 지연 또는 소실은 S1 경로 이상을 보강합니다."
        ],
        "differentials": [
            "정강신경병증",
            "궁둥신경병증",
            "아킬레스힘줄 병변"
        ],
        "pt_points": [
            "한발 뒤꿈치 들기 평가",
            "아킬레스힘줄반사 확인",
            "발바닥굽힘 근력저하와 통증 억제성 약화 구분"
        ],
    },

    "S2 엉치 신경뿌리병증 예제": {
        "category": "다리 신경뿌리",
        "diagnosis": "S2 엉치 신경뿌리병증 의심",
        "diagnosis_level": "S2",
        "lesion_type": "radiculopathy",
        "side": "좌",
        "difficulty": "어려움",
        "clinical_hint": [
            "엉치 또는 뒤넓적다리 깊은 통증",
            "골반저 기능, 배뇨·배변 증상 동반 여부 확인 필요",
            "S2는 표준 다리 근육만으로 특정하기 어려움"
        ],
        "motor_ncs": [
            {"nerve": "좌 정강신경", "site": "발목/엄지벌림근", "latency": "정상", "velocity": "정상", "amplitude": "정상 또는 경미한 감소", "interpretation": "대체로 보존"},
        ],
        "sensory_ncs": [
            {"nerve": "좌 장딴지신경", "site": "종아리/발목", "latency": "정상", "velocity": "정상", "amplitude": "정상", "interpretation": "정상"},
        ],
        "needle_emg": [
            {"muscle": "허리 척추주위근", "nerve": "척수신경 뒤가지", "root": "L2-S1", "state": "정상 또는 경미한 이상"},
            {"muscle": "뒤넓적다리근", "nerve": "궁둥신경", "root": "L5-S2", "state": "동원 감소"},
            {"muscle": "장딴지근", "nerve": "정강신경", "root": "S1-S2", "state": "동원 감소"},
            {"muscle": "항문조임근", "nerve": "음부신경", "root": "S2-S4", "state": "섬유자발전위/양성예파"},
            {"muscle": "앞정강근", "nerve": "깊은종아리신경", "root": "L4-L5", "state": "정상"},
        ],
        "expected_root_scores": {"L5": 10, "S1": 40, "S2": 95},
        "key_reasoning": [
            "S2는 표준 근전도만으로 특정하기 어렵고 골반저 관련 평가가 중요합니다.",
            "항문조임근 이상과 엉치 관련 증상이 있으면 S2-S4 병변을 고려합니다.",
            "배뇨·배변 증상이나 말안장 감각저하가 있으면 즉시 의학적 평가가 필요합니다."
        ],
        "differentials": [
            "말총증후군",
            "엉치신경얼기병증",
            "음부신경병증"
        ],
        "pt_points": [
            "말안장 감각저하, 배뇨·배변 변화는 red flag",
            "골반저 증상 문진",
            "응급 의학적 평가 필요성 판단"
        ],
    },

    # =====================================================
    # 허리엉치신경얼기병증
    # =====================================================
    "허리엉치신경얼기병증 예제": {
        "category": "다리 신경얼기",
        "diagnosis": "좌측 허리엉치신경얼기병증",
        "diagnosis_level": "Lumbosacral plexus",
        "lesion_type": "plexopathy",
        "side": "좌",
        "difficulty": "중요",
        "clinical_hint": [
            "좌측 다리 광범위 약화와 보행장애",
            "발처짐과 발목 조절 저하",
            "여러 말초신경 영역의 감각저하"
        ],
        "sensory_ncs": [
            {"nerve": "우 얕은종아리신경", "site": "종아리/발목", "latency": "3.4 ms", "velocity": "-", "amplitude": "17.6 μV", "interpretation": "정상"},
            {"nerve": "우 장딴지신경", "site": "종아리/발목", "latency": "3.4 ms", "velocity": "-", "amplitude": "14.4 μV", "interpretation": "정상"},
            {"nerve": "좌 얕은종아리신경", "site": "종아리/발목", "latency": "3.4 ms", "velocity": "-", "amplitude": "17.6 μV", "interpretation": "정상"},
            {"nerve": "좌 장딴지신경", "site": "종아리/발목", "latency": "3.2 ms", "velocity": "-", "amplitude": "6.5 μV", "interpretation": "진폭 감소"},
        ],
        "motor_ncs": [
            {"nerve": "우 깊은종아리신경", "site": "발목/짧은발가락폄근", "latency": "3.4 ms", "velocity": "48.7 m/s", "amplitude": "3367.4 μV", "interpretation": "정상"},
            {"nerve": "좌 깊은종아리신경", "site": "발목/짧은발가락폄근", "latency": "-", "velocity": "-", "amplitude": "-", "interpretation": "반응 소실"},
            {"nerve": "좌 깊은종아리신경", "site": "발목/앞정강근", "latency": "7.6 ms", "velocity": "21.9 m/s", "amplitude": "291.4 μV", "interpretation": "현저한 진폭 감소 및 전도속도 저하"},
            {"nerve": "좌 정강신경", "site": "발목/엄지벌림근", "latency": "3.5 ms", "velocity": "43.8 m/s", "amplitude": "9040.3 μV", "interpretation": "상대적 보존"},
        ],
        "needle_emg": [
            {"muscle": "허리 척추주위근", "nerve": "척수신경 뒤가지", "root": "L2-S1", "state": "정상"},
            {"muscle": "우 앞정강근", "nerve": "깊은종아리신경", "root": "L4-L5", "state": "정상"},
            {"muscle": "우 큰볼기근", "nerve": "아래볼기신경", "root": "L5-S2", "state": "정상"},
            {"muscle": "가쪽넓은근", "nerve": "넓적다리신경", "root": "L2-L4", "state": "섬유자발전위"},
            {"muscle": "엉덩허리근", "nerve": "허리신경얼기", "root": "L2-L4", "state": "섬유자발전위"},
            {"muscle": "큰볼기근", "nerve": "아래볼기신경", "root": "L5-S2", "state": "섬유자발전위"},
            {"muscle": "중간볼기근", "nerve": "위볼기신경", "root": "L4-S1", "state": "섬유자발전위"},
            {"muscle": "뒤넓적다리근", "nerve": "궁둥신경", "root": "L5-S2", "state": "섬유자발전위"},
            {"muscle": "장딴지근", "nerve": "정강신경", "root": "S1-S2", "state": "섬유자발전위"},
            {"muscle": "가자미근", "nerve": "정강신경", "root": "S1-S2", "state": "섬유자발전위"},
            {"muscle": "앞정강근", "nerve": "깊은종아리신경", "root": "L4-L5", "state": "운동단위전위 없음"},
            {"muscle": "긴종아리근", "nerve": "얕은종아리신경", "root": "L5-S1", "state": "운동단위전위 없음"},
            {"muscle": "긴엄지폄근", "nerve": "깊은종아리신경", "root": "L5", "state": "운동단위전위 없음"},
        ],
        "expected_root_scores": {"L3": 35, "L4": 60, "L5": 100, "S1": 90, "S2": 45},
        "key_reasoning": [
            "좌측 장딴지신경 감각진폭 감소는 병변이 뒤뿌리신경절보다 원위부에 있음을 시사합니다.",
            "허리 척추주위근이 정상으로 보존되어 다발 허리 신경뿌리병증보다 신경얼기병증을 더 지지합니다.",
            "넓적다리신경, 위볼기신경, 아래볼기신경, 궁둥신경, 정강신경, 종아리신경 영역이 광범위하게 침범됩니다.",
            "단일 온종아리신경병증이나 단일 L5 신경뿌리병증으로 설명하기 어렵습니다."
        ],
        "differentials": [
            "다발 허리 신경뿌리병증",
            "궁둥신경병증",
            "온종아리신경병증",
            "당뇨병성 허리엉치신경뿌리얼기병증"
        ],
        "pt_points": [
            "발처짐뿐 아니라 무릎관절 폄, 엉덩관절 굽힘/벌림/폄을 모두 평가",
            "감각저하 범위가 단일 신경 또는 단일 피부분절인지 확인",
            "낙상 위험, 보조기 필요성, 피부 보호 교육 필요",
            "진행성 또는 통증성 광범위 약화는 의학적 평가와 원인 확인이 중요"
        ],
    },
}
