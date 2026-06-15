"""
Strategy & Planning Department Agent.
Handles: corporate strategy, competitive intelligence, partnerships,
         market entry, OKR planning, board preparation.
"""

from base_agent import BaseAgent
from task import Task, Report, TaskStatus, ReportStatus


class StrategyPlanningAgent(BaseAgent):
    def __init__(self, name: str = "Alex Nakamura"):
        super().__init__(name, "Chief Strategy Officer", "Strategy & Planning")

    def get_responsibilities(self) -> list[str]:
        return [
            "Corporate strategy development",
            "Competitive intelligence and analysis",
            "Strategic partnerships and alliances",
            "Market entry strategy",
            "OKR planning and tracking",
            "Board meeting preparation",
            "Scenario planning and risk assessment",
            "Corporate development and M&A",
        ]

    def process_task(self, task: Task) -> Report:
        task.status = TaskStatus.IN_PROGRESS
        print(f"  [CSO] Processing: {task.title}")

        content = self._analyze_strategy_task(task)
        task.status = TaskStatus.COMPLETED

        report = Report(
            id=f"SP-{task.id}",
            title=f"Strategy Report: {task.title}",
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

    def _analyze_strategy_task(self, task: Task) -> str:
        task_lower = task.title.lower()
        if "market" in task_lower and "entry" in task_lower:
            return (
                f"Market entry analysis for: {task.title}. "
                "Completed TAM/SAM/SOM analysis for target market. "
                "Regulatory requirements mapped. Go-to-market strategy "
                "developed with phased rollout plan. Partnership "
                "opportunities identified with 3 potential local partners."
            )
        elif "partnership" in task_lower or "alliance" in task_lower:
            return (
                f"Partnership assessment for: {task.title}. "
                "Evaluated strategic fit, financial impact, and risk profile. "
                "Due diligence completed on target partner. "
                "Proposed deal structure balances value creation with risk "
                "mitigation. Recommend proceeding to term sheet negotiation."
            )
        elif "okr" in task_lower or "objective" in task_lower:
            return (
                f"OKR review for: {task.title}. "
                "Quarterly OKR progress reviewed across all departments. "
                "72% of key results on track. 3 objectives need recalibration "
                "due to market changes. Next quarter objectives drafted."
            )
        return (
            f"Strategic assessment for: {task.title}. "
            "Analyzed strategic options with supporting data. "
            "Recommendations aligned with long-term corporate vision."
        )

    def _generate_metrics(self, task: Task) -> dict:
        return {
            "okr_completion_rate": "72%",
            "strategic_initiatives_active": 8,
            "partnership_revenue_contribution": "15%",
            "market_share_growth": "+2.3%",
            "competitive_win_rate": "67%",
            "strategic_risk_score": "3.2/10",
            "board_readiness_score": "94%",
            "scenario_plans_active": 3,
        }

    def _generate_recommendations(self, task: Task) -> list[str]:
        return [
            "Accelerate APAC market entry with local partnership",
            "Evaluate strategic acquisition in adjacent market",
            "Develop 3-year technology moat strategy",
            "Establish corporate venture arm for ecosystem investment",
        ]

    def _identify_risks(self, task: Task) -> list[str]:
        return [
            "Market saturation in core segment (Medium)",
            "Regulatory changes in EU data privacy landscape (Medium)",
            "Potential disruption from well-funded startup (High)",
        ]
