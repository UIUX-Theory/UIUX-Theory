#!/usr/bin/env python3
"""UI/UX 적용 예시 목업 생성 (SVG + HTML). 톤: grayscale + accent (#6541F2), gen_diagrams.py와 동일 팔레트."""
import os, textwrap

OUT = os.path.join(os.path.dirname(__file__), "docs", "assets", "examples")
os.makedirs(OUT, exist_ok=True)

BG, INK, MID, DOM, HI, FLOOR, ACCENT, WHITE = (
    "#EBEBEB", "#5A5A5A", "#8C8C8C", "#B0B0B0",
    "#D2D2D2", "#707070", "#6541F2", "#FFFFFF",
)
W, H = 880, 460
FONT = "system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif"

def svg_frame(inner, w=W, h=H):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
            f'font-family="{FONT}">'
            f'<rect width="{w}" height="{h}" rx="20" fill="{BG}"/>'
            f'{inner}</svg>')

def save(name, svg, html):
    open(os.path.join(OUT, name + ".svg"), "w").write(svg)
    open(os.path.join(OUT, name + ".html"), "w").write(html)
    print("saved", name)

def html_doc(title, body, extra_css=""):
    return textwrap.dedent(f"""\
    <!doctype html>
    <html lang="ko"><head><meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width,initial-scale=1"/>
    <title>{title}</title>
    <style>
      :root {{
        --bg:{BG}; --ink:{INK}; --mid:{MID}; --dom:{DOM};
        --hi:{HI}; --floor:{FLOOR}; --accent:{ACCENT}; --white:{WHITE};
      }}
      *{{box-sizing:border-box}}
      body{{margin:0;padding:40px;background:var(--bg);color:var(--ink);
        font-family:{FONT};font-size:14px;line-height:1.5}}
      h1{{font-size:18px;margin:0 0 24px;color:var(--floor)}}
      .stage{{max-width:880px;margin:0 auto;background:var(--white);
        border-radius:20px;padding:32px;box-shadow:0 1px 0 rgba(0,0,0,.04)}}
      {extra_css}
    </style></head>
    <body><h1>{title}</h1><div class="stage">{body}</div></body></html>
    """)

# ---------- 2.1 Proximity — Form ----------
s = ''
TITLE_Y = 50
CONTENT_Y = 110
LEFT_X, RIGHT_X = 60, 500
W_F, H_F = 320, 32

# LEFT — bad: every gap = 24px, so each label is equidistant from
# the field below AND the field above. You can't tell which it belongs to.
s += f'<text x="{LEFT_X}" y="{TITLE_Y}" font-size="14" font-weight="700" fill="{FLOOR}">✗ 모호한 간격</text>'
y = CONTENT_Y
for lab in ["이메일", "비밀번호", "이름", "전화번호"]:
    s += f'<text x="{LEFT_X}" y="{y}" font-size="13" fill="{MID}">{lab}</text>'
    s += f'<rect x="{LEFT_X}" y="{y+24}" width="{W_F}" height="{H_F}" rx="8" fill="{WHITE}" stroke="{HI}"/>'
    y += 80  # pitch = 24 + 32 + 24 (all equal)

# RIGHT — good: tight label↔field bond (6px), clear row gap (22px),
# much larger section break (56px). Section title is plain bold purple
# text — no decoration, proximity does the grouping work.
s += f'<text x="{RIGHT_X}" y="{TITLE_Y}" font-size="14" font-weight="700" fill="{FLOOR}">✓ 라벨 붙임 + 섹션 분리</text>'
y = CONTENT_Y
for gi, (gtitle, fields) in enumerate([("계정", ["이메일", "비밀번호"]),
                                        ("프로필", ["이름", "전화번호"])]):
    if gi > 0:
        y += 34  # extra so field-bottom → next-section-title = 22+34 = 56
    s += f'<text x="{RIGHT_X}" y="{y}" font-size="13" font-weight="700" fill="{ACCENT}">{gtitle}</text>'
    y += 22  # section title → first field label
    for lab in fields:
        s += f'<text x="{RIGHT_X}" y="{y}" font-size="13" font-weight="600" fill="{INK}">{lab}</text>'
        s += f'<rect x="{RIGHT_X}" y="{y+6}" width="{W_F}" height="{H_F}" rx="8" fill="{WHITE}" stroke="{DOM}"/>'
        y += 60  # 6 + 32 + 22 → tight pair, generous row gap
save("02-1-proximity-form", svg_frame(s), html_doc(
    "근접성 — 폼 라벨/섹션",
    """
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:48px">
      <div>
        <p style="color:var(--floor);font-weight:700;margin:0 0 32px">✗ 모호한 간격</p>
        <div style="display:flex;flex-direction:column;gap:24px">
          <div><div style="margin-bottom:24px;color:var(--mid)">이메일</div><input style="width:100%;padding:8px;border:1px solid var(--hi);border-radius:8px"/></div>
          <div><div style="margin-bottom:24px;color:var(--mid)">비밀번호</div><input type="password" style="width:100%;padding:8px;border:1px solid var(--hi);border-radius:8px"/></div>
          <div><div style="margin-bottom:24px;color:var(--mid)">이름</div><input style="width:100%;padding:8px;border:1px solid var(--hi);border-radius:8px"/></div>
          <div><div style="margin-bottom:24px;color:var(--mid)">전화번호</div><input style="width:100%;padding:8px;border:1px solid var(--hi);border-radius:8px"/></div>
        </div>
      </div>
      <div>
        <p style="color:var(--floor);font-weight:700;margin:0 0 32px">✓ 라벨 붙임 + 섹션 분리</p>
        <section style="margin-bottom:48px">
          <div style="color:var(--accent);font-weight:700;font-size:13px;margin-bottom:14px">계정</div>
          <label style="display:block;margin-bottom:22px;font-weight:600">이메일<input style="display:block;margin-top:4px;width:100%;padding:8px;border:1px solid var(--dom);border-radius:8px"/></label>
          <label style="display:block;font-weight:600">비밀번호<input type="password" style="display:block;margin-top:4px;width:100%;padding:8px;border:1px solid var(--dom);border-radius:8px"/></label>
        </section>
        <section>
          <div style="color:var(--accent);font-weight:700;font-size:13px;margin-bottom:14px">프로필</div>
          <label style="display:block;margin-bottom:22px;font-weight:600">이름<input style="display:block;margin-top:4px;width:100%;padding:8px;border:1px solid var(--dom);border-radius:8px"/></label>
          <label style="display:block;font-weight:600">전화번호<input style="display:block;margin-top:4px;width:100%;padding:8px;border:1px solid var(--dom);border-radius:8px"/></label>
        </section>
      </div>
    </div>
    """))

# ---------- 2.2 Similarity — Button hierarchy ----------
s = ''
s += f'<text x="60" y="60" font-size="14" font-weight="600" fill="{FLOOR}">✗ 같은 색의 버튼 세 개 (위계 없음)</text>'
for i, lab in enumerate(["취소", "임시저장", "발행하기"]):
    x = 60 + i*150
    s += f'<rect x="{x}" y="80" width="130" height="40" rx="10" fill="{ACCENT}"/>'
    s += f'<text x="{x+65}" y="105" text-anchor="middle" font-size="13" font-weight="600" fill="{WHITE}">{lab}</text>'
s += f'<text x="60" y="200" font-size="14" font-weight="600" fill="{FLOOR}">✓ 주요 CTA만 차별화 (유사성 → 위계)</text>'
# secondary: text-like, primary: accent filled
s += f'<text x="80" y="248" font-size="13" font-weight="600" fill="{MID}">취소</text>'
s += f'<rect x="180" y="220" width="130" height="40" rx="10" fill="none" stroke="{DOM}" stroke-width="1.5"/>'
s += f'<text x="245" y="245" text-anchor="middle" font-size="13" font-weight="600" fill="{INK}">임시저장</text>'
s += f'<rect x="330" y="220" width="160" height="40" rx="10" fill="{ACCENT}"/>'
s += f'<text x="410" y="245" text-anchor="middle" font-size="13" font-weight="700" fill="{WHITE}">발행하기</text>'
# tag color consistency strip
s += f'<text x="60" y="330" font-size="14" font-weight="600" fill="{FLOOR}">상태 태그도 같은 종류는 같은 색</text>'
for i, (lab, fill, fg) in enumerate([("진행중", ACCENT, WHITE), ("진행중", ACCENT, WHITE),
                                      ("완료", MID, WHITE), ("완료", MID, WHITE)]):
    x = 60 + i*90
    s += f'<rect x="{x}" y="345" width="74" height="26" rx="13" fill="{fill}"/>'
    s += f'<text x="{x+37}" y="362" text-anchor="middle" font-size="11" font-weight="600" fill="{fg}">{lab}</text>'
save("02-2-similarity-buttons", svg_frame(s), html_doc(
    "유사성 — 버튼 위계 / 상태 태그",
    """
    <p style="color:var(--floor);font-weight:600">✗ 같은 색 버튼 세 개</p>
    <div style="display:flex;gap:12px;margin-bottom:32px">
      <button style="padding:10px 20px;border:0;border-radius:10px;background:var(--accent);color:#fff;font-weight:600">취소</button>
      <button style="padding:10px 20px;border:0;border-radius:10px;background:var(--accent);color:#fff;font-weight:600">임시저장</button>
      <button style="padding:10px 20px;border:0;border-radius:10px;background:var(--accent);color:#fff;font-weight:600">발행하기</button>
    </div>
    <p style="color:var(--floor);font-weight:600">✓ 주요 CTA만 차별화</p>
    <div style="display:flex;gap:12px;align-items:center;margin-bottom:32px">
      <button style="padding:10px 20px;border:0;background:none;color:var(--mid);font-weight:600;cursor:pointer">취소</button>
      <button style="padding:10px 20px;border:1.5px solid var(--dom);border-radius:10px;background:#fff;color:var(--ink);font-weight:600">임시저장</button>
      <button style="padding:10px 24px;border:0;border-radius:10px;background:var(--accent);color:#fff;font-weight:700">발행하기</button>
    </div>
    <p style="color:var(--floor);font-weight:600">상태 태그는 종류별로 같은 색</p>
    <div style="display:flex;gap:8px">
      <span style="padding:4px 12px;border-radius:13px;background:var(--accent);color:#fff;font-size:11px;font-weight:600">진행중</span>
      <span style="padding:4px 12px;border-radius:13px;background:var(--accent);color:#fff;font-size:11px;font-weight:600">진행중</span>
      <span style="padding:4px 12px;border-radius:13px;background:var(--mid);color:#fff;font-size:11px;font-weight:600">완료</span>
      <span style="padding:4px 12px;border-radius:13px;background:var(--mid);color:#fff;font-size:11px;font-weight:600">완료</span>
    </div>
    """))

# ---------- 2.3 Common Region — Card grouping ----------
s = ''
s += f'<text x="60" y="50" font-size="14" font-weight="600" fill="{FLOOR}">카드(공통영역)로 설정 그룹 묶기</text>'
def card(x, y, w, h, title, rows):
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{WHITE}" stroke="{HI}"/>'
    out += f'<text x="{x+20}" y="{y+28}" font-size="13" font-weight="700" fill="{INK}">{title}</text>'
    for i, (label, on) in enumerate(rows):
        ry = y + 56 + i*36
        out += f'<text x="{x+20}" y="{ry+14}" font-size="12" fill="{INK}">{label}</text>'
        fill = ACCENT if on else HI
        out += f'<rect x="{x+w-60}" y="{ry-2}" width="42" height="22" rx="11" fill="{fill}"/>'
        cx = x+w-60 + (31 if on else 11)
        out += f'<circle cx="{cx}" cy="{ry+9}" r="8" fill="{WHITE}"/>'
    return out
s += card(60, 70, 360, 240, "알림", [("이메일 알림", True), ("푸시 알림", True), ("주간 요약", False), ("프로모션", False)])
s += card(460, 70, 360, 240, "개인정보", [("프로필 공개", False), ("활동 기록 수집", True), ("위치 사용", False), ("광고 맞춤", False)])
s += f'<text x="60" y="350" font-size="12" fill="{MID}">→ 테두리/카드 배경이 같은 종류의 컨트롤을 묶어준다 (근접성을 거스르고도)</text>'
save("02-3-common-region-cards", svg_frame(s), html_doc(
    "공통 영역 — 설정 카드",
    """
    <p style="color:var(--floor);font-weight:600;margin-bottom:24px">카드(공통영역)로 설정 그룹 묶기</p>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:24px">""" +
    "".join(f"""
      <section style="background:#fff;border:1px solid var(--hi);border-radius:14px;padding:20px">
        <h3 style="margin:0 0 16px;font-size:13px">{title}</h3>
        {"".join(f'<div style="display:flex;justify-content:space-between;align-items:center;padding:8px 0"><span>{lab}</span><span style="display:inline-block;width:42px;height:22px;border-radius:11px;background:{(ACCENT if on else HI)};position:relative"><span style="position:absolute;top:3px;{("right:3px" if on else "left:3px")};width:16px;height:16px;border-radius:50%;background:#fff"></span></span></div>' for lab, on in rows)}
      </section>""" for title, rows in [
        ("알림", [("이메일 알림", True), ("푸시 알림", True), ("주간 요약", False), ("프로모션", False)]),
        ("개인정보", [("프로필 공개", False), ("활동 기록 수집", True), ("위치 사용", False), ("광고 맞춤", False)]),
    ]) + """</div>
    <p style="color:var(--mid);font-size:12px;margin-top:24px">→ 테두리/카드 배경이 같은 종류의 컨트롤을 묶어준다 (근접성을 거스르고도)</p>
    """))

# ---------- 2.4 Connectedness — Stepper ----------
s = ''
s += f'<text x="60" y="60" font-size="14" font-weight="600" fill="{FLOOR}">단계 인디케이터: 선으로 흐름을 만든다</text>'
steps = [("계정 생성", "완료"), ("프로필 입력", "진행중"), ("이메일 인증", "대기"), ("완료", "대기")]
y = 160
n = len(steps)
xs = [120 + i*200 for i in range(n)]
# connecting line
s += f'<line x1="{xs[0]}" y1="{y}" x2="{xs[-1]}" y2="{y}" stroke="{HI}" stroke-width="4"/>'
# filled portion to current step
s += f'<line x1="{xs[0]}" y1="{y}" x2="{xs[1]}" y2="{y}" stroke="{ACCENT}" stroke-width="4"/>'
for i, ((label, state), x) in enumerate(zip(steps, xs)):
    if state == "완료":
        s += f'<circle cx="{x}" cy="{y}" r="22" fill="{ACCENT}"/>'
        s += f'<polyline points="{x-7},{y} {x-2},{y+6} {x+8},{y-6}" fill="none" stroke="{WHITE}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
    elif state == "진행중":
        s += f'<circle cx="{x}" cy="{y}" r="22" fill="{WHITE}" stroke="{ACCENT}" stroke-width="3"/>'
        s += f'<text x="{x}" y="{y+5}" text-anchor="middle" font-size="13" font-weight="700" fill="{ACCENT}">{i+1}</text>'
    else:
        s += f'<circle cx="{x}" cy="{y}" r="22" fill="{WHITE}" stroke="{HI}" stroke-width="3"/>'
        s += f'<text x="{x}" y="{y+5}" text-anchor="middle" font-size="13" font-weight="700" fill="{DOM}">{i+1}</text>'
    s += f'<text x="{x}" y="{y+50}" text-anchor="middle" font-size="12" fill="{INK if state!="대기" else MID}">{label}</text>'
save("02-4-connectedness-stepper", svg_frame(s), html_doc(
    "연결성 — 단계 인디케이터",
    """
    <p style="color:var(--floor);font-weight:600;margin-bottom:40px">단계 인디케이터: 선이 단계들을 "하나의 흐름"으로 묶는다</p>
    <div style="position:relative;display:flex;justify-content:space-between;padding:0 40px">
      <div style="position:absolute;left:60px;right:60px;top:21px;height:4px;background:var(--hi);z-index:0"></div>
      <div style="position:absolute;left:60px;width:200px;top:21px;height:4px;background:var(--accent);z-index:0"></div>""" +
    "".join(f"""
      <div style="position:relative;z-index:1;text-align:center;width:80px">
        <div style="width:46px;height:46px;border-radius:50%;margin:0 auto;display:flex;align-items:center;justify-content:center;font-weight:700;{
            'background:var(--accent);color:#fff' if state=='완료'
            else 'background:#fff;border:3px solid var(--accent);color:var(--accent)' if state=='진행중'
            else 'background:#fff;border:3px solid var(--hi);color:var(--dom)'
        }">{"✓" if state=='완료' else i+1}</div>
        <div style="margin-top:12px;font-size:12px;color:{('var(--ink)' if state!='대기' else 'var(--mid)')}">{label}</div>
      </div>""" for i, (label, state) in enumerate([("계정 생성","완료"),("프로필 입력","진행중"),("이메일 인증","대기"),("완료","대기")])) +
    """</div>"""))

# ---------- 2.5 Continuity — Carousel peek ----------
s = ''
s += f'<text x="60" y="50" font-size="14" font-weight="600" fill="{FLOOR}">캐러셀: 다음 카드를 살짝 잘라 보여 "더 있음"을 암시</text>'
# show 3.5 cards: full 3 + a peek of 4th cropped on right
card_w, card_h, gap, x0, y0 = 200, 240, 16, 60, 80
for i in range(4):
    x = x0 + i*(card_w + gap)
    s += f'<rect x="{x}" y="{y0}" width="{card_w}" height="{card_h}" rx="14" fill="{WHITE}" stroke="{HI}"/>'
    s += f'<rect x="{x+16}" y="{y0+16}" width="{card_w-32}" height="120" rx="8" fill="{DOM}"/>'
    s += f'<rect x="{x+16}" y="{y0+150}" width="120" height="12" rx="6" fill="{INK}"/>'
    s += f'<rect x="{x+16}" y="{y0+172}" width="{card_w-60}" height="10" rx="5" fill="{HI}"/>'
    s += f'<rect x="{x+16}" y="{y0+190}" width="100" height="10" rx="5" fill="{HI}"/>'
# right fade mask to suggest cut-off
s += f'<defs><linearGradient id="fade" x1="0" x2="1"><stop offset="0" stop-color="{BG}" stop-opacity="0"/><stop offset="1" stop-color="{BG}"/></linearGradient></defs>'
s += f'<rect x="{W-130}" y="0" width="130" height="{H}" fill="url(#fade)"/>'
# dots indicator
s += f'<g transform="translate({W//2 - 28},{H-30})">'
s += f'<circle cx="0" cy="0" r="4" fill="{ACCENT}"/><circle cx="14" cy="0" r="4" fill="{HI}"/><circle cx="28" cy="0" r="4" fill="{HI}"/><circle cx="42" cy="0" r="4" fill="{HI}"/></g>'
save("02-5-continuity-carousel", svg_frame(s), html_doc(
    "연속성 — 캐러셀 peek",
    """
    <p style="color:var(--floor);font-weight:600;margin-bottom:16px">캐러셀: 다음 카드를 살짝 잘라 보여 "옆으로 더 있음"을 암시</p>
    <div style="position:relative">
      <div style="display:flex;gap:16px;overflow-x:auto;padding:8px 0 16px;scroll-snap-type:x mandatory">""" +
    "".join(f"""
        <article style="flex:0 0 200px;background:#fff;border:1px solid var(--hi);border-radius:14px;padding:16px;scroll-snap-align:start">
          <div style="height:120px;background:var(--dom);border-radius:8px"></div>
          <h4 style="margin:12px 0 6px;font-size:13px">카드 제목 {i+1}</h4>
          <p style="margin:0;color:var(--mid);font-size:12px">정렬된 축이 시선 동선을 매끄럽게 만든다.</p>
        </article>""" for i in range(6)) +
    """</div>
      <div style="position:absolute;right:0;top:0;bottom:0;width:80px;background:linear-gradient(to right, transparent, var(--white))"></div>
    </div>
    """, extra_css="::-webkit-scrollbar{height:6px}::-webkit-scrollbar-thumb{background:var(--hi);border-radius:3px}"))

# ---------- 2.6 Closure — Cut-off / read more ----------
s = ''
s += f'<text x="60" y="50" font-size="14" font-weight="600" fill="{FLOOR}">긴 글을 살짝 잘라 "더 있음"을 폐쇄성으로 암시</text>'
# article block with fade
lines = [340, 280, 320, 300, 360, 240, 310, 280, 300]
y = 90
for i, lw in enumerate(lines):
    s += f'<rect x="60" y="{y}" width="{lw}" height="10" rx="5" fill="{INK if i<3 else (DOM if i<6 else HI)}"/>'
    y += 22
# fade overlay bottom half
s += f'<defs><linearGradient id="vfade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{BG}" stop-opacity="0"/><stop offset="1" stop-color="{BG}"/></linearGradient></defs>'
s += f'<rect x="0" y="180" width="500" height="160" fill="url(#vfade)"/>'
# CTA "더 읽기 ↓"
s += f'<rect x="170" y="350" width="170" height="44" rx="22" fill="{ACCENT}"/>'
s += f'<text x="255" y="378" text-anchor="middle" font-size="13" font-weight="700" fill="{WHITE}">더 읽기 ↓</text>'
# right side: minimalist logo demonstrating closure
s += f'<text x="560" y="80" font-size="14" font-weight="600" fill="{FLOOR}">로고도 폐쇄성으로 형태를 암시</text>'
# minimal "M" formed by two strokes (negative space closes triangle)
s += f'<path d="M580 200 L580 110 L640 170 L700 110 L700 200" fill="none" stroke="{INK}" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/>'
s += f'<text x="640" y="260" text-anchor="middle" font-size="12" fill="{MID}">최소 단서로 M 인식</text>'
save("02-6-closure-readmore", svg_frame(s), html_doc(
    "폐쇄성 — 잘린 콘텐츠 / 더 읽기",
    """
    <p style="color:var(--floor);font-weight:600;margin-bottom:16px">긴 글을 살짝 잘라 "더 있음"을 폐쇄성으로 암시</p>
    <div style="position:relative;max-height:280px;overflow:hidden">
      <p>게슈탈트 심리학은 1910~30년대 독일에서 정립된 시지각 이론입니다. "전체는 부분의 합과 다르다"는 명제 아래, 인간이 무질서 속에서 어떻게 질서를 찾는지를 연구했습니다.</p>
      <p>이 이론의 핵심은 인간의 시각 시스템이 개별 요소를 따로 보지 않고, 의식하기 전에 먼저 묶고 분리하고 완성한다는 것입니다. 이러한 자동적인 그룹핑은 우리가 복잡한 환경을 빠르게 이해할 수 있게 해줍니다.</p>
      <p>오늘날 UI/UX 디자인에서 게슈탈트 원리는 매우 중요한 도구로 활용됩니다. 디자이너가 의도적으로 그룹핑 신호를 잘 주면 사용자의 인지 부하가 줄어들고, 화면의 의미가 빠르게 전달됩니다.</p>
      <div style="position:absolute;left:0;right:0;bottom:0;height:140px;background:linear-gradient(to bottom, transparent, #fff)"></div>
    </div>
    <div style="text-align:center;margin-top:16px">
      <button style="padding:12px 32px;border:0;border-radius:22px;background:var(--accent);color:#fff;font-weight:700;cursor:pointer">더 읽기 ↓</button>
    </div>
    """))

# ---------- 2.7 Figure-Ground — Modal ----------
s = ''
# ground: a faux page with header + content
s += f'<rect x="0" y="0" width="{W}" height="{H}" fill="{BG}" rx="20"/>'
s += f'<rect x="40" y="40" width="{W-80}" height="44" rx="10" fill="{WHITE}"/>'
s += f'<rect x="60" y="58" width="80" height="10" rx="5" fill="{INK}"/>'
s += f'<circle cx="{W-60}" cy="62" r="12" fill="{HI}"/>'
for i in range(3):
    cw3 = (W - 100) // 3
    s += f'<rect x="{40 + i*cw3}" y="110" width="{cw3 - 20}" height="200" rx="12" fill="{WHITE}" stroke="{HI}"/>'
# dim overlay
s += f'<rect x="0" y="0" width="{W}" height="{H}" fill="{FLOOR}" opacity="0.55" rx="20"/>'
# modal (figure)
mw, mh = 400, 220
mx, my = (W-mw)//2, (H-mh)//2
s += f'<rect x="{mx+8}" y="{my+10}" width="{mw}" height="{mh}" rx="16" fill="#000" opacity="0.25"/>'
s += f'<rect x="{mx}" y="{my}" width="{mw}" height="{mh}" rx="16" fill="{WHITE}"/>'
s += f'<text x="{mx+24}" y="{my+40}" font-size="16" font-weight="700" fill="{INK}">계정 삭제</text>'
s += f'<text x="{mx+24}" y="{my+72}" font-size="13" fill="{MID}">이 작업은 되돌릴 수 없습니다.</text>'
s += f'<text x="{mx+24}" y="{my+92}" font-size="13" fill="{MID}">정말 계속하시겠습니까?</text>'
# buttons
s += f'<rect x="{mx+mw-220}" y="{my+mh-58}" width="90" height="38" rx="10" fill="none" stroke="{DOM}" stroke-width="1.5"/>'
s += f'<text x="{mx+mw-175}" y="{my+mh-34}" text-anchor="middle" font-size="13" font-weight="600" fill="{INK}">취소</text>'
s += f'<rect x="{mx+mw-120}" y="{my+mh-58}" width="100" height="38" rx="10" fill="{ACCENT}"/>'
s += f'<text x="{mx+mw-70}" y="{my+mh-34}" text-anchor="middle" font-size="13" font-weight="700" fill="{WHITE}">삭제</text>'
save("02-7-figure-ground-modal", svg_frame(s), html_doc(
    "전경-배경 — 모달 다이얼로그",
    """
    <p style="color:var(--floor);font-weight:600;margin-bottom:16px">모달이 어두운 배경 위로 전경으로 떠오른다</p>
    <div style="position:relative;height:380px;border-radius:14px;overflow:hidden;background:var(--bg)">
      <header style="background:#fff;padding:14px 20px;display:flex;justify-content:space-between"><strong>페이지</strong><span style="width:24px;height:24px;border-radius:50%;background:var(--hi)"></span></header>
      <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px;padding:20px">
        <div style="background:#fff;border:1px solid var(--hi);border-radius:12px;height:180px"></div>
        <div style="background:#fff;border:1px solid var(--hi);border-radius:12px;height:180px"></div>
        <div style="background:#fff;border:1px solid var(--hi);border-radius:12px;height:180px"></div>
      </div>
      <div style="position:absolute;inset:0;background:rgba(112,112,112,.55);display:flex;align-items:center;justify-content:center">
        <div style="background:#fff;border-radius:16px;padding:24px;width:380px;box-shadow:0 12px 32px rgba(0,0,0,.25)">
          <h3 style="margin:0 0 8px;font-size:16px">계정 삭제</h3>
          <p style="margin:0 0 24px;color:var(--mid);font-size:13px">이 작업은 되돌릴 수 없습니다. 정말 계속하시겠습니까?</p>
          <div style="display:flex;justify-content:flex-end;gap:8px">
            <button style="padding:10px 20px;border:1.5px solid var(--dom);border-radius:10px;background:#fff;font-weight:600">취소</button>
            <button style="padding:10px 24px;border:0;border-radius:10px;background:var(--accent);color:#fff;font-weight:700">삭제</button>
          </div>
        </div>
      </div>
    </div>
    """))

# ---------- 2.8 Common Fate — Accordion before/after ----------
s = ''
s += f'<text x="60" y="50" font-size="14" font-weight="600" fill="{FLOOR}">아코디언: 펼쳐지는 항목들이 함께 움직여 한 묶음으로 인식</text>'
# before frame
s += f'<text x="80" y="90" font-size="12" fill="{MID}">접힌 상태</text>'
y = 110
for i, lab in enumerate(["배송 정보", "결제 수단", "주문 요약"]):
    s += f'<rect x="80" y="{y + i*42}" width="280" height="34" rx="8" fill="{WHITE}" stroke="{HI}"/>'
    s += f'<text x="100" y="{y + i*42 + 22}" font-size="13" font-weight="600" fill="{INK}">{lab}</text>'
    s += f'<text x="340" y="{y + i*42 + 22}" font-size="14" fill="{MID}">＋</text>'
# after: 1st expanded, both expansion items appear together (motion arrows down)
s += f'<text x="500" y="90" font-size="12" fill="{MID}">펼쳐진 상태</text>'
s += f'<rect x="500" y="110" width="280" height="34" rx="8" fill="{WHITE}" stroke="{ACCENT}" stroke-width="2"/>'
s += f'<text x="520" y="132" font-size="13" font-weight="700" fill="{INK}">배송 정보</text>'
s += f'<text x="760" y="132" font-size="14" fill="{ACCENT}">－</text>'
# expanded content (highlighted to imply moved together)
s += f'<rect x="500" y="150" width="280" height="100" rx="8" fill="{BG}" stroke="{HI}"/>'
s += f'<rect x="520" y="170" width="240" height="10" rx="5" fill="{DOM}"/>'
s += f'<rect x="520" y="188" width="180" height="10" rx="5" fill="{DOM}"/>'
s += f'<rect x="520" y="218" width="220" height="20" rx="6" fill="{WHITE}" stroke="{HI}"/>'
# motion: down arrows next to following items showing they slid down
for i, lab in enumerate(["결제 수단", "주문 요약"]):
    yy = 260 + i*42
    s += f'<rect x="500" y="{yy}" width="280" height="34" rx="8" fill="{WHITE}" stroke="{HI}"/>'
    s += f'<text x="520" y="{yy+22}" font-size="13" font-weight="600" fill="{INK}">{lab}</text>'
    s += f'<text x="760" y="{yy+22}" font-size="14" fill="{MID}">＋</text>'
    s += f'<path d="M785 {yy-6} l0 18 m-5 -6 l5 6 5 -6" stroke="{ACCENT}" stroke-width="2" fill="none" stroke-linecap="round"/>'
save("02-8-common-fate-accordion", svg_frame(s), html_doc(
    "공동운명 — 아코디언 펼침",
    """
    <p style="color:var(--floor);font-weight:600;margin-bottom:24px">펼쳐지는 콘텐츠와 아래 항목들이 같은 방향으로 움직여 "한 묶음" 인지</p>
    <details style="border:1px solid var(--hi);border-radius:8px;padding:12px 16px;margin-bottom:8px" open>
      <summary style="font-weight:700;cursor:pointer">배송 정보</summary>
      <div style="margin-top:12px;color:var(--mid)">받는 분 / 주소 / 연락처 입력 필드 영역</div>
    </details>
    <details style="border:1px solid var(--hi);border-radius:8px;padding:12px 16px;margin-bottom:8px">
      <summary style="font-weight:700;cursor:pointer">결제 수단</summary>
      <div style="margin-top:12px;color:var(--mid)">카드 / 계좌이체 / 간편결제 선택</div>
    </details>
    <details style="border:1px solid var(--hi);border-radius:8px;padding:12px 16px">
      <summary style="font-weight:700;cursor:pointer">주문 요약</summary>
      <div style="margin-top:12px;color:var(--mid)">상품 / 금액 / 할인 정보</div>
    </details>
    """))

# ---------- 2.9 Symmetry — Pricing grid ----------
s = ''
s += f'<text x="60" y="50" font-size="14" font-weight="600" fill="{FLOOR}">대칭 그리드: 일관된 정렬이 "정돈됨 = 신뢰감"을 준다</text>'
plans = [("Basic", "₩0", False), ("Pro", "₩9,900", True), ("Team", "₩29,900", False)]
cw, ch, x0, y0, gap = 240, 320, 60, 80, 20
for i, (name, price, recommended) in enumerate(plans):
    x = x0 + i*(cw + gap)
    stroke = ACCENT if recommended else HI
    sw = 3 if recommended else 1
    s += f'<rect x="{x}" y="{y0}" width="{cw}" height="{ch}" rx="16" fill="{WHITE}" stroke="{stroke}" stroke-width="{sw}"/>'
    if recommended:
        s += f'<rect x="{x+cw//2 - 40}" y="{y0-14}" width="80" height="26" rx="13" fill="{ACCENT}"/>'
        s += f'<text x="{x+cw//2}" y="{y0+4}" text-anchor="middle" font-size="11" font-weight="700" fill="{WHITE}">추천</text>'
    s += f'<text x="{x+cw//2}" y="{y0+50}" text-anchor="middle" font-size="14" font-weight="700" fill="{INK}">{name}</text>'
    s += f'<text x="{x+cw//2}" y="{y0+96}" text-anchor="middle" font-size="26" font-weight="800" fill="{INK}">{price}</text>'
    s += f'<text x="{x+cw//2}" y="{y0+116}" text-anchor="middle" font-size="11" fill="{MID}">/월</text>'
    # 3 feature rows
    for j in range(3):
        fy = y0 + 150 + j*32
        s += f'<circle cx="{x+30}" cy="{fy}" r="6" fill="{ACCENT}"/>'
        s += f'<polyline points="{x+27},{fy} {x+30},{fy+3} {x+34},{fy-3}" fill="none" stroke="{WHITE}" stroke-width="1.6"/>'
        s += f'<rect x="{x+46}" y="{fy-5}" width="{cw - 76}" height="10" rx="5" fill="{HI}"/>'
    # CTA
    bg = ACCENT if recommended else WHITE
    fg = WHITE if recommended else INK
    border = '' if recommended else f' stroke="{DOM}" stroke-width="1.5"'
    s += f'<rect x="{x+24}" y="{y0+ch-58}" width="{cw-48}" height="38" rx="10" fill="{bg}"{border}/>'
    s += f'<text x="{x+cw//2}" y="{y0+ch-34}" text-anchor="middle" font-size="13" font-weight="700" fill="{fg}">선택</text>'
save("02-9-symmetry-pricing", svg_frame(s), html_doc(
    "대칭/질서 — 가격표 그리드",
    """
    <p style="color:var(--floor);font-weight:600;margin-bottom:24px">대칭 그리드: 일관된 정렬이 "정돈됨 = 신뢰감"을 만든다</p>
    <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:20px">""" +
    "".join(f"""
      <article style="position:relative;background:#fff;border:{('3px solid var(--accent)' if rec else '1px solid var(--hi)')};border-radius:16px;padding:24px;text-align:center">
        {('<span style="position:absolute;top:-14px;left:50%;transform:translateX(-50%);background:var(--accent);color:#fff;padding:4px 14px;border-radius:13px;font-size:11px;font-weight:700">추천</span>' if rec else '')}
        <h3 style="margin:0 0 12px">{name}</h3>
        <div style="font-size:28px;font-weight:800">{price}<span style="font-size:12px;font-weight:400;color:var(--mid)"> /월</span></div>
        <ul style="list-style:none;padding:0;margin:24px 0;text-align:left">
          <li style="padding:6px 0;color:var(--mid)">✓ 핵심 기능 A</li>
          <li style="padding:6px 0;color:var(--mid)">✓ 핵심 기능 B</li>
          <li style="padding:6px 0;color:var(--mid)">✓ 핵심 기능 C</li>
        </ul>
        <button style="width:100%;padding:12px;border:{('0' if rec else '1.5px solid var(--dom)')};border-radius:10px;background:{('var(--accent)' if rec else '#fff')};color:{('#fff' if rec else 'var(--ink)')};font-weight:700">선택</button>
      </article>""" for name, price, rec in [("Basic","₩0",False),("Pro","₩9,900",True),("Team","₩29,900",False)]) +
    """</div>"""))

print("DONE")
