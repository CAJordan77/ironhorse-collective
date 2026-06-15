
content = """# How to Build a Customer Health Score That Predicts Churn

## Introduction

Customer churn is the silent killer of SaaS businesses. By the time a customer cancels, the damage is usually done — months of declining engagement, unanswered support tickets, and missed expansion signals that were hiding in your data the whole time.

A well-designed Customer Health Score changes that equation. It transforms raw usage data into a single, actionable number that predicts churn risk 90 days before it happens. This guide walks you through building one from scratch.

## What Is a Customer Health Score and Why It Predicts Churn

A Customer Health Score (CHS) is a composite metric that combines product usage, support interactions, engagement patterns, payment history, and qualitative signals into a single score on a 0-100 scale.

The insight behind health scoring is simple: customers do not churn suddenly. They disengage gradually. Product usage declines. Support sentiment turns negative. Champion contacts leave. A health score catches these signals early.

Research from Gainsight shows that companies using health scores reduce churn by 25-40% compared to those relying on reactive methods.

### The Five Core Metrics

| Metric Category | What to Track | Weight |
|----------------|---------------|--------|
| Product Usage | Active users, feature adoption, session depth | 30% |
| Support Health | Ticket count, CSAT, escalation rate | 20% |
| Engagement | Login frequency, page views, time-in-app | 25% |
| Payment History | On-time payments, failed charges, plan tier | 10% |
| Qualitative | NPS score, champion engagement, exec sponsor | 15% |

## How to Build a Scoring Model from Scratch

Step 1: Define Your Dimensions. Pull historical data for the 90 days before churned customers left. Common patterns include login frequency dropping by more than 50%, support tickets increasing by 2x, and key features going unused for 30+ days.

Step 2: Build the Scoring Algorithm. Define thresholds for each dimension: Green (70-100, Healthy), Yellow (40-69, At-Risk), Red (0-39, Critical). Score each dimension independently, then calculate the weighted average.

Step 3: Set Up Data Pipelines. Connect your product analytics (Mixpanel, Amplitude), CRM (HubSpot, Salesforce), support tool (Zendesk, Intercom), and billing system (Stripe, Chargebee).

Step 4: Define Playbook Triggers. Green gets upsell plays and referral requests. Yellow triggers CSM outreach within 48 hours. Red triggers immediate escalation and executive intervention.

Step 5: Test and Calibrate. Run your model against historical data. Tune weights and thresholds until the model correctly identifies at least 80% of churned customers as at-risk before they churned.

## Segmentation Strategies

Not all customers are equal. Segment by company size (enterprise vs SMB have different signals), lifecycle stage (new customers need onboarding metrics, renewal-stage needs usage trend analysis), plan tier (higher tiers warrant more sophisticated scoring), and industry (usage patterns vary by vertical).

## Automated Health Score Tools

| Tool | Best For | Starting Price |
|------|----------|---------------|
| Gainsight | Enterprise CS teams | $2,500/mo |
| Totango | Mid-market SaaS | $1,000/mo |
| ChurnZero | Real-time alerts | $1,500/mo |
| Vitally | PLG companies | $150/mo |
| Catalyst | Revenue operations | $500/mo |
| Custom (dbt + BI) | Technical teams | Engineering time |

## Case Studies

Slack (Early Days): Slack tracked messages sent per team. Teams sending 2,000+ messages had near-zero churn. Teams under 500 messages were at high risk.

HubSpot: HubSpot built a multi-factor health score combining product usage, support interactions, NPS scores, and Academy content engagement. The model identifies at-risk accounts 60-90 days before renewal.

Mid-Market SaaS: A $20M ARR company reduced churn from 15% to 8% annually. Key insight: customers who stopped using their core workflow feature for 14+ days had a 70% chance of churning within 60 days.

## Customer Health Score Template

### Scoring Criteria

| Dimension | Green (70-100) | Yellow (40-69) | Red (0-39) |
|-----------|---------------|----------------|------------|
| Product Usage | Daily active use, 3+ features | Weekly active, 1-2 features | Less than weekly, 0-1 features |
| Support Health | CSAT > 4.0, no escalations | CSAT 3.0-4.0, minor escalations | CSAT < 3.0, frequent escalations |
| Engagement | Login 5+ days/week | Login 2-4 days/week | Login < 2 days/week |
| Payment | On-time, no issues | Late payment 1-2x | Failed charges or >30 days late |
| Qualitative | NPS 9-10, champion engaged | NPS 7-8, neutral | NPS < 6, champion disengaged |

### Implementation Checklist

- [ ] Pull 12 months of churn data and identify behavioral patterns
- [ ] Define your scoring dimensions and weights
- [ ] Build the scoring model (spreadsheet or tool)
- [ ] Run against historical data and calibrate
- [ ] Set up data pipelines from product, support, CRM, and billing
- [ ] Define playbook triggers for each health tier
- [ ] Train CS team on health score interpretation
- [ ] Launch weekly Health Review meeting
- [ ] Create automated alerts for tier changes
- [ ] Build executive dashboard
- [ ] Review and refine model quarterly

## Conclusion

A Customer Health Score is one of the highest-leverage investments a SaaS company can make. It transforms customer success from reactive to predictive, and gives every team a shared language for customer health. Start simple. Get the data flowing. Refine over time. The best health score is the one your team actually uses.

Want help building your health model? Book a free strategy call and we will assess your current customer data and design a scoring framework for your business.

---
© 2026 ProShield Consulting. This guide is provided for educational purposes.
"""

path = r"C:\Users\chris\corporate_agents\content\pillar-articles\customer-health-score.md"
with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print(f"Written {len(content)} chars to {path}")
print(f"File size: {os.path.getsize(path)} bytes")
