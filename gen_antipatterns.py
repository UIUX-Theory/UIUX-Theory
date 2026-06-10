#!/usr/bin/env python3
"""5장 안티패턴 6개 각각의 ✗ vs ✓ 비교 SVG 생성. gen_examples.py와 동일 팔레트."""
import os

OUT = os.path.join(os.path.dirname(__file__), "docs", "assets", "examples")
os.makedirs(OUT, exist_ok=True)

BG, INK, MID, DOM, HI, FLOOR, ACCENT, WHITE = (
    "#EBEBEB", "#5A5A5A", "#8C8C8C", "#B0B0B0",
    "#D2D2D2", "#707070", "#6541F2", "#FFFFFF",
)
TINT = "#F2EEFE"  # accent 12% tint
W, H = 880, 460
FONT = "system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif"

def frame(inner):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
            f'font-family="{FONT}">'
            f'<rect width="{W}" height="{H}" rx="20" fill="{BG}"/>'
            f'{inner}</svg>')

def label(x, y, text, ok):
    color = "#C53434" if not ok else ACCENT
    mark = "✗" if not ok else "✓"
    return (f'<text x="{x}" y="{y}" font-size="14" font-weight="700" '
            f'fill="{color}">{mark} {text}</text>')

def save(name, body):
    open(os.path.join(OUT, name + ".svg"), "w").write(frame(body))
    print("saved", name)

# divider line between left/right halves
DIV = f'<line x1="440" y1="40" x2="440" y2="{H-40}" stroke="{HI}" stroke-width="1" stroke-dasharray="4 6"/>'

# 05-1 어중간한 간격 — 모호한 행간 vs 명확한 그룹 간격
s = DIV
s += label(40, 60, "모호한 간격 — 그룹이 안 보임", False)
# Both columns end at last-box-bottom y≈410 (≈50px margin top & bottom in H=460)
# Left: 6 evenly-spaced boxes, pitch 57
for i in range(6):
    y = 90 + i*57
    s += f'<rect x="40" y="{y}" width="360" height="34" rx="6" fill="{WHITE}" stroke="{HI}"/>'
    s += f'<rect x="58" y="{y+8}" width="180" height="10" rx="5" fill="{INK}"/>'
    s += f'<rect x="58" y="{y+22}" width="240" height="6" rx="3" fill="{DOM}"/>'
s += label(460, 60, "그룹 간격 대비 — 3+3 묶음", True)
# Right: top group [90, 138, 186], bottom group [280, 328, 376] — group gap 60
ys = [90, 138, 186, 280, 328, 376]
for i, y in enumerate(ys):
    s += f'<rect x="460" y="{y}" width="360" height="34" rx="6" fill="{WHITE}" stroke="{HI}"/>'
    s += f'<rect x="478" y="{y+8}" width="180" height="10" rx="5" fill="{INK}"/>'
    s += f'<rect x="478" y="{y+22}" width="240" height="6" rx="3" fill="{DOM}"/>'
save("05-1-spacing", s)

# 05-2 유사성 과용 — 모든 버튼 같은 색 vs 주요 CTA만 채움
s = DIV
s += label(40, 60, "모든 버튼 동일 강조 — 위계 소실", False)
for i, lab in enumerate(["뒤로", "초기화", "임시저장", "발행"]):
    y = 110 + i*60
    s += f'<rect x="60" y="{y}" width="340" height="42" rx="10" fill="{ACCENT}"/>'
    s += f'<text x="230" y="{y+27}" text-anchor="middle" font-size="14" font-weight="700" fill="{WHITE}">{lab}</text>'
s += label(460, 60, "주요 CTA만 차별화 — 위계 회복", True)
specs = [("뒤로", "ghost"), ("초기화", "ghost"), ("임시저장", "outline"), ("발행", "primary")]
for i, (lab, kind) in enumerate(specs):
    y = 110 + i*60
    if kind == "primary":
        s += f'<rect x="480" y="{y}" width="340" height="42" rx="10" fill="{ACCENT}"/>'
        s += f'<text x="650" y="{y+27}" text-anchor="middle" font-size="14" font-weight="700" fill="{WHITE}">{lab}</text>'
    elif kind == "outline":
        s += f'<rect x="480" y="{y}" width="340" height="42" rx="10" fill="{WHITE}" stroke="{DOM}" stroke-width="1.5"/>'
        s += f'<text x="650" y="{y+27}" text-anchor="middle" font-size="14" font-weight="600" fill="{INK}">{lab}</text>'
    else:
        s += f'<text x="650" y="{y+27}" text-anchor="middle" font-size="14" font-weight="600" fill="{MID}">{lab}</text>'
save("05-2-similarity-overuse", s)

# 05-3 상자 천지 — 모든 그룹 박스 vs 여백 위주
s = DIV
s += label(40, 60, "상자 천지 — 시각 복잡도 폭발", False)
boxes = [(60, 90, 360, 90), (60, 196, 174, 70), (246, 196, 174, 70), (60, 282, 360, 60)]
for (x, y, w, h) in boxes:
    s += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{WHITE}" stroke="{ACCENT}" stroke-width="2"/>'
    s += f'<rect x="{x+14}" y="{y+14}" width="{min(160,w-28)}" height="10" rx="5" fill="{INK}"/>'
    s += f'<rect x="{x+14}" y="{y+32}" width="{w-40}" height="6" rx="3" fill="{DOM}"/>'
s += label(460, 60, "여백 우선 — 박스 없이도 묶임", True)
# same content but separated by gaps, no borders
s += f'<rect x="478" y="104" width="160" height="10" rx="5" fill="{INK}"/>'
s += f'<rect x="478" y="122" width="320" height="6" rx="3" fill="{DOM}"/>'
s += f'<rect x="478" y="134" width="280" height="6" rx="3" fill="{DOM}"/>'
s += f'<rect x="478" y="200" width="120" height="10" rx="5" fill="{INK}"/>'
s += f'<rect x="478" y="218" width="160" height="6" rx="3" fill="{DOM}"/>'
s += f'<rect x="650" y="200" width="120" height="10" rx="5" fill="{INK}"/>'
s += f'<rect x="650" y="218" width="160" height="6" rx="3" fill="{DOM}"/>'
s += f'<rect x="478" y="290" width="160" height="10" rx="5" fill="{INK}"/>'
s += f'<rect x="478" y="308" width="320" height="6" rx="3" fill="{DOM}"/>'
save("05-3-box-everywhere", s)

# 05-3b 상자 천지 — 카드 안의 카드 (nested) vs 단일 카드 + 여백
s = DIV
s += label(40, 60, "중첩 카드 — 깊이 인지 혼란", False)
# Outer card y=90 h=302; 3 inner cards h=78 with 14px gaps; 20px outer padding top/bottom
s += f'<rect x="40" y="90" width="380" height="302" rx="14" fill="{WHITE}" stroke="{ACCENT}" stroke-width="2"/>'
for i, y in enumerate([110, 202, 294]):
    s += f'<rect x="58" y="{y}" width="344" height="78" rx="10" fill="{TINT}" stroke="{ACCENT}" stroke-width="1.5"/>'
    s += f'<rect x="76" y="{y+18}" width="140" height="10" rx="5" fill="{INK}"/>'
    s += f'<rect x="76" y="{y+38}" width="280" height="26" rx="8" fill="{WHITE}" stroke="{DOM}"/>'
s += label(460, 60, "단일 카드 + 섹션 여백", True)
s += f'<rect x="460" y="90" width="380" height="320" rx="14" fill="{WHITE}" stroke="{HI}"/>'
for i, y in enumerate([114, 218, 322]):
    s += f'<rect x="480" y="{y}" width="140" height="10" rx="5" fill="{INK}"/>'
    s += f'<rect x="480" y="{y+18}" width="320" height="8" rx="4" fill="{DOM}"/>'
    s += f'<rect x="480" y="{y+32}" width="260" height="8" rx="4" fill="{DOM}"/>'
    if i < 2:
        s += f'<line x1="480" y1="{y+66}" x2="820" y2="{y+66}" stroke="{HI}" stroke-width="1" stroke-dasharray="2 4"/>'
save("05-3b-nested-cards", s)

# 05-3c 상자 천지 — 모든 폼 필드를 박스로 감싸기 vs 라벨+필드만
s = DIV
s += label(40, 60, "필드마다 카드 — 폼 산만", False)
fields = ["이메일", "이름", "전화번호", "회사명"]
for i, lab in enumerate(fields):
    y = 96 + i*78
    # outer card wrapping label + field
    s += f'<rect x="40" y="{y}" width="380" height="62" rx="12" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.5"/>'
    s += f'<text x="60" y="{y+22}" font-size="12" fill="{MID}">{lab}</text>'
    s += f'<rect x="60" y="{y+30}" width="340" height="22" rx="6" fill="{BG}" stroke="{DOM}"/>'
s += label(460, 60, "라벨 + 필드만 — 간결", True)
for i, lab in enumerate(fields):
    y = 96 + i*78
    s += f'<text x="460" y="{y+12}" font-size="12" fill="{INK}" font-weight="600">{lab}</text>'
    s += f'<rect x="460" y="{y+22}" width="360" height="36" rx="8" fill="{WHITE}" stroke="{DOM}"/>'
save("05-3c-boxed-fields", s)

# 05-4 전부 강조 = 강조 없음 — 모든 텍스트 색/굵게 vs 핵심만 강조
s = DIV
s += label(40, 60, "전부 강조 — 핵심 사라짐", False)
for i in range(5):
    y = 100 + i*50
    s += f'<rect x="60" y="{y}" width="340" height="12" rx="6" fill="{ACCENT}"/>'
    s += f'<rect x="60" y="{y+20}" width="280" height="10" rx="5" fill="{ACCENT}"/>'
s += label(460, 60, "한 곳만 강조 — 핵심 부각", True)
for i in range(5):
    y = 100 + i*50
    text_color = ACCENT if i == 2 else MID
    bar_color = ACCENT if i == 2 else HI
    s += f'<rect x="480" y="{y}" width="340" height="12" rx="6" fill="{bar_color}"/>'
    s += f'<rect x="480" y="{y+20}" width="280" height="10" rx="5" fill="{bar_color}"/>'
save("05-4-emphasis-everywhere", s)

# 05-5 과한 폐쇄성/생략 — 너무 잘린 도형 vs 충분한 단서
s = DIV
s += label(40, 60, "과한 생략 — 형태 인식 실패", False)
# almost nothing: tiny disconnected dots that don't suggest the shape
import math
cx, cy, r = 220, 250, 90
for ang in [10, 80, 150, 220, 290]:
    x = cx + r*math.cos(math.radians(ang))
    y = cy + r*math.sin(math.radians(ang))
    s += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3" fill="{INK}"/>'
s += label(460, 60, "충분한 단서 — 원이 보임", True)
cx2 = 660
# many small dots tracing the circle
for ang in range(0, 360, 18):
    x = cx2 + r*math.cos(math.radians(ang))
    y = cy + r*math.sin(math.radians(ang))
    s += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="{INK}"/>'
save("05-5-over-closure", s)

# 05-6 저대비 텍스트 — 배경 위 회색 텍스트 vs 오버레이 + 진한 텍스트
s = DIV
s += label(40, 60, "저대비 — 텍스트 묻힘", False)
s += f'<rect x="60" y="90" width="340" height="240" rx="14" fill="{DOM}"/>'
# faint white text
s += f'<text x="80" y="138" font-size="22" font-weight="800" fill="#CDCDCD">캠페인 시작</text>'
s += f'<text x="80" y="170" font-size="13" fill="#BFBFBF">매주 화요일 추첨 이벤트</text>'
s += f'<rect x="80" y="200" width="130" height="38" rx="10" fill="#BFBFBF"/>'
s += f'<text x="145" y="225" text-anchor="middle" font-size="13" font-weight="700" fill="#FFFFFF" opacity="0.7">자세히 보기</text>'
s += label(460, 60, "오버레이 + 고대비 — 명확", True)
s += f'<rect x="480" y="90" width="340" height="240" rx="14" fill="{DOM}"/>'
# dark gradient overlay
s += '<defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#000" stop-opacity="0.05"/><stop offset="1" stop-color="#000" stop-opacity="0.55"/></linearGradient></defs>'
s += f'<rect x="480" y="90" width="340" height="240" rx="14" fill="url(#g)"/>'
s += f'<text x="500" y="200" font-size="22" font-weight="800" fill="#FFFFFF">캠페인 시작</text>'
s += f'<text x="500" y="232" font-size="13" fill="#FFFFFF" opacity="0.85">매주 화요일 추첨 이벤트</text>'
s += f'<rect x="500" y="262" width="130" height="38" rx="10" fill="{ACCENT}"/>'
s += f'<text x="565" y="287" text-anchor="middle" font-size="13" font-weight="700" fill="#FFFFFF">자세히 보기</text>'
save("05-6-low-contrast", s)

print("DONE")
