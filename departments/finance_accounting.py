"""
Finance & Accounting Department Agent.
Handles: financial planning, budgeting, forecasting, audits,
         cash flow, investor relations, tax, M&A analysis.
"""

from base_agent import BaseAgent
from task import Task, Report, TaskStatus, ReportStatus


class FinanceAccountingAgent(BaseAgent):
    def __init__(self, name: str = "David Kim"):
        super().__init__(name, "CFO", "Finance & Accounting")

    def get_responsibilities(self) -> list[str]:
        return [
            "Financial planning and analysis (FP&A)",
            "Budgeting and forecasting",
            "Cash flow management",
            "External audit coordination",
            "Investor relations and board reporting",
            "Tax planning and compliance",
            "Mergers and acquisitions analysis",
            "Treasury and risk management",
        ]

    def process_task(self, task: Task) -> Report:
        task.status = TaskStatus.IN_PROGRESS
        print(f"  [CFO] Processing: {task.title}")

        content = self._analyze_finance_task(task)
        task.status = TaskStatus.COMPLETED

        report = Report(
            id=f"FIN-{task.id}",
            title=f"Financial Report: {task.title}",
            department=self.department,
            content=content,
            task_id=task.id,
            status=ReportStatus.SUBMITTED,
            metrics=self._generate_metrics(task),
            recommendations=self._generate_recommendations(task),
            risks=self._identify_risks(task),
        )
        self.reports.append(report)
        return report

    def _analyze_finance_task(self, task: Task) -> str:
        task_lower = task.title.lower()
        if "budget" in task_lower:
            return (
                f"Budget analysis for: {task.title}. "
                "Department budgets reviewed and consolidated. "
                "Identified 12% cost optimization opportunity in cloud "
                "infrastructure. Revenue projections updated based on latest "
                "pipeline data. Board-ready budget package prepared."
            )
        elif "forecast" in task_lower or "projection" in task_lower:
            return (
                f"Financial forecast for: {task.title}. "
                "Updated rolling 18-month forecast. Three scenarios modeled: "
                "base, optimistic, and conservative. Key assumptions validated "
                "with department heads. Cash runway extends 24 months."
            )
        elif "audit" in task_lower:
            return (
                f"Audit preparation for: {task.title}. "
                "All financial records reconciled. Internal controls tested "
                "and documented. No material weaknesses identified. "
                "Ready for external auditor review."
            )
        return (
            f"Financial assessment for: {task.title}. "
            "Reviewed financial statements and key metrics. "
            "All reporting deadlines met. Cash position healthy."
        )

    def _generate_metrics(self, task: Task) -> dict:
        return {
            "annual_recurring_revenue": "$18.5M",
            "monthly_burn_rate": "$420K",
            "cash_runway_months": 24,
            "gross_margin": "72%",
            "operating_margin": "15%",
            "accounts_receivable_days": 38,
            "budget_variance": "+2.1%",
            "debt_to_equity": "0.15",
        }

    def _generate_recommendations(self, task: Task) -> list[str]:
        return [
            "Renegotiate vendor contracts for 15% cost savings",
            "Implement rolling forecast model for better agility",
            "Establish credit facility for M&A flexibility",
            "Optimize tax strategy with R&D credit maximization",
        ]

    def _identify_risks(self, task: Task) -> list[str]:
        return [
            "Customer concentration risk - top 5 clients = 40% revenue (High)",
            "Foreign currency exposure in international operations (Medium)",
            "Interest rate impact on debt refinancing (Low)",
        ]
