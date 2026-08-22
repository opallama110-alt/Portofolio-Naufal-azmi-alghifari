from html.parser import HTMLParser
from pathlib import Path
import re
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

    def test_certificate_assets_are_published_and_linked(self):
        certificate_dir = ROOT / "assets" / "certificates"
        bootcamp_certificate = certificate_dir / "ai-bootcamp-certificate.png"
        hacktiv8_pdf = certificate_dir / "hacktiv8-ai-integration-certificate.pdf"
        hacktiv8_preview = certificate_dir / "hacktiv8-ai-integration-certificate.webp"

        self.assertGreater(bootcamp_certificate.stat().st_size, 100_000)
        self.assertGreater(hacktiv8_pdf.stat().st_size, 100_000)
        self.assertGreater(hacktiv8_preview.stat().st_size, 50_000)
        self.assertIn('href="assets/certificates/ai-bootcamp-certificate.png"', HTML)
        self.assertIn('src="assets/certificates/ai-bootcamp-certificate.png"', HTML)
        self.assertIn('href="assets/certificates/hacktiv8-ai-integration-certificate.pdf"', HTML)
        self.assertIn('src="assets/certificates/hacktiv8-ai-integration-certificate.webp"', HTML)
        self.assertIn("AI Bootcamp — ImpactPreneur Business Challenge 2026", HTML)
        self.assertIn("AI Productivity and AI API Integration for Developers", HTML)

    def test_social_buttons_have_accessible_inline_brand_icons(self):
        expected_links = {
            "instagram": "https://www.instagram.com/naz_all_/",
            "linkedin": "https://linkedin.com/in/naufal-azmi-55869838b",
            "github": "https://github.com/opallama110-alt",
        }
        social_links = {
            link.get("data-social"): link
            for link in self.page.links
            if link.get("data-social")
        }

        for name, href in expected_links.items():
            with self.subTest(name=name):
                self.assertIn(name, social_links)
                self.assertEqual(social_links[name].get("href"), href)
                self.assertTrue(social_links[name].get("aria-label"))
                self.assertNotIn(f'data-lucide="{name}"', HTML)
                self.assertRegex(HTML, rf'(?s)data-social="{name}"[^>]*>\s*<svg\b')

    def test_whatsapp_link_uses_international_number_format(self):
        self.assertIn('href="https://wa.me/62813166000376"', HTML)
        self.assertNotRegex(HTML, re.compile(r'https://wa\.me/0'))


if __name__ == "__main__":
    unittest.main()
