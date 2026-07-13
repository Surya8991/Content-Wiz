"""Generic loader for the flat prompt files in prompts/.

`templates.py` holds 25 richly-parameterized prompt builders. The remaining
prompt files were previously reachable only by hand. This module wires them into
the CLI: it loads a prompts/*.txt file, substitutes the standard tokens, and
prepends a short generation context. Brand tokens ([BRAND NAME], [BRAND
DESCRIPTION], ...) are left intact on purpose so the LLM performs brand
auto-detection per prompts/_Brand_Detection_Rules.txt.

To add a content type: drop a prompt file in prompts/ and add one row here.
"""
import os

PROMPTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "prompts")

# alias -> (prompt filename, output subfolder). First alias per file is canonical.
TEXT_PROMPT_MAP = {
    "backlink":            ("Backlink_Outreach_Email_Prompt.txt", "Backlink_Outreach"),
    "backlink_outreach":   ("Backlink_Outreach_Email_Prompt.txt", "Backlink_Outreach"),
    "buyer_persona":       ("Buyer_Persona_Prompt.txt",           "Buyer_Personas"),
    "persona":             ("Buyer_Persona_Prompt.txt",           "Buyer_Personas"),
    "competitor_gap":      ("Competitor_Content_Gap_Prompt.txt",  "Competitor_Gap_Analysis"),
    "competitor":          ("Competitor_Content_Gap_Prompt.txt",  "Competitor_Gap_Analysis"),
    "course":              ("Course_Training_Description_Prompt.txt", "Course_Descriptions"),
    "course_description":  ("Course_Training_Description_Prompt.txt", "Course_Descriptions"),
    "email_drip":          ("Email_Drip_Sequence_Prompt.txt",     "Email_Drip"),
    "drip":                ("Email_Drip_Sequence_Prompt.txt",     "Email_Drip"),
    "google_ads":          ("Google_Ads_Prompt.txt",              "Google_Ads"),
    "alt_text":            ("Image_Alt_Text_Prompt.txt",          "Image_Alt_Text"),
    "image_alt":           ("Image_Alt_Text_Prompt.txt",          "Image_Alt_Text"),
    "interactive":         ("Interactive_Content_Prompt.txt",     "Interactive_Content"),
    "quiz":                ("Interactive_Content_Prompt.txt",     "Interactive_Content"),
    "internal_linking":    ("Internal_Linking_Prompt.txt",        "Internal_Linking"),
    "linking":             ("Internal_Linking_Prompt.txt",        "Internal_Linking"),
    "linkedin_ads":        ("LinkedIn_Ads_Prompt.txt",            "LinkedIn_Ads"),
    "linkedin_article":    ("LinkedIn_Article_Prompt.txt",        "LinkedIn_Article"),
    "meta_ads":            ("Meta_Facebook_Ads_Prompt.txt",       "Meta_Facebook_Ads"),
    "facebook_ads":        ("Meta_Facebook_Ads_Prompt.txt",       "Meta_Facebook_Ads"),
    "research_report":     ("Original_Research_Report_Prompt.txt", "Research_Reports"),
    "research":            ("Original_Research_Report_Prompt.txt", "Research_Reports"),
    "reddit":              ("Reddit_Post_Prompt.txt",             "Reddit"),
    "schema":              ("Schema_Markup_Prompt.txt",           "Schema_Markup"),
    "schema_markup":       ("Schema_Markup_Prompt.txt",           "Schema_Markup"),
    "skills_gap":          ("Skills_Gap_Analysis_Prompt.txt",     "Skills_Gap_Analysis"),
    "slideshare":          ("SlideShare_Presentation_Prompt.txt", "SlideShare"),
    "presentation":        ("SlideShare_Presentation_Prompt.txt", "SlideShare"),
    "testimonial":         ("Testimonial_Review_Request_Prompt.txt", "Testimonial_Request"),
    "review_request":      ("Testimonial_Review_Request_Prompt.txt", "Testimonial_Request"),
    "thought_leadership":  ("Thought_Leadership_OpEd_Prompt.txt", "Thought_Leadership"),
    "oped":                ("Thought_Leadership_OpEd_Prompt.txt", "Thought_Leadership"),
    "topic_cluster":       ("Topic_Cluster_Prompt.txt",           "Topic_Cluster"),
    "cluster":             ("Topic_Cluster_Prompt.txt",           "Topic_Cluster"),
    "trainer_bio":         ("Trainer_Speaker_Bio_Prompt.txt",     "Trainer_Bios"),
    "bio":                 ("Trainer_Speaker_Bio_Prompt.txt",     "Trainer_Bios"),
    "webinar":             ("Webinar_Promo_Prompt.txt",           "Webinar_Promo"),
    "webinar_promo":       ("Webinar_Promo_Prompt.txt",           "Webinar_Promo"),
    "whitepaper":          ("Whitepaper_eBook_Prompt.txt",        "Whitepaper_eBook"),
    "ebook":               ("Whitepaper_eBook_Prompt.txt",        "Whitepaper_eBook"),
}


def is_text_prompt(alias):
    return alias.lower().strip() in TEXT_PROMPT_MAP


def subfolder_for(alias):
    entry = TEXT_PROMPT_MAP.get(alias.lower().strip())
    return entry[1] if entry else "Misc"


def render(alias, topic, audience, wordcount=None, cta=None, url=None):
    """Load the prompt file for `alias` and fill the standard tokens."""
    entry = TEXT_PROMPT_MAP.get(alias.lower().strip())
    if entry is None:
        raise ValueError(f"No text prompt registered for alias '{alias}'.")
    filename = entry[0]
    path = os.path.join(PROMPTS_DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()

    subs = {
        "[TOPIC]":                    topic,
        "[TARGET AUDIENCE]":          audience,
        "[AUDIENCE]":                 audience,
        "[INSERT CTA LINK]":          cta or "[INSERT CTA LINK]",
        "[INSERT URL IF APPLICABLE]": url or "[INSERT URL IF APPLICABLE]",
        "[INSERT URL]":               url or "[INSERT URL]",
    }
    if wordcount:
        subs["[WORDCOUNT]"] = str(wordcount)
        subs["[WORD COUNT]"] = str(wordcount)

    for token, value in subs.items():
        raw = raw.replace(token, value)

    header = (
        "GENERATION CONTEXT (filled by the generator)\n"
        f"- Topic: {topic}\n"
        f"- Target audience: {audience}\n"
    )
    if url:
        header += f"- Brand URL: {url}\n"
    header += (
        "- Brand tokens like [BRAND NAME] are intentionally left for you to resolve "
        "via _Brand_Detection_Rules.txt.\n"
        + "=" * 60 + "\n\n"
    )
    return header + raw
