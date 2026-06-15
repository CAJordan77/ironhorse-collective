"""
Information Security Department Agent.
Handles: security audits, threat assessment, incident response,
         policy enforcement, compliance, data protection.
"""

from base_agent import BaseAgent
from task import Task, Report, TaskStatus, ReportStatus, Priority
from datetime import datetime


class InfoSecurityAgent(BaseAgent):
    def __init__(self, name: str = "Morgan Chen"):
        super().__init__(name, "CISO", "Information Security")

    def get_responsibilities(self) -> list[str]:
        return [
            "Security audits and penetration testing",
            "Threat detection and incident response",
            "Security policy development and enforcement",
            "Regulatory compliance (GDPR, SOC2, HIPAA)",
            "Data protection and encryption standards",
            "Employee security awareness training",
            "Vendor security assessments",
            "Disaster recovery and business continuity planning",
        ]

    def process_task(self, task: Task) -> Report:
        task.status = TaskStatus.IN_PROGRESS
        print(f"  [CISO] Processing: {task.title}")

        # Simulate domain-specific processing
        content = self._analyze_security_task(task)
        task.status = TaskStatus.COMPLETED

        report = Report(
            id=f"SEC-{task.id}",
            title=f"Security Report: {task.title}",
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

    def _analyze_security_task(self, task: Task) -> str:
        analyses = {
            "audit": (
                f"Comprehensive security audit completed for: {task.title}. "
                "Reviewed access controls, network segmentation, encryption at rest "
                "and in transit, and endpoint protection. Identified areas of "
                "improvement and confirmed compliance with industry standards."
            ),
            "incident": (
                f"Incident response analysis for: {task.title}. "
                "Contained the threat within the target SLA. Root cause analysis "
                "completed. Implemented additional monitoring rules to prevent "
                "recurrence. All affected systems have been remediated."
            ),
            "compliance": (
                f"Compliance review for: {task.title}. "
                "Mapped current controls against regulatory requirements. "
                "Documentation updated. Gap analysis completed with remediation "
                "timeline. Ready for external audit."
            ),
        }
        task_lower = task.title.lower()
        for key, analysis in analyses.items():
            if key in task_lower:
                return analysis
        return (
            f"Security assessment completed for: {task.title}. "
            "All security controls reviewed and validated. "
            "No critical vulnerabilities detected."
        )

    def _generate_metrics(self, task: Task) -> dict:
        return {
            "vulnerabilities_found": 3,
            "vulnerabilities_resolved": 3,
            "compliance_score": "94%",
            "mean_time_to_detect": "2.3 hours",
            "mean_time_to_respond": "45 minutes",
            "security_incidents_30d": 1,
            "phishing_test_pass_rate": "87%",
        }

    def _generate_recommendations(self, task: Task) -> list[str]:
        return [
            "Implement zero-trust network architecture by Q3",
            "Upgrade SIEM solution for better threat correlation",
            "Conduct quarterly red team exercises",
            "Enforce MFA on all privileged accounts",
        ]

    def _identify_risks(self, task: Task) -> list[str]:
        return [
            "Legacy systems running end-of-life software (Medium)",
            "Third-party vendor access not fully audited (Low)",
            "Insider threat detection capabilities need enhancement (Medium)",
        ]
