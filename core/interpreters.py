# 교육용 근전도 정상 참고치 (Educational Reference Cut-offs)
# (진폭 하한치, 잠복기 상한치)
# 감각신경(Sensory): 진폭(uV), 잠복기(ms)
# 운동신경(Motor): 진폭(mV), 잠복기(ms)
NCS_CUTOFFS = {
    "정중신경 감각신경활동전위 (Median SNAP)": (20.0, 3.5),
    "자신경 감각신경활동전위 (Ulnar SNAP)": (10.0, 3.1),
    "노신경 감각신경활동전위 (Radial SNAP)": (15.0, 2.9),
    "장딴지신경 감각신경활동전위 (Sural SNAP)": (6.0, 4.2),
    "얕은종아리신경 감각신경활동전위 (Superficial Peroneal SNAP)": (6.0, 4.4),

    "정중신경 복합근육활동전위 (Median CMAP)": (4.0, 4.4),
    "자신경 복합근육활동전위 (Ulnar CMAP)": (3.0, 3.3),
    "노신경 복합근육활동전위 (Radial CMAP)": (2.0, 3.3),
    "종아리신경 복합근육활동전위 (Peroneal CMAP)": (2.0, 6.0),
    "정강신경 복합근육활동전위 (Tibial CMAP)": (4.0, 6.0),
}


def evaluate_ncs_numeric(item, domain, amp, lat):
    """실제 수치를 입력받아 상태(정상, 감소, 지연, 무반응)를 자동 판독합니다."""
    if amp == 0.0 and lat == 0.0:
        return "무반응 (No response)", "무반응 (No response)"

    # 기본값 설정 (목록에 없는 신경인 경우)
    default_sensory = (10.0, 3.5)
    default_motor = (3.0, 5.0)

    cutoff = NCS_CUTOFFS.get(item)
    if not cutoff:
        cutoff = default_sensory if domain == "sensory" else default_motor

    amp_cutoff, lat_cutoff = cutoff

    # 판독 로직
    amp_status = "정상 (Normal)" if amp >= amp_cutoff else "감소 (Reduced)"
    lat_status = "정상 (Normal)" if lat <= lat_cutoff else "잠복기 지연 (Delayed latency)"

    # 진폭이 0에 수렴하면 무반응 처리
    if amp <= 0.1:
        amp_status = "무반응 (No response)"
        lat_status = "무반응 (No response)"

    return amp_status, lat_status


def compose_ncs_result(distal_amp, distal_lat, proximal_amp=None, proximal_lat=None):
    tags = []

    def build_segment_text(seg_name, amp, lat):
        if amp == "무반응 (No response)":
            return f"{seg_name} 무반응"

        parts = []
        if amp == "감소 (Reduced)":
            parts.append("감소 (Reduced)")
        if lat == "잠복기 지연 (Delayed latency)":
            parts.append("잠복기 지연 (Delayed latency)")

        if parts:
            return f"{' 및 '.join(parts)}"
        return ""

    distal_text = build_segment_text("원위부", distal_amp, distal_lat)
    if distal_text:
        tags.append(distal_text)

    if proximal_amp is not None or proximal_lat is not None:
        proximal_text = build_segment_text("근위부", proximal_amp, proximal_lat)
        if proximal_text:
            tags.append(proximal_text)

    return "정상 (Normal)" if not tags else " / ".join(tags)


def compose_fwave_result(latency_status, response_status):
    if response_status == "소실 (Absent)":
        return "지연 또는 소실 (Delayed/Absent)"
    if latency_status == "잠복기 지연 (Delayed latency)":
        return "지연 또는 소실 (Delayed/Absent)"
    return "정상 (Normal)"


def compute_hm_ratio_text(hmax, mmax):
    try:
        h = float(hmax)
        m = float(mmax)
        if m <= 0:
            return None, "계산 불가"
        ratio = h / m
        percent = ratio * 100
        return ratio, f"{ratio:.3f} ({percent:.1f}%)"
    except Exception:
        return None, "계산 불가"


def interpret_hm_ratio(ratio):
    if ratio is None:
        return {
            "label": "계산 불가",
            "detail": "Mmax가 0이거나 입력되지 않아 H/M 비율을 계산할 수 없습니다.",
            "warning": "※ H/M 비율은 교육용 참고 지표입니다."
        }

    if ratio < 0.30:
        return {
            "label": "낮거나 뚜렷한 항진 소견 없음",
            "detail": "교육용 기준에서 반사 흥분성 증가를 강하게 시사하지는 않습니다.",
            "warning": "※ 조건에 따라 값이 달라질 수 있습니다."
        }

    if ratio <= 0.60:
        return {
            "label": "일반 범위 가능",
            "detail": "교육용 기준에서 일반 범위로 해석할 수 있습니다.",
            "warning": "※ 단독 수치보다 임상 소견과 함께 해석해야 합니다."
        }

    return {
        "label": "증가 가능",
        "detail": "교육용 기준에서 H/M 비율 증가 가능 범위입니다.",
        "warning": "※ 단독으로 경직을 확정하지 않습니다."
    }


def get_domain_options(domain, item=None):
    if domain in ["sensory", "motor"]:
        return ["정상 (Normal)", "감소 (Reduced)", "잠복기 지연 (Delayed latency)", "무반응 (No response)"]

    if domain == "muscle":
        return [
            "정상 (Normal)",
            "비정상 자발전위 (Fibrillation, Positive sharp wave 등) 출현",
            "무반응 / 전기적 침묵 (Electrical silence)"
        ]

    if domain == "h_reflex":
        return ["정상 (Normal)"]

    if domain == "f_wave":
        return ["정상 (Normal)", "지연 (Delayed)", "소실 (Absent)"]

    if domain == "blink":
        return ["정상 (Normal)", "지연 (Delayed)", "소실 (Absent)"]

    return ["정상 (Normal)"]