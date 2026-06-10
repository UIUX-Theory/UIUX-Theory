#!/usr/bin/env python3
"""§2 각 법칙별 보조 케이스 이미지 (메인 예시와 중복 X). 동일 팔레트."""
import os, math

OUT = os.path.join(os.path.dirname(__file__), "docs", "assets", "examples")
os.makedirs(OUT, exist_ok=True)

BG, INK, MID, DOM, HI, FLOOR, ACCENT, WHITE = (
    "#EBEBEB", "#5A5A5A", "#8C8C8C", "#B0B0B0",
    "#D2D2D2", "#707070", "#6541F2", "#FFFFFF",
)
TINT = "#F2EEFE"
RED, GREEN, AMBER = "#C53434", "#1F9D55", "#D97706"
W, H = 880, 460
FONT = "system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif"

def frame(inner, h=H):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" '
            f'font-family="{FONT}">'
            f'<rect width="{W}" height="{h}" rx="20" fill="{BG}"/>'
            f'{inner}</svg>')

def title(x, y, text, color=FLOOR):
    return f'<text x="{x}" y="{y}" font-size="14" font-weight="700" fill="{color}">{text}</text>'

def caption(x, y, text, color=MID):
    return f'<text x="{x}" y="{y}" font-size="12" fill="{color}">{text}</text>'

def save(name, body, h=H):
    open(os.path.join(OUT, name + ".svg"), "w").write(frame(body, h))
    print("saved", name)

# ==================== 2.1 Proximity — Spacing ratio ====================
s = title(40, 50, "라벨–필드 vs 행간 간격 비율")
# Three columns showing 1:1 (bad), 1:2 (borderline), 1:3 (good)
configs = [(60, "1 : 1  모호", 24, 24, RED),
           (340, "1 : 2  경계", 12, 24, AMBER),
           (620, "1 : 3  명확", 8, 24, GREEN)]
for (x0, lab, lf, fl, col) in configs:
    s += f'<text x="{x0}" y="90" font-size="12" font-weight="700" fill="{col}">{lab}</text>'
    y = 110
    for fi in range(3):
        s += f'<text x="{x0}" y="{y}" font-size="11" fill="{MID}">필드 {fi+1}</text>'
        s += f'<rect x="{x0}" y="{y+lf}" width="200" height="28" rx="6" fill="{WHITE}" stroke="{HI}"/>'
        # annotation arrows for first row
        if fi == 0:
            s += f'<text x="{x0+210}" y="{y+lf//2+4}" font-size="10" fill="{col}">↕ {lf}</text>'
            s += f'<text x="{x0+210}" y="{y+lf+28+fl//2+4}" font-size="10" fill="{col}">↕ {fl}</text>'
        y += lf + 28 + fl
s += caption(40, 410, "→ 라벨–필드 간격이 행간보다 명백히 작아야(1:3 이상) 라벨이 자기 필드에 묶여 보임")
save("02-1-proximity-ratio", s)

# ==================== 2.2 Similarity — Button hierarchy 4 levels ====================
s = title(40, 50, "버튼 위계 4단계 — 같은 종류는 같은 형태 (유사성)")
levels = [
    ("Primary", "주요 액션 1개", ACCENT, WHITE, "fill"),
    ("Secondary", "보조 액션 1–2개", WHITE, INK, "outline"),
    ("Tertiary", "약한 강조", TINT, ACCENT, "tint"),
    ("Ghost", "최소 강조 / 취소", None, MID, "ghost"),
]
for i, (name, desc, bg, fg, kind) in enumerate(levels):
    y = 100 + i*70
    s += f'<text x="40" y="{y+8}" font-size="13" font-weight="700" fill="{INK}">{name}</text>'
    s += f'<text x="40" y="{y+28}" font-size="11" fill="{MID}">{desc}</text>'
    bx = 280
    if kind == "fill":
        s += f'<rect x="{bx}" y="{y-8}" width="160" height="42" rx="10" fill="{bg}"/>'
    elif kind == "outline":
        s += f'<rect x="{bx}" y="{y-8}" width="160" height="42" rx="10" fill="{bg}" stroke="{DOM}" stroke-width="1.5"/>'
    elif kind == "tint":
        s += f'<rect x="{bx}" y="{y-8}" width="160" height="42" rx="10" fill="{bg}"/>'
    # ghost: no background
    s += f'<text x="{bx+80}" y="{y+18}" text-anchor="middle" font-size="13" font-weight="700" fill="{fg}">실행</text>'
    # show 3 of them grouped to demonstrate "same style for same role"
    for j in range(3):
        sx = 500 + j*120
        if kind == "fill":
            s += f'<rect x="{sx}" y="{y-8}" width="100" height="42" rx="10" fill="{bg}"/>'
        elif kind == "outline":
            s += f'<rect x="{sx}" y="{y-8}" width="100" height="42" rx="10" fill="{bg}" stroke="{DOM}" stroke-width="1.5"/>'
        elif kind == "tint":
            s += f'<rect x="{sx}" y="{y-8}" width="100" height="42" rx="10" fill="{bg}"/>'
        labels = ["저장", "삭제", "복사"]
        s += f'<text x="{sx+50}" y="{y+18}" text-anchor="middle" font-size="12" font-weight="600" fill="{fg}">{labels[j]}</text>'
save("02-2-similarity-button-hierarchy", s)

# ==================== 2.3 Common Region — Elevation system ====================
s = title(40, 50, "Elevation 시스템 — depth 위계로 figure-ground 단계화")
# 5 cards at 0/1/3/8/16dp
elevs = [(0, "Background"), (1, "Card"), (3, "Active card"), (8, "Menu / Sheet"), (16, "Modal / Dialog")]
for i, (dp, name) in enumerate(elevs):
    x = 50 + i*160
    y_top = 130
    # shadow simulation: multiple offset rectangles
    if dp > 0:
        shadow_blur = min(dp*2, 16)
        for sh in range(min(dp, 5)):
            opacity = 0.06
            s += f'<rect x="{x+sh+1}" y="{y_top+sh+2}" width="140" height="120" rx="12" fill="#000000" opacity="{opacity}"/>'
    s += f'<rect x="{x}" y="{y_top}" width="140" height="120" rx="12" fill="{WHITE}" stroke="{HI}"/>'
    s += f'<rect x="{x+16}" y="{y_top+20}" width="80" height="10" rx="5" fill="{INK}"/>'
    s += f'<rect x="{x+16}" y="{y_top+40}" width="108" height="6" rx="3" fill="{DOM}"/>'
    s += f'<rect x="{x+16}" y="{y_top+54}" width="80" height="6" rx="3" fill="{DOM}"/>'
    s += f'<text x="{x+70}" y="{y_top+148}" text-anchor="middle" font-size="13" font-weight="700" fill="{ACCENT}">{dp}dp</text>'
    s += f'<text x="{x+70}" y="{y_top+168}" text-anchor="middle" font-size="11" fill="{MID}">{name}</text>'
s += caption(40, 410, "→ 같은 elevation = 같은 위계. 모달은 16dp로 가장 강한 figure로 떠오름")
save("02-3-common-region-elevation", s)

# ==================== 2.4 Connectedness — 3 variants ====================
s = title(40, 50, "연결성 컨트롤 변형 — 같은 옵션 세트, 다른 그룹 신호")
# variant 1: segmented control (strongest connection)
s += caption(40, 100, "Segmented control — 하나의 막대(가장 강한 묶음, 상호배타적)")
opts = ["일간", "주간", "월간", "연간"]
sx, sy, sw, sh = 40, 120, 360, 40
s += f'<rect x="{sx}" y="{sy}" width="{sw}" height="{sh}" rx="10" fill="{TINT}"/>'
for i, lab in enumerate(opts):
    ox = sx + i*(sw//4)
    if i == 1:  # selected
        s += f'<rect x="{ox+4}" y="{sy+4}" width="{sw//4 - 8}" height="{sh-8}" rx="7" fill="{WHITE}"/>'
        s += f'<text x="{ox+sw//8}" y="{sy+sh//2+5}" text-anchor="middle" font-size="13" font-weight="700" fill="{ACCENT}">{lab}</text>'
    else:
        s += f'<text x="{ox+sw//8}" y="{sy+sh//2+5}" text-anchor="middle" font-size="13" font-weight="600" fill="{MID}">{lab}</text>'

# variant 2: tabs with underline
s += caption(440, 100, "Tab + underline — 콘텐츠 영역에 연결되는 약한 묶음")
tx, ty, tw = 440, 120, 360
for i, lab in enumerate(opts):
    ox = tx + i*(tw//4)
    s += f'<text x="{ox+tw//8}" y="{ty+24}" text-anchor="middle" font-size="13" font-weight="{"700" if i==1 else "600"}" fill="{ACCENT if i==1 else MID}">{lab}</text>'
    if i == 1:
        s += f'<rect x="{ox+12}" y="{ty+36}" width="{tw//4 - 24}" height="3" rx="1.5" fill="{ACCENT}"/>'
s += f'<line x1="{tx}" y1="{ty+40}" x2="{tx+tw}" y2="{ty+40}" stroke="{HI}" stroke-width="1"/>'

# variant 3: separated buttons (no connection)
s += caption(40, 220, "분리된 버튼들 — 연결 신호 없음 (관계 모호)")
bsx, bsy = 40, 240
for i, lab in enumerate(opts):
    bx = bsx + i*100
    style_fill = ACCENT if i == 1 else WHITE
    style_text = WHITE if i == 1 else INK
    s += f'<rect x="{bx}" y="{bsy}" width="84" height="38" rx="8" fill="{style_fill}" stroke="{DOM if i!=1 else "none"}" stroke-width="1.5"/>'
    s += f'<text x="{bx+42}" y="{bsy+24}" text-anchor="middle" font-size="13" font-weight="600" fill="{style_text}">{lab}</text>'

# variant 4: pills with shared row
s += caption(440, 220, "Pill chips — 같은 컨테이너 안에 인접(중간 강도)")
px, py = 440, 240
s += f'<rect x="{px-8}" y="{py-8}" width="376" height="54" rx="27" fill="{WHITE}" stroke="{HI}"/>'
for i, lab in enumerate(opts):
    cx_ = px + i*90 + 28
    if i == 1:
        s += f'<rect x="{cx_-32}" y="{py}" width="80" height="38" rx="19" fill="{ACCENT}"/>'
        s += f'<text x="{cx_+8}" y="{py+24}" text-anchor="middle" font-size="12" font-weight="700" fill="{WHITE}">{lab}</text>'
    else:
        s += f'<text x="{cx_+8}" y="{py+24}" text-anchor="middle" font-size="12" font-weight="600" fill="{MID}">{lab}</text>'

s += caption(40, 360, "→ 의미적으로 상호배타적이면 segmented, 콘텐츠 전환이면 tab, 약한 그룹이면 pill, 독립 액션이면 분리")
save("02-4-connectedness-variants", s, h=400)

# ==================== 2.5 Continuity — F-pattern ====================
s = title(40, 50, "F-패턴 — 텍스트 중심 페이지의 시선 동선")
# layout: heading bar + 3 paragraph blocks + sidebar
# eye tracking heatmap: stronger on top + left
# Page mock
s += f'<rect x="40" y="90" width="800" height="320" rx="12" fill="{WHITE}" stroke="{HI}"/>'
# header
s += f'<rect x="60" y="110" width="280" height="16" rx="8" fill="{INK}"/>'
# paragraphs
y = 150
for plen in [[760, 700, 720, 640], [560, 520, 480, 440], [440, 400, 360]]:
    for lw in plen:
        s += f'<rect x="60" y="{y}" width="{lw}" height="8" rx="4" fill="{DOM}"/>'
        y += 18
    y += 16
# F-shaped overlay (heatmap)
# top horizontal bar
s += f'<rect x="60" y="106" width="780" height="32" rx="4" fill="{ACCENT}" opacity="0.20"/>'
# second horizontal (smaller)
s += f'<rect x="60" y="170" width="540" height="22" rx="4" fill="{ACCENT}" opacity="0.15"/>'
# vertical stem (left side)
s += f'<rect x="60" y="138" width="160" height="240" rx="4" fill="{ACCENT}" opacity="0.10"/>'
# Annotations
s += f'<text x="650" y="130" font-size="11" font-weight="700" fill="{ACCENT}">① 헤드라인</text>'
s += f'<text x="650" y="186" font-size="11" font-weight="700" fill="{ACCENT}">② 첫 단락 첫 줄</text>'
s += f'<text x="650" y="280" font-size="11" font-weight="700" fill="{ACCENT}">③ 좌측 시선 트랙</text>'
s += caption(40, 440, "→ 헤드라인과 좌측 정렬 콘텐츠의 처음 단어가 가장 많이 읽힘 (NN/g eye-tracking)")
save("02-5-continuity-f-pattern", s, h=470)

# ==================== 2.6 Closure — Skeleton screen ====================
s = title(40, 50, "Skeleton screen — 폐쇄성으로 곧 채워질 구조를 미리 보임")
# Two side-by-side: spinner vs skeleton
s += caption(40, 90, "Spinner — '뭔가 로딩 중'만 알림")
s += f'<rect x="40" y="110" width="380" height="280" rx="12" fill="{WHITE}" stroke="{HI}"/>'
# spinner
import math as m
cx, cy = 230, 250
for i in range(8):
    ang = i * 45
    x1 = cx + 18 * m.cos(m.radians(ang))
    y1 = cy + 18 * m.sin(m.radians(ang))
    x2 = cx + 30 * m.cos(m.radians(ang))
    y2 = cy + 30 * m.sin(m.radians(ang))
    opacity = 0.2 + (i / 8) * 0.8
    s += f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{ACCENT}" stroke-width="4" stroke-linecap="round" opacity="{opacity:.2f}"/>'

s += caption(460, 90, "Skeleton — 콘텐츠 형태를 미리 인지 (체감 시간 ↓)")
s += f'<rect x="460" y="110" width="380" height="280" rx="12" fill="{WHITE}" stroke="{HI}"/>'
# avatar circle
s += f'<circle cx="495" cy="145" r="20" fill="{HI}"/>'
# name + meta
s += f'<rect x="525" y="135" width="120" height="12" rx="6" fill="{HI}"/>'
s += f'<rect x="525" y="155" width="80" height="8" rx="4" fill="{HI}" opacity="0.7"/>'
# image placeholder
s += f'<rect x="480" y="190" width="340" height="100" rx="8" fill="{HI}"/>'
# body lines
s += f'<rect x="480" y="306" width="320" height="10" rx="5" fill="{HI}"/>'
s += f'<rect x="480" y="324" width="280" height="10" rx="5" fill="{HI}"/>'
s += f'<rect x="480" y="342" width="200" height="10" rx="5" fill="{HI}"/>'
s += caption(40, 420, "→ 사용자가 마음속에서 구조를 완성 — 같은 로딩 시간이라도 더 빠르게 느낌")
save("02-6-closure-skeleton", s)

# ==================== 2.7 Figure-Ground — Interactive states ====================
s = title(40, 50, "버튼 상태별 figure-ground 단계")
states = [
    ("Default", "기본 상태", ACCENT, WHITE, 1.0, 0),
    ("Hover", "마우스 위", "#5634D9", WHITE, 1.0, 4),
    ("Focus", "키보드 포커스", ACCENT, WHITE, 1.0, 0, True),
    ("Active", "누르는 중", "#4527B8", WHITE, 0.98, 0),
    ("Disabled", "비활성 (ground로 물러남)", HI, MID, 1.0, 0),
]
for i, st in enumerate(states):
    name, desc, bg, fg, scale, shadow = st[:6]
    has_focus = len(st) > 6
    y = 100 + i*64
    s += f'<text x="40" y="{y+10}" font-size="13" font-weight="700" fill="{INK}">{name}</text>'
    s += f'<text x="40" y="{y+30}" font-size="11" fill="{MID}">{desc}</text>'
    bx, by, bw, bh = 320, y-12, 160, 42
    # shadow
    if shadow > 0:
        s += f'<rect x="{bx+2}" y="{by+shadow}" width="{bw}" height="{bh}" rx="10" fill="#000000" opacity="0.15"/>'
    # focus ring
    if has_focus:
        s += f'<rect x="{bx-4}" y="{by-4}" width="{bw+8}" height="{bh+8}" rx="13" fill="none" stroke="{ACCENT}" stroke-width="3" opacity="0.4"/>'
    s += f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="10" fill="{bg}"/>'
    s += f'<text x="{bx+bw/2}" y="{by+bh/2+5}" text-anchor="middle" font-size="13" font-weight="700" fill="{fg}">발행하기</text>'
    # describe what changed
    notes = ["기본 fill 색", "10% darker + shadow", "ring 3px (WCAG 2.4.7)", "20% darker (눌림)", "opacity ↓ + ground화"]
    s += f'<text x="510" y="{y+10}" font-size="11" fill="{MID}">{notes[i]}</text>'
save("02-7-figure-ground-states", s)

# ==================== 2.8 Common Fate — Tab indicator slide ====================
s = title(40, 50, "Tab indicator slide — 공동운명으로 '같은 시스템' 학습")
# Two frames
# Frame 1: before
s += caption(40, 100, "[프레임 A] 첫 번째 탭 선택")
y0 = 130
tabs = ["개요", "활동", "설정", "권한"]
fw = 380
tab_w = fw // 4
for i, lab in enumerate(tabs):
    x = 40 + i * tab_w
    s += f'<text x="{x + tab_w//2}" y="{y0+24}" text-anchor="middle" font-size="13" font-weight="{"700" if i==0 else "600"}" fill="{ACCENT if i==0 else MID}">{lab}</text>'
s += f'<line x1="40" y1="{y0+40}" x2="{40+fw}" y2="{y0+40}" stroke="{HI}" stroke-width="1"/>'
s += f'<rect x="{40+12}" y="{y0+37}" width="{tab_w-24}" height="3" rx="1.5" fill="{ACCENT}"/>'

# Arrow / motion
s += f'<text x="40" y="{y0+90}" font-size="20" fill="{ACCENT}">↓ 두 번째 탭 클릭 — 인디케이터가 슬라이드</text>'
s += f'<path d="M{40+tab_w//2} {y0+95} Q {40+tab_w} {y0+115} {40+tab_w + tab_w//2} {y0+105}" fill="none" stroke="{ACCENT}" stroke-width="2" stroke-dasharray="4 4"/>'
s += f'<polygon points="{40+tab_w+tab_w//2-5},{y0+102} {40+tab_w+tab_w//2+5},{y0+108} {40+tab_w+tab_w//2-3},{y0+112}" fill="{ACCENT}"/>'

# Frame 2: after
y1 = y0 + 180
s += caption(40, y1-30, "[프레임 B] 두 번째 탭 활성 — 인디케이터가 자연스럽게 이동")
for i, lab in enumerate(tabs):
    x = 40 + i * tab_w
    s += f'<text x="{x + tab_w//2}" y="{y1+24}" text-anchor="middle" font-size="13" font-weight="{"700" if i==1 else "600"}" fill="{ACCENT if i==1 else MID}">{lab}</text>'
s += f'<line x1="40" y1="{y1+40}" x2="{40+fw}" y2="{y1+40}" stroke="{HI}" stroke-width="1"/>'
s += f'<rect x="{40+tab_w+12}" y="{y1+37}" width="{tab_w-24}" height="3" rx="1.5" fill="{ACCENT}"/>'

# Right side: explanation
s += f'<rect x="500" y="100" width="340" height="320" rx="12" fill="{WHITE}" stroke="{HI}"/>'
s += f'<text x="520" y="130" font-size="13" font-weight="700" fill="{INK}">왜 슬라이드인가?</text>'
notes = [
    "• 인디케이터가 함께 움직이면",
    "  탭들이 '한 시스템'으로 인지",
    "",
    "• 점프 트랜지션은 시각 단절",
    "  → 사용자가 위치를 잃음",
    "",
    "• 200–250ms ease-in-out 권장",
    "• 콘텐츠 영역도 fade로 함께 전환",
]
for i, line in enumerate(notes):
    s += f'<text x="520" y="{160+i*22}" font-size="12" fill="{MID}">{line}</text>'
save("02-8-common-fate-tab-slide", s)

# ==================== 2.9 Symmetry — 8pt grid baseline ====================
s = title(40, 50, "8pt 그리드 시스템 — 모든 간격·크기를 8의 배수로")
# Background grid
for i in range(0, W, 8):
    op = "0.3" if i % 32 == 0 else "0.12"
    s += f'<line x1="{i}" y1="80" x2="{i}" y2="430" stroke="{ACCENT}" stroke-width="0.5" opacity="{op}"/>'
for j in range(80, 430, 8):
    op = "0.3" if (j-80) % 32 == 0 else "0.12"
    s += f'<line x1="40" y1="{j}" x2="840" y2="{j}" stroke="{ACCENT}" stroke-width="0.5" opacity="{op}"/>'
# Sample card on grid: w=320 (8*40), h=192 (8*24), padding 24 (8*3)
cx_, cy_ = 80, 112
s += f'<rect x="{cx_}" y="{cy_}" width="320" height="192" rx="8" fill="{WHITE}" stroke="{ACCENT}" stroke-width="2"/>'
s += f'<rect x="{cx_+24}" y="{cy_+24}" width="120" height="16" rx="4" fill="{INK}"/>'
s += f'<rect x="{cx_+24}" y="{cy_+56}" width="272" height="8" rx="4" fill="{DOM}"/>'
s += f'<rect x="{cx_+24}" y="{cy_+72}" width="200" height="8" rx="4" fill="{DOM}"/>'
s += f'<rect x="{cx_+24}" y="{cy_+104}" width="96" height="40" rx="8" fill="{ACCENT}"/>'
s += f'<text x="{cx_+72}" y="{cy_+130}" text-anchor="middle" font-size="13" font-weight="700" fill="{WHITE}">실행</text>'
# Annotations
s += f'<text x="440" y="130" font-size="12" font-weight="700" fill="{ACCENT}">카드 320 × 192 (8 × 40, 8 × 24)</text>'
s += f'<text x="440" y="156" font-size="12" fill="{MID}">패딩 24 (8 × 3) — 외부 여백도 8의 배수</text>'
s += f'<text x="440" y="182" font-size="12" fill="{MID}">제목 16 / 본문 8 — 행 높이 4의 배수 (sub-8pt)</text>'
s += f'<text x="440" y="208" font-size="12" fill="{MID}">버튼 96 × 40 → CTA가 그리드에 정확히 안착</text>'
s += f'<text x="440" y="252" font-size="13" font-weight="700" fill="{INK}">왜 8pt인가?</text>'
s += f'<text x="440" y="278" font-size="12" fill="{MID}">• 1x/1.5x/2x/3x 모든 디바이스 해상도에서 정수</text>'
s += f'<text x="440" y="296" font-size="12" fill="{MID}">• 디자이너·개발자 spec 협업이 단순해짐</text>'
s += f'<text x="440" y="314" font-size="12" fill="{MID}">• 그리드에 자동 안착 → 정렬·균형 노력 ↓</text>'
s += f'<text x="440" y="332" font-size="12" fill="{MID}">• Material·HIG·Atlassian 등 대부분 채택</text>'
save("02-9-symmetry-8pt-grid", s)

print("DONE")
