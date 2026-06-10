# 게슈탈트 시지각 원리 → UI/UX 적용 레퍼런스

> **목적** — 게슈탈트 시지각 이론을 깊게 이해하고, 그 원리를 화면 설계(레이아웃·그룹핑·시각 위계)에 적용하기 위한 개인 학습/작업 레퍼런스.
> **작성일** — 2026-06-10 · **버전** — v0.2 · **관리** — GitHub private repo (이미지는 `assets/`에 상대경로로 관리)
> **변경** — v0.2: 메인 컬러 `#6541F2` 통일, 9개 UI/UX 예시(SVG + HTML 데모) 추가, 안티패턴 6개 비교 이미지 추가, placeholder 시각화

---

## 이 문서 사용법

- 각 법칙은 **정의 → 시각 예시 → 왜(인지 원리) → UI/UX 적용 → 레퍼런스 → 체크리스트**의 6블록 구조로 반복됩니다.
- 처음 볼 때는 **2장(개별 법칙)** 보다 **1장(프레그난츠)** 을 먼저 읽으면 "왜 이런 법칙들이 존재하는지" 뼈대가 잡힙니다.
- 실무 적용 감각은 **4장(케이스 스터디)** 가 핵심입니다. 한 화면엔 여러 법칙이 동시에 작동합니다.
- 빠른 리뷰용으로는 **6장(체크리스트)** 만 펼쳐 쓰세요.
- 원리 설명 다이어그램은 모두 제작본이 들어가 있습니다. 각 PNG는 편집 가능한 **`.svg` 원본**이 `assets/`에 함께 있어, Figma·일러스트레이터로 색/형태를 바로 수정할 수 있습니다.
- **3장(위계 분석)·4.5절(이벤트 페이지)** 두 곳은 본인 작업 화면이 들어갈 자리라 임시 placeholder 이미지가 들어가 있습니다. 같은 파일명(`assets/03-hierarchy-annotated.png`, `assets/04-5-event-page.png`)으로 캡처를 덮어쓰면 교체됩니다.
- 각 법칙의 **UI/UX 적용** 절에는 SVG 목업 예시와 인터랙티브 HTML 데모(`assets/examples/`)가 함께 들어 있습니다. HTML은 원시 보기(`raw.githack.com`)로 열거나 로컬에서 직접 확인할 수 있습니다.

## 목차

1. [게슈탈트 심리학 개요](#1-게슈탈트-심리학-개요)
2. [핵심 그룹핑 법칙](#2-핵심-그룹핑-법칙)
   - [2.1 근접성 Proximity](#21-근접성-proximity)
   - [2.2 유사성 Similarity](#22-유사성-similarity)
   - [2.3 공통 영역 Common Region](#23-공통-영역-common-region)
   - [2.4 연결성 Uniform Connectedness](#24-연결성-uniform-connectedness)
   - [2.5 연속성 Continuity](#25-연속성-continuity--good-continuation)
   - [2.6 폐쇄성 Closure](#26-폐쇄성-closure)
   - [2.7 전경-배경 Figure-Ground](#27-전경-배경-figureground)
   - [2.8 공동운명 Common Fate](#28-공동운명-common-fate)
   - [2.9 대칭과 질서 Symmetry / Prägnanz](#29-대칭과-질서-symmetry--prägnanz)
3. [시각 위계 Visual Hierarchy](#3-시각-위계-visual-hierarchy)
4. [화면 적용 케이스 스터디](#4-화면-적용-케이스-스터디)
5. [안티패턴 / 흔한 실수](#5-안티패턴--흔한-실수)
   - [5.1 어중간한 간격](#51-어중간한-간격)
   - [5.2 유사성 과용](#52-유사성-과용)
   - [5.3 상자 천지](#53-상자-천지)
   - [5.4 전부 강조 = 강조 없음](#54-전부-강조--강조-없음)
   - [5.5 과한 폐쇄성 / 생략](#55-과한-폐쇄성--생략)
   - [5.6 배경 위 저대비 텍스트](#56-배경-위-저대비-텍스트)
6. [실무 체크리스트](#6-실무-체크리스트)
7. [참고 자료](#7-참고-자료)
8. [부록: 용어집](#8-부록-용어집)

---

## 1. 게슈탈트 심리학 개요

**한 줄 정의** — "전체는 부분의 합과 다르다(The whole is different from the sum of its parts)." 우리 시각 시스템은 개별 요소를 따로 보지 않고, 의식하기 전에 먼저 **묶고·분리하고·완성해서** 의미 있는 구조로 지각한다.

**배경** — 1910~30년대 독일에서 막스 베르트하이머(Max Wertheimer), 쿠르트 코프카(Kurt Koffka), 볼프강 쾰러(Wolfgang Köhler)가 정립했다. "Gestalt"는 독일어로 형태·구조·전체를 뜻한다. 이들은 인간이 무질서 속에서 어떻게 질서를 찾는지를 연구했고, 그 결과가 오늘날 UI 설계의 기반이 되는 그룹핑 법칙들이다.

### 프레그난츠 법칙 (Law of Prägnanz) — 모든 법칙의 상위 원리

개별 법칙(근접성·유사성 등)을 외우기 전에 이걸 먼저 잡아야 한다. **프레그난츠(= 단순성의 법칙, the law of simplicity / minimum principle)** 는 이렇게 말한다:

> 뇌는 주어진 자극을 **가능한 한 가장 단순하고 안정적인 형태로** 조직하려 한다.

즉 개별 그룹핑 법칙들은 제각각 따로 있는 규칙이 아니라, "지각을 최대한 단순하게 만들려는" 하나의 경향이 상황별로 발현된 것이다. 근접성도, 유사성도, 폐쇄성도 결국 "이렇게 묶는 게 더 단순하니까" 일어난다.

**왜 UI/UX에서 중요한가**

- 사용자는 화면을 **읽기 전에 스캔**한다. 그 스캔 단계에서 무의식적으로 그룹을 만든다.
- 디자이너가 그룹핑 신호를 잘 주면 → 사용자의 **인지 부하**가 줄고, 의미가 빠르게 전달된다.
- 신호가 모호하면 → 뇌가 "잘못된 그룹"을 만들어 오해·이탈로 이어진다.
- 핵심: **간격·정렬·색·테두리 같은 작은 선택이 "무엇이 한 묶음인지"를 결정**한다.

![프레그난츠: 복잡함을 단순한 두 형태로 본다](./assets/01-pragnanz.png)
> 겹친 사각형과 원이 하나의 복잡한 윤곽이 아니라 두 개의 단순한 도형으로 분리되어 보인다 — 단순성으로 향하는 지각의 기본 경향.

---

## 2. 핵심 그룹핑 법칙

### 2.1 근접성 Proximity

**정의** — 서로 가까이 있는 요소들은 한 그룹으로 지각된다. 멀리 떨어진 요소들은 다른 역할을 하는 것으로 본다.

![근접성: 간격만으로 그룹이 나뉜다](./assets/02-1-proximity.png)
> 같은 점 9개를 ① 균등 배치 ② 3개씩 가깝게 배치한 두 버전. 같은 요소인데 간격만으로 묶임이 달라지는 걸 보여줄 것.

**왜 (인지 원리)** — 근접성은 가장 강력한 그룹핑 단서 중 하나로, **색이나 모양 같은 다른 단서를 압도(override)** 할 수 있다. 뇌는 공간적으로 가까운 것을 "같은 출처/같은 의미"로 추정하는 경향이 강하다. 여러 그룹핑 단서가 경쟁할 때 어떤 게 이기는지를 이해하는 게 설계의 핵심이다.

**UI/UX 적용**

- **폼**: 라벨은 해당 입력 필드에 붙이고, 필드 묶음 사이는 간격을 넓혀 섹션을 구분한다.
- **카드/리스트**: 카드 내부 요소는 가깝게, 카드 사이는 멀게 → 테두리 없이도 그룹이 보인다.
- **여백 우선 원칙**: 테두리·구분선을 추가하기 전에 **간격만으로** 그룹을 만들 수 있는지 먼저 시도한다. 시각 복잡도가 낮아진다.

> **예시 데모** — [SVG 미리보기](./assets/examples/02-1-proximity-form.svg) · [HTML 데모](./assets/examples/02-1-proximity-form.html)
>
> ![근접성 UI 예시 — 폼 라벨/섹션 그룹핑](./assets/examples/02-1-proximity-form.svg)

**레퍼런스**

- NN/g — Proximity Principle in Visual Design: https://www.nngroup.com/articles/gestalt-proximity/
- NN/g (영상) — Proximity: Gestalt Principle for UI Design: https://www.nngroup.com/videos/proximity-gestalt/
- IxDF — Gestalt Principles (Part 2: Proximity, Connectedness, Continuation): https://www.interaction-design.org/literature/article/laws-of-proximity-uniform-connectedness-and-continuation-gestalt-principles-2

**체크리스트**

- [ ] 관련된 요소는 가깝게, 관련 없는 요소는 충분히 멀게 배치했는가?
- [ ] 라벨이 엉뚱한 필드에 더 가까워 보이지 않는가?
- [ ] 테두리 없이 간격만으로 그룹이 읽히는가?

---

### 2.2 유사성 Similarity

**정의** — 색·모양·크기·방향 등 시각 특성을 공유하는 요소들은 서로 관련된 것으로 지각된다. 달라 보이는 요소는 다른 그룹으로 본다.

![유사성: 색/모양이 같으면 한 묶음으로 보인다](./assets/02-2-similarity.png)
> 격자로 배열된 점들에서 한 줄(또는 한 열)만 색을 다르게 → 배치와 무관하게 색으로 묶여 보이는 예시.

**왜 (인지 원리)** — 동일하지 않아도 **하나의 가시적 특성만 공유해도** 묶인다. 시각 시스템은 "비슷한 건 같은 부류"라는 통계적 규칙성을 자연계에서 학습해왔기 때문에, 공유 특성을 관계의 신호로 읽는다.

**UI/UX 적용**

- **버튼 위계**: 같은 색 버튼은 같은 중요도로 읽힌다. 따라서 **주요 CTA는 별도 색**을 부여해 보조 버튼들 사이에서 튀게 한다.
- **상태/카테고리 표현**: 태그·뱃지의 색을 일관되게 써서 "같은 종류"임을 알린다.
- **기능 일관성**: 링크는 링크끼리, 아이콘 버튼은 아이콘 버튼끼리 모양을 통일해 학습 비용을 낮춘다.

> **예시 데모** — [SVG 미리보기](./assets/examples/02-2-similarity-buttons.svg) · [HTML 데모](./assets/examples/02-2-similarity-buttons.html)
>
> ![유사성 UI 예시 — 버튼 위계 / 상태 태그](./assets/examples/02-2-similarity-buttons.svg)

**레퍼런스**

- NN/g — Similarity Principle in Visual Design: https://www.nngroup.com/articles/gestalt-similarity/
- NN/g (영상) — Similarity: https://www.nngroup.com/videos/similarity-gestalt-principle/
- IxDF — Gestalt Principles topic: https://www.interaction-design.org/literature/topics/gestalt-principles

**체크리스트**

- [ ] 같은 기능을 하는 요소는 시각적으로 비슷한가?
- [ ] 주요 CTA가 보조 버튼과 색/형태로 구분되는가?
- [ ] "비슷하게 생겼는데 다른 일을 하는" 요소가 사용자를 헷갈리게 하지 않는가?

---

### 2.3 공통 영역 Common Region

**정의** — 하나의 경계(테두리·배경색·박스) 안에 있는 요소들은 한 그룹으로 지각된다. 20세기 후반에 추가된 법칙으로, UX에서 특히 활용도가 높다.

![공통 영역: 테두리/배경이 묶음을 만든다](./assets/02-3-common-region.png)
> 흩어진 점들 위에 박스(배경색 영역)를 씌우면, 박스 안 점들이 한 묶음으로 보이는 예시. 근접성을 거스르고도 묶이는 점을 보여줄 것.

**왜 (인지 원리)** — 공통 영역은 강력해서, 멀리 떨어진 요소라도 같은 경계 안에 있으면 묶어버린다. 단, 가능하면 **여백만으로 묶는 게 시각 복잡도가 낮다**. 경계는 여백으로 부족할 때 보강 수단으로 쓰는 게 좋다.

**UI/UX 적용**

- **카드 UI**: 배경색/그림자/테두리로 영역을 만들어 콘텐츠 묶음을 명확히 한다.
- **섹션 구획**: 설정 화면, 대시보드 위젯 등에서 관련 컨트롤을 한 박스에 담는다.
- **남용 주의**: 모든 그룹에 박스를 치면 화면이 "상자 천지"가 되어 위계가 사라진다. 여백 → 배경색 → 테두리 순으로 가볍게.

> **예시 데모** — [SVG 미리보기](./assets/examples/02-3-common-region-cards.svg) · [HTML 데모](./assets/examples/02-3-common-region-cards.html)
>
> ![공통 영역 UI 예시 — 설정 카드 그룹핑](./assets/examples/02-3-common-region-cards.svg)

**레퍼런스**

- NN/g — The Principle of Common Region: Containers Create Groupings: https://www.nngroup.com/articles/common-region/
- NN/g (영상) — Common Region: https://www.nngroup.com/videos/common-region-gestalt/

**체크리스트**

- [ ] 경계를 추가하기 전에 여백만으로 묶을 수 없는지 검토했는가?
- [ ] 박스/카드가 너무 많아 화면이 분절되어 보이지 않는가?

---

### 2.4 연결성 Uniform Connectedness

**정의** — 선·막대 등으로 **물리적으로 연결된** 요소들은 한 그룹으로 지각된다. 이 신호는 근접성·유사성의 작은 차이를 덮을 만큼 강하다.

![연결성: 선으로 이으면 묶인다](./assets/02-4-connectedness.png)
> 떨어진 두 요소를 선으로 연결한 버전 vs 안 한 버전. 색/거리가 달라도 연결선이 묶음을 만드는 걸 보여줄 것.

**왜 (인지 원리)** — 연결은 가장 강한 그룹핑 단서 중 하나다. 시각 시스템은 물리적으로 이어진 것을 "같은 객체"로 보는 경향이 매우 강해, **근접성·유사성과 충돌해도 이긴다.**

**UI/UX 적용**

- **스텝 인디케이터**: 단계들을 선으로 이어 "하나의 흐름"임을 보여준다.
- **연결된 컨트롤**: 토글 그룹, 세그먼트 컨트롤, 차트의 데이터 라인.
- **관계 시각화**: 노드-엣지 다이어그램, 플로우.

> **예시 데모** — [SVG 미리보기](./assets/examples/02-4-connectedness-stepper.svg) · [HTML 데모](./assets/examples/02-4-connectedness-stepper.html)
>
> ![연결성 UI 예시 — 단계 인디케이터](./assets/examples/02-4-connectedness-stepper.svg)

**레퍼런스**

- NN/g (영상) — Connectedness: Gestalt Principle for UI Design: https://www.nngroup.com/videos/connectedness-gestalt/
- IxDF — Part 2 (Uniform Connectedness 포함): https://www.interaction-design.org/literature/article/laws-of-proximity-uniform-connectedness-and-continuation-gestalt-principles-2

**체크리스트**

- [ ] 흐름/순서를 보여줄 때 연결선을 쓸 수 있는가?
- [ ] 의도치 않은 선/구분선이 엉뚱한 요소를 묶고 있지 않은가?

---

### 2.5 연속성 Continuity / Good Continuation

**정의** — 눈은 선과 곡선을 따라 자연스럽게 이어서 지각한다. 정렬되어 한 방향으로 흐르는 요소들을 한 그룹·한 경로로 본다.

![연속성: 정렬된 흐름을 따라간다](./assets/02-5-continuity.png)
> 일렬로 정렬된 요소들이 하나의 경로로 읽히는 예시, 또는 두 선이 교차할 때 꺾이기보다 매끄럽게 이어 보이는 예시.

**왜 (인지 원리)** — 시각 시스템은 급격한 방향 전환보다 **매끄러운 연속**을 선호한다. 이는 자연계에서 윤곽선이 대체로 연속적이라는 통계적 규칙성에서 비롯된 것으로 본다.

**UI/UX 적용**

- **정렬**: 요소를 격자에 맞춰 정렬하면 시선이 줄을 따라 흘러 스캔이 쉬워진다.
- **캐러셀/슬라이더**: 잘린 다음 항목을 살짝 보여줘 "옆으로 더 있다"는 경로를 암시.
- **시선 유도**: 리스트·폼에서 한 축으로 정렬해 읽기 동선을 만든다.

> **예시 데모** — [SVG 미리보기](./assets/examples/02-5-continuity-carousel.svg) · [HTML 데모](./assets/examples/02-5-continuity-carousel.html)
>
> ![연속성 UI 예시 — 캐러셀 peek](./assets/examples/02-5-continuity-carousel.svg)

**레퍼런스**

- NN/g (영상) — Continuation: https://www.nngroup.com/videos/continuation-gestalt/
- IxDF — Part 2: https://www.interaction-design.org/literature/article/laws-of-proximity-uniform-connectedness-and-continuation-gestalt-principles-2

**체크리스트**

- [ ] 요소들이 명확한 축에 정렬되어 시선 동선이 매끄러운가?
- [ ] 캐러셀에서 "더 있음"을 연속성으로 암시하고 있는가?

---

### 2.6 폐쇄성 Closure

**정의** — 외부 자극이 어떤 형태와 부분적으로 맞아떨어지면, 사람은 빈 곳을 **스스로 채워** 완성된 형태로 지각한다.

![폐쇄성: 끊긴 윤곽을 완성해 본다](./assets/02-6-closure.png)
> 끊긴 원/사각형이 완성된 도형으로 보이는 예시, 또는 세 개의 팩맨 모양이 (실재하지 않는) 삼각형을 만드는 카니자 삼각형.

**왜 (인지 원리)** — 정보가 부족해도 뇌는 환경을 이해하려 빈틈을 메운다. 이 인식은 **자동적이고 지각 처리 초기에** 일어나, 완성된 형태의 빠른 인식을 돕는다. 단, 올바른 경계를 만들 **충분한 정보가 있을 때만** 작동한다.

**UI/UX 적용**

- **로고/아이콘**: 최소한의 선으로 형태를 암시해 간결하고 기억에 남게.
- **"더 있음" 암시**: 콘텐츠를 일부러 살짝 잘라 보여줘 스크롤/더보기를 유도.
- **절제**: 너무 많이 생략하면 인식 실패. 핵심 단서는 남긴다.

> **예시 데모** — [SVG 미리보기](./assets/examples/02-6-closure-readmore.svg) · [HTML 데모](./assets/examples/02-6-closure-readmore.html)
>
> ![폐쇄성 UI 예시 — 잘린 콘텐츠 / 더 읽기](./assets/examples/02-6-closure-readmore.svg)

**레퍼런스**

- NN/g — Principle of Closure in Visual Design: https://www.nngroup.com/articles/principle-closure/
- IxDF — Law of Closure: https://www.interaction-design.org/literature/topics/law-of-closure

**체크리스트**

- [ ] 형태를 완성하기에 충분한 단서를 남겼는가? (과한 생략 금지)
- [ ] 잘린 콘텐츠가 "더 있음"을 자연스럽게 암시하는가?

---

### 2.7 전경-배경 Figure/Ground

**정의** — 사람은 장면을 전경(figure, 주목 대상)과 배경(ground)으로 나누고, 전경에 지각을 집중한다. 한 번에 하나의 해석에만 집중할 수 있다(루빈의 꽃병).

![전경-배경: 무엇이 떠오르고 무엇이 물러나는가](./assets/02-7-figure-ground.png)
> 루빈의 꽃병(얼굴/꽃병) 또는 모달 다이얼로그가 어두운 오버레이 위로 떠오르는 화면.

**왜 (인지 원리)** — 시각 시스템은 자극을 받자마자 "무엇이 대상이고 무엇이 바탕인지"를 가른다. 대비·명도·크기·심도(그림자) 단서로 이 분리가 결정된다.

**UI/UX 적용**

- **모달/오버레이**: 배경을 어둡게 깔아 다이얼로그를 전경으로 띄운다.
- **CTA 강조**: 충분한 대비로 행동 버튼을 전경에 둔다.
- **가독성**: 배경 이미지 위 텍스트는 오버레이/그림자로 전경-배경을 확실히 분리한다(이게 깨지면 텍스트가 묻힌다).

> **예시 데모** — [SVG 미리보기](./assets/examples/02-7-figure-ground-modal.svg) · [HTML 데모](./assets/examples/02-7-figure-ground-modal.html)
>
> ![전경-배경 UI 예시 — 모달 다이얼로그](./assets/examples/02-7-figure-ground-modal.svg)

**레퍼런스**

- NN/g (영상) — Figure/Ground: https://www.nngroup.com/videos/figure-ground-gestalt/
- IxDF — Part 3 (Figure/Ground, Prägnanz, Closure, Common Fate): https://www.interaction-design.org/literature/article/the-laws-of-figure-ground-praegnanz-closure-and-common-fate-gestalt-principles-3
- IxDF (HCI 용어집) — Figure-ground & 폼 지각: https://www.interaction-design.org/literature/book/the-glossary-of-human-computer-interaction/gestalt-principles-of-form-perception

**체크리스트**

- [ ] 사용자가 "지금 봐야 할 것(전경)"이 분명한가?
- [ ] 배경 이미지 위 텍스트의 대비가 충분한가?
- [ ] 전경 요소가 둘 이상 경쟁하며 시선을 분산시키지 않는가?

---

### 2.8 공동운명 Common Fate

**정의** — 같은 방향·같은 속도로 **함께 움직이는** 요소들은 한 그룹으로 지각된다. 가만히 있거나 다르게 움직이는 요소와는 구별된다.

![공동운명: 함께 움직이면 한 묶음](./assets/02-8-common-fate.png)
> 정적 매체라 표현이 어려우면, 함께 펼쳐지는 서브메뉴/아코디언의 전·후 프레임 2장 또는 움직임 방향 화살표로 표현.

**왜 (인지 원리)** — 움직임의 동기화는 매우 강한 그룹핑 단서다. 자연계에서 함께 움직이는 것은 대개 같은 객체이기 때문이다. 폐쇄성·전경-배경과도 상호작용해, 함께 움직이는 요소를 전경으로 부각시킬 수 있다.

**UI/UX 적용**

- **모션/트랜지션**: 펼쳐지는 메뉴·콘텐츠가 같은 방향으로 움직여 "한 묶음"임을 전달.
- **로딩/상태 변화**: 동시에 페이드되는 요소들을 한 단위로 인식시킴.
- **모바일 특히 주의**: 작은 화면일수록 모션이 그룹 관계를 전달하는 비중이 크다.

> **예시 데모** — [SVG 미리보기](./assets/examples/02-8-common-fate-accordion.svg) · [HTML 데모](./assets/examples/02-8-common-fate-accordion.html)
>
> ![공동운명 UI 예시 — 아코디언 펼침 전/후](./assets/examples/02-8-common-fate-accordion.svg)

**레퍼런스**

- NN/g (영상) — Common Fate: https://www.nngroup.com/videos/common-fate-gestalt/
- IxDF — Law of Common Fate: https://www.interaction-design.org/literature/topics/law-of-common-fate

**체크리스트**

- [ ] 관련 요소가 트랜지션에서 같은 방식으로 움직이는가?
- [ ] 무관한 요소가 같은 모션을 공유해 잘못 묶이지 않는가?

---

### 2.9 대칭과 질서 Symmetry / Prägnanz

**정의** — 사람은 대상을 가능한 한 단순하고 대칭적인 형태로 지각한다. 떨어져 있어도 대칭을 이루는 요소들을 하나의 정돈된 전체로 본다.

![대칭/질서: 균형 잡힌 단순한 형태로 본다](./assets/02-9-symmetry.png)
> 대칭 배치된 괄호/요소가 하나의 단위로 묶여 보이는 예시, 또는 균형 잡힌 그리드 레이아웃 한 장.

**왜 (인지 원리)** — 1장의 프레그난츠가 형태 차원에서 발현된 모습이다. 복잡한 배열도 뇌는 "가장 단순하고 균형 잡힌 해석"으로 정리한다.

**UI/UX 적용**

- **그리드 시스템**: 일관된 그리드와 정렬이 "정돈됨 = 신뢰감"을 준다(금융 앱에서 특히 중요).
- **균형**: 대칭/비대칭 균형으로 시선 무게를 설계.
- **단순화**: 불필요한 장식을 덜어내면 핵심 구조가 또렷해진다.

> **예시 데모** — [SVG 미리보기](./assets/examples/02-9-symmetry-pricing.svg) · [HTML 데모](./assets/examples/02-9-symmetry-pricing.html)
>
> ![대칭/질서 UI 예시 — 가격표 그리드](./assets/examples/02-9-symmetry-pricing.svg)

**레퍼런스**

- IxDF — Part 3 (Prägnanz 포함): https://www.interaction-design.org/literature/article/the-laws-of-figure-ground-praegnanz-closure-and-common-fate-gestalt-principles-3
- (이론 심화) Wagemans et al. (2012) Part II — 프레그난츠/단순성 원리: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3728284/

**체크리스트**

- [ ] 레이아웃이 일관된 그리드/정렬을 따르는가?
- [ ] 장식 요소가 핵심 구조를 흐리지 않는가?

---

## 3. 시각 위계 Visual Hierarchy

게슈탈트 법칙들은 결국 **"무엇이 한 묶음이고, 그중 무엇이 더 중요한가"** 를 설계하는 도구다. 그룹핑은 곧 우선순위 신호다.

**위계를 만드는 레버**

- **크기/굵기**: 큰 것·굵은 것이 먼저 읽힌다.
- **대비/색**: 전경-배경 + 유사성으로 강조점을 만든다.
- **여백**: 근접성 + 공통영역으로 묶고 분리한다.
- **위치**: 상단·좌측이 스캔 우선순위가 높다(읽기 방향).

**스캔 패턴과의 연결**

- 텍스트 중심 화면은 **F-패턴**, 시각 요소가 많은 화면은 **Z-패턴/레이어케이크 패턴**으로 스캔되는 경향. 위계 설계 시 첫 시선이 닿는 지점에 핵심을 배치한다.
- NN/g — The Gestalt Principles for UI Design (위계·스케일·대비 종합): https://www.nngroup.com/videos/the-gestalt-principles-intro/
- NN/g — Visual Design 용어집/치트시트: https://www.nngroup.com/articles/visual-design-cheat-sheet/

![위계 분석 placeholder](./assets/03-hierarchy-annotated.svg)
> 본인 작업 화면 한 장에 그룹 경계를 색 오버레이로 그려 "어떤 법칙이 어디서 작동하는지" 분석 주석을 단 이미지로 교체하세요 (`assets/03-hierarchy-annotated.png`).

---

## 4. 화면 적용 케이스 스터디

> 핵심: **실제 화면엔 여러 법칙이 동시에 작동한다.** 단일 법칙으로 보지 말고 "겹쳐 읽는" 연습을 한다.

### 4.1 카드 레이아웃
- 작동 법칙: **근접성**(카드 내부 요소) + **공통 영역**(카드 배경/테두리) + **유사성**(카드 구조 통일)
- 체크: 카드 내부는 가깝게, 카드 사이는 멀게. 카드 구조는 통일.

### 4.2 폼 / 입력
- 작동 법칙: **근접성**(라벨-필드) + **연결성/공통영역**(섹션 구획)
- 체크: 라벨이 올바른 필드에 붙었는가. 섹션 간 간격이 충분한가.

### 4.3 내비게이션 / 탭
- 작동 법칙: **유사성**(탭 형태 통일) + **전경-배경**(현재 탭 강조) + **공동운명**(전환 모션)
- 체크: 현재 위치가 전경으로 떠오르는가.

### 4.4 가격표 / 플랜 비교
- 작동 법칙: **유사성**(열 구조 통일) + **대칭**(균형) + **전경-배경**(추천 플랜 강조)
- 체크: 추천 플랜이 전경으로 분리되는가. 비교 항목이 행으로 정렬(연속성)되는가.

### 4.5 이벤트 페이지 *(실무 직결 — 직접 사례 채우기)*
- 작동 법칙: **전경-배경**(혜택/CTA 강조) + **근접성**(혜택 묶음) + **유사성**(반복 모듈)

![이벤트 페이지 placeholder](./assets/04-5-event-page.svg)
> 본인이 만든 이벤트 페이지 캡처 + 그룹 분석 주석으로 교체하세요 (`assets/04-5-event-page.png`).

---

## 5. 안티패턴 / 흔한 실수

각 항목은 **✗ 잘못된 예 ↔ ✓ 바로잡은 예** 비교 이미지가 함께 있습니다.

### 5.1 어중간한 간격
그룹 내부와 그룹 사이 간격 차이가 작아 묶음이 모호해진다. → **간격 대비를 키운다.**

![어중간한 간격 vs 그룹 간격 대비](./assets/examples/05-1-spacing.svg)

### 5.2 유사성 과용
모든 버튼이 같은 색·크기 → 위계가 사라져 주요 행동이 안 보인다. → **주요 CTA만 채움 색·다른 형태로 차별화.**

![모든 버튼 동일 강조 vs 주요 CTA만 차별화](./assets/examples/05-2-similarity-overuse.svg)

### 5.3 상자 천지
모든 그룹에 테두리·박스를 두르면 시각 복잡도가 폭발하고, 정작 중요한 위계가 사라진다. → **여백 → 배경색 → 테두리 순으로 가장 약한 신호부터 시도한다.**

이 안티패턴은 한 가지 모습이 아니다. 자주 보는 변형들:

- **모든 섹션 박스화** — 페이지 안의 모든 그룹에 카드/테두리. 위계가 사라져 어디부터 봐야 할지 모름.
- **중첩 카드(card-in-card)** — 카드 안에 또 카드, 또 그 안에 입력 박스. 깊이감이 과해져 "지금 내가 어느 계층에 있는지" 인지 비용 증가.
- **모든 폼 필드를 카드로 감싸기** — 라벨+필드 하나하나가 카드. 입력해야 할 흐름이 보이지 않고 폼이 산만해 보임.
- **리스트 항목마다 테두리** — `<li>` 하나하나에 박스. 리스트라는 "이미 묶인 구조"에 박스가 중복 신호로 작용.
- **섹션마다 다른 배경색** — 영역을 나누려고 배경색을 다르게 쓰면 색이 의미 없이 늘어나 색 위계까지 무너짐.
- **불필요한 디바이더(divider)** — 가로선이 너무 자주 나오면 콘텐츠가 토막 나 흐름이 끊김.

**처방** — 여백으로 묶을 수 있다면 박스를 쓰지 않는다. 정말 필요할 때만 ① 옅은 배경색 → ② 가는 테두리 순으로, 단 한 계층만 사용한다.

#### (a) 너무 많은 카드 → 여백 위주
![상자 천지 vs 여백 우선](./assets/examples/05-3-box-everywhere.svg)

#### (b) 중첩 카드 → 단일 카드 + 섹션 여백
![중첩 카드 vs 단일 카드](./assets/examples/05-3b-nested-cards.svg)

#### (c) 필드마다 카드 → 라벨 + 필드만
![필드마다 카드 vs 라벨+필드](./assets/examples/05-3c-boxed-fields.svg)

### 5.4 전부 강조 = 강조 없음
강조 요소가 너무 많으면 전경이 사라진다. → **화면당 핵심 전경은 1~2개.**

![모든 텍스트 강조 vs 한 곳만 강조](./assets/examples/05-4-emphasis-everywhere.svg)

### 5.5 과한 폐쇄성 / 생략
정보가 너무 부족하면 형태 인식에 실패한다. → **윤곽을 암시할 최소 단서는 남긴다.**

![과한 생략 vs 충분한 단서](./assets/examples/05-5-over-closure.svg)

### 5.6 배경 위 저대비 텍스트
전경-배경 분리가 깨지면 가독성이 무너진다. → **그라디언트 오버레이/그림자로 대비 보강.**

![저대비 텍스트 vs 오버레이 + 고대비](./assets/examples/05-6-low-contrast.svg)

---

## 6. 실무 체크리스트

설계 리뷰할 때 이 한 페이지만 펼쳐 쓴다.

- [ ] **근접성** — 관련 요소는 가깝게, 무관 요소는 멀게?
- [ ] **유사성** — 같은 기능 = 비슷한 모양? 주요 CTA는 차별화?
- [ ] **공통 영역** — 경계 전에 여백으로 묶을 수 있나? 박스 남용 아닌가?
- [ ] **연결성** — 흐름/관계를 선으로 보여줄 수 있나? 의도치 않은 연결 없나?
- [ ] **연속성** — 정렬 축이 명확해 시선 동선이 매끄럽나?
- [ ] **폐쇄성** — 형태 인식에 충분한 단서? 과한 생략 아닌가?
- [ ] **전경-배경** — 지금 봐야 할 것이 분명? 배경 위 텍스트 대비 충분?
- [ ] **공동운명** — 관련 요소가 같은 모션? 무관 요소가 잘못 묶이지 않나?
- [ ] **대칭/질서** — 일관된 그리드? 장식이 구조를 흐리지 않나?
- [ ] **위계** — 첫 시선 지점에 핵심이 있나? 강조 전경이 1~2개로 절제됐나?

---

## 7. 참고 자료

### 원전 (이론의 뿌리)
- **Wertheimer, M. (1923). Laws of Organization in Perceptual Forms.** — 그룹핑 법칙의 출발점. 영어 번역본 무료 공개(Classics in the History of Psychology):
  http://psychclassics.yorku.ca/Wertheimer/Forms/forms.htm

### 현대 학술 종합 리뷰 (깊이의 핵심 · 오픈 액세스)
- **Wagemans et al. (2012). A century of Gestalt psychology in visual perception: I. Perceptual grouping and figure–ground organization.** *Psychological Bulletin.* — 그룹핑·전경-배경 100년 연구 정리. PMC 무료:
  https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3482144/
- **Wagemans et al. (2012). II. Conceptual and theoretical foundations.** — 프레그난츠/단순성 등 이론적 기초:
  https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3728284/

### 실무 (UI/UX 적용)
- **Nielsen Norman Group — Gestalt 토픽 허브**: https://www.nngroup.com/topic/gestalt/
  - Proximity: https://www.nngroup.com/articles/gestalt-proximity/
  - Similarity: https://www.nngroup.com/articles/gestalt-similarity/
  - Common Region: https://www.nngroup.com/articles/common-region/
  - Closure: https://www.nngroup.com/articles/principle-closure/
  - 영상 모음(Connectedness/Continuation/Figure-Ground/Common Fate): 위 토픽 허브에서 접근
  - 종합 영상 — The Gestalt Principles for UI Design: https://www.nngroup.com/videos/the-gestalt-principles-intro/
  - Visual Design 치트시트/용어집: https://www.nngroup.com/articles/visual-design-cheat-sheet/
- **Interaction Design Foundation (IxDF)**
  - Gestalt Principles 토픽: https://www.interaction-design.org/literature/topics/gestalt-principles
  - Part 2 (Proximity·Connectedness·Continuation): https://www.interaction-design.org/literature/article/laws-of-proximity-uniform-connectedness-and-continuation-gestalt-principles-2
  - Part 3 (Figure-Ground·Prägnanz·Closure·Common Fate): https://www.interaction-design.org/literature/article/the-laws-of-figure-ground-praegnanz-closure-and-common-fate-gestalt-principles-3
  - Law of Closure: https://www.interaction-design.org/literature/topics/law-of-closure
  - Law of Common Fate: https://www.interaction-design.org/literature/topics/law-of-common-fate

> ※ 위 외부 페이지의 예시 스크린샷을 외부 공유 문서에 그대로 옮기는 것은 저작권 문제가 될 수 있음. 개인 학습용 캡처는 자유롭게, 공유 시에는 직접 제작 다이어그램으로 대체할 것.

---

## 8. 부록: 용어집

- **게슈탈트(Gestalt)** — 형태·구조·전체. 부분의 단순 합과 다른 통합된 지각.
- **프레그난츠(Prägnanz)** — 단순성의 법칙. 뇌가 가능한 한 단순·안정적 형태로 지각하려는 상위 경향.
- **그룹핑(perceptual grouping)** — 개별 요소를 묶어 단위로 지각하는 과정.
- **전경-배경(figure–ground)** — 장면을 주목 대상과 바탕으로 분리하는 지각.
- **시각 위계(visual hierarchy)** — 요소의 중요도를 시각적 차이로 설계해 시선 순서를 만드는 것.
- **F-패턴 / Z-패턴** — 사용자가 화면을 스캔하는 전형적 시선 경로.

---

*문서 끝 · 갱신 시 버전과 날짜를 상단에 기록할 것.*
