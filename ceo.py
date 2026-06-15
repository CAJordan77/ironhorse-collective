"""
CEO Agent — Top-level orchestrator for the Corporate Agent Hierarchy.

The CEO assigns tasks to department agents, collects reports,
provides strategic direction, and synthesizes cross-department insights.
"""

from typing import Optional
from base_agent import BaseAgent
from task import Task, Report, TaskStatus, ReportStatus, Priority, BoardMeeting
from departments import DEPARTMENT_REGISTRY


class CEOAgent(BaseAgent):
    """Chief Executive Officer — orchestrates all department agents."""

    def __init__(self, name: str = "Victoria Sterling"):
        super().__init__(name, "CEO", "Executive")
        self.team: dict[str, BaseAgent] = {}
        self.board_meetings: list[BoardMeeting] = []
        self.strategic_directives: list[str] = []
        self._task_counter = 0

    def hire_department(self, department_name: str, agent_name: str | None = None):
        """Hire a department agent by department name."""
        if department_name not in DEPARTMENT_REGISTRY:
            available = ", ".join(DEPARTMENT_REGISTRY.keys())
            raise ValueError(
                f"Unknown department: {department_name}. Available: {available}"
            )
        agent_class = DEPARTMENT_REGISTRY[department_name]
        agent = agent_class(agent_name) if agent_name else agent_class()
        self.team[department_name] = agent
        print(f"  [CEO] Hired {agent.title} {agent.name} for {department_name}")
        return agent

    def hire_full_team(self):
        """Hire all department agents with default names."""
        for dept_name in DEPARTMENT_REGISTRY:
            self.hire_department(dept_name)

    def get_responsibilities(self) -> list[str]:
        return [
            "Corporate vision and strategic direction",
            "Board and investor relations",
            "Cross-department coordination",
            "Major decision approval",
            "Company culture and values",
            "External partnerships and PR",
            "M&A and corporate development",
            "Executive team management",
        ]

    def process_task(self, task: Task) -> Report:
        """CEO processes a task by delegating to the appropriate department."""
        if task.assigned_to in self.team:
            agent = self.team[task.assigned_to]
            agent.receive_task(task)
            return agent.process_task(task)
        raise ValueError(f"No agent assigned to department: {task.assigned_to}")

    def assign_task(
        self,
        title: str,
        description: str,
        department: str,
        priority: Priority = Priority.MEDIUM,
        due_date: str | None = None,
    ) -> tuple[Task, Report]:
        """Assign a task to a department and get the report back."""
        self._task_counter += 1
        task = Task(
            id=f"T-{self._task_counter:03d}",
            title=title,
            description=description,
            assigned_to=department,
            assigned_by=f"CEO {self.name}",
            priority=priority,
            due_date=due_date,
        )
        print(f"\n[CEO] Assigning task {task.id} to {department}: {title}")
        report = self.process_task(task)
        self.reports.append(report)
        return task, report

    def assign_multi_department(
        self,
        title: str,
        description: str,
        departments: list[str],
        priority: Priority = Priority.MEDIUM,
    ) -> list[tuple[Task, Report]]:
        """Assign the same task to multiple departments."""
        results = []
        for dept in departments:
            task, report = self.assign_task(title, description, dept, priority)
            results.append((task, report))
        return results

    def issue_strategic_directive(self, directive: str):
        """Issue a company-wide strategic directive."""
        self.strategic_directives.append(directive)
        print(f"\n[CEO] STRATEGIC DIRECTIVE: {directive}")
        print(f"  -> Distributed to all {len(self.team)} department heads")

    def conduct_board_meeting(self, agenda_items: list[str]) -> BoardMeeting:
        """Conduct a board meeting with reports from all departments."""
        print("\n" + "=" * 70)
        print(f"  BOARD MEETING — Chaired by CEO {self.name}")
        print("=" * 70)

        all_reports = []
        for dept_name, agent in self.team.items():
            dept_reports = [r for r in agent.reports if r.status == ReportStatus.SUBMITTED]
            all_reports.extend(dept_reports)
            print(f"\n  --- {dept_name} ({agent.title} {agent.name}) ---")
            if dept_reports:
                latest = dept_reports[-1]
                print(f"  Latest Report: {latest.title}")
                print(f"  Key Metrics: {latest.metrics}")
                if latest.risks:
                    print(f"  Top Risk: {latest.risks[0]}")
            else:
                print("  No reports submitted yet.")

        meeting = BoardMeeting(
            title="Quarterly Board Meeting",
            presenter=f"CEO {self.name}",
            summary=f"Reviewed {len(all_reports)} department reports",
            decisions=[
                "Approved Q3 budget allocation",
                "Authorized APAC market entry initiative",
                "Approved headcount increase for engineering",
            ],
            action_items=[
                "CISO: Complete zero-trust architecture plan by month end",
                "CMO: Finalize APAC go-to-market strategy",
                "CTO: Deliver technical debt reduction roadmap",
                "CFO: Prepare Series C investor materials",
            ],
        )
        self.board_meetings.append(meeting)

        print(f"\n  DECISIONS:")
        for d in meeting.decisions:
            print(f"    [APPROVED] {d}")
        print(f"\n  ACTION ITEMS:")
        for a in meeting.action_items:
            print(f"    [ACTION] {a}")
        print("=" * 70)

        return meeting

    def get_company_dashboard(self) -> dict:
        """Get a full company status dashboard."""
        dashboard = {
            "ceo": self.name,
            "total_departments": len(self.team),
            "strategic_directives": len(self.strategic_directives),
            "board_meetings_held": len(self.board_meetings),
            "departments": {},
        }
        for dept_name, agent in self.team.items():
            dashboard["departments"][dept_name] = agent.get_status()
        return dashboard

    def print_dashboard(self):
        """Print a formatted company dashboard."""
        dash = self.get_company_dashboard()
        print("\n" + "=" * 60)
        print(f"  COMPANY DASHBOARD — CEO: {dash['ceo']}")
        print("=" * 60)
        print(f"  Departments: {dash['total_departments']}")
        print(f"  Strategic Directives: {dash['strategic_directives']}")
        print(f"  Board Meetings Held: {dash['board_meetings_held']}")
        print()
        for dept, status in dash["departments"].items():
            print(f"  [{dept}]")
            print(f"    Head: {status['title']} {status['name']}")
            print(f"    Active Tasks: {status['active_tasks']}")
            print(f"    Completed: {status['completed_tasks']}")
            print(f"    Reports: {status['reports_submitted']}")
        print("=" * 60)
