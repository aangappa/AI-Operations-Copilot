def get_cpu_metrics():
    """
    Returns the current CPU utilization of the database server.
    """
    return """
Database CPU: 99%
Memory: 72%
Disk IO: Normal
"""


def get_recent_changes():
    """
    Returns recent infrastructure or application changes.
    """
    return """
Database Patch deployed 30 minutes before incident.
"""


def search_knowledge():
    """
    Searches the enterprise knowledge base for known incidents.
    """

    return """
Known Issue:
FordPass outage after database patch.

Resolution:
Restart Authentication Service.
Clear API Cache.
Health Check completed successfully.
"""