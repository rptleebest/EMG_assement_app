from collections import defaultdict
from datetime import datetime

from data.anatomy import ANATOMY
from utils.helpers import normalize_case_item_name, simplify_level_text, is_abnormal
from core.formatters import summarize_status, severity_text

def build_diff_dx_details(dx_name):
    detail_map = {
        "원위부 정중신경병증 (손목굴증후군, CTS)": "정중신경 감각/운동 잠복기 지연과 짧은엄지벌림근(APB)의 탈신경 소견이 있으나, 근위부(원엎침근 등)는 정상일 때 수근관(손목) 부위 포착을 강하게 시사합니다.",
        "근위부 정중신경병증 (Proximal Median Neuropathy)": "정중신경 이상 소견과 함께, 손목 상부에 위치한 원엎침근(Pronator Teres) 등 근위부 근육의 침근전도 이상이 동반될 때 의심합니다.",
        "팔꿈치부 자신경병증 (Cubital Tunnel Syndrome)": "자신경 관련 검사 이상과 첫째등쪽뼈사이근(FDI) 등 손 내재근의 침근전도 이상이 동반되면 팔꿈치 부위 자신경 포착 가능성이 높습니다.",
        "자신경병증 (Ulnar Neuropathy)": "자신경 지배 영역의 감각/운동 이상이 확인됩니다. 포착 부위 확인을 위해 임상 증상(티넬 징후 등)과 대조가 필요합니다.",
        "노신경병증 (Radial Neuropathy)": "노신경 감각저하 및 손목/손가락 폄근의 침근전도 이상이 확인될 때 의심합니다. C7 신경뿌리병증과의 감별을 위해 목 척추주위근 확인이 필수입니다.",
        "종아리신경병증 (Peroneal Neuropathy)": "발처짐과 함께 얕은종아리신경(SNAP) 진폭 감소, 앞정강근 등 종아리신경 지배 근육의 이상이 나타날 때 의심합니다. 중간볼기근이 정상인 것이 L5 신경뿌리병증과의 감별 포인트입니다.",
        "정강신경병증 (Tibial Neuropathy)": "정강신경 영역의 국소적인 감각/운동 전도 이상 및 장딴지근 등 관련 근육 침범 시 의심합니다.",
        
        "목 신경뿌리병증 (Cervical Radiculopathy)": "가장 중요한 감별 포인트는 '감각신경전도(SNAP)의 보존'과 '목 척추주위근의 비정상 자발전위'입니다. 말초신경병증과 유사해 보이나 이 두 가지 소견으로 감별합니다.",
        "허리 신경뿌리병증 (Lumbar Radiculopathy)": "발처짐 등이 있더라도 얕은종아리/장딴지 감각신경(SNAP)이 정상이고, 허리 척추주위근 및 동분절 타 신경 영역(중간볼기근 등) 침범이 있으면 허리 신경뿌리병증으로 감별합니다.",
        
        "팔신경얼기병증 (Brachial Plexopathy)": "여러 팔 말초신경(정중, 자, 노 등)에 걸친 이상과 감각신경전도 이상이 동반되나, 목 척추주위근은 정상일 때 의심합니다.",
        "허리엉치신경얼기병증 (Lumbosacral Plexopathy)": "여러 다리 신경(종아리, 정강, 넓적다리 등)에 광범위한 이상과 감각신경전도 저하가 있으나, 허리 척추주위근은 정상일 때 의심합니다.",
        
        "말이집탈락성 다발신경병증 (Demyelinating Polyneuropathy)": "양측성으로 여러 신경에 걸쳐 '진폭 감소'보다는 '잠복기 지연'과 'F파 지연/소실'이 두드러지게 나타나는 패턴입니다.",
        "축삭성 다발신경병증 (Axonal Polyneuropathy)": "양측성, 길이의존성(발끝부터 시작)으로 여러 감각 및 운동신경에서 '진폭 감소'가 중심이 되는 패턴입니다.",
        
        "위운동신경세포 병변 / 척수반사 항진 (UMN Lesion / Spasticity)": "H반사 문턱값 감소 및 H/M 비율 증가는 말초 하위운동신경 손상이 아닌 중추성(뇌졸중/척수손상) 척수 반사 흥분성 증가(경직)를 시사합니다.",
        "S1 신경뿌리/근위부 경로 이상 (S1 Radiculopathy)": "정강신경 말초 전도는 정상이나 H반사만 지연/소실된 경우 S1 신경뿌리 병변을 의심합니다.",
        "급성 다발신경뿌리병증 (GBS 초기 의심)": "말초 운동전도검사는 정상에 가까우나 여러 신경에서 F파만 조기에 지연/소실된다면 초기 길랭-바레 증후군 등 근위부 탈수초성 병변을 의심합니다.",
        "삼차-안면신경 반사경로 편측 이상": "눈깜빡반사 검사 시 자측/우측 자극에 비대칭적 반응이 나타나면 해당 구심성(삼차) 또는 원심성(안면) 뇌신경 병변을 시사합니다.",
        "비특이적 소견 (추가 검사 요망)": "현재 입력된 데이터만으로는 특정 신경이나 분절의 명확한 손상 패턴을 특정하기 어렵습니다. 추가적인 근육/신경 검사가 필요합니다."
    }
    return detail_map.get(dx_name, "임상 증상(MMT, 감각 검사)과 전기생리학적 검사 결과를 종합적으로 연결하여 해석해야 합니다.")


def analyze_case(age, sex, side, selected_rows):
    scores = defaultdict(int)
    reasons = []
    suggestions = set()
    lesion_tags = set()
    involved_nerves = set()
    involved_levels = set()
    top3_details = []
    abnormal_items = []

    # 1. 상태 및 부위별 카운터
    stats = {
        "sensory_abnorm": 0, "motor_abnorm": 0, "muscle_abnorm": 0, "paraspinal_abnorm": 0,
        "delayed_count": 0, "reduced_count": 0, "no_response_count": 0,
        "f_wave_abnorm": 0, "h_reflex_abnorm": 0, "h_reflex_hyper": 0, "hm_ratio_inc": 0, "blink_abnorm": 0,
        "arm_abnorm": 0, "leg_abnorm": 0
    }

    # 신경별 해부학적 트래킹 (근위부 vs 원위부 / 신경얼기 vs 신경뿌리 감별용)
    tracking = {
        "median_distal": False, "median_proximal": False, "median_ncs": False,
        "ulnar_muscle": False, "ulnar_ncs": False,
        "radial_muscle": False, "radial_ncs": False,
        "peroneal_muscle": False, "peroneal_ncs": False, "gluteus_muscle": False,
        "tibial_muscle": False, "tibial_ncs": False,
        "arm_plexus": False, "leg_plexus": False
    }

    # 2. 데이터 파싱
    for row in selected_rows:
        item = normalize_case_item_name(row["item"])
        left = str(row.get("left", "")).lower()
        right = str(row.get("right", "")).lower()
        combined_val = left + " " + right
        is_item_abnormal = is_abnormal(row.get("left")) or is_abnormal(row.get("right"))

        if not is_item_abnormal or item not in ANATOMY:
            continue

        a = ANATOMY[item]
        involved_nerves.add(a["nerve"])
        involved_levels.add(simplify_level_text(a["level"]))
        abnormal_items.append({"항목": item, "신경": a["nerve"], "레벨": simplify_level_text(a["level"]), "결과": summarize_status(row.get("left"), row.get("right"), side)})

        # 카운트 누적
        if a["region"] == "arm": stats["arm_abnorm"] += 1
        elif a["region"] == "leg": stats["leg_abnorm"] += 1

        if a["domain"] == "sensory": stats["sensory_abnorm"] += 1
        elif a["domain"] == "motor": stats["motor_abnorm"] += 1
        elif a["domain"] == "muscle": stats["muscle_abnorm"] += 1
        
        if "척추주위근" in item: stats["paraspinal_abnorm"] += 1
        if "감소" in combined_val or "reduced" in combined_val: stats["reduced_count"] += 1
        if "지연" in combined_val or "delayed" in combined_val: stats["delayed_count"] += 1
        if "무반응" in combined_val or "absent" in combined_val: stats["no_response_count"] += 1
        
        # 특수검사 카운트
        if "f-wave" in item.lower() or "f파" in item: stats["f_wave_abnorm"] += 1
        if "h 반사" in item:
            if "항진" in combined_val or "hyperactive" in combined_val: stats["h_reflex_hyper"] += 1
            else: stats["h_reflex_abnorm"] += 1
        if "h/m 비율" in item and "증가" in combined_val: stats["hm_ratio_inc"] += 1
        if "자극" in item: stats["blink_abnorm"] += 1

        # 신경 국소화(Localization) 맵핑
        if "정중신경" in item: tracking["median_ncs"] = True
        if "짧은엄지벌림근" in item: tracking["median_distal"] = True
        if "원엎침근" in item: tracking["median_proximal"] = True
        
        if "자신경" in item: tracking["ulnar_ncs"] = True
        if "첫째등쪽뼈사이근" in item or "새끼벌림근" in item: tracking["ulnar_muscle"] = True
        
        if "노신경" in item: tracking["radial_ncs"] = True
        if "손목폄근" in item or "집게폄근" in item or "위팔노근" in item: tracking["radial_muscle"] = True
        
        if "종아리신경" in item: tracking["peroneal_ncs"] = True
        if "앞정강근" in item or "짧은발가락" in item or "긴종아리근" in item: tracking["peroneal_muscle"] = True
        if "중간볼기근" in item or "큰볼기근" in item: tracking["gluteus_muscle"] = True
        
        if "정강신경" in item: tracking["tibial_ncs"] = True
        if "장딴지근" in item or "가자미근" in item: tracking["tibial_muscle"] = True

        if "가쪽아래팔피부신경" in item or "겨드랑신경" in item or "근피신경" in item: tracking["arm_plexus"] = True
        if "넓적다리신경" in item or "뒤넓적다리근" in item or "가쪽넓은근" in item: tracking["leg_plexus"] = True

    # -------------------------------------------------------------
    # 3. 임상 추론 로직 (Clinical Brain: Localization)
    # -------------------------------------------------------------
    is_cervical_root = False
    is_lumbar_root = False

    # [규칙 1] 다발신경병증 (Polyneuropathy)
    if stats["sensory_abnorm"] >= 2 and stats["motor_abnorm"] >= 2 and side == "양측":
        if stats["delayed_count"] > stats["reduced_count"]:
            scores["말이집탈락성 다발신경병증 (Demyelinating Polyneuropathy)"] += 20
            lesion_tags.add("다발성/탈수초성")
            reasons.append("양측성으로 다수 신경에서 '잠복기 지연'이 두드러져 말이집탈락(수초 손상) 다발신경병증 패턴을 보입니다.")
        else:
            scores["축삭성 다발신경병증 (Axonal Polyneuropathy)"] += 20
            lesion_tags.add("다발성/축삭성")
            reasons.append("양측성으로 다수 신경에서 '진폭 감소'가 두드러져 축삭 손상 다발신경병증 패턴을 보입니다.")

    # [규칙 2] 신경뿌리병증 (Radiculopathy) 판단 - 척추주위근 이상 또는 감각전도 보존
    if (stats["paraspinal_abnorm"] > 0) or (stats["muscle_abnorm"] >= 2 and stats["sensory_abnorm"] == 0):
        if stats["arm_abnorm"] > 0:
            scores["목 신경뿌리병증 (Cervical Radiculopathy)"] += 15
            is_cervical_root = True
            lesion_tags.add("신경뿌리(근) 수준")
            reasons.append("감각신경전도(SNAP)가 보존되어 있거나 목 척추주위근 이상이 관찰되어 말초신경병증보다 경추 신경뿌리 병변 가능성이 매우 높습니다.")
            suggestions.add("경추 MRI 및 근위부 도수근력검사(MMT) 확인이 필요합니다.")
        
        if stats["leg_abnorm"] > 0:
            scores["허리 신경뿌리병증 (Lumbar Radiculopathy)"] += 15
            is_lumbar_root = True
            lesion_tags.add("신경뿌리(근) 수준")
            reasons.append("감각신경전도(SNAP)가 보존되어 있거나 허리 척추주위근 이상이 관찰되어 요천추 신경뿌리 병변 가능성이 매우 높습니다.")

    # [규칙 3] 신경얼기병증 (Plexopathy)
    if stats["sensory_abnorm"] >= 1 and stats["muscle_abnorm"] >= 2 and stats["paraspinal_abnorm"] == 0:
        if tracking["arm_plexus"] or (tracking["median_ncs"] and tracking["ulnar_ncs"] and not is_cervical_root):
            scores["팔신경얼기병증 (Brachial Plexopathy)"] += 12
            lesion_tags.add("신경얼기 수준")
            reasons.append("여러 팔 말초신경에 걸친 이상과 감각전도 저하가 있으나, 목 척추주위근은 정상이므로 신경얼기 병변을 시사합니다.")
        if tracking["leg_plexus"] or (tracking["peroneal_ncs"] and tracking["tibial_ncs"] and not is_lumbar_root):
            scores["허리엉치신경얼기병증 (Lumbosacral Plexopathy)"] += 12
            lesion_tags.add("신경얼기 수준")
            reasons.append("다리의 여러 신경 영역에 광범위한 침범과 감각전도 저하가 있으나, 허리 척추주위근이 정상이어서 신경얼기 병변을 시사합니다.")

    # [규칙 4] 정중신경병증 (원위부 vs 근위부)
    if (tracking["median_ncs"] or tracking["median_distal"] or tracking["median_proximal"]) and not is_cervical_root:
        if tracking["median_proximal"]:
            scores["근위부 정중신경병증 (Proximal Median Neuropathy)"] += 10
            lesion_tags.add("근위부 말초신경")
            reasons.append("근위부(손목 상부)에 위치한 '원엎침근(Pronator Teres)'에 탈신경 소견이 동반되어 근위부 포착을 시사합니다.")
        else:
            scores["원위부 정중신경병증 (손목굴증후군, CTS)"] += 10
            lesion_tags.add("원위부 말초신경(손목)")
            reasons.append("근위부(원엎침근) 침범 소견 없이 짧은엄지벌림근 및 감각전도 지연이 관찰되어 손목터널증후군 가능성이 높습니다.")

    # [규칙 5] 자신경병증
    if (tracking["ulnar_ncs"] or tracking["ulnar_muscle"]) and not is_cervical_root:
        if tracking["ulnar_muscle"]:
            scores["팔꿈치부 자신경병증 (Cubital Tunnel Syndrome)"] += 10
            lesion_tags.add("단일 말초신경(팔꿈치)")
            reasons.append("자신경 전도 이상 및 손 내재근(FDI, ADM) 침근전도 이상이 동반되어 팔꿈치 부위 포착을 강하게 의심합니다.")
        else:
            scores["자신경병증 (Ulnar Neuropathy)"] += 8
            lesion_tags.add("단일 말초신경")
            reasons.append("자신경 영역에 국한된 신경전도 이상이 관찰됩니다.")

    # [규칙 6] 노신경병증
    if (tracking["radial_ncs"] or tracking["radial_muscle"]) and not is_cervical_root:
        scores["노신경병증 (Radial Neuropathy)"] += 10
        lesion_tags.add("단일 말초신경")
        reasons.append("노신경 영역의 감각/운동 이상이 있으며 목 척추주위근 침범이 없어 단일 노신경 손상을 시사합니다.")

    # [규칙 7] 종아리신경병증 (비골신경)
    if (tracking["peroneal_ncs"] or tracking["peroneal_muscle"]) and not is_lumbar_root:
        # L5 신경뿌리병증과 감별 (중간볼기근이 정상일 경우 말초신경으로 확정)
        if not tracking["gluteus_muscle"]:
            scores["종아리신경병증 (Peroneal Neuropathy)"] += 10
            lesion_tags.add("단일 말초신경(종아리뼈머리)")
            reasons.append("종아리신경 지배 영역 이상이 뚜렷하며, L5 지배인 중간볼기근(Gluteus medius)과 허리 척추주위근은 정상이므로 말초 종아리신경(비골신경) 단독 병변입니다.")

    # [규칙 8] 정강신경병증 (경골신경)
    if (tracking["tibial_ncs"] or tracking["tibial_muscle"]) and not is_lumbar_root:
        scores["정강신경병증 (Tibial Neuropathy)"] += 9
        lesion_tags.add("단일 말초신경")
        reasons.append("정강신경 영역에 국한된 감각/운동 신경전도 및 근육 이상이 관찰됩니다.")

    # [규칙 9] 특수검사 해석
    if stats["h_reflex_hyper"] > 0 or stats["hm_ratio_inc"] > 0:
        scores["위운동신경세포 병변 / 척수반사 항진 (UMN Lesion / Spasticity)"] += 12
        lesion_tags.add("중추신경계/반사항진")
        reasons.append("H반사 항진 및 H/M 비율 증가는 하위운동신경(LMN) 손상이 아닌 중추성 경직(Spasticity)을 나타냅니다.")

    if stats["f_wave_abnorm"] >= 2 and stats["motor_abnorm"] == 0:
        scores["급성 다발신경뿌리병증 (GBS 초기 의심)"] += 10
        lesion_tags.add("근위부 신경뿌리(탈수초성)")
        reasons.append("말단 신경전도는 정상에 가까우나 여러 F파가 지연/소실되어 초기 길랭-바레 증후군 등 근위부 병변을 강력히 시사합니다.")
    
    if stats["h_reflex_abnorm"] > 0 and tracking["tibial_ncs"] and not is_lumbar_root:
        scores["S1 신경뿌리/근위부 경로 이상 (S1 Radiculopathy)"] += 8
        reasons.append("S1 분절을 경유하는 H반사가 지연/소실되어 S1 신경뿌리 병변이 의심됩니다.")

    if stats["blink_abnorm"] > 0:
        scores["삼차-안면신경 반사경로 편측 이상"] += 10
        lesion_tags.add("뇌신경 반사경로")
        reasons.append("눈깜빡반사 검사 이상으로 뇌줄기를 경유하는 뇌신경(삼차-안면) 회로 문제가 확인됩니다.")

    if len(abnormal_items) == 0:
        scores["정상 또는 이상 소견 없음"] += 1
        reasons.append("비정상 기준을 충족하는 항목이 입력되지 않았습니다.")

    if not scores:
        scores["비특이적 소견 (추가 검사 요망)"] += 1
        reasons.append("입력된 조합만으로는 단일 질환으로 국소화(Localization)하기 어렵습니다.")

    # 4. 결과 정리 및 정렬
    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    final_dx = ranked[0][0]

    # 교육 목적을 위해 1위 질환에 따른 "반드시 감별해야 할 질환(Preferred diff map)" 연결
    preferred_diff_map = {
        "원위부 정중신경병증 (손목굴증후군, CTS)": ["근위부 정중신경병증 (Proximal Median Neuropathy)", "목 신경뿌리병증 (Cervical Radiculopathy)"],
        "근위부 정중신경병증 (Proximal Median Neuropathy)": ["원위부 정중신경병증 (손목굴증후군, CTS)", "목 신경뿌리병증 (Cervical Radiculopathy)"],
        "팔꿈치부 자신경병증 (Cubital Tunnel Syndrome)": ["목 신경뿌리병증 (Cervical Radiculopathy)", "팔신경얼기병증 (Brachial Plexopathy)"],
        "자신경병증 (Ulnar Neuropathy)": ["팔꿈치부 자신경병증 (Cubital Tunnel Syndrome)", "목 신경뿌리병증 (Cervical Radiculopathy)"],
        "노신경병증 (Radial Neuropathy)": ["목 신경뿌리병증 (Cervical Radiculopathy)", "팔신경얼기병증 (Brachial Plexopathy)"],
        "종아리신경병증 (Peroneal Neuropathy)": ["허리 신경뿌리병증 (Lumbar Radiculopathy)", "허리엉치신경얼기병증 (Lumbosacral Plexopathy)"],
        "정강신경병증 (Tibial Neuropathy)": ["허리 신경뿌리병증 (Lumbar Radiculopathy)", "S1 신경뿌리/근위부 경로 이상 (S1 Radiculopathy)"],
        "목 신경뿌리병증 (Cervical Radiculopathy)": ["원위부 정중신경병증 (손목굴증후군, CTS)", "팔신경얼기병증 (Brachial Plexopathy)"],
        "허리 신경뿌리병증 (Lumbar Radiculopathy)": ["종아리신경병증 (Peroneal Neuropathy)", "허리엉치신경얼기병증 (Lumbosacral Plexopathy)"]
    }

    score_dict = dict(ranked)
    diff_names = []

    # 1. 맵핑된 강제 감별진단 먼저 추가
    for name in preferred_diff_map.get(final_dx, []):
        if name != final_dx and name not in diff_names:
            diff_names.append(name)

    # 2. 점수가 높은 순으로 남은 것들 추가
    for name, _ in ranked:
        if name != final_dx and name not in diff_names:
            diff_names.append(name)

    # 최종 Top 3 선정
    top3_names = [final_dx] + diff_names[:2]

    for dx in top3_names:
        top3_details.append({
            "name": dx,
            "how_to_differentiate": build_diff_dx_details(dx)
        })

    top3 = [(dx, score_dict.get(dx, 0)) for dx in top3_names]

    return {
        "age": age,
        "sex": sex,
        "side": side,
        "final_dx": final_dx,
        "top3": top3,
        "top3_details": top3_details,
        "severity": severity_text(stats["sensory_abnorm"] + stats["motor_abnorm"] + stats["muscle_abnorm"], stats["no_response_count"]),
        "lesion_tags": sorted(lesion_tags) if lesion_tags else ["특이 태그 없음"],
        "reasons": reasons,
        "suggestions": sorted(suggestions),
        "involved_nerves": ", ".join(sorted(involved_nerves)) if involved_nerves else "특이 소견 없음",
        "involved_levels": ", ".join(sorted(involved_levels)) if involved_levels else "특이 소견 없음",
        "abnormal_items": abnormal_items,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }