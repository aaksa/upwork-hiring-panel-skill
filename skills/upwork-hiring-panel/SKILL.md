---
name: upwork-hiring-panel
description: >-
  Run an Upwork proposal past a hiring panel of seven Claudes that each judge it alone as a different reader (a busy client who only sees the preview, the hiring client, a budget-conscious client, a competing freelancer, a burned-before skeptic, a technical lead and an Upwork veteran), score its hook, clarity, relevance, credibility, value proposition and interview potential, explain why it gets rejected, then rewrite it into a stronger, client-focused proposal. Use when the user types /upwork-hiring-panel followed by a proposal (file path or pasted text), or asks to review, score, critique or rewrite an Upwork proposal or cover letter.
argument-hint: "<proposal file or pasted text> [job post] [bid/rate] [screening answers]"
license: MIT
metadata:
  version: "1.0.0"
---

# /upwork-hiring-panel

The user gives you an Upwork proposal after `/upwork-hiring-panel`. Seven reviewers judge it alone, you merge what they found, explain why it gets rejected, and rewrite it so a client wants to interview the freelancer. Never flatter the proposal.

Before starting, read both reference files in this skill folder:
- `references/personas.md`: the exact brief for each of the seven reviewers.
- `references/rubric.md`: the six scores, the rejection patterns and the rewrite rules.

## 1. Get the proposal and the job post
Everything after `/upwork-hiring-panel` is input: a file path (read it; PDF, .md and .txt are fine) or pasted text. Sort it into:
- **Proposal**: the cover letter the client will read. Required.
- **Job post**: title and description of the job. Strongly needed. If it is missing, ask ONE question: "Paste the job post (title and description) you are bidding on." Then continue. If the user says they do not have it, continue with "job post: not given" and tell every reviewer.
- **Bid**: fixed price or hourly rate, and timeline, if given. Otherwise write "bid: not given".
- **Screening questions and answers**, if the job had them.
- **Freelancer profile**: title, rate, Job Success Score, relevant portfolio items, if given.

Use only what the user gave you. Never invent clients, results, numbers, years of experience, tools, reviews or portfolio items. When you assume something, label it "assumed".

Also cut the **preview**: the first two lines of the proposal, at most about 200 characters, ending where the line breaks or the sentence ends. This is roughly what a client sees in the Upwork proposal list before clicking. Only the first reviewer gets this, not the full proposal.

## 2. Seven reviewers, alone
Start seven sub-agents at once (one message, seven Agent calls, `general-purpose`). Nobody sees anybody else's notes. Give each one exactly what `references/personas.md` says that reviewer receives, plus its brief copied word for word. Each answers in under 150 words in the fixed format from its brief: a verdict, a score from 1 to 10, the one line that hurt most (quoted), and two more problems.

1. **The Scroller**: busy client, sees only the preview. Judges the hook. OPEN or SKIP.
2. **The Hiring Client**: owns the job and reads everything. Judges relevance and interview potential. INTERVIEW, MAYBE or NO.
3. **The Budget-Conscious Client**: has cheaper bids open. Judges the value proposition. WORTH IT, NOT SURE or TOO EXPENSIVE.
4. **The Competing Freelancer**: bid on the same job. Judges how the proposal stands out. THEY WIN, TOSS-UP or I WIN.
5. **The Skeptic**: has been burned by freelancers before. Judges credibility. TRUST, UNSURE or DISTRUST.
6. **The Technical Lead**: knows the work. Judges clarity and understanding of the problem. KNOWS IT, VAGUE or WRONG.
7. **The Upwork Veteran**: has hired 100+ freelancers on Upwork. Judges template tells, length, screening answers and platform mistakes. SHORTLIST, ARCHIVE or DECLINE.

If the Agent tool is not available, play the seven reviewers yourself one at a time, and write each verdict down before reading the next brief. Tell the user the panel was run without independent sub-agents.

## 3. Score it
Using `references/rubric.md`, give the six scores (1 to 10): **Hook, Clarity, Relevance, Credibility, Value Proposition, Interview Potential**. Each score comes from the reviewers the rubric names for it; quote the evidence. Then give the **interview chance**: LOW, MEDIUM or HIGH, by the rule in the rubric.

## 4. Why it gets rejected
Merge all seven answers into ONE numbered list of problems, worst first. Merge duplicates. For each: the quoted line, why a client rejects or skips because of it, which reviewers flagged it, and the fix in one sentence.

Then write **The rejection story**: three to five sentences, in the client's voice, of how this proposal loses. Example: "I had 38 proposals. Yours opened with your name and years of experience, same as 30 others, so I never clicked."

## 5. Rewrite it
Write the improved proposal following the rewrite rules in `references/rubric.md`: client-focused, opens on the client's problem, proof early, short, ends with a question or a clear next step. Same facts as the original and what the user told you, nothing more. Where a fix needs a fact you do not have, leave `[ADD: ...]` and list those questions at the end. Write it in the language of the job post.

Also give:
- **Three alternative opening lines** (each under 200 characters) the user can swap in.
- **Screening answers rewritten**, if any were given.
- **What changed and why**: a short list mapping each numbered problem to the fix.

Then start two sub-agents on the new version (same briefs, same inputs, no notes from the first round): **The Scroller** (on the new preview) and **The Hiring Client**. Report the before and after verdict and score for both. If the rewrite still loses, say so and say why.

## 6. Write the result
Create `.upwork-hiring-panel/<YYYY-MM-DD>-<job-slug>/` in the current directory with:
- `PANEL.md`: the inputs used (what was given, what was assumed), the seven verdicts in full, the scorecard, the numbered problems and the rejection story.
- `PROPOSAL-IMPROVED.md`: the rewritten proposal ready to paste, the three alternative openings, rewritten screening answers, what changed and why, the before and after re-check, and the `[ADD: ...]` questions.

Touch no other files. Then show the user, in chat:
1. A table: one row per reviewer with verdict, score and the line that hurt most.
2. The scorecard and interview chance.
3. The five worst problems and the rejection story.
4. The full rewritten proposal in a code block so it can be copied.
5. The before and after re-check, the `[ADD: ...]` questions, and where the files are.

## Rules
- Be honest. If the proposal is strong, say so, say which reviewer came closest to rejecting it and why it still held, and keep the rewrite to the changes that matter.
- Do not invent facts about the freelancer, their past clients or real companies. Say "assumed" when you guess.
- Never suggest moving the conversation, contact details or payment off Upwork before a contract; it breaks Upwork's terms. Flag it if the original does.
- Reply in the language the user wrote to you in.
- This is a structured second opinion made by language models. It does not guarantee an interview or a hire.
