# Additional Platform Distribution Strategy

Updated: 2026-11-02. Applies to Content Wiz 0.11.0.

These are editorial briefs for drafting, not account connections or publishing
APIs. Select channels where the brand already has a relevant audience and a
real account owner. No posting cadence or reach outcome is guaranteed.

## Deliverables and routing

| Platform | Primary CLI alias | Output folder | Deliverable |
|---|---|---|---|
| Bluesky | `bluesky` | `Bluesky` | One standalone text post plus one optional follow-up reply. |
| Mastodon | `mastodon` | `Mastodon` | One standalone post, an optional content-warning line, and image alt-text only if an image is supplied. |
| Telegram Channels | `telegram` | `Telegram` | One channel update: short headline, useful body, and one action. |
| WhatsApp Channels | `whatsapp` | `WhatsApp_Channels` | One concise channel update and an optional suggested reaction prompt. |
| YouTube Community posts | `youtube_community` | `YouTube_Community` | One text-post draft and one optional poll alternative, clearly separated. |
| Snapchat | `snapchat` | `Snapchat` | A three-frame Story copyboard and one short Spotlight caption alternative. |
| Twitch | `twitch` | `Twitch` | Three stream-title options, a short schedule announcement, and a 20-second opening script. |
| Kick | `kick` | `Kick` | Three stream titles, a short go-live announcement, and a viewer welcome script. |
| Spotify | `spotify` | `Spotify` | Three episode-title options and one episode description with an optional resource section. |
| Patreon | `patreon` | `Patreon` | A member update and a separate short public-preview excerpt. |
| Product Hunt | `product_hunt` | `Product_Hunt` | A product tagline, short description, maker first comment, and three FAQ responses. |
| Slack | `slack` | `Slack` | One community-channel announcement and a short thread follow-up. |
| Nextdoor | `nextdoor` | `Nextdoor` | One clearly attributed neighborhood business update. |
| Lemon8 | `lemon8` | `Lemon8` | A cover headline, five-card editorial outline, caption, and image descriptions. |
| WeChat | `wechat` | `WeChat` | An Official Account article draft with title, summary, scannable sections, and one closing action. |
| Weibo | `weibo` | `Weibo` | One short topical post and an optional expanded-context comment. |
| Xiaohongshu / RED | `xiaohongshu` | `Xiaohongshu` | A note title, cover-text suggestion, practical body, and a five-image outline. |
| Douyin | `douyin` | `Douyin` | A 20-40 second short-video script with shot directions, on-screen text, and a caption. |
| Bilibili | `bilibili` | `Bilibili` | Three title options, an opening script, a three-part video outline, and a description. |
| LINE Official Account | `line` | `LINE` | One Official Account broadcast message and a separate short reminder alternative. |

## Editorial approach

Short feeds should carry one useful insight per post. Subscriber channels should
lead with the practical update and one action, without pretending to be private
one-to-one messages. Stream announcements need an actual activity, date, time,
and timezone. Podcast/video copy must reflect supplied source material rather
than invent quotes, chapters, or guests. Member posts need a known access tier;
local-business posts need clear affiliation and real service-area information.

Treat the regional platforms as distinct editorial contexts. Honor `--language`
and the supplied audience instead of assuming the reader's language or identity.
Use native-language editorial review for localization, and check the account's
actual permissions, link behavior, commercial-disclosure requirements, and
regional feature availability in the live publisher before scheduling.

Length, card-count, and duration budgets in these new prompts are editorial
choices except where a platform limit is explicitly named. A generic CLI
wordcount does not override the channel brief. The model cannot certify exact
counts; the editor must check the final copy in the publishing UI.

## Quality and measurement

Start with a small editorial batch, then adjust cadence based on observed
responses and team capacity. Use actual destination links after publication;
never fabricate cross-platform companion URLs. Measure useful replies and
qualified visits for short feeds, resource clicks for channels, attendance for
streams, consumption for audio/video, and member feedback for membership posts.
These are suggested measures, not promises that every platform exposes them.

Failure modes: recycled posts with the wrong format; invented personal product
experience; implied private familiarity in broadcasts; fake launch rankings;
missing timezone; unsupported shopping/link features; fabricated timestamps;
excessive mentions; and public previews leaking paid or confidential content.

Before publication: verify claims and destinations, attribute authorship, disclose
sponsorships, check accessibility, remove unresolved placeholders, and record
review. The CLI approval gate does not perform factual verification.

## Official references and limits

Checked on 2026-11-02 where public documentation was readable. Platform changes
require rechecking before publication; this is not a permanent policy reference.

- [Mastodon posting guide](https://docs.joinmastodon.org/user/posting/) documents
  the default 500-character post length; server configuration can differ.
- [Telegram channel FAQ](https://telegram.org/faq_channels) distinguishes channel
  broadcasts from group discussion. Do not assume discussion is configured.
- [WhatsApp Channels introduction](https://blog.whatsapp.com/introducing-whatsapp-channels-a-private-way-to-follow-what-matters)
  explains the broadcast surface. Do not reuse this copy as a Business API template.
- [YouTube Posts help](https://support.google.com/youtube/answer/9409631?hl=en)
  describes post types and eligibility restrictions. Check the current channel
  role, audience setting, and regional availability.
- [Snapchat creator tools](https://creators.snapchat.com/start-creating) provides
  the Story/Spotlight context; the template's duration is an editorial target.
- [Twitch channel setup](https://help.twitch.tv/s/article/channel-page-setup?language=en_US)
  covers channel presentation and schedules.
- [Spotify episode descriptions](https://creators.spotify.com/resources/podcast-episode-descriptions)
  provides description-writing guidance; use the actual episode content.
- [Patreon posting guide](https://support.patreon.com/hc/en-us/articles/115004048046-Posting-to-your-Patreon)
  distinguishes public, free-member, and paid-member audiences.
- [Product Hunt preparation](https://www.producthunt.com/launch/preparing-for-launch)
  gives the 60-character tagline limit. [Launch promotion guidance](https://www.producthunt.com/launch/sharing-your-launch)
  rejects rewards for upvotes.
- [Slack announcements](https://slack.com/help/articles/220105027-Use-the-general-channel-to-share-announcements)
  describes announcement channels; broad mentions require permission and restraint.
- [Nextdoor Business Posts](https://business.nextdoor.com/en-us/getting-started/business-post)
  describes the local-business surface.
- [LINE Official Account help](https://lineforbusiness.com/th-en/helpcenter/line-oa)
  describes account messaging. Confirm local account features separately.
- [Lemon8 official creator guide](https://www.lemon8-app.com/@captainlemon8?region=us)
  is a starting point for current creator guidance.

Bluesky documentation redirected during this review; the template uses a
conservative editorial target rather than an asserted maximum. Xiaohongshu,
Douyin, and Bilibili returned login, loading, or browser gates, so no numeric
platform limits were verified for them. Weibo, WeChat, and Kick briefs likewise
avoid unverified hard limits or eligibility claims. Use each account's official
publisher/help surface to confirm those details before scheduling.
