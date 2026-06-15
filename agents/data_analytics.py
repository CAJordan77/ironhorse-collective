"""
Ironhorse Collective, LLC — Data Analytics Agent
Department: Strategy & Planning
Role: Data Analyst
Reports to: CEO (Victoria Sterling)

Responsibilities:
- KPI Dashboard management and updates
- Market intelligence tracking and reporting
- Financial analysis and revenue forecasting
- Competitive analysis
- Performance reporting (weekly, monthly, quarterly)
- Lessons Log maintenance
"""

from __future__ import annotations
from typing import Optional
import datetime


class Report:
    """Data Analytics report structure."""
    def __init__(self, title: str, content: str, metrics: dict = None,
                 recommendations: list = None, risks: list = None,
                 report_type: str = "general"):
        self.id = f"DA-{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}"
        self.title = title
        self.content = content
        self.department = "Strategy & Planning"
        self.report_type = report_type  # kpi, market, financial, competitive, lessons
        self.metrics = metrics or {}
        self.recommendations = recommendations or []
        self.risks = risks or []
        self.created_at = datetime.datetime.now().isoformat()


class Task:
    """Task structure for Data Analytics agent."""
    def __init__(self, title: str, description: str, priority: str = "medium",
                 due_date: str = None, assigned_by: str = "CEO"):
        self.id = f"T-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
        self.title = title
        self.description = description
        self.priority = priority  # low, medium, high, critical
        self.status = "pending"  # pending, in_progress, completed, blocked
        self.assigned_to = "Data Analytics"
        self.assigned_by = assigned_by
        self.due_date = due_date
        self.deliverables = []
        self.created_at = datetime.datetime.now().isoformat()


class DataAnalyticsAgent:
    """Data Analytics Agent for Ironhorse Collective.
    
    Handles all data analysis, KPI tracking, market intelligence,
    financial reporting, and competitive analysis.
    """
    
    def __init__(self, name: str = "Atlas"):
        self.name = name
        self.title = "Data Analyst"
        self.department = "Strategy & Planning"
        self.reports: list[Report] = []
        self.tasks: list[Task] = []
        self.kpi_baseline = {}
        self.market_intel_log = []
        self.competitive_data = {}
        self.lessons_log = []
    
    def get_responsibilities(self) -> list[str]:
        return [
            "Build and maintain KPI dashboard",
            "Weekly KPI data collection and reporting",
            "Market intelligence tracking (industry, competitors, trends)",
            "Financial analysis and revenue forecasting",
            "Competitive positioning analysis",
            "Lessons Log maintenance and analysis",
            "Monthly business review reports",
            "Quarterly strategic analysis",
            "Ad-hoc data analysis for leadership decisions"
        ]
    
    def get_status(self) -> dict:
        """Return current agent status."""
        pending_tasks = [t for t in self.tasks if t.status == "pending"]
        in_progress_tasks = [t for t in self.tasks if t.status == "in_progress"]
        completed_tasks = [t for t in self.tasks if t.status == "completed"]
        latest_report = self.reports[-1] if self.reports else None
        
        return {
            "name": self.name,
            "title": self.title,
            "department": self.department,
            "total_tasks": len(self.tasks),
            "pending": len(pending_tasks),
            "in_progress": len(in_progress_tasks),
            "completed": len(completed_tasks),
            "total_reports": len(self.reports),
            "latest_report": latest_report.title if latest_report else "None",
            "kpi_baselines_set": len(self.kpi_baseline) > 0,
            "market_intel_entries": len(self.market_intel_log),
            "competitive_profiles": len(self.competitive_data),
            "lessons_logged": len(self.lessons_log)
        }
    
    def receive_task(self, task: Task) -> None:
        """Receive a new task."""
        self.tasks.append(task)
        print(f"[{self.name}] Task received: {task.title} (Priority: {task.priority})")
    
    def process_task(self, task: Task) -> Report:
        """Process a task and generate a report."""
        task.status = "in_progress"
        print(f"[{self.name}] Processing: {task.title}")
        
        # Route to appropriate handler based on task type
        if "kpi" in task.title.lower() or "dashboard" in task.title.lower():
            report = self._generate_kpi_report(task)
        elif "market" in task.title.lower() or "intel" in task.title.lower():
            report = self._generate_market_intel_report(task)
        elif "financial" in task.title.lower() or "revenue" in task.title.lower():
            report = self._generate_financial_report(task)
        elif "competitive" in task.title.lower() or "competitor" in task.title.lower():
            report = self._generate_competitive_report(task)
        elif "lesson" in task.title.lower():
            report = self._generate_lessons_report(task)
        else:
            report = self._generate_general_report(task)
        
        task.status = "completed"
        self.reports.append(report)
        print(f"[{self.name}] Report generated: {report.title}")
        return report
    
    def set_kpi_baseline(self, metrics: dict) -> None:
        """Set KPI baseline values for tracking."""
        self.kpi_baseline = metrics
        print(f"[{self.name}] KPI baseline set: {len(metrics)} metrics")
    
    def update_kpi(self, metric: str, value) -> None:
        """Update a single KPI value."""
        self.kpi_baseline[metric] = {
            "value": value,
            "updated_at": datetime.datetime.now().isoformat()
        }
    
    def log_market_intel(self, source: str, insight: str,
                         impact: str = "medium") -> None:
        """Log a market intelligence item."""
        entry = {
            "source": source,
            "insight": insight,
            "impact": impact,
            "logged_at": datetime.datetime.now().isoformat()
        }
        self.market_intel_log.append(entry)
        print(f"[{self.name}] Market intel logged: {insight[:50]}...")
    
    def log_competitor(self, competitor: str, data: dict) -> None:
        """Log competitive intelligence."""
        self.competitive_data[competitor] = {
            **data,
            "updated_at": datetime.datetime.now().isoformat()
        }
        print(f"[{self.name}] Competitor profile updated: {competitor}")
    
    def log_lesson(self, issue: str, root_cause: str,
                   action_item: str, owner: str) -> None:
        """Log a lesson learned."""
        entry = {
            "issue": issue,
            "root_cause": root_cause,
            "action_item": action_item,
            "owner": owner,
            "logged_at": datetime.datetime.now().isoformat()
        }
        self.lessons_log.append(entry)
        print(f"[{self.name}] Lesson logged: {issue[:50]}...")
    
    def _generate_kpi_report(self, task: Task) -> Report:
        """Generate KPI dashboard report."""
        current_metrics = self.kpi_baseline
        report = Report(
            title=f"KPI Dashboard Report — {datetime.datetime.now().strftime('%B %d, %Y')}",
            content=f"KPI analysis for: {task.title}. "
                    f"Currently tracking {len(current_metrics)} metrics. "
                    f"Data sources: Stripe (revenue), HubSpot (pipeline), "
                    f"website analytics (traffic), manual (operational).",
            metrics=current_metrics or {
                "MRR": "$0 (pre-revenue)",
                "Pipeline Value": "$0",
                "Leads (Month)": "0",
                "Website Traffic": "Baseline being established",
                "Calendly Bookings": "0",
                "SME Utilization": "0%"
            },
            recommendations=[
                "Establish weekly data collection routine (every Friday)",
                "Connect HubSpot API for automated pipeline tracking",
                "Set up Stripe dashboard as primary revenue data source",
                "Create automated weekly email digest of KPI changes"
            ],
            risks=[
                "Manual data collection is error-prone — prioritize automation",
                "Limited historical data for trend analysis in early months",
                "KPI targets may need adjustment as business matures"
            ],
            report_type="kpi"
        )
        return report
    
    def _generate_market_intel_report(self, task: Task) -> Report:
        """Generate market intelligence report."""
        recent_intel = self.market_intel_log[-10:]  # Last 10 entries
        report = Report(
            title=f"Market Intelligence Brief — {datetime.datetime.now().strftime('%B %d, %Y')}",
            content=f"Market intel analysis: {task.title}. "
                    f"{len(self.market_intel_log)} total intelligence items logged. "
                    f"Recent focus areas: {', '.join(set(i['source'] for i in recent_intel)) if recent_intel else 'No recent data'}.",
            metrics={
                "Total Intel Items": len(self.market_intel_log),
                "High Impact Items": len([i for i in self.market_intel_log if i.get('impact') == 'high']),
                "Sources Tracked": len(set(i['source'] for i in self.market_intel_log)) if self.market_intel_log else 0
            },
            recommendations=[
                "Subscribe to CISA alerts, NIST updates, AICPA SOC2 changes",
                "Monitor competitor pricing quarterly",
                "Track CMMC/DFARS regulatory changes for DoD market",
                "Set up Google Alerts for key terms"
            ],
            risks=[
                "Intel becomes stale if not refreshed weekly",
                "Over-reliance on free sources may miss premium insights",
                "No dedicated budget for paid intelligence services yet"
            ],
            report_type="market"
        )
        return report
    
    def _generate_financial_report(self, task: Task) -> Report:
        """Generate financial analysis report."""
        report = Report(
            title=f"Financial Analysis — {datetime.datetime.now().strftime('%B %d, %Y')}",
            content=f"Financial analysis: {task.title}. "
                    "Revenue allocation framework: Phase 1 (first $50K) = 50% ops, "
                    "25% sales/marketing, 15% tools, 10% reserve. "
                    "No owner distributions until 6-month reserve funded.",
            metrics={
                "Current Revenue": "$0",
                "Phase": "Phase 1 (pre-$50K)",
                "Operating Reserve Target": "3 months → 6 months",
                "Tool Budget (Phase 1)": "15% of revenue",
                "Marketing Budget (Phase 1)": "25% of revenue"
            },
            recommendations=[
                "Track burn rate weekly",
                "Model revenue scenarios at different conversion rates",
                "Prepare 90-day cash flow projection",
                "Set up Stripe → QuickBooks integration for automated tracking"
            ],
            risks=[
                "Consulting revenue is lumpy — maintain reserve",
                "Tool costs can escalate quickly with team growth",
                "Revenue recognition timing affects cash flow planning"
            ],
            report_type="financial"
        )
        return report
    
    def _generate_competitive_report(self, task: Task) -> Report:
        """Generate competitive analysis report."""
        competitors = list(self.competitive_data.keys())
        report = Report(
            title=f"Competitive Analysis — {datetime.datetime.now().strftime('%B %d, %Y')}",
            content=f"Competitive analysis: {task.title}. "
                    f"Tracking {len(competitors)} competitors: {', '.join(competitors) if competitors else 'None yet'}. "
                    "Key differentiator: Ironhorse is the only firm our size covering "
                    "all 4 legacy infrastructure domains (Mainframe, Telephony, "
                    "Contact Center, Storage).",
            metrics={
                "Competitors Tracked": len(competitors),
                "Differentiation Score": "High (4-domain coverage vs. typical 1-2)",
                "Pricing Position": "Mid-market (SOC2 $15K-$20K)",
                "Geographic Reach": "Global (remote-first)"
            },
            recommendations=[
                "Build competitive battle cards for sales team",
                "Monitor competitor pricing quarterly",
                "Track competitor content/publications for positioning intelligence",
                "Develop case studies that highlight multi-domain advantage"
            ],
            risks=[
                "Larger firms may expand into legacy infrastructure space",
                "Competitors with stronger brand recognition may undercut on price",
                "Niche competitors may have deeper domain expertise in single areas"
            ],
            report_type="competitive"
        )
        return report
    
    def _generate_lessons_report(self, task: Task) -> Report:
        """Generate lessons learned report."""
        recent_lessons = self.lessons_log[-10:]
        report = Report(
            title=f"Lessons Learned Summary — {datetime.datetime.now().strftime('%B %d, %Y')}",
            content=f"Lessons analysis: {task.title}. "
                    f"{len(self.lessons_log)} total lessons logged. "
                    f"Recent issues: {len(recent_lessons)} in the last reporting period.",
            metrics={
                "Total Lessons Logged": len(self.lessons_log),
                "Open Action Items": len([l for l in self.lessons_log if "open" in l.get("action_item", "").lower()]),
                "Resolved": len([l for l in self.lessons_log if "resolved" in l.get("action_item", "").lower()]),
                "Recurring Themes": "TBD as data accumulates"
            },
            recommendations=[
                "Review Lessons Log in every Friday standup",
                "Tag lessons by department for targeted improvement",
                "Escalate recurring issues to CEO for systemic solutions",
                "Celebrate fixes — not just failures"
            ],
            risks=[
                "Lessons Log becomes shelfware without enforcement",
                "Blame culture may discourage honest reporting",
                "Lessons don't translate into action without owner accountability"
            ],
            report_type="lessons"
        )
        return report
    
    def _generate_general_report(self, task: Task) -> Report:
        """Generate general-purpose report."""
        report = Report(
            title=f"Analysis: {task.title}",
            content=f"Data analysis for: {task.description}",
            metrics={"Status": "Analysis pending data availability"},
            recommendations=["Gather relevant data sources", "Define analysis scope"],
            risks=["Insufficient data for meaningful analysis"],
            report_type="general"
        )
        return report
