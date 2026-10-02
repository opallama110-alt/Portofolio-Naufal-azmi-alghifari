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
        self.images = []
        self.metas = []
        self.stylesheets = []
        self.scripts = []
        self.icon_refs = []
        self.headings = []
        self._heading = None

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if "id" in attributes:
            self.ids.append(attributes["id"])
        if tag == "a":
            self.links.append(attributes)
        if tag == "button":
            self.buttons.append(attributes)
        if tag == "img":
            self.images.append(attributes)
        if tag == "meta":
            self.metas.append(attributes)
        if tag == "link" and attributes.get("rel") == "stylesheet":
            self.stylesheets.append(attributes.get("href", ""))
        if tag == "script" and "src" in attributes:
            self.scripts.append(attributes["src"])
        if tag == "use":
            self.icon_refs.append(attributes.get("href", ""))
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self._heading = [tag, ""]

    def handle_data(self, data):
        if self._heading is not None:
            self._heading[1] += data

    def handle_endtag(self, tag):
        if self._heading is not None and tag == self._heading[0]:
            self.headings.append((tag, " ".join(self._heading[1].split())))
            self._heading = None


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
        bootcamp_preview = certificate_dir / "ai-bootcamp-certificate.webp"
        hacktiv8_pdf = certificate_dir / "hacktiv8-ai-integration-certificate.pdf"
        hacktiv8_preview = certificate_dir / "hacktiv8-ai-integration-certificate.webp"

        self.assertGreater(bootcamp_certificate.stat().st_size, 100_000)
        self.assertGreater(hacktiv8_pdf.stat().st_size, 100_000)
        self.assertGreater(hacktiv8_preview.stat().st_size, 50_000)
        # The full-size PNG stays available, but the page only loads a lightweight preview.
        self.assertGreater(bootcamp_preview.stat().st_size, 50_000)
        self.assertLess(bootcamp_preview.stat().st_size, 400_000)
        self.assertIn('href="assets/certificates/ai-bootcamp-certificate.png"', HTML)
        self.assertIn('src="assets/certificates/ai-bootcamp-certificate.webp"', HTML)
        self.assertNotIn('src="assets/certificates/ai-bootcamp-certificate.png"', HTML)
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

    def test_page_uses_compiled_stylesheet_instead_of_runtime_cdns(self):
        self.assertIn("assets/css/styles.css", self.page.stylesheets)
        stylesheet = ROOT / "assets" / "css" / "styles.css"
        self.assertGreater(stylesheet.stat().st_size, 10_000)
        for runtime_cdn in ("cdn.tailwindcss.com", "unpkg.com", "lucide@latest"):
            with self.subTest(runtime_cdn=runtime_cdn):
                self.assertNotIn(runtime_cdn, HTML)
        self.assertEqual(self.page.scripts, [], "Page scripts should be inline, not loaded from third parties")

    def test_document_has_one_h1_and_ordered_section_headings(self):
        h1s = [text for tag, text in self.page.headings if tag == "h1"]
        self.assertEqual(h1s, ["Naufal Azmi Alghifari"])
        levels = [int(tag[1]) for tag, _ in self.page.headings]
        for previous, current in zip(levels, levels[1:]):
            self.assertLessEqual(current - previous, 1, "Heading levels must not skip a level")

    def test_document_has_seo_metadata(self):
        self.assertRegex(HTML, r'<html[^>]*\blang="en"')
        meta = {item.get("name") or item.get("property"): item.get("content", "") for item in self.page.metas}
        self.assertGreater(len(meta.get("description", "")), 80)
        self.assertTrue(meta.get("og:title"))
        self.assertTrue(meta.get("og:description"))
        self.assertTrue((ROOT / "assets" / "favicon.svg").is_file())

    def test_images_have_alt_text_and_reserved_dimensions(self):
        self.assertTrue(self.page.images)
        for image in self.page.images:
            with self.subTest(src=image.get("src", "")[:60]):
                self.assertTrue(image.get("alt", "").strip())
                self.assertTrue(image.get("width"))
                self.assertTrue(image.get("height"))

    def test_icon_references_resolve_to_sprite_symbols(self):
        ids = set(self.page.ids)
        self.assertTrue(self.page.icon_refs)
        for ref in self.page.icon_refs:
            with self.subTest(ref=ref):
                self.assertTrue(ref.startswith("#"))
                self.assertIn(ref[1:], ids)

    def test_primary_navigation_covers_every_section(self):
        nav_targets = {link.get("href") for link in self.page.links if "data-nav-link" in link}
        for section in ("about", "skills", "projects", "certificates", "contact"):
            with self.subTest(section=section):
                self.assertIn(f"#{section}", nav_targets)

    def test_skip_link_targets_main_content(self):
        self.assertIn("main", self.page.ids)
        self.assertTrue(any(link.get("href") == "#main" for link in self.page.links))


if __name__ == "__main__":
    unittest.main()
