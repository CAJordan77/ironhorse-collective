"""
Base agent class for all corporate agents.
"""

from abc import ABC, abstractmethod
from typing import Optional
from task import Task, Report


class BaseAgent(ABC):
    """Abstract base class for all corporate agents."""

    def __init__(self, name: str, title: str, department: str):
        self.name = name
        self.title = title
        self.department = department
        self.reports: list[Report] = []
        self.tasks: list[Task] = []

    @abstractmethod
    def get_responsibilities(self) -> list[str]:
        """Return the list of responsibilities for this agent."""
        pass

    @abstractmethod
    def process_task(self, task: Task) -> Report:
        """Process an assigned task and return a report."""
        pass

    def receive_task(self, task: Task):
        """Receive a task assignment."""
        self.tasks.append(task)
        print(f"  [{self.title} {self.name}] received task: {task.title}")

    def get_status(self) -> dict:
        return {
            "name": self.name,
            "title": self.title,
            "department": self.department,
            "active_tasks": len([t for t in self.tasks if t.status.value != "completed"]),
            "completed_tasks": len([t for t in self.tasks if t.status.value == "completed"]),
            "reports_submitted": len(self.reports),
        }

    def __repr__(self):
        return f"{self.title}({self.name})"
