"""
Agent (Human) Resources Department Agent.
Handles: recruiting, onboarding, performance management, compensation,
         culture, training, employee relations, compliance.
"""

from base_agent import BaseAgent
from task import Task, Report, TaskStatus, ReportStatus


class HumanResourcesAgent(BaseAgent):
    def __init__(self, name: str = "Sam Williams"):
        super().__init__(name, "CHRO", "Agent (Human) Resources")

    def get_responsibilities(self) -> list[str]:
        return [
            "Talent acquisition and recruiting",
            "Employee onboarding and offboarding",
            "Performance management and reviews",
            "Compensation and benefits administration",
            "Company culture and engagement",
            "Learning and development programs",
            "Employee relations and conflict resolution",
            "HR compliance and policy management",
        ]

    def process_task(self, task: Task) -> Report:
        task.status = TaskStatus.IN_PROGRESS
        print(f"  [CHRO] Processing: {task.title}")

        content = self._analyze_hr_task(task)
        task.status = TaskStatus.COMPLETED

        report = Report(
            id=f"HR-{task.id}",
            title=f"HR Report: {task.title}",
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

    def _analyze_hr_task(self, task: Task) -> str:
        task_lower = task.title.lower()
        if "recruit" in task_lower or "hir" in task_lower:
            return (
                f"Recruiting update for: {task.title}. "
                "Revised employer branding strategy launched. "
                "Sourcing pipeline strengthened through employee referral "
                "program. Interview-to-offer ratio improved. "
                "Diversity hiring metrics trending positively."
            )
        elif "performance" in task_lower or "review" in task_lower:
            return (
                f"Performance management update for: {task.title}. "
                "Completed quarterly review cycle. Top performers identified "
                "for accelerated development paths. Performance improvement "
                "plans initiated where needed. Calibration sessions completed."
            )
        elif "culture" in task_lower or "engagement" in task_lower:
            return (
                f"Culture and engagement report for: {task.title}. "
                "Employee satisfaction survey completed with 94% participation. "
                "Key themes: strong alignment with mission, desire for more "
                "flexible work options, positive feedback on recent benefits "
                "enhancements."
            )
        return (
            f"HR assessment for: {task.title}. "
            "Reviewed current HR metrics and programs. "
            "All compliance requirements met. Employee satisfaction stable."
        )

    def _generate_metrics(self, task: Task) -> dict:
        return {
            "headcount": 342,
            "open_positions": 28,
            "time_to_fill_days": 32,
            "offer_acceptance_rate": "91%",
            "employee_satisfaction": "4.2/5.0",
            "turnover_rate_annual": "8.3%",
            "training_hours_per_employee": 24,
            "diversity_ratio": "46%",
        }

    def _generate_recommendations(self, task: Task) -> list[str]:
        return [
            "Implement AI-powered resume screening to reduce time-to-fill",
            "Launch leadership development program for high-potential ICs",
            "Enhance parental leave policy to match top competitors",
            "Conduct pay equity audit across all departments",
        ]

    def _identify_risks(self, task: Task) -> list[str]:
        return [
            "Burnout indicators in engineering team (High)",
            "Competitive talent market for AI/ML roles (High)",
            "Upcoming labor regulation changes (Medium)",
        ]
