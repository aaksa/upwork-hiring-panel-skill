---
name: upwork-hiring-panel
description: >-
  Run an Upwork proposal past a hiring panel of seven Claudes that each judge it alone as a different reader (a busy client who only sees the profile card and preview, the hiring client, a budget-conscious client, a competing freelancer, a burned-before skeptic, a technical lead and an Upwork veteran), grounded in what Upwork shows clients, market data and the freelancer's own hired proposals. Scores hook, clarity, relevance, credibility, value proposition and interview potential, explains why it gets skipped or rejected, then rewrites it in the proof-first shape, tests the hook against a blind lineup of competitor previews until clients would open it first, with a fixed answer for every screening question and a visibility checklist. Has a fast mode for freshly posted jobs. Use when the user types /upwork-hiring-panel followed by a proposal (file path or pasted text), or asks to review, score, critique or rewrite an Upwork proposal or cover letter.
argument-hint: "[fast] <proposal file or pasted text> [job post] [bid/rate] [screening questions] [profile]"
license: MIT
metadata:
  version: "1.3.0"
---

# /upwork-hiring-panel

The user gives you an Upwork proposal after `/upwork-hiring-panel`. Seven reviewers judge it alone, you merge what they found, explain why it gets skipped or rejected, and rewrite it so a client opens it and wants to interview the freelancer. Never flatter the proposal.

Before starting, read these files in this skill folder:
- `references/winning-patterns.md`: what clients see before opening, what the data says, and the proof-first shape of hired proposals. **This overrides any reviewer's taste.**
- `references/personas.md`: the exact brief for each of the seven reviewers.
- `references/rubric.md`: the six scores, the rejection patterns, the rewrite rules and the screening answer rules.
- `references/hook-lab.md`: the loop that tests the first two lines with The Scroller, solo and in a blind lineup, until they win, plus what earlier runs learned.

Then check for the freelancer's own wins at `~/.claude/upwork-hiring-panel/wins.md` (job posts and proposals that got hired). If it exists, read it. It is the strongest evidence you have: what got THIS freelancer hired beats general advice.

## 0. Pick the mode
- **Fast mode**: the arguments start with `fast`, or the user says the job was just posted or they are in a hurry. Do steps 1 and 5 only (no sub-agents), plus the visibility checklist. Deliver within a couple of minutes. Speed of sending matters more than a perfect letter: replies drop sharply after the first minutes and hour after posting (see `winning-patterns.md`). Tell the user they can send now, run the full panel afterwards, and edit the cover letter within Upwork's edit window.
- **Full mode** (default): every step below. If the job post shows it was posted under 2 hours ago, first give the fast rewrite in chat, then run the full panel.

## 1. Get the inputs
Everything after `/upwork-hiring-panel` is input: a file path (read it; PDF, .md and .txt are fine) or pasted text. If the Read tool cannot extract a PDF's text, extract it another way (for example a short script) before going on. Sort it into:
- **Proposal**: the cover letter the client will read. Required.
- **Job post**: title, description and any attached brief. Strongly needed. If missing, ask ONE question: "Paste the job post (title and description) you are bidding on." If the user does not have it, continue with "job post: not given" and tell every reviewer.
- **Bid**: fixed price or hourly rate, and timeline. Otherwise "bid: not given".
- **Screening questions**, each with the user's answer if there is one. Every screening question has its own input box on Upwork, so keep each question and answer separate, in order. Questions with no answer are fine: reviewers see "answer: not given", and step 5 writes the answer.
- **Profile card**: title, rate, Job Success Score, badges, if given. Otherwise "not given".
- **Job signals**, if visible in the post: how long ago it was posted, number of proposals, payment verified, client hire rate, budget.

Then build three lists you will use in every later step:
- **The client's asks**: every explicit request in the post ("To apply, please send…", "include…", "start your proposal with…", "tell us your rate") plus every screening question. Number them.
- **Match keywords**: the client's kind of app in their own words (for example "private gym booking", "health research app", "race discovery"), the platform, and the stack they named. These must appear early in the rewrite: Upwork ranks proposals by how well they match the post.
- **Proof bank**: every true, checkable fact the user gave you in this message or in `wins.md`: live app links, demo videos, named projects, numbers. Mark which ones are closest to this job. Never add anything not in these sources.

Use only what the user gave you (this message, earlier messages in this conversation, and `wins.md`). Never invent clients, results, numbers, years of experience, tools, reviews, links or portfolio items. Label guesses "assumed".

Also cut the **preview**: the first two lines of the proposal, at most about 200 characters. This is roughly what a client sees in the proposal list before clicking. Only the first reviewer gets it, together with the profile card.

## 2. Seven reviewers, alone
Start seven sub-agents at once (one message, seven Agent calls, `general-purpose`). Nobody sees anybody else's notes. Give each one exactly what `references/personas.md` says that reviewer receives, plus its brief and the shared rules copied word for word. Each answers in under 150 words in the fixed format from its brief.

1. **The Scroller**: busy client, sees only the profile card and the preview. Judges the hook. OPEN or SKIP.
2. **The Hiring Client**: owns the job and reads everything. Judges relevance, the asks and interview potential. INTERVIEW, MAYBE or NO.
3. **The Budget-Conscious Client**: has cheaper bids open. Judges the value proposition. WORTH IT, NOT SURE or TOO EXPENSIVE.
4. **The Competing Freelancer**: bid on the same job. Judges how the proposal stands out. THEY WIN, TOSS-UP or I WIN.
5. **The Skeptic**: has been burned by freelancers before. Judges credibility. TRUST, UNSURE or DISTRUST.
6. **The Technical Lead**: knows the work. Judges clarity and understanding of the problem. KNOWS IT, VAGUE or WRONG.
7. **The Upwork Veteran**: has hired 100+ freelancers on Upwork. Judges template tells, length, screening answers and platform mistakes. SHORTLIST, ARCHIVE or DECLINE.

If the Agent tool is not available, play the seven reviewers yourself one at a time, and write each verdict down before reading the next brief. Tell the user the panel was run without independent sub-agents.

## 3. Score it
Using `references/rubric.md`, give the six scores (1 to 10): **Hook, Clarity, Relevance, Credibility, Value Proposition, Interview Potential**. Each score comes from the reviewers the rubric names for it; quote the evidence. Then give the **interview chance**: LOW, MEDIUM or HIGH, by the rule in the rubric.

Then check the proposal against the proof-first shape in `winning-patterns.md`, and against `wins.md` if it exists: which parts of the winning shape are missing? Where the panel's taste and the winning shape disagree (for example a reviewer liked a clever opener that has no proof or keywords), follow the winning shape and say so.

## 4. Why it gets skipped or rejected
Merge all seven answers and the shape check into ONE numbered list of problems, worst first. Merge duplicates. For each: the quoted line, why a client skips or rejects because of it, which reviewers flagged it, and the fix in one sentence.

Then the **Ask checklist**: each numbered client ask, and whether the proposal or a screening answer answers it (yes / partly / no).

Then write **The rejection story**: three to five sentences, in the client's voice, of how this proposal loses. Example: "I had 38 proposals. Yours opened with your name and years of experience, same as 30 others, so I never clicked."

## 5. Rewrite it
Write the improved proposal in the **proof-first shape** from `winning-patterns.md`, following the rewrite rules in `references/rubric.md`. If `wins.md` exists, match the shape, tone and length of those hired proposals. Use the match keywords early, the most relevant items from the proof bank, and answer every client ask. Same facts as the original and the proof bank, nothing more. Where a fix needs a fact you do not have, leave `[ADD: ...]` and list those questions at the end. Write it in the language of the job post.

Also give:
- **Three alternative opening lines** (each under 200 characters), all in the proof-first style: the client's kind of app plus proof.
- **Screening answers, fixed**: if the job had screening questions, write one answer for EVERY question, whether or not the user wrote one. Each answer sits in its own code block directly under its question (`**Q1: <question>**`), as plain text ready to paste into that question's own input box. Follow the screening answer rules in `references/rubric.md`. Never merge the answers into the cover letter.
- **Visibility checklist**: the "Not opened? Check these" list from `winning-patterns.md`, filled in for this job with what you know (job age, proposal count, profile card fit, keywords, boost) and "unknown" where you do not. If the profile card looks like the problem, suggest `/upwork-profile-panel`.
- **What changed and why**: a short list mapping each numbered problem to the fix.

## 5b. Test the hook until it wins (full mode)
Run the loop in `references/hook-lab.md`, using The Scroller only. Each round: 4 or 5 hook candidates from the proof bank, one fresh Scroller per candidate (solo), plus one blind lineup Scroller that ranks your candidates against 6 competitor previews and picks the 5 it would open. Include the original proposal's hook in round 1 as the baseline. Show the score table after every round, read the reviewers' reasons, and write the next round to answer them.

Stop when a candidate scores 9 or 10 solo AND ranks in the top 2 of the lineup, after 3 rounds, or when two rounds in a row gain nothing. Put the winning hook at the top of the rewritten proposal and adjust the rest so it reads naturally. If the best honest hook plateaus, say so plainly, give its score and rank, and name the one piece of proof that would break the ceiling (for example a small demo of the client's core screen). Hypothetical candidates must be labelled HYPOTHETICAL and never go into the paste-ready proposal unless the user confirms the fact.

Then start one sub-agent: **The Hiring Client** on the full new version (with the fixed screening answers in place of the originals). Report the before and after verdict and score for The Scroller (the winning hook) and The Hiring Client. If the rewrite still loses, say so and say why. Tell the user plainly that these are model reviewers: the real test is the view rate in Upwork's Stats and trends.

## 6. Write the result
Create `.upwork-hiring-panel/<YYYY-MM-DD>-<job-slug>/` in the current directory with:
- `PANEL.md`: the inputs used (what was given, what was assumed), the client's asks, the match keywords, the seven verdicts in full, the scorecard, the shape check, the numbered problems, the ask checklist and the rejection story. In fast mode, only the inputs, asks, keywords and shape check.
- `PROPOSAL-IMPROVED.md`: the rewritten proposal ready to paste, the hook lab score table for every round, the three alternative openings, the fixed screening answers (one code block per question), the visibility checklist, what changed and why, the before and after re-check, and the `[ADD: ...]` questions.

Touch no other files, except `wins.md` when the user agrees (see Rules). Then show the user, in chat:
1. A table: one row per reviewer with verdict, score and the line that hurt most (full mode only).
2. The scorecard and interview chance (full mode only).
3. The five worst problems, the ask checklist and the rejection story.
4. The full rewritten proposal in a code block so it can be copied.
5. If there were screening questions: every fixed answer, each in its own code block under its question, labelled so the user can paste each into its own box. This is never left only in the file.
6. The hook lab table (every round) and which hook won, or where it plateaued and why.
7. The visibility checklist.
8. The before and after re-check, the `[ADD: ...]` questions, and where the files are.

## Rules
- Be honest. If the proposal is strong, say so, say which reviewer came closest to rejecting it and why it still held, and keep the rewrite to the changes that matter.
- Do not invent facts about the freelancer, their past clients or real companies. Say "assumed" when you guess.
- Proof over cleverness: never trade a clickable proof link or the job's keywords for a clever line.
- Never suggest moving the conversation, contact details or payment off Upwork before a contract; it breaks Upwork's terms. Flag it if the original does.
- **Learn from results.** When the user says a proposal got hired or got an interview, offer to save the job post and the proposal to `~/.claude/upwork-hiring-panel/wins.md` (create the folder if needed), under a dated heading with the outcome. Do it only when they agree. When they say proposals are not being viewed, ask for their Stats and trends numbers and walk the visibility checklist before changing the letter again.
- Reply in the language the user wrote to you in.
- This is a structured second opinion made by language models. It does not guarantee an interview or a hire.
