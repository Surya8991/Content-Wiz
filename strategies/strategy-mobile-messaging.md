# Mobile Messaging Strategy: SMS, Push Notifications, and In-App Messages

_Last updated: 2026-07-14_


## Goal and Metric

Drive high-intent conversions and reduce churn through precisely timed, behaviorally triggered mobile messages that reach the right audience in the right channel at the right moment. Primary success metric: SMS click-through rate above 18%, push notification opt-in rate above 45%, and a mobile messaging attribution of 12%+ of monthly revenue within 6 months of full implementation.

---

## Core Principles

**1. Compliance is not a box to check; it is the foundation.** SMS marketing without explicit opt-in consent violates the Telephone Consumer Protection Act (TCPA) in the US and the General Data Protection Regulation (GDPR) in the EU. A single non-compliant SMS campaign can trigger class-action litigation or regulatory fines. Consent architecture must be built before the first message is sent, not retrofitted after growth demonstrates the channel works.

**2. Channel selection is a message priority decision.** SMS, push notifications, and in-app messages are not interchangeable. SMS reaches the user wherever they are (no app required) and carries the highest urgency signal. Push reaches users who have the app installed and opted in to notifications. In-app messages reach users who are already inside the app. Match the message's urgency and context to the channel that fits it.

**3. Frequency caps are customer experience decisions, not arbitrary limits.** Sending too many messages in too short a window produces unsubscribes, app notification disables, and negative sentiment that outlasts the campaign. The frequency caps in this strategy are not conservative guesses; they represent the point at which message value-to-interruption ratio inverts for most audiences.

**4. Behavioral triggers outperform scheduled broadcasts.** A message triggered by what the user just did (abandoned a cart, completed a milestone, went inactive for 7 days) arrives with context and relevance that a scheduled promotional blast cannot replicate. Behavioral trigger programs earn 3 to 5x the conversion rate of broadcast campaigns on comparable audiences.

**5. Personalization below the first-name level requires data infrastructure.** Using a recipient's first name in an SMS is a baseline, not a differentiator. Personalization that drives measurably higher engagement incorporates behavioral context (what the user did most recently), preference data (what they have engaged with), or situational data (their location, their plan type, their stage in the customer lifecycle). Build the data infrastructure before building the personalization.

---

## Strategy Architecture

**Step 1: Compliance and consent architecture**

SMS opt-in requirements (TCPA and GDPR):
- Explicit written consent is required before sending any marketing SMS; pre-checked boxes and implied consent do not satisfy TCPA requirements
- The opt-in confirmation message must include: brand name, message frequency disclosure, data rate disclosure, and STOP opt-out instructions
- Store the opt-in timestamp, the opt-in source, and the specific consent language the user agreed to; this data is required for legal defense if consent is disputed
- Maintain a suppression list of all STOP opt-outs; do not re-subscribe users who have opted out without a new explicit opt-in through a separate mechanism

Push notification opt-in strategy:
- iOS requires an explicit permission prompt before push notifications can be sent; time the permission request to a high-value moment in the app experience rather than at first launch (users who understand the value of push notifications before being asked opt in at 2x the rate of users asked on first open)
- Android's notification permission requirement (introduced in Android 13) requires the same deliberate timing approach

**Step 2: Channel hierarchy by message type**

Assign message types to channels based on urgency, context, and channel fit:

SMS appropriate for:
- Time-sensitive purchase confirmations and shipping updates (users expect these via SMS regardless of app installation)
- Exclusive, high-value promotions (genuine flash sales, first-access events)
- Appointment reminders with confirmed opt-in
- Transactional security notifications (password reset codes, account alerts)
- Win-back messages for churned subscribers who are no longer engaging with the app

Push notifications appropriate for:
- In-the-moment activity triggers (you have a new message, your order shipped, your task is due)
- App re-engagement for users who have installed but not opened the app in 7 to 14 days
- Personalized content recommendations
- Milestone celebrations and gamification rewards

In-app messages appropriate for:
- Onboarding guidance during the first session
- Feature discovery and upsell prompts shown to users who are actively using the app
- Feedback requests and NPS surveys
- Contextual help triggered by specific actions within the app

**Step 3: Behavioral trigger mapping**
Map the most valuable behavioral triggers for the brand's user lifecycle:

High-priority triggers (build first):
- Cart abandonment: send a push notification 1 hour after abandonment, an SMS 4 hours after abandonment if no conversion, and an in-app message on next app open
- Milestone reached: congratulatory in-app message immediately, followed by a push notification if the user has closed the app
- Inactivity at 7 days: push notification with a personalized re-engagement hook based on the user's most recent activity
- Inactivity at 21 days: SMS with a win-back incentive if the user is not responding to push notifications (SMS bypass becomes justified when push engagement has failed)

Secondary triggers (build after core triggers are live and optimized):
- Post-purchase (24 hours after confirmed delivery): in-app or push with usage tips or related recommendations
- Subscription expiration approaching (7 days before): push and email (not SMS unless the urgency is high and the relationship is established)
- Price drop on a previously viewed item: push notification

**Step 4: Frequency caps**
Apply these limits as system-level rules, not campaign-level guidelines:
- SMS: maximum 4 messages per month per contact, minimum 48 hours between messages
- Push notifications: maximum 2 per week per user, minimum 12 hours between messages
- In-app messages: maximum 1 per session, minimum 24 hours between messages

Exception: transactional messages (order confirmations, shipping updates, security codes) do not count against frequency caps because they are expected and requested by the user.

**Step 5: Quiet hours enforcement**
Block all outbound marketing messages outside of 8am to 8pm in the recipient's local time zone:
- Configure quiet hours at the platform level, not as a manual step in campaign setup
- For users without a detectable time zone (no location data), default to the brand's primary market time zone
- TCPA quiet hours requirements are 8am to 9pm; setting the brand's quiet hours to 8am to 8pm provides a compliance buffer

---

## Personalization Requirements

Minimum personalization for every marketing message:
- First name in the salutation or opening line
- Brand name in the SMS sender ID or push notification title (do not send from an unidentified short code)

Recommended personalization for push and in-app messages:
- Reference the user's most recent action or most recent product/feature interaction
- Use the user's lifecycle stage to inform tone (new users receive welcome-oriented language; long-term users receive loyalty-affirming language)
- Personalize the CTA based on where the user is in the conversion funnel

---

## Cadence

- SMS: 2 to 4 messages per month per subscriber; more than 4 per month requires exceptional content and a clearly communicated frequency expectation at opt-in
- Push notifications: 2 per week maximum for marketing messages; behavioral triggers are exempt from this cap but should not stack on top of it (behavioral and scheduled push combined should not exceed 3 per week for a single user)
- In-app messages: 1 per session, shown at a contextually relevant moment rather than at session open
- Frequency cap review: reassess caps quarterly based on unsubscribe rate trends; if SMS opt-out rate exceeds 2% in any calendar month, reduce frequency immediately

---

## Failure Modes

1. **Mass blasts without segmentation.** Sending the same message to the entire subscriber list regardless of behavior, location, lifecycle stage, or product usage is the surest way to drive opt-outs and damage deliverability. SMS lists built through proper opt-in should be treated as high-trust relationships, not broadcast lists.

2. **No opt-out mechanism.** Every marketing SMS must include STOP opt-out instructions. Omitting these is a TCPA violation. Every push notification settings screen must provide users with granular notification controls. Omitting these results in the user disabling all notifications rather than adjusting them.

3. **Sending outside quiet hours.** A promotional SMS received at 11pm produces an immediate opt-out and lasting negative brand association. Quiet hours enforcement at the platform level (not the campaign level) is the only way to guarantee compliance across all campaigns and automated triggers.

4. **Treating push notifications like email.** Email tolerates longer copy, lower urgency, and weekly or daily cadences. Push notifications require short copy (under 75 characters for optimal display), immediate relevance, and infrequent sending. Applying email content and cadence logic to push notifications produces opt-outs and notification disables.

5. **No behavioral trigger program.** A mobile messaging strategy that consists only of promotional broadcasts and no behavioral triggers is operating at 20 to 30% of its potential revenue contribution. Cart abandonment and inactivity triggers alone typically account for more revenue than all scheduled broadcast campaigns combined.

6. **Re-subscribing opted-out users.** Adding a contact who sent STOP back to the SMS list through a different opt-in mechanism, or through a platform migration, is a TCPA violation. Suppression lists must persist through platform migrations and list imports.

---

## Recommended Tools

- **Attentive or Klaviyo SMS** (enterprise SMS marketing platforms with TCPA-compliant opt-in flows, behavioral trigger automation, audience segmentation, and quiet hours enforcement built into the platform; Attentive is the industry leader for ecommerce SMS; Klaviyo provides stronger email-SMS integration for brands using Klaviyo for email)
- **Braze** (enterprise mobile engagement platform covering SMS, push, and in-app messaging in a single workflow; the behavioral trigger capabilities and lifecycle stage segmentation are best-in-class for brands with complex user journeys)
- **OneSignal** (push notification and in-app message platform with a free tier suitable for smaller brands; supports A/B testing, behavioral triggers, and audience segmentation; integrates with most mobile development stacks)
- **Segment** (customer data platform that consolidates behavioral event data from mobile apps, web, and other sources into a single user profile; enables the personalization logic that makes behavioral triggers more relevant without building a custom data pipeline)
- **Postman or Charles Proxy** (developer tools for auditing mobile API calls to verify that opt-in data is being captured and stored correctly; compliance documentation depends on proof that consent was recorded at the correct moment)

---

## Adaptation for Your Brand

Mobile messaging strategy effectiveness depends entirely on the brand's app ecosystem and customer lifecycle. Brands without a mobile app cannot use push notifications or in-app messages and should focus exclusively on SMS. Brands with an app and high daily active usage ratios should prioritize in-app messages and push before SMS, because the in-app and push channels are lower friction and lower compliance risk than SMS.

For B2B brands, mobile messaging is typically limited to transactional notifications (platform alerts, task reminders, usage reports) rather than promotional campaigns. Promotional SMS in B2B contexts rarely performs well because the buyer relationship is professional and the urgency signals of SMS feel misaligned with B2B purchasing cycles.

Consumer brands in ecommerce, food delivery, fitness, and entertainment typically see the highest returns from mobile messaging because the purchase cycle is short, the behavioral triggers are frequent, and the SMS channel matches the urgency of time-sensitive offers.

The TCPA enforcement environment in the US continues to produce class-action litigation against brands with insufficient consent records. Before launching any SMS program, have legal counsel review the opt-in flow, the consent storage architecture, and the suppression list management process.
