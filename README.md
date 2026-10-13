# The Upwork hiring panel skill

You send proposals on Upwork, spend Connects, and almost never hear why a client didn't reply. This skill tells you
first: seven Claudes read your proposal as seven different people, each alone, explain why it gets skipped or declined,
then rewrite it into a client-focused proposal built to get the interview.

## The panel

| # | Reviewer | Reads | Judges | Verdict |
|---|---|---|---|---|
| 1 | **The Scroller** | Only the first two lines, like a busy client in the proposal list | Hook | OPEN / SKIP |
| 2 | **The Hiring Client** | Everything, next to the job post | Relevance, interview potential | INTERVIEW / MAYBE / NO |
| 3 | **The Budget-Conscious Client** | Scope, timeline, price | Value proposition | WORTH IT / NOT SURE / TOO EXPENSIVE |
| 4 | **The Competing Freelancer** | Your proposal as a rival on the same job | Differentiation | THEY WIN / TOSS-UP / I WIN |
| 5 | **The Skeptic** | Proof versus claims | Credibility | TRUST / UNSURE / DISTRUST |
| 6 | **The Technical Lead** | Approach and understanding | Clarity | KNOWS IT / VAGUE / WRONG |
| 7 | **The Upwork Veteran** | Template tells, length, screening answers, platform rules | Interview potential | SHORTLIST / ARCHIVE / DECLINE |

Nobody sees anybody else's notes. Then the skill:

1. Scores **Hook, Clarity, Relevance, Credibility, Value Proposition and Interview Potential** (1–10) and gives an
   interview chance: LOW, MEDIUM or HIGH.
2. Merges everything into one list of problems, worst first, and writes **the rejection story** in the client's voice.
3. **Rewrites the proposal** (same facts, nothing invented), plus three alternative opening lines.
   If the job has screening questions, it also writes a **fixed answer for every question**, each in its own code
   block, ready to paste into that question's own input box on Upwork (even when you had no answer yet).
4. Runs The Scroller and The Hiring Client again on the rewrite and shows the before and after verdict.

Everything goes in `.upwork-hiring-panel/` where you run it: `PANEL.md` and `PROPOSAL-IMPROVED.md`.

## Install

Paste this into Claude Code:

```
https://github.com/aaksa/upwork-hiring-panel-skill
Install this skill, then confirm /upwork-hiring-panel works.
```

Or as a plugin:

```
/plugin marketplace add aaksa/upwork-hiring-panel-skill
/plugin install upwork-hiring-panel-skill@upwork-hiring-panel-skill
```

Or copy `skills/upwork-hiring-panel` into `~/.claude/skills/`. Open a new Claude Code session afterwards.

## Use

```
/upwork-hiring-panel examples/sample-proposal.md
```

Or paste it: the proposal, then the job post, then your bid and any screening answers. The job post matters most; without
it the panel can only guess at relevance. One run is nine sub-agent calls (seven reviewers plus two re-checks) and counts
toward your Claude plan's usage.

## Layout

```
skills/upwork-hiring-panel/
  SKILL.md                 the workflow
  references/personas.md   the seven reviewer briefs, passed to each sub-agent word for word
  references/rubric.md     scores, interview-chance rule, rejection patterns, rewrite rules
examples/sample-proposal.md  a weak proposal and job post to try it on
tests/test_skill.py
```

Change a reviewer by editing its brief in `personas.md`; change what "good" means by editing `rubric.md`.

## Good to know

- It never invents clients, results, numbers or portfolio items. Where a fix needs a fact it doesn't have, it leaves
  `[ADD: ...]` and asks you.
- It flags any attempt to move contact or payment off Upwork, since that breaks Upwork's terms.
- It's a structured second opinion made by language models. It doesn't guarantee an interview or a hire.
- Not affiliated with Upwork or Anthropic.

Run the tests with `python3 -m unittest discover -s tests`.

## Credit

The seven-reviewer structure is adapted from [hiring-panel-skill](https://github.com/alexyc9381/hiring-panel-skill)
by Alex Chen (MIT), which runs the same idea on resumes.
