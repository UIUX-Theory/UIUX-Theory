# 게슈탈트 시지각 원리 → UI/UX 적용 레퍼런스

> 게슈탈트 시지각 이론을 깊게 이해하고, 그 원리를 화면 설계(레이아웃·그룹핑·시각 위계)에 적용하기 위한 학습 레퍼런스.

## 📖 문서 사이트

**전체 콘텐츠는 정적 사이트로 보세요** → **https://uiux-theory.github.io/UIUX-Theory/**

좌측 LNB로 각 법칙·케이스·체크리스트로 빠르게 이동할 수 있고, 다크 모드·검색·각 헤딩 앵커 링크가 지원됩니다.

## 📂 리포지토리 구조

```
docs/
├── index.md                 # 개요 + 프레그난츠
├── principles/              # 2장 — 9개 그룹핑 법칙
│   ├── proximity.md
│   ├── similarity.md
│   ├── common-region.md
│   ├── connectedness.md
│   ├── continuity.md
│   ├── closure.md
│   ├── figure-ground.md
│   ├── common-fate.md
│   └── symmetry.md
├── hierarchy.md             # 3장 — 시각 위계
├── case-studies.md          # 4장 — 화면 적용 케이스
├── antipatterns.md          # 5장 — 안티패턴
├── checklist.md             # 6장 — 실무 체크리스트
├── references.md            # 7장 — 참고 자료
├── glossary.md              # 8장 — 용어집
└── assets/                  # SVG 다이어그램 + 인터랙티브 HTML 데모

gen_diagrams.py              # 원리 설명 다이어그램 생성
gen_examples.py              # UI/UX 예시 + HTML 데모 생성
gen_antipatterns.py          # 안티패턴 비교 이미지 생성
gen_cases.py                 # 보조 케이스 스터디 이미지 생성

mkdocs.yml                   # MkDocs Material 설정
.github/workflows/deploy-docs.yml  # GitHub Pages 자동 배포
```

## 🛠 로컬 미리보기

```bash
pip install -r requirements.txt
mkdocs serve
# → http://127.0.0.1:8000
```

## 🎨 다이어그램 재생성

```bash
python3 gen_diagrams.py     # 9개 법칙 설명 다이어그램
python3 gen_examples.py     # 9개 UI 예시 (SVG + HTML)
python3 gen_antipatterns.py # 8개 안티패턴 비교
python3 gen_cases.py        # 9개 보조 케이스 스터디
```

생성된 SVG는 `docs/assets/`에 저장되며, 메인 컬러는 `#6541F2`.

## 📌 메타

- **버전** v0.4 · **언어** 한국어
- **테마** MkDocs Material (deep purple `#6541F2`)
- **배포** GitHub Pages via GitHub Actions
