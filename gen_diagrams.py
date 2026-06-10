#!/usr/bin/env python3
"""게슈탈트 원리 설명용 추상 다이어그램 생성 (SVG + PNG). 브랜드 톤: grayscale + accent (#6541F2)."""
import math, cairosvg, os

ASSETS = os.path.join(os.path.dirname(__file__), "assets")
os.makedirs(ASSETS, exist_ok=True)

BG      = "#EBEBEB"
HI      = "#D2D2D2"
DOM     = "#B0B0B0"
MID     = "#8C8C8C"
FLOOR   = "#707070"
ACCENT   = "#6541F2"
INK     = "#5A5A5A"
W, H    = 720, 360

def frame(inner):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}">'
            f'<rect x="0" y="0" width="{W}" height="{H}" rx="16" fill="{BG}"/>'
            f'{inner}</svg>')

def dot(cx, cy, r=20, fill=MID, **kw):
    extra = "".join(f' {k.replace("_","-")}="{v}"' for k,v in kw.items())
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"{extra}/>'

def save(name, svg):
    svg_path = os.path.join(ASSETS, name + ".svg")
    png_path = os.path.join(ASSETS, name + ".png")
    with open(svg_path, "w") as f:
        f.write(svg)
    cairosvg.svg2png(bytestring=svg.encode(), write_to=png_path,
                     output_width=W*2, output_height=H*2)
    print("saved", name)

# 01 프레그난츠: 겹친 두 단순 도형 → 복잡함을 단순한 두 형태로 본다
s = ''
s += f'<rect x="240" y="95" width="180" height="180" rx="14" fill="{MID}" opacity="0.9"/>'
s += f'<circle cx="470" cy="200" r="98" fill="{ACCENT}" opacity="0.88"/>'
save("01-pragnanz", frame(s))

# 02-1 근접성: 좌(균등 그리드) vs 우(3개 클러스터)
s = ''
# divider
s += f'<line x1="360" y1="60" x2="360" y2="300" stroke="{HI}" stroke-width="2" stroke-dasharray="6 8"/>'
# left even grid 3x3
for i in range(3):
    for j in range(3):
        s += dot(80 + j*90, 110 + i*70)
# right 3 clusters of 3 (triangles), well separated
clusters = [(450,120),(610,120),(530,250)]
for (cx,cy) in clusters:
    s += dot(cx-22, cy+14); s += dot(cx+22, cy+14); s += dot(cx, cy-22)
save("02-1-proximity", frame(s))

# 02-2 유사성: 5x4 그리드, 2번째 행만 앰버 → 가로 띠로 묶임
s = ''
for r in range(4):
    for c in range(5):
        fill = ACCENT if r == 1 else DOM
        s += dot(120 + c*120, 90 + r*65, r=22, fill=fill)
save("02-2-similarity", frame(s))

# 02-3 공통영역: 2x4 균등 그리드 + 우측 2열을 박스로 묶음
s = ''
for r in range(2):
    for c in range(4):
        s += dot(150 + c*145, 140 + r*90)
s += f'<rect x="555" y="95" width="245" height="180" rx="18" fill="{ACCENT}" opacity="0.16" stroke="{ACCENT}" stroke-width="3"/>'
# move box inside frame: redo with box around right two columns (x cols at 150,295,440,585)
s = ''
cols = [150, 295, 440, 585]
for r in range(2):
    for c in range(4):
        s += dot(cols[c], 140 + r*90)
s += f'<rect x="400" y="95" width="245" height="180" rx="18" fill="{ACCENT}" opacity="0.15" stroke="{ACCENT}" stroke-width="3"/>'
save("02-3-common-region", frame(s))

# 02-4 연결성: 위(분리) vs 아래(선으로 연결 → 묶임)
s = ''
s += dot(250, 115); s += dot(470, 115)
s += f'<line x1="270" y1="255" x2="450" y2="255" stroke="{INK}" stroke-width="6"/>'
s += dot(250, 255, fill=DOM); s += dot(470, 255, fill=ACCENT)
save("02-4-connectedness", frame(s))

# 02-5 연속성: 두 매끄러운 곡선이 교차 → 4조각이 아닌 2개의 연속선
s = ''
s += f'<path d="M70,90 C260,90 460,270 650,270" fill="none" stroke="{ACCENT}" stroke-width="7" stroke-linecap="round"/>'
s += f'<path d="M70,270 C260,270 460,90 650,90" fill="none" stroke="{MID}" stroke-width="7" stroke-linecap="round"/>'
save("02-5-continuity", frame(s))

# 02-6 폐쇄성: 카니자 삼각형 (팩맨 3개가 보이지 않는 삼각형을 만든다)
def pacman(cx, cy, r, ang):
    # wedge cut facing direction ang(deg), 60deg opening
    a1 = math.radians(ang - 30); a2 = math.radians(ang + 30)
    x1 = cx + r*math.cos(a1); y1 = cy + r*math.sin(a1)
    x2 = cx + r*math.cos(a2); y2 = cy + r*math.sin(a2)
    # full circle then bg wedge cut
    c = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{MID}"/>'
    wedge = (f'<path d="M{cx},{cy} L{x1:.1f},{y1:.1f} '
             f'A{r},{r} 0 0 1 {x2:.1f},{y2:.1f} Z" fill="{BG}"/>')
    return c + wedge
s = ''
# vertices of upward triangle
verts = [(360, 110), (250, 280), (470, 280)]
# directions: each wedge points toward triangle centroid
cen = (360, 223)
for (vx, vy) in verts:
    ang = math.degrees(math.atan2(cen[1]-vy, cen[0]-vx))
    s += pacman(vx, vy, 42, ang)
save("02-6-closure", frame(s))

# 02-7 전경배경: 어두운 ground 위로 밝은 카드(figure)가 그림자와 함께 떠오름
s = ''
s += f'<rect x="40" y="40" width="640" height="280" rx="14" fill="{FLOOR}"/>'
s += f'<rect x="218" y="118" width="290" height="150" rx="14" fill="#000000" opacity="0.22"/>'  # shadow
s += f'<rect x="210" y="108" width="290" height="150" rx="14" fill="{HI}"/>'
s += f'<rect x="234" y="132" width="120" height="16" rx="8" fill="{ACCENT}"/>'
s += f'<rect x="234" y="162" width="240" height="10" rx="5" fill="{DOM}"/>'
s += f'<rect x="234" y="184" width="200" height="10" rx="5" fill="{DOM}"/>'
save("02-7-figure-ground", frame(s))

# 02-8 공동운명: 같은 방향(위) 화살표끼리 묶임, 다른 방향 하나 분리
def arrow(cx, cy, up=True, color=ACCENT):
    d = -1 if up else 1
    shaft = f'<line x1="{cx}" y1="{cy- d*0}" x2="{cx}" y2="{cy + d*42}" stroke="{color}" stroke-width="6"/>'
    head_y = cy + d*42
    head = (f'<path d="M{cx-9},{head_y - d*0} L{cx},{head_y + d*14} L{cx+9},{head_y} Z" fill="{color}"/>')
    return shaft + head
s = ''
xs = [110, 230, 350, 470, 590]
for i, x in enumerate(xs):
    up = not (i == 3)  # one different direction
    s += dot(x, 180, r=18, fill=(DOM if up else MID))
    s += arrow(x, 152 if up else 208, up=up, color=(ACCENT if up else INK))
save("02-8-common-fate", frame(s))

# 02-9 대칭/질서: 좌우 대칭 브래킷이 하나의 단위로 묶임
s = ''
s += f'<path d="M300,90 C235,90 235,270 300,270" fill="none" stroke="{MID}" stroke-width="12" stroke-linecap="round"/>'
s += f'<path d="M420,90 C485,90 485,270 420,270" fill="none" stroke="{MID}" stroke-width="12" stroke-linecap="round"/>'
s += dot(360, 180, r=26, fill=ACCENT)
save("02-9-symmetry", frame(s))


print("DONE")
