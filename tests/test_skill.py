import json
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SKILL_DIR = os.path.join(ROOT, "skills", "upwork-hiring-panel")

REVIEWERS = ("The Scroller", "The Hiring Client", "The Budget-Conscious Client", "The Competing Freelancer",
             "The Skeptic", "The Technical Lead", "The Upwork Veteran")
SCORES = ("Hook", "Clarity", "Relevance", "Credibility", "Value Proposition", "Interview Potential")


def read(*parts):
    with open(os.path.join(SKILL_DIR, *parts)) as f:
        return f.read()


class SkillTest(unittest.TestCase):
    def setUp(self):
        self.skill = read("SKILL.md")
        self.personas = read("references", "personas.md")
        self.rubric = read("references", "rubric.md")
        self.patterns = read("references", "winning-patterns.md")
        self.lab = read("references", "hook-lab.md")

    def test_frontmatter(self):
        self.assertTrue(self.skill.startswith("---\nname: upwork-hiring-panel\n"))
        front = self.skill.split("---")[1]
        for key in ("description:", "argument-hint:", "license: MIT"):
            self.assertIn(key, front)

    def test_seven_reviewers_everywhere(self):
        for who in REVIEWERS:
            self.assertIn(who, self.skill)
            self.assertIn("## %d. %s" % (REVIEWERS.index(who) + 1, who), self.personas)
        self.assertIn("Start seven sub-agents at once", self.skill)

    def test_scroller_sees_only_preview(self):
        scroller = self.personas.split("## 1. The Scroller")[1].split("## 2.")[0]
        self.assertIn("Never the full proposal", scroller)

    def test_every_brief_has_verdict_and_score(self):
        briefs = self.personas.split("\n## ")[1:]
        self.assertEqual(len(briefs), 7)
        for brief in briefs:
            self.assertIn("VERDICT:", brief)
            self.assertIn("SCORE: n/10", brief)

    def test_six_scores(self):
        for score in SCORES:
            self.assertIn(score, self.skill)
            self.assertIn("**%s**" % score, self.rubric)

    def test_rejection_and_rewrite(self):
        self.assertIn("## 4. Why it gets skipped or rejected", self.skill)
        self.assertIn("## 5. Rewrite it", self.skill)
        self.assertIn("before and after verdict", self.skill)
        self.assertIn("## Rewrite rules", self.rubric)

    def test_never_invents(self):
        self.assertIn("Never invent clients, results, numbers", self.skill)
        self.assertIn("[ADD: ...]", self.skill)

    def test_screening_answers_each_get_a_box(self):
        self.assertIn("own input box", self.skill)
        self.assertIn("one answer for EVERY question", self.skill)
        self.assertIn("each in its own code block", self.skill)
        self.assertIn("## Screening answer rules", self.rubric)
        self.assertIn("Never \"see cover letter\"", self.rubric)

    def test_grounded_in_winning_patterns(self):
        self.assertIn("references/winning-patterns.md", self.skill)
        self.assertIn("This overrides any reviewer's taste", self.skill)
        self.assertIn("## The proof-first shape", self.patterns)
        self.assertIn("## Not opened? Check these", self.patterns)
        self.assertIn("proof-first shape", self.rubric)
        self.assertIn("Judge like a real Upwork client", self.personas)

    def test_learns_from_wins(self):
        self.assertIn("~/.claude/upwork-hiring-panel/wins.md", self.skill)
        self.assertIn("**Learn from results.**", self.skill)

    def test_fast_mode_and_checklists(self):
        self.assertIn("**Fast mode**", self.skill)
        self.assertIn("**The client's asks**", self.skill)
        self.assertIn("**Match keywords**", self.skill)
        self.assertIn("**Visibility checklist**", self.skill)
        self.assertIn("Ask checklist", self.skill)

    def test_hook_lab_loop(self):
        self.assertIn("## 5b. Test the hook until it wins", self.skill)
        self.assertIn("references/hook-lab.md", self.skill)
        self.assertIn("## The loop", self.lab)
        self.assertIn("**Blind lineup**", self.lab)
        self.assertIn("## Competitor previews for the lineup", self.lab)
        self.assertIn("HYPOTHETICAL", self.lab)
        self.assertIn("9 or 10 solo AND ranks in the top 2", self.lab)

    def test_stays_on_upwork(self):
        self.assertIn("off Upwork", self.skill)
        self.assertIn("Stay on Upwork", self.rubric)

    def test_manifests_are_valid_json(self):
        for name in ("plugin.json", "marketplace.json"):
            with open(os.path.join(ROOT, ".claude-plugin", name)) as f:
                self.assertEqual(json.load(f)["name"], "upwork-hiring-panel-skill")


if __name__ == "__main__":
    unittest.main()
