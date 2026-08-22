from html.parser import HTMLParser
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.links = []
        self.buttons = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if "id" in attributes:
            self.ids.append(attributes["id"])
        if tag == "a":
            self.links.append(attributes)
        if tag == "button":
            self.buttons.append(attributes)


class PortfolioContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.page = PageParser()
        cls.page.feed(HTML)

    def test_ids_are_unique_and_internal_links_have_targets(self):
        self.assertEqual(len(self.page.ids), len(set(self.page.ids)))
        ids = set(self.page.ids)
        for link in self.page.links:
            href = link.get("href", "")
            if href.startswith("#") and len(href) > 1:
                self.assertIn(href[1:], ids, f"Missing target for {href}")

    def test_new_tab_links_are_protected(self):
        for link in self.page.links:
            if link.get("target") == "_blank":
                rel = set(link.get("rel", "").split())
                self.assertTrue({"noopener", "noreferrer"}.issubset(rel))

    def test_cv_action_is_honest_and_actionable(self):
        self.assertNotIn("Download CV", HTML)
        self.assertRegex(HTML, r'href="mailto:[^"]+subject=CV%20Request"[^>]*>\s*Request CV')

    def test_mobile_menu_exposes_and_updates_expanded_state(self):
        button = next(item for item in self.page.buttons if item.get("id") == "mobile-menu-btn")
        self.assertEqual(button.get("aria-controls"), "mobile-menu")
        self.assertEqual(button.get("aria-expanded"), "false")
        self.assertIn("setAttribute('aria-expanded', String(isOpen))", HTML)
        self.assertIn("setMobileMenuOpen(false)", HTML)


if __name__ == "__main__":
    unittest.main()
