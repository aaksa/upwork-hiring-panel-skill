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
4. **Tests the hook until it wins**: The Scroller rates 4 or 5 opening lines one by one, and a blind lineup Scroller
   ranks them against 6 realistic competitor previews. It iterates (up to 3 rounds) until a hook scores 9+ and lands
   in the top 2, or reports honestly where it plateaus and what proof would break the ceiling.
5. Runs The Hiring Client again on the full rewrite and shows the before and after verdict.

Everything goes in `.upwork-hiring-panel/` where you run it: `PANEL.md` and `PROPOSAL-IMPROVED.md`.

## Grounded in what actually gets hired

Language-model reviewers like clever, long, analytical proposals. Real clients skim and click proof. So the panel and the
rewrite are grounded in `references/winning-patterns.md`: what Upwork shows a client before they open a proposal, vendor
data on timing and crowding, and the **proof-first shape** of proposals that were actually hired:

1. Line one names the client's kind of app, in their words, and says you've built it.
2. One hard credential with a number.
3. Three to seven clickable links (store listings, demos), most relevant first.
4. Every "To apply, please send…" item answered.
5. Availability. Short sign-off.

It also gives a **visibility checklist** (timing, competition, profile card, keywords, boost), because a proposal that is
never opened is often a visibility problem, not a wording problem.

### Teach it your wins

Put proposals that got you hired in `~/.claude/upwork-hiring-panel/wins.md` (job post, proposal, outcome, and a proof
bank of your real links). The skill reads it on every run, reuses your real proof and matches the shape that worked for
you. When you tell it a proposal got hired, it offers to add it. This file stays on your machine.

### Fast mode

Replies drop fast after a job is posted, so speed beats polish. `/upwork-hiring-panel fast …` skips the panel and gives
you the proof-first rewrite, screening answers and checklist in a couple of minutes. Send it, then run the full panel
and edit within Upwork's edit window.

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
/upwork-hiring-panel fast <proposal> <job post>
```

Or paste it: the proposal, then the job post, then your bid and any screening answers. The job post matters most; without
it the panel can only guess at relevance. One full run is roughly 8 sub-agent calls for the panel plus up to 18 short calls for the hook lab, and it counts
toward your Claude plan's usage.

## Layout

```
skills/upwork-hiring-panel/
  SKILL.md                 the workflow
  references/personas.md   the seven reviewer briefs, passed to each sub-agent word for word
  references/rubric.md     scores, interview-chance rule, rejection patterns, rewrite and screening rules
  references/winning-patterns.md  what clients see, market data, the proof-first shape, visibility checklist
  references/hook-lab.md   the solo + blind-lineup hook test loop, competitor preview types, lessons so far
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
