ANATOMY = {
    # ---------------- 감각신경전도검사 (Sensory NCS) ----------------
    "정중신경 감각신경활동전위 (Median SNAP)": {"nerve": "정중신경", "level": "C6-T1", "domain": "sensory", "region": "arm"},
    "자신경 감각신경활동전위 (Ulnar SNAP)": {"nerve": "자신경", "level": "C8-T1", "domain": "sensory", "region": "arm"},
    "노신경 감각신경활동전위 (Radial SNAP)": {"nerve": "노신경", "level": "C5-C8", "domain": "sensory", "region": "arm"},
    "노신경 표재감각신경활동전위 (Superficial Radial SNAP)": {"nerve": "노신경 표재분지", "level": "C6-C8", "domain": "sensory", "region": "arm"},
    "가쪽아래팔피부신경 감각신경활동전위 (Lateral Antebrachial Cutaneous SNAP)": {"nerve": "가쪽아래팔피부신경", "level": "C5-C6", "domain": "sensory", "region": "arm"},
    # [추가] 다발신경병증 사례용 복합 항목
    "정중/자신경 감각신경활동전위 (SNAP)": {"nerve": "정중/자신경", "level": "상지 전반", "domain": "sensory", "region": "arm"},
    
    "장딴지신경 감각신경활동전위 (Sural SNAP)": {"nerve": "장딴지신경", "level": "S1-S2", "domain": "sensory", "region": "leg"},
    "얕은종아리신경 감각신경활동전위 (Superficial Peroneal SNAP)": {"nerve": "얕은종아리신경", "level": "L5-S1", "domain": "sensory", "region": "leg"},
    "두렁신경 감각신경활동전위 (Saphenous SNAP)": {"nerve": "두렁신경", "level": "L3-L4", "domain": "sensory", "region": "leg"},
    "첫째 발가락사이 감각 (First Dorsal Web Space Sensation)": {"nerve": "깊은종아리신경 감각분지", "level": "L5", "domain": "sensory", "region": "leg"},

    # ---------------- 운동신경전도검사 (Motor NCS) ----------------
    "정중신경 복합근육활동전위 (Median CMAP)": {"nerve": "정중신경", "level": "C8-T1", "domain": "motor", "region": "arm"},
    "자신경 복합근육활동전위 (Ulnar CMAP)": {"nerve": "자신경", "level": "C8-T1", "domain": "motor", "region": "arm"},
    "노신경 복합근육활동전위 (Radial CMAP)": {"nerve": "노신경", "level": "C6-C8", "domain": "motor", "region": "arm"},
    "겨드랑신경 복합근육활동전위 (Axillary CMAP)": {"nerve": "겨드랑신경", "level": "C5-C6", "domain": "motor", "region": "arm"},
    "근육피부신경 복합근육활동전위 (Musculocutaneous CMAP)": {"nerve": "근육피부신경", "level": "C5-C6", "domain": "motor", "region": "arm"},

    "종아리신경 복합근육활동전위 (Peroneal CMAP)": {"nerve": "온종아리신경", "level": "L4-S1", "domain": "motor", "region": "leg"},
    "깊은종아리신경 복합근육활동전위 (Deep Peroneal CMAP)": {"nerve": "깊은종아리신경", "level": "L5-S1", "domain": "motor", "region": "leg"},
    "정강신경 복합근육활동전위 (Tibial CMAP)": {"nerve": "정강신경", "level": "L4-S3", "domain": "motor", "region": "leg"},
    "넓적다리신경 복합근육활동전위 (Femoral CMAP)": {"nerve": "넓적다리신경", "level": "L2-L4", "domain": "motor", "region": "leg"},
    # [추가] 다발신경병증 사례용 복합 항목
    "정중/종아리신경 복합근육활동전위 (CMAP)": {"nerve": "정중/종아리신경", "level": "전신 전도", "domain": "motor", "region": "mixed"},

    # ---------------- 침근전도검사 (Needle EMG) ----------------
    "짧은엄지벌림근 (Abductor Pollicis Brevis, APB)": {"nerve": "정중신경", "level": "C8-T1", "domain": "muscle", "region": "arm"},
    "첫째등쪽뼈사이근 (First Dorsal Interosseous, FDI)": {"nerve": "자신경", "level": "C8-T1", "domain": "muscle", "region": "arm"},
    "새끼벌림근 (Abductor Digiti Minimi, ADM)": {"nerve": "자신경", "level": "C8-T1", "domain": "muscle", "region": "arm"},
    "집게폄근 (Extensor Indicis Proprius, EIP)": {"nerve": "노신경", "level": "C7-C8", "domain": "muscle", "region": "arm"},
    "노쪽손목폄근 (Extensor Carpi Radialis)": {"nerve": "노신경", "level": "C6-C7", "domain": "muscle", "region": "arm"},
    "가시아래근 (Infraspinatus)": {"nerve": "어깨위신경", "level": "C5-C6", "domain": "muscle", "region": "arm"},
    "삼각근 (Deltoid)": {"nerve": "겨드랑신경", "level": "C5-C6", "domain": "muscle", "region": "arm"},
    "위팔두갈래근 (Biceps Brachii)": {"nerve": "근육피부신경", "level": "C5-C6", "domain": "muscle", "region": "arm"},
    "위팔노근 (Brachioradialis)": {"nerve": "노신경", "level": "C5-C6", "domain": "muscle", "region": "arm"},
    "원엎침근 (Pronator Teres)": {"nerve": "정중신경", "level": "C6-C7", "domain": "muscle", "region": "arm"},
    "위팔세갈래근 (Triceps Brachii)": {"nerve": "노신경", "level": "C6-C8", "domain": "muscle", "region": "arm"},
    "목 척추주위근 (Cervical Paraspinal)": {"nerve": "척수뒤가지", "level": "목 신경뿌리", "domain": "muscle", "region": "arm"},

    "앞정강근 (Tibialis Anterior, TA)": {"nerve": "깊은종아리신경", "level": "L4-L5", "domain": "muscle", "region": "leg"},
    "짧은발가락폄근 (Extensor Digitorum Brevis, EDB)": {"nerve": "깊은종아리신경", "level": "L5-S1", "domain": "muscle", "region": "leg"},
    "짧은발가락벌림근 (Abductor Digiti Minimi pedis)": {"nerve": "가쪽발바닥신경", "level": "S1-S2", "domain": "muscle", "region": "leg"},
    "긴엄지폄근 (Extensor Hallucis Longus, EHL)": {"nerve": "깊은종아리신경", "level": "L5", "domain": "muscle", "region": "leg"},
    "긴종아리근 (Peroneus Longus)": {"nerve": "얕은종아리신경", "level": "L5-S1", "domain": "muscle", "region": "leg"},
    "장딴지근 (Gastrocnemius)": {"nerve": "정강신경", "level": "S1-S2", "domain": "muscle", "region": "leg"},
    "가자미근 (Soleus)": {"nerve": "정강신경", "level": "S1-S2", "domain": "muscle", "region": "leg"},
    "가쪽넓은근 (Vastus Lateralis)": {"nerve": "넓적다리신경", "level": "L2-L4", "domain": "muscle", "region": "leg"},
    "엉덩허리근 (Iliopsoas)": {"nerve": "넓적다리신경", "level": "L2-L4", "domain": "muscle", "region": "leg"},
    "큰볼기근 (Gluteus Maximus)": {"nerve": "아래볼기신경", "level": "L5-S2", "domain": "muscle", "region": "leg"},
    "중간볼기근 (Gluteus Medius)": {"nerve": "위볼기신경", "level": "L4-S1", "domain": "muscle", "region": "leg"},
    "뒤넓적다리근 (Biceps Femoris)": {"nerve": "궁둥신경", "level": "L5-S2", "domain": "muscle", "region": "leg"},
    "허리 척추주위근 (Lumbar Paraspinal)": {"nerve": "척수뒤가지", "level": "허리 신경뿌리", "domain": "muscle", "region": "leg"},

    # ---------------- 특수 및 반사 검사 (Reflex & F-wave) ----------------
    "H 반사 (좌)": {"nerve": "정강신경 반사고리", "level": "S1 경로", "domain": "h_reflex", "region": "leg"},
    "H 반사 (우)": {"nerve": "정강신경 반사고리", "level": "S1 경로", "domain": "h_reflex", "region": "leg"},
    "H/M 비율": {"nerve": "척수 반사 흥분성", "level": "S1 경로", "domain": "h_ratio", "region": "leg"},
    
    "정중신경 F파 (Median F-wave)": {"nerve": "정중신경 근위부", "level": "C8-T1", "domain": "f_wave", "region": "arm"},
    "자신경 F파 (Ulnar F-wave)": {"nerve": "자신경 근위부", "level": "C8-T1", "domain": "f_wave", "region": "arm"},
    "정강신경 F파 (Tibial F-wave)": {"nerve": "정강신경 근위부", "level": "L5-S2", "domain": "f_wave", "region": "leg"},
    "종아리신경 F파 (Peroneal F-wave)": {"nerve": "종아리신경 근위부", "level": "L4-S1", "domain": "f_wave", "region": "leg"},
    # [추가] 다발신경병증 사례용 복합 항목
    "정강/종아리신경 F파 (F-wave)": {"nerve": "정강/종아리신경 근위부", "level": "하지 근위부", "domain": "f_wave", "region": "leg"},

    "우측 자극-우측 R1": {"nerve": "삼차-얼굴신경 반사", "level": "뇌줄기", "domain": "blink", "region": "face"},
    "우측 자극-우측 R2": {"nerve": "삼차-얼굴신경 반사", "level": "뇌줄기", "domain": "blink", "region": "face"},
    "우측 자극-좌측 R2": {"nerve": "삼차-얼굴신경 반사", "level": "뇌줄기", "domain": "blink", "region": "face"},
    "좌측 자극-좌측 R1": {"nerve": "삼차-얼굴신경 반사", "level": "뇌줄기", "domain": "blink", "region": "face"},
    "좌측 자극-좌측 R2": {"nerve": "삼차-얼굴신경 반사", "level": "뇌줄기", "domain": "blink", "region": "face"},
    "좌측 자극-우측 R2": {"nerve": "삼차-얼굴신경 반사", "level": "뇌줄기", "domain": "blink", "region": "face"},
}
