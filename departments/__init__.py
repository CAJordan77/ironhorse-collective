"""
Department agents for the Corporate Agent Hierarchy.
"""

from departments.info_security import InfoSecurityAgent
from departments.sales_marketing import SalesMarketingAgent
from departments.research_development import ResearchDevelopmentAgent
from departments.human_resources import HumanResourcesAgent
from departments.finance_accounting import FinanceAccountingAgent
from departments.customer_service import CustomerServiceAgent
from departments.strategy_planning import StrategyPlanningAgent

__all__ = [
    "InfoSecurityAgent",
    "SalesMarketingAgent",
    "ResearchDevelopmentAgent",
    "HumanResourcesAgent",
    "FinanceAccountingAgent",
    "CustomerServiceAgent",
    "StrategyPlanningAgent",
]

# Registry mapping department names to agent classes
DEPARTMENT_REGISTRY = {
    "Information Security": InfoSecurityAgent,
    "Sales & Marketing": SalesMarketingAgent,
    "Research & Development": ResearchDevelopmentAgent,
    "Agent (Human) Resources": HumanResourcesAgent,
    "Finance & Accounting": FinanceAccountingAgent,
    "Customer Service": CustomerServiceAgent,
    "Strategy & Planning": StrategyPlanningAgent,
}
