# Scoring, rejection patterns and rewrite rules

## The six scores

Score each from 1 to 10. Start from the scores the named reviewers gave, then adjust by at most 2 points with a reason. Quote the evidence for every score.

| Score | What it asks | Comes from |
|---|---|---|
| **Hook** | Do the profile card and the first two lines make a busy client click? | The Scroller (main), The Upwork Veteran |
| **Clarity** | Is it easy to follow, concrete and correct? | The Technical Lead (main), The Upwork Veteran |
| **Relevance** | Does it answer this job post, not any job post? | The Hiring Client (main), The Technical Lead, The Competing Freelancer |
| **Credibility** | Is there proof, or only claims? | The Skeptic (main), The Competing Freelancer |
| **Value Proposition** | Is it clear what the client gets, by when, and why it is worth the price? | The Budget-Conscious Client (main), The Competing Freelancer |
| **Interview Potential** | Would the client message this person now? | The Hiring Client (main), The Upwork Veteran |

What the numbers mean: 1–3 gets the proposal skipped or declined; 4–6 is average, it blends in with the pile; 7–8 is a real contender; 9–10 is the proposal the client messages first.

## Interview chance

Count the seven verdicts. Positive verdicts count as 1: OPEN, INTERVIEW, WORTH IT, THEY WIN, TRUST, KNOWS IT, SHORTLIST. (For The Competing Freelancer, THEY WIN is good for the proposal and I WIN is bad.) Middle verdicts count as 0.5: MAYBE, NOT SURE, TOSS-UP, UNSURE, VAGUE, ARCHIVE. Everything else counts as 0.

- **HIGH**: 5.5 or more, and The Scroller said OPEN, and The Hiring Client said INTERVIEW.
- **LOW**: under 3, or The Scroller said SKIP and The Hiring Client did not say INTERVIEW.
- **MEDIUM**: everything else.

A SKIP from The Scroller caps the chance at MEDIUM no matter what else happened: a proposal that never gets opened never gets read.

## Common rejection patterns

Check the proposal against these. Each one the panel found becomes a numbered problem.

**Hook**
- The first two lines never name the client's kind of app, in their words, or say the freelancer has built one like it.
- Opens with a self-introduction (name, title, years of experience) and no domain match.
- Opens with clever analysis of the client's project but no proof and none of the job's keywords. Models like these lines; skimming clients skip them.
- Restates the job title or says "I have read your job description".
- The job's main keywords (app type, stack) are missing from the first lines, which can also lower Upwork's match ranking.
- A short "Hi," on its own is not a problem.

**Relevance**
- Could be pasted into any job in the category without changes.
- Ignores a stated requirement, deliverable, tool or deadline from the post.
- Answers the keywords, not the actual goal behind the post.

**Credibility**
- Claims without proof: "expert", "high quality", "100% satisfaction".
- No specific past project, result or portfolio piece that matches this job.
- No clickable live app, store listing or demo video. Clients click; claims without links lose.
- Overpromising: unrealistic timelines or guarantees.
- Sounds machine-written: "I hope this message finds you well", "delve", "leverage", "seamless", "elevate", "I am thrilled".
- Spelling or grammar mistakes.

**Clarity**
- Wall of text; no paragraph breaks.
- Lists every skill the freelancer has.
- Approach is buzzwords instead of steps.
- Over about 300 words for a normal job.
- A long plan, milestone breakdown or technical essay before any proof, when the post did not ask for one.

**Value proposition**
- No clear deliverable, timeline or next step.
- Price with no reason it is worth it, or "it depends" with no range.
- Nothing about what happens after delivery (revisions, handover, support) when the job needs it.

**Interview potential and Upwork mechanics**
- An explicit ask from the post ("To apply, please send…") is not answered.
- No availability or start date when the post asks for it.
- No question and no call to action at the end (less important than the asks and the proof).
- Screening questions skipped or answered with "see cover letter".
- Links that need a login or download.
- Contact details, or asking to move to email, WhatsApp, Telegram or another platform before a contract. This breaks Upwork's terms and can get the account suspended; always flag it as problem #1.

## Rewrite rules

The rewrite follows the proof-first shape in `winning-patterns.md`, and the freelancer's own `wins.md` when it exists. It is for the client: it shows them, fast, that this person has built their kind of app and can prove it.

1. **Line one: the client's kind of app, in their words, plus "I've built it".** For example "Hi, I've built booking and fitness apps before, including …". Put the job's main keywords (app type, platform, stack) in the first two lines. No clever analysis, no years-of-experience opener.
2. **Line two: the single strongest credential with a number**, from the proof bank.
3. **A proof list of 3 to 7 clickable links**, most relevant to this job first, each with a short label naming what in it matches the job ("booking, payments, admin"). Store listings first, then demo videos, then screenshots. Only links the user gave. If the closest match has no link, use `[ADD: link]`.
4. **Answer every client ask**, in the order the post lists them, briefly: examples, experience, timeline, rate, availability, NDA, whatever was asked.
5. **Availability**: start date, and hours per day if relevant.
6. **At most one sharp insight or question about the project**, in one sentence, only after the proof. No milestone plan or technical essay unless the post asks for it; if it does, three bullets at most.
7. **Short.** Usually 60 to 180 words before the links; never over 250 unless the post asks for detail. Short paragraphs.
8. **Plain, human language.** No clichés, no buzzwords, no emoji unless the client's post uses them. Match the client's tone and language.
9. **Personal.** Use the client's name or company only if it appears in the job post; no "Dear Sir/Madam".
10. **Stay on Upwork.** No contact details, no links that need a login, no off-platform payment.
11. **Never invent.** No new clients, numbers, years, tools, reviews, links or results. Keep every true fact that helps; cut the ones that do not. Where a fix needs a fact you do not have, write `[ADD: what is needed]`.
12. **Do not remove proof to make room.** If the original had live links and the rewrite would drop them, keep the links and cut words instead.

## Screening answer rules

Every screening question has its own input box, and clients often read the answers before the cover letter. Each answer must stand on its own. Write them in the order the questions came, one per question, as plain text (no markdown headings or bold; a plain `-` list only when the question asks for a list).

1. **Answer the question in the first sentence**: the pick, the link, or "Yes". No warm-up, no restating the question.
2. **Never "see cover letter" or "see above"**, and never repeat sentences from the cover letter or another answer.
3. **Use the job's own terms**: its milestones, tools, deliverables and numbers, so the answer could not be pasted into another job.
4. **Short**: 2 to 5 sentences, usually under 100 words, unless the question asks for more.
5. **Links**: when the question asks for links, give only links the user supplied, as full URLs after a short label.
6. **Honesty over polish**: if the question asks for proof the user does not have (for example a live app with a specific feature), never invent it or imply it. Say plainly what they did ship, then name one concrete step that covers the gap. Add `[ADD: ...]` where a true detail the user can supply would make the answer stronger.
7. **Confirmation questions** ("confirm you have reviewed…", "agree to…"): start with "Yes", show it was read by naming one or two specifics from the document, then state the commitment. If the document was provided, never hedge with "once I have reviewed". If the user has not read it, tell them to read it first instead of writing a false "Yes".
8. **Recommendation questions** ("which tool or framework and why"): name the pick in the first sentence, give two or three reasons tied to this job's requirements, then the one real trade-off and how it would be handled.
9. **Same language as the question.**
