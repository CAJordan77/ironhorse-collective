"""
Customer Service Department Agent.
Handles: support operations, SLA management, customer success,
         knowledge base, feedback analysis, retention programs.
"""

from base_agent import BaseAgent
from task import Task, Report, TaskStatus, ReportStatus


class CustomerServiceAgent(BaseAgent):
    def __init__(self, name: str = "Riley Thompson"):
        super().__init__(name, "VP of Customer Success", "Customer Service")

    def get_responsibilities(self) -> list[str]:
        return [
            "Customer support operations",
            "SLA management and monitoring",
            "Customer success programs",
            "Knowledge base and self-service",
            "Voice of the customer analysis",
            "Retention and churn prevention",
            "Support team training and development",
            "Escalation management",
        ]

    def process_task(self, task: Task) -> Report:
        task.status = TaskStatus.IN_PROGRESS
        print(f"  [VP Customer Success] Processing: {task.title}")

        content = self._analyze_cs_task(task)
        task.status = TaskStatus.COMPLETED

        report = Report(
            id=f"CS-{task.id}",
            title=f"Customer Service Report: {task.title}",
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

    def _analyze_cs_task(self, task: Task) -> str:
        task_lower = task.title.lower()
        if "retention" in task_lower or "churn" in task_lower:
            return (
                f"Retention analysis for: {task.title}. "
                "Churn analysis completed. Identified 3 primary churn drivers: "
                "onboarding friction, feature gaps, and pricing sensitivity. "
                "Proactive outreach program shown to reduce churn by 23%. "
                "Expansion revenue from existing customers up 18%."
            )
        elif "support" in task_lower or "ticket" in task_lower:
            return (
                f"Support operations review for: {task.title}. "
                "Ticket volume stable with improved resolution times. "
                "Self-service adoption increasing - deflection rate at 34%. "
                "Agent utilization optimized through smart routing."
            )
        return (
            f"Customer service assessment for: {task.title}. "
            "Reviewed support metrics and customer feedback. "
            "SLA adherence strong. Customer health scores stable."
        )

    def _generate_metrics(self, task: Task) -> dict:
        return {
            "customer_satisfaction_score": "4.5/5.0",
            "net_promoter_score": 72,
            "first_response_time_minutes": 4,
            "average_resolution_time_hours": 2.1,
            "sla_compliance_rate": "98.7%",
            "customer_churn_rate_monthly": "1.2%",
            "expansion_revenue_rate": "18%",
            "self_service_deflection_rate": "34%",
        }

    def _generate_recommendations(self, task: Task) -> list[str]:
        return [
            "Deploy AI chatbot for tier-1 support deflection",
            "Launch customer health scoring dashboard",
            "Implement proactive onboarding for enterprise clients",
            "Create customer advisory board for product feedback",
        ]

    def _identify_risks(self, task: Task) -> list[str]:
        return [
            "Increasing ticket volume from new product launch (Medium)",
            "Support team capacity at 92% utilization (High)",
            "Key enterprise client showing churn signals (High)",
        ]
