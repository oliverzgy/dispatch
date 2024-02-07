default_incident_priorities = [
    {
        "name": "Low",
        "description": "This incident may require your team's attention during working hours until the incident is stable.",
        "view_order": 1,
        "tactical_report_reminder": 12,
        "executive_report_reminder": 9999,
        "color": "#8bc34a",
        "page_commander": False,
        "default": True,
        "enabled": True,
    },
    {
        "name": "Medium",
        "description": "This incident may require your team's full attention during waking hours, including weekends, until the incident is stable.",
        "view_order": 2,
        "tactical_report_reminder": 6,
        "executive_report_reminder": 12,
        "color": "#ff9800",
        "page_commander": False,
        "default": False,
        "enabled": True,
    },
    {
        "name": "High",
        "description": "This incident may require your team's full attention 24x7, and should be prioritized over all other work, until the incident is stable.",
        "view_order": 3,
        "tactical_report_reminder": 2,
        "executive_report_reminder": 6,
        "color": "#e53935",
        "page_commander": False,
        "default": False,
        "enabled": True,
    },
]
