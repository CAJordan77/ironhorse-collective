"""
Pre-built demo workflows for the Corporate Agent Hierarchy.
Each function is a self-contained scenario you can run.
"""

from ceo import CEOAgent
from task import Priority


def demo_quarterly_planning():
    """Quarterly planning cycle: CEO sets OKRs and tasks each department."""
    print("\n" + "#" * 70)
    print("  DEMO: Quarterly Planning Cycle")
    print("#" * 70)

    ceo = CEOAgent("Victoria Sterling")
    ceo.hire_full_team()

    ceo.issue_strategic_directive(
        "Focus Q3 on: 1) Revenue growth to $5M ARR, 2) APAC expansion, "
        "3) Zero-trust security implementation, 4) Reduce churn to <1%"
    )

    ceo.assign_task(
        "Develop Q3 revenue forecast and pipeline strategy",
        "Create detailed revenue forecast with pipeline analysis",
        "Sales & Marketing",
        Priority.HIGH,
    )
    ceo.assign_task(
        "Prepare APAC market entry feasibility study",
        "Analyze regulatory, competitive, and partnership landscape for APAC",
        "Strategy & Planning",
        Priority.HIGH,
    )
    ceo.assign_task(
        "Create zero-trust security implementation roadmap",
        "Design phased zero-trust architecture rollout plan",
        "Information Security",
        Priority.HIGH,
    )
    ceo.assign_task(
        "Develop customer retention improvement program",
        "Design proactive churn prevention and expansion program",
        "Customer Service",
        Priority.HIGH,
    )
    ceo.assign_task(
        "Model Q3 budget with APAC expansion costs",
        "Update financial model with new market entry costs",
        "Finance & Accounting",
        Priority.MEDIUM,
    )
    ceo.assign_task(
        "Plan engineering hiring for Q3 growth",
        "Define roles, sourcing strategy, and interview process",
        "Agent (Human) Resources",
        Priority.MEDIUM,
    )
    ceo.assign_task(
        "Assess technical requirements for APAC deployment",
        "Evaluate infrastructure needs for new region",
        "Research & Development",
        Priority.MEDIUM,
    )

    ceo.print_dashboard()
    return ceo


def demo_security_incident():
    """Security incident response: CEO coordinates cross-department response."""
    print("\n" + "#" * 70)
    print("  DEMO: Security Incident Response")
    print("#" * 70)

    ceo = CEOAgent("Victoria Sterling")
    ceo.hire_full_team()

    ceo.issue_strategic_directive(
        "PRIORITY ALERT: Potential data breach detected. All departments "
        "to assess impact and report within 2 hours."
    )

    ceo.assign_task(
        "Security incident investigation and containment",
        "Investigate potential breach, contain threat, assess scope",
        "Information Security",
        Priority.CRITICAL,
    )
    ceo.assign_task(
        "Assess financial impact and insurance implications",
        "Calculate potential financial exposure and notify insurers",
        "Finance & Accounting",
        Priority.HIGH,
    )
    ceo.assign_task(
        "Prepare customer communication and support response",
        "Draft customer notifications and prepare support team",
        "Customer Service",
        Priority.HIGH,
    )
    ceo.assign_task(
        "Assess technical systems affected and recovery plan",
        "Identify affected systems and create recovery timeline",
        "Research & Development",
        Priority.HIGH,
    )
    ceo.assign_task(
        "Review regulatory notification requirements",
        "Determine GDPR/SOC2 notification obligations and timeline",
        "Strategy & Planning",
        Priority.HIGH,
    )
    ceo.assign_task(
        "Prepare external communications and PR response",
        "Draft press statement and investor communication",
        "Sales & Marketing",
        Priority.MEDIUM,
    )

    ceo.print_dashboard()
    return ceo


def demo_product_launch():
    """Product launch: Cross-department coordination for new product."""
    print("\n" + "#" * 70)
    print("  DEMO: New Product Launch Coordination")
    print("#" * 70)

    ceo = CEOAgent("Victoria Sterling")
    ceo.hire_full_team()

    ceo.issue_strategic_directive(
        "Launch Project Horizon: New AI-powered analytics product. "
        "Target launch in 90 days. All departments to align."
    )

    # Cross-department task
    ceo.assign_multi_department(
        "Product launch readiness assessment",
        "Assess department readiness for Project Horizon launch",
        [
            "Research & Development",
            "Sales & Marketing",
            "Customer Service",
            "Information Security",
            "Finance & Accounting",
        ],
        Priority.HIGH,
    )

    ceo.assign_task(
        "Develop go-to-market strategy and campaign",
        "Create launch campaign, pricing, and sales enablement",
        "Sales & Marketing",
        Priority.HIGH,
    )
    ceo.assign_task(
        "Complete product development and QA testing",
        "Finalize feature set, complete testing, prepare for GA",
        "Research & Development",
        Priority.CRITICAL,
    )
    ceo.assign_task(
        "Security review and penetration testing",
        "Complete security assessment before public launch",
        "Information Security",
        Priority.CRITICAL,
    )
    ceo.assign_task(
        "Prepare support documentation and training",
        "Create knowledge base, train support team, prepare onboarding",
        "Customer Service",
        Priority.HIGH,
    )
    ceo.assign_task(
        "Financial modeling and pricing analysis",
        "Build pricing model, project revenue, analyze unit economics",
        "Finance & Accounting",
        Priority.HIGH,
    )
    ceo.assign_task(
        "Hire additional support and sales staff",
        "Recruit 5 support agents and 3 sales reps for launch",
        "Agent (Human) Resources",
        Priority.MEDIUM,
    )

    ceo.print_dashboard()
    return ceo


def demo_board_meeting():
    """Full board meeting with all department reports."""
    print("\n" + "#" * 70)
    print("  DEMO: Quarterly Board Meeting")
    print("#" * 70)

    ceo = CEOAgent("Victoria Sterling")
    ceo.hire_full_team()

    # Generate some reports first
    ceo.assign_task(
        "Quarterly security audit and compliance review",
        "Complete Q2 security audit and compliance assessment",
        "Information Security",
    )
    ceo.assign_task(
        "Q2 revenue and pipeline report",
        "Compile revenue results and pipeline analysis for Q2",
        "Sales & Marketing",
    )
    ceo.assign_task(
        "Product development progress report",
        "Report on product roadmap progress and technical milestones",
        "Research & Development",
    )
    ceo.assign_task(
        "Employee satisfaction and hiring update",
        "Present Q2 HR metrics and hiring progress",
        "Agent (Human) Resources",
    )
    ceo.assign_task(
        "Q2 financial statements and forecast",
        "Present financial results and updated forecast",
        "Finance & Accounting",
    )
    ceo.assign_task(
        "Customer satisfaction and retention report",
        "Present NPS, churn, and customer health metrics",
        "Customer Service",
    )
    ceo.assign_task(
        "Strategic initiatives progress report",
        "Update on partnerships, market entry, and OKRs",
        "Strategy & Planning",
    )

    # Now conduct the board meeting
    ceo.conduct_board_meeting([
        "Q2 Financial Results",
        "Product Development Update",
        "Security and Compliance",
        "Customer Metrics",
        "Strategic Initiatives",
        "Q3 Planning",
    ])

    return ceo


def demo_custom():
    """Interactive custom scenario."""
    print("\n" + "#" * 70)
    print("  CUSTOM SCENARIO MODE")
    print("#" * 70)

    ceo = CEOAgent("Victoria Sterling")
    ceo.hire_full_team()

    ceo.issue_strategic_directive(
        "Company pivot: Shifting focus to enterprise customers. "
        "All departments to assess impact and create transition plans."
    )

    ceo.assign_task(
        "Develop enterprise sales strategy and pricing",
        "Create enterprise-tier pricing and sales playbook",
        "Sales & Marketing",
        Priority.CRITICAL,
    )
    ceo.assign_task(
        "Assess product gaps for enterprise requirements",
        "Identify features needed for enterprise segment",
        "Research & Development",
        Priority.CRITICAL,
    )
    ceo.assign_task(
        "Enterprise security and compliance requirements",
        "Map enterprise security requirements and compliance needs",
        "Information Security",
        Priority.HIGH,
    )
    ceo.assign_task(
        "Financial impact analysis of enterprise pivot",
        "Model revenue impact, costs, and timeline for pivot",
        "Finance & Accounting",
        Priority.HIGH,
    )
    ceo.assign_task(
        "Hire enterprise sales and solutions engineering team",
        "Recruit 8 enterprise sales reps and 4 solutions engineers",
        "Agent (Human) Resources",
        Priority.HIGH,
    )
    ceo.assign_task(
        "Design enterprise customer success program",
        "Create enterprise onboarding and success framework",
        "Customer Service",
        Priority.HIGH,
    )
    ceo.assign_task(
        "Competitive analysis of enterprise market",
        "Analyze enterprise competitors and positioning strategy",
        "Strategy & Planning",
        Priority.MEDIUM,
    )

    ceo.print_dashboard()
    return ceo


DEMO_WORKFLOWS = {
    "quarterly_planning": demo_quarterly_planning,
    "security_incident": demo_security_incident,
    "product_launch": demo_product_launch,
    "board_meeting": demo_board_meeting,
    "custom": demo_custom,
}
