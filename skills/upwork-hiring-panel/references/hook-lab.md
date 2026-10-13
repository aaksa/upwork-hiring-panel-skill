# Hook lab: test the preview until clients open it

The first two lines decide whether the proposal is ever opened, and a single model score is easy to fool (one panel gave 8/10 to a clever opener that real clients skipped). So the hook is tested two ways, with The Scroller only, and iterated until it wins.

## The loop

1. **Write 4 or 5 hook candidates** (each the first two lines, about 200 characters), all from the proof bank. Vary one idea per candidate: which proof leads, whether the client's own feature or tab names are used, where the stack goes, whether "live apps below" is promised. Keep the best candidate from the last round in the next round.
2. **Solo test**: one fresh Scroller sub-agent per candidate, in parallel, with the brief from `personas.md` (job title plus the first lines of the job post, the profile card, and only that candidate's preview).
3. **Blind lineup**: one more Scroller sub-agent sees all candidates mixed with 6 competitor previews, unlabelled and shuffled, and picks the 5 it would open, ranked, with a 3-word reason for each skip. Use the lineup brief below.
4. **Keep score** in a table: candidate, solo verdict and score, lineup rank (or "skipped" and why).
5. **Read the reasons, not just the numbers.** Every reviewer usually asks for the same missing thing. Write the next round to answer it, using true facts only.
6. **Stop** when a candidate scores **9 or 10 solo AND ranks in the top 2 of the lineup** (where only a competitor who has already built the exact app may rank above it). Also stop after **3 rounds**, or when two rounds in a row gain nothing. The ceiling is information too: report it honestly.

Run at most 3 rounds by default (about 18 short sub-agent calls). Show the user the score table after every round.

## Competitor previews for the lineup

Write 6 previews for this job, one of each type, so the lineup looks like a real proposal list:

1. **The specialist**: has already built this exact kind of app on this stack, with a demo or store link. (Usually ranks #1. If it does, no wording beats it; only proof does.)
2. **The near-match**: built several similar apps on the other allowed stack, with links.
3. **The template**: "Hello Dear, I am a senior … with 8+ years … I have carefully read your job description …"
4. **The skill list**: a list of technologies and "can start immediately".
5. **The consultant**: an analysis of the client's project with no proof.
6. **The enthusiast**: emoji, "I'd love to help bring your … to life", no apps.

Keep the same 6 competitors across rounds so ranks are comparable.

## Lineup brief (copy word for word, then append the job and the lettered previews)

> You posted a job on Upwork three hours ago and already have 40+ proposals. You are on your phone between meetings. In the proposal list Upwork shows you each freelancer's photo, name, title, rate, Job Success Score and the first two lines of their cover letter. That is all you see. You give each one three seconds and click on maybe five. You are not a writing critic and clever lines do not impress you. You click when the card and line one tell you this person has already built an app like yours (your kind of app, your words, your stack) and there is something you can check. You skip when the title on the card does not match your job, when line one is about the freelancer in general (years of experience, a list of skills) without naming your kind of app, or when line one is an analysis of your project with no sign they have built one. A short "Hi," does not bother you.
>
> Below are proposal previews from different freelancers (profile cards not shown). Pick exactly the 5 you would open, ranked 1 to 5, and say in one short line why for each. Then list the others and a 3-word reason each was skipped.
>
> Shared rules: Stay in character. Be blunt and specific. Judge like a real Upwork client, not like a writing critic: real clients skim, and they reward a clear match to their kind of app and proof they can click (live apps, demos) far more than clever analysis, long plans or polished prose. Do not reward length. Do not use any tools; just answer.

Answer format:
```
OPEN (ranked):
1. <letter>: reason
...
5. <letter>: reason
SKIPPED:
<letter>: reason
```

## Honesty rules

- Every candidate uses only facts from the proof bank. Never imply a matching app, feature or link the freelancer does not have.
- A **hypothetical** candidate (for example "I built a quick demo of your main screen: [demo link]") may be tested to show the user what a piece of proof would be worth. Label it HYPOTHETICAL in every table, and never put it in the paste-ready proposal unless the user confirms they built it.
- If the best honest hook plateaus below the target, say so, give its score and rank, and name the one piece of proof that would break the ceiling.

## What the lab has found so far

From a real run on a race-discovery and season-planning app job (Flutter + Supabase), where the freelancer had sports, booking and tracking apps but no race or map app:

| Hook idea | Solo | Lineup |
|---|---|---|
| "Flutter + Supabase developer, built sports, fitness and booking apps, including a gym booking platform…" | OPEN 6 | skipped: "gym booking, generic" |
| Funding credential first, then the sports apps | OPEN 7 | #4 |
| "…Race discovery + season planning fits." | OPEN 7 | skipped: "claims fit, nothing checkable" |
| "Season Plan = scheduling, Athlete Locker = performance tracking…" | OPEN 7 | skipped |
| "I build sports apps in Flutter + Supabase: scheduling (…) and performance tracking (…), the same core as your Season Plan and Athlete Locker. Live apps below." | **OPEN 8** | **#4** (best honest) |
| HYPOTHETICAL: "I built a quick Flutter + Supabase demo of your Discover tab (race search, filters, clustered map): [demo link]…" | **OPEN 9** | **#2**, behind only the specialist |

Lessons:
1. **Say what you build, on their stack, in the first words**: "I build sports apps in Flutter + Supabase" beat "I'm a Flutter + Supabase developer and I've built …".
2. **Use the client's own feature or tab names** to connect your proof to their app.
3. **Promise something checkable**: hooks ending "live apps below" ranked; the same hook without it was skipped.
4. **Do not spend the preview on an unrelated credential** (funding, users) or on a claim that you "fit".
5. **Formula-style mappings ("A = B") read as a stretch.**
6. **When you lack the exact app, a small demo of the client's core screen is the strongest lever**, worth more than any wording. If the job is worth it, build the demo; otherwise pick jobs where your proof already matches.
7. **The specialist always wins the lineup.** No hook beats a competitor who has built the exact app; choose jobs accordingly.
