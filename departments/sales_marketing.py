"""
Sales & Marketing Department Agent.
Handles: revenue targets, campaigns, market analysis, brand management,
         customer acquisition, pipeline management.
"""

from base_agent import BaseAgent
from task import Task, Report, TaskStatus, ReportStatus


class SalesMarketingAgent(BaseAgent):
    def __init__(self, name: str = "Jordan Rivera"):
        super().__init__(name, "CMO", "Sales & Marketing")

    def get_responsibilities(self) -> list[str]:
        return [
            "Revenue target planning and tracking",
            "Marketing campaign strategy and execution",
            "Market research and competitive analysis",
            "Brand management and positioning",
            "Customer acquisition and retention",
            "Sales pipeline management",
            "Partner and channel development",
            "Digital marketing and analytics",
        ]

    def process_task(self, task: Task) -> Report:
        task.status = TaskStatus.IN_PROGRESS
        print(f"  [CMO] Processing: {task.title}")

        content = self._analyze_sales_task(task)
        task.status = TaskStatus.COMPLETED

        report = Report(
            id=f"SM-{task.id}",
            title=f"Sales & Marketing Report: {task.title}",
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

    def _analyze_sales_task(self, task: Task) -> str:
        task_lower = task.title.lower()
        if "campaign" in task_lower:
            return (
                f"Campaign analysis for: {task.title}. "
                "Launched multi-channel campaign across digital, social, and "
                "email platforms. A/B testing completed on creative variants. "
                "Results show strong engagement metrics with positive ROI trajectory."
            )
        elif "revenue" in task_lower or "forecast" in task_lower:
            return (
                f"Revenue analysis for: {task.title}. "
                "Pipeline health is strong with balanced distribution across "
                "stages. Win rate improved quarter-over-quarter. Key deals "
                "in enterprise segment expected to close this quarter."
            )
        elif "market" in task_lower:
            return (
                f"Market analysis for: {task.title}. "
                "Completed competitive landscape review. Identified 3 emerging "
                "market segments with high growth potential. Customer sentiment "
                "analysis indicates strong brand positioning."
            )
        return (
            f"Sales & Marketing assessment for: {task.title}. "
            "Reviewed current pipeline, campaign performance, and market "
            "conditions. All KPIs trending positively."
        )

    def _generate_metrics(self, task: Task) -> dict:
        return {
            "quarterly_revenue": "$4.2M",
            "revenue_growth_qoq": "12%",
            "customer_acquisition_cost": "$127",
            "customer_lifetime_value": "$3,800",
            "pipeline_value": "$12.5M",
            "win_rate": "34%",
            "marketing_roi": "4.2x",
            "nps_score": "72",
        }

    def _generate_recommendations(self, task: Task) -> list[str]:
        return [
            "Increase investment in ABM for enterprise segment",
            "Launch referral program to reduce CAC",
            "Expand into APAC market by Q4",
            "Implement predictive lead scoring with ML",
        ]

    def _identify_risks(self, task: Task) -> list[str]:
        return [
            "Heavy dependency on top 3 enterprise clients (High)",
            "Increasing CAC in digital channels (Medium)",
            "Competitor pricing pressure in SMB segment (Medium)",
        ]
