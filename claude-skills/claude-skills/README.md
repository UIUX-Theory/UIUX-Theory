# claude-skills

내 Claude 스킬들의 **단일 소스 저장소**예요.
스킬을 여기에 모아두고, 각 컴퓨터에서 `~/.claude/skills/` 로 심볼릭 링크해 씁니다.
계정이 자동 동기화해주지 않는 Claude Code 쪽을, 깃으로 메우는 구조예요.

---

## 폴더 구조

```
claude-skills/
├── README.md
├── scripts/
│   └── install.sh          # 모든 스킬을 ~/.claude/skills/ 로 링크
└── skills/
    ├── product-designer-mindset/  # 기획안→문제·퍼널·가설·우선순위로 환원하는 코치
    │   ├── SKILL.md
    │   └── references/
    ├── ux-burden-check/     # 심리 기반 인지 부담 진단 → 확인 → 코드 수정
    │   ├── SKILL.md
    │   └── references/
    └── ui-detail-check/     # (소스 채워넣기 — 아래 참고)
```

스킬 하나 = `SKILL.md` 를 가진 폴더 하나. `skills/` 아래라면 어떤 깊이에 둬도 돼요
(`skills/design/...` 처럼 분류해도 install.sh 가 알아서 찾아 평탄하게 링크합니다).

> **주의 — 폴더 이름이 곧 명령어 이름입니다.**
> `skills/ux-burden-check/` → Claude Code 에서 `/ux-burden-check`.
> 나중에 폴더명을 바꾸면 명령어도 바뀌니, 이름은 처음에 신중히. (kebab-case 권장)

---

## 새 컴퓨터에서 셋업 (한 번)

```bash
git clone <이-레포-주소> ~/dev/claude-skills
cd ~/dev/claude-skills
./scripts/install.sh
```

처음 설치라(이전에 `~/.claude/skills/` 가 없었다면) Claude Code 를 **한 번 재시작**하세요.
이후부터는 재시작 없이 반영됩니다.

옵션:
- `./scripts/install.sh --project` — 현재 프로젝트 전용으로 `./.claude/skills/` 에 링크
- `./scripts/install.sh --dry-run` — 실제로 만들지 않고 뭐가 링크될지만 확인

---

## 일상 흐름

**스킬 수정** — `skills/<이름>/SKILL.md` 를 고치고 커밋.
링크로 걸려 있어서 그 컴퓨터에선 **재시작 없이 바로** 반영돼요.
다른 컴퓨터는 `git pull` 만 하면 됩니다 (링크는 이미 걸려 있으니 install.sh 재실행 불필요).

**스킬 추가** — `skills/` 아래에 새 폴더 + `SKILL.md` 를 만들고 커밋.
각 컴퓨터에서 `git pull` 후 `./scripts/install.sh` 한 번 (새 링크를 걸어야 하므로).

**스킬 삭제** — 폴더를 지우고 커밋. 각 컴퓨터에서 `~/.claude/skills/<이름>` 링크를 수동으로 제거
(`rm ~/.claude/skills/<이름>`).

---

## ui-detail-check 채우기

이 스킬은 이미 계정에 설치돼 있어 소스가 레포엔 없어요.
`skills/ui-detail-check/_ADD_HERE.md` 의 안내대로 폴더를 채운 뒤, 그 안내 파일은 지우고 커밋하세요.
`SKILL.md` 가 없는 동안에는 install.sh 가 이 폴더를 자동으로 건너뜁니다.

---

## 나중에 — 팀과 공유하게 되면

지금은 **개인 비공개 레포 하나면 충분**해요. GitHub 조직은 아직 필요 없습니다.
핀테크 디자인팀에서 같이 쓰게 되는 순간이 공유 레포(또는 조직)를 만들 타이밍이에요. 그때는:

- 공용으로 쓸 디자인 스킬만 팀 레포에 올리고, 개인/클라이언트 전용은 개인 레포에 남깁니다.
- `CLAUDE.md`(프로젝트별 맥락)는 공유하지 않는 게 보통이에요 — 사람·프로젝트마다 다르니까.
- 스킬에 agents·hooks·MCP 까지 묶어 배포하고 싶으면 **플러그인** 형태로 올리는 길도 있어요
  (스킬 폴더에 `.claude-plugin/plugin.json` 추가).

출처: [Claude Code — Extend Claude with skills](https://code.claude.com/docs/en/skills)
