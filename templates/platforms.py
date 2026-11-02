"""Platform-specific copy briefs for additional global and regional channels.

Lengths below are editorial targets unless a verified platform limit is stated.
See strategies/strategy-additional-platforms.md for sources and review date.
"""
from ._shared import BANNED_CTA_PHRASES, HUMAN_WRITING_RULES, market_voice


def _brief(platform, deliverables, rules, topic, audience, market):
    banned = ", ".join(BANNED_CTA_PHRASES)
    return f"""Write a {platform} content draft about: {topic}
Target audience: {audience}

DELIVERABLES:
{deliverables}

PLATFORM DIRECTION:
- {rules}
- These channel-specific length budgets take precedence over a generic CLI wordcount.
- Use [INSERT CTA LINK] for a useful destination when a link is appropriate. If the
  publishing surface cannot accept links, keep it in an editor-only destination note.
- Treat current eligibility, field limits, and account features as items to confirm
  in the live publishing UI. Do not invent algorithm rules or guarantee reach.

EVIDENCE AND AUTHORSHIP:
- Do not add statistics merely to sound authoritative. External claims require a
  specific source, report/article title, and year; otherwise use a qualitative claim.
- Proprietary statistics must trace to supplied data/HARO_DataBank.csv evidence.
  If the data is not supplied, do not imply access to it or invent internal results.
- Use only real supplied personal experiences. Attribute first-person brand copy
  to a named real author or disclose it as posted on behalf of [Brand].
- Preserve truthful sponsorship disclosures and leave missing facts as clear
  editor placeholders. A related piece has no usable URL until it is published.
- Stat-bearing and first-person drafts require human review before publication.
- Never use these CTA phrases: {banned}.

{HUMAN_WRITING_RULES}

{market_voice(market)}

OUTPUT CHECK:
Return only the requested deliverables, labeled separately from editor-only notes.
Check the channel budget, links, attribution, and missing-fact placeholders. Do not
claim that a generated draft passed factual verification or was already published.
"""


def bluesky_post(topic, audience, market=None, **_):
    return _brief(
        'Bluesky',
        'One standalone text post plus one optional follow-up reply.',
        'Use an editorial target of 280 characters for the main post, including the supplied link. Check the live composer before publishing; this target is not a claim about the platform maximum.\n- Lead with one useful observation, then one concrete implication; avoid a numbered X-style thread.\n- Use at most two relevant hashtags and no invented handles. Put overflow context into the optional reply.',
        topic, audience, market,
    )


def mastodon_post(topic, audience, market=None, **_):
    return _brief(
        'Mastodon',
        'One standalone post, an optional content-warning line, and image alt-text only if an image is supplied.',
        'Keep the main post within 500 characters as a conservative default and check the account server limit.\n- Respect the server community and avoid unsolicited mentions or cross-posted sales copy.\n- Use a content warning only when the actual subject warrants it; keep essential context accessible. Use descriptive hashtags sparingly.',
        topic, audience, market,
    )


def telegram_channel_post(topic, audience, market=None, **_):
    return _brief(
        'Telegram Channels',
        'One channel update: short headline, useful body, and one action.',
        'Target 80-160 words as an editorial budget. Write to existing subscribers, not cold direct-message recipients.\n- Put the key update in the first two lines, with up to three actionable bullets.\n- Do not promise replies, comments, bots, or polls unless the channel has those features configured. Never invent a channel invite link.',
        topic, audience, market,
    )


def whatsapp_channel_update(topic, audience, market=None, **_):
    return _brief(
        'WhatsApp Channels',
        'One concise channel update and an optional suggested reaction prompt.',
        'Target 40-90 words as an editorial budget, with one clear benefit and one action.\n- This is channel broadcast copy, not a private sales DM, group message, or Business API template.\n- Do not imply a personal relationship with every follower or promise that followers can reply. Use only supplied links and avoid unnecessary personal data.',
        topic, audience, market,
    )


def youtube_community_post(topic, audience, market=None, **_):
    return _brief(
        'YouTube Community posts',
        'One text-post draft and one optional poll alternative, clearly separated.',
        'Target 50-100 words for the text post. Tie it to a real supplied video or an upcoming topic; never invent a published video URL.\n- For the poll alternative use one neutral question and three distinct short choices; do not invent results.\n- Check current Posts eligibility and account/region availability before scheduling. Do not assume comments or subscriber notifications are enabled.',
        topic, audience, market,
    )


def snapchat_story(topic, audience, market=None, **_):
    return _brief(
        'Snapchat',
        'A three-frame Story copyboard and one short Spotlight caption alternative.',
        'For each frame provide visual direction, a brief on-screen line, and optional spoken copy. Keep one action per frame.\n- Use a hook, demonstration, and payoff; target a total 15-30 seconds as an editorial choice, not an upload limit.\n- Keep captions readable and provide a text alternative. Do not promise views, monetization, or access to unavailable link features.',
        topic, audience, market,
    )


def twitch_stream(topic, audience, market=None, **_):
    return _brief(
        'Twitch',
        'Three stream-title options, a short schedule announcement, and a 20-second opening script.',
        'State the actual activity and who will benefit. Use [DATE], [TIME], and [TIME ZONE] when the schedule is not supplied.\n- Include a meaningful chat question and one channel-link placeholder. Do not invent guests, drops, prizes, or sponsorships.\n- Keep title options under an editorial target of 80 characters; check live field limits. Avoid copyrighted music suggestions without permission.',
        topic, audience, market,
    )


def kick_stream(topic, audience, market=None, **_):
    return _brief(
        'Kick',
        'Three stream titles, a short go-live announcement, and a viewer welcome script.',
        'Describe the actual stream activity and distinguish this creator from similar channels without unsupported claims.\n- Use explicit schedule placeholders for missing date/time/time zone. Ask one topic-relevant chat question.\n- Do not invent rewards, giveaways, betting promotions, subscriber benefits, or platform monetization eligibility.',
        topic, audience, market,
    )


def spotify_episode(topic, audience, market=None, **_):
    return _brief(
        'Spotify',
        'Three episode-title options and one episode description with an optional resource section.',
        'Use only supplied episode notes or transcript facts. If neither exists, label the draft as a planned episode concept.\n- Open with the listener problem and specific takeaway. Target 100-180 words for the description; no keyword stuffing.\n- Do not fabricate guest quotes, credentials, timestamps, transcript details, or published episode URLs. Include timestamps only when verified against supplied media.',
        topic, audience, market,
    )


def patreon_post(topic, audience, market=None, **_):
    return _brief(
        'Patreon',
        'A member update and a separate short public-preview excerpt.',
        'Target 150-250 words for the update; deliver a real progress note or member resource, not just an upgrade pitch.\n- Identify the intended audience as public, free members, or a supplied paid tier. If unknown, mark it for editor selection.\n- Never invent tier names, prices, release dates, rewards, or exclusivity. Keep paid-only details out of the public preview.',
        topic, audience, market,
    )


def product_hunt_launch(topic, audience, market=None, **_):
    return _brief(
        'Product Hunt',
        'A product tagline, short description, maker first comment, and three FAQ responses.',
        'Keep the tagline within 60 characters and describe the concrete function plainly. Use supplied product facts; leave missing pricing/availability as editor placeholders.\n- The maker comment should explain the problem, what shipped, and the feedback sought. Do not invent a founder biography.\n- Ask for product feedback, not incentivized upvotes. Never fabricate awards, launch ranking, testimonials, or user counts.',
        topic, audience, market,
    )


def slack_community_post(topic, audience, market=None, **_):
    return _brief(
        'Slack',
        'One community-channel announcement and a short thread follow-up.',
        'Target 80-140 words, organized as what changed, why it matters, and the next action.\n- Name an owner and deadline only if supplied; otherwise use [OWNER] and [DEADLINE WITH TIME ZONE].\n- Avoid @channel, @here, and @everyone by default. Respect workspace rules and avoid promoting confidential internal material to a public community.',
        topic, audience, market,
    )


def nextdoor_post(topic, audience, market=None, **_):
    return _brief(
        'Nextdoor',
        'One clearly attributed neighborhood business update.',
        'Target 80-150 words. Start with a concrete local service or useful neighborhood detail.\n- Use [NEIGHBORHOOD], [SERVICE AREA], and [OPENING HOURS] for missing details; never invent proximity, local events, reviews, or endorsements.\n- Identify the business relationship openly, use the appropriate business surface, and avoid fear-based messaging or impersonating an independent neighbor.',
        topic, audience, market,
    )


def lemon8_post(topic, audience, market=None, **_):
    return _brief(
        'Lemon8',
        'A cover headline, five-card editorial outline, caption, and image descriptions.',
        'Build a useful checklist, comparison, or how-to around the topic; put one useful takeaway on each card.\n- Treat the five cards as a suggested creative package, not a claim about platform upload limits.\n- Never invent personal product usage or before/after results. Disclose supplied sponsorships and use only relevant topical tags.',
        topic, audience, market,
    )


def wechat_article(topic, audience, market=None, **_):
    return _brief(
        'WeChat',
        'An Official Account article draft with title, summary, scannable sections, and one closing action.',
        'Target 400-600 words unless the editor supplies a different article length. Keep terminology consistent and audience-specific.\n- Honor the requested language; do not infer language, citizenship, or location solely from platform choice. Recommend native-language editorial review when localized.\n- Use only supplied account names, QR destinations, sources, and links. Do not assume external links, commerce, or account features are available.',
        topic, audience, market,
    )


def weibo_post(topic, audience, market=None, **_):
    return _brief(
        'Weibo',
        'One short topical post and an optional expanded-context comment.',
        'Use a concise editorial target of 100-200 characters for the lead post; verify the actual composer limit for the account.\n- Honor the requested language. Use relevant topic tags only; do not invent trending topics, public reactions, celebrity endorsements, or engagement counts.\n- Put a specific useful observation before promotion and avoid unsupported urgency or news claims.',
        topic, audience, market,
    )


def xiaohongshu_note(topic, audience, market=None, **_):
    return _brief(
        'Xiaohongshu / RED',
        'A note title, cover-text suggestion, practical body, and a five-image outline.',
        'Use a problem, practical steps, caveats, and takeaway structure. The image count is an editorial plan rather than a platform limit.\n- Do not manufacture first-person product trials, purchases, results, reviews, or testimonials. Clearly label illustrative examples and sponsored material.\n- Honor the requested language and recommend native-language review when localized. Do not invent external-link access or current trending tags.',
        topic, audience, market,
    )


def douyin_script(topic, audience, market=None, **_):
    return _brief(
        'Douyin',
        'A 20-40 second short-video script with shot directions, on-screen text, and a caption.',
        'Use a fast problem setup, visible demonstration, and clear payoff; the duration is an editorial target.\n- Honor the requested language and adapt examples to the supplied audience, not stereotypes.\n- Never invent product demonstrations, shopping features, performance claims, licensed music, or creator endorsements. Mark any missing proof shots as production requirements.',
        topic, audience, market,
    )


def bilibili_video(topic, audience, market=None, **_):
    return _brief(
        'Bilibili',
        'Three title options, an opening script, a three-part video outline, and a description.',
        'Make the outline useful for an explanation, tutorial, or informed commentary with concrete demonstrations.\n- Honor the requested language. Explain unfamiliar terms and specify where source credits belong.\n- Do not invent timestamps, published episode links, audience statistics, credentials, or copyrighted footage permissions. Add chapters only after checking the finished edit.',
        topic, audience, market,
    )


def line_message(topic, audience, market=None, **_):
    return _brief(
        'LINE Official Account',
        'One Official Account broadcast message and a separate short reminder alternative.',
        'Target 40-90 words per message as an editorial budget. State one practical benefit and one action.\n- Write for opted-in account followers; do not imply private familiarity or propose unsolicited bulk DMs.\n- Honor the requested language. Never invent coupons, expiry times, rich-menu destinations, account features, or audience consent; leave missing operational details as editor placeholders.',
        topic, audience, market,
    )
