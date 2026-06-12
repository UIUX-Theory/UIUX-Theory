#!/usr/bin/env bash
#
# install.sh — 이 레포의 모든 스킬을 Claude Code가 읽는 위치로 심볼릭 링크합니다.
#
# 사용법:
#   ./scripts/install.sh            # 개인(personal) 스킬로 설치 → ~/.claude/skills/
#   ./scripts/install.sh --project  # 현재 프로젝트 전용으로 설치 → ./.claude/skills/
#   ./scripts/install.sh --dry-run  # 실제로 만들지 않고 뭐가 링크될지만 출력
#
# 동작 원리:
#   skills/ 아래 (깊이 무관) 모든 */SKILL.md 를 찾아, 그 부모 폴더를
#   대상 위치에 같은 이름으로 심볼릭 링크합니다.
#   링크라서, 레포에서 SKILL.md 를 고치면 재설치 없이 바로 반영됩니다.

set -euo pipefail

# ── 레포 루트(이 스크립트의 한 단계 위) 절대경로 ────────────────────────────
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
SKILLS_SRC="$REPO_ROOT/skills"

# ── 옵션 파싱 ──────────────────────────────────────────────────────────────
TARGET="$HOME/.claude/skills"
DRY_RUN=0
for arg in "$@"; do
  case "$arg" in
    --project) TARGET="$(pwd)/.claude/skills" ;;
    --dry-run) DRY_RUN=1 ;;
    -h|--help) sed -n '2,20p' "$0"; exit 0 ;;
    *) echo "알 수 없는 옵션: $arg" >&2; exit 1 ;;
  esac
done

if [ ! -d "$SKILLS_SRC" ]; then
  echo "❌ skills/ 폴더를 찾을 수 없어요: $SKILLS_SRC" >&2
  exit 1
fi

echo "📂 소스 : $SKILLS_SRC"
echo "🎯 대상 : $TARGET"
[ "$DRY_RUN" = 1 ] && echo "🔎 (dry-run: 실제로는 만들지 않습니다)"
echo

[ "$DRY_RUN" = 0 ] && mkdir -p "$TARGET"

linked=0; skipped=0; conflict=0
declare -a seen_names=()

# SKILL.md 를 가진 모든 스킬 폴더 순회 (깊이 무관)
while IFS= read -r skillmd; do
  skill_dir="$(cd "$(dirname "$skillmd")" && pwd)"
  name="$(basename "$skill_dir")"

  # 같은 이름 중복 방지 (명령어 충돌)
  dup=0
  for s in "${seen_names[@]:-}"; do [ "$s" = "$name" ] && dup=1; done
  if [ "$dup" = 1 ]; then
    echo "⚠️  이름 중복 → 건너뜀: $name  ($skill_dir)"
    conflict=$((conflict+1)); continue
  fi
  seen_names+=("$name")

  dest="$TARGET/$name"

  # 이미 존재하는 경우 처리
  if [ -L "$dest" ]; then
    # 기존 심링크 → 갱신
    [ "$DRY_RUN" = 0 ] && { rm "$dest"; ln -s "$skill_dir" "$dest"; }
    echo "🔄 갱신   : $name"
    linked=$((linked+1)); continue
  elif [ -e "$dest" ]; then
    # 실제 폴더/파일이 이미 있음 → 덮어쓰지 않음
    echo "⛔ 충돌   : $name (대상에 이미 실제 폴더가 있어 건너뜀)"
    conflict=$((conflict+1)); continue
  fi

  [ "$DRY_RUN" = 0 ] && ln -s "$skill_dir" "$dest"
  echo "✅ 링크   : $name"
  linked=$((linked+1))
done < <(find "$SKILLS_SRC" -type f -name SKILL.md | sort)

echo
echo "── 요약 ──────────────────────────────"
echo "링크/갱신: $linked   충돌/건너뜀: $conflict"
echo
echo "처음 설치라면(이전에 $TARGET 가 없었다면) Claude Code 를 한 번 재시작하세요."
echo "이후 스킬 수정은 재시작 없이 바로 반영됩니다."
