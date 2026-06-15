"""
Ironhorse Collective, LLC — Agents Package
"""

import os
import sys

# Add parent directory to path for imports
_agents_dir = os.path.dirname(os.path.abspath(__file__))
_parent_dir = os.path.dirname(_agents_dir)
if _parent_dir not in sys.path:
    sys.path.insert(0, _parent_dir)

# Import the Data Analytics agent directly
from agents.departments.data_analytics import DataAnalyticsAgent

DEPARTMENT_REGISTRY = {
    "Strategy & Planning": DataAnalyticsAgent,
}

__all__ = ["DEPARTMENT_REGISTRY", "DataAnalyticsAgent"]
