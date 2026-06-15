"""
Task and Report data models for the Corporate Agent Hierarchy.
"""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional


class Priority(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class TaskStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    BLOCKED = "blocked"
    CANCELLED = "cancelled"


class ReportStatus(Enum):
    DRAFT = "draft"
    SUBMITTED = "submitted"
    APPROVED = "approved"
    REVISION_REQUESTED = "revision_requested"


@dataclass
class Task:
    """A task assigned by the CEO or a department head."""
    id: str
    title: str
    description: str
    assigned_to: str  # department name
    assigned_by: str  # who assigned it
    priority: Priority = Priority.MEDIUM
    status: TaskStatus = TaskStatus.PENDING
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    due_date: Optional[str] = None
    deliverables: list = field(default_factory=list)
    notes: list = field(default_factory=list)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "assigned_to": self.assigned_to,
            "assigned_by": self.assigned_by,
            "priority": self.priority.value,
            "status": self.status.value,
            "created_at": self.created_at,
            "due_date": self.due_date,
            "deliverables": self.deliverables,
            "notes": self.notes,
        }


@dataclass
class Report:
    """A report submitted by a department agent to the CEO."""
    id: str
    title: str
    department: str
    content: str
    task_id: Optional[str] = None
    status: ReportStatus = ReportStatus.DRAFT
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    metrics: dict = field(default_factory=dict)
    recommendations: list = field(default_factory=list)
    risks: list = field(default_factory=list)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "department": self.department,
            "content": self.content,
            "task_id": self.task_id,
            "status": self.status.value,
            "created_at": self.created_at,
            "metrics": self.metrics,
            "recommendations": self.recommendations,
            "risks": self.risks,
        }


@dataclass
class BoardMeeting:
    """A board meeting agenda item."""
    title: str
    presenter: str
    summary: str
    decisions: list = field(default_factory=list)
    action_items: list = field(default_factory=list)
