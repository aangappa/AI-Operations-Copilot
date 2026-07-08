from services.tool_service import (
    get_cpu_metrics,
    get_recent_changes
)

from services.knowledge_service import get_knowledge

TOOLS = {
    "cpu": get_cpu_metrics,
    "changes": get_recent_changes,
    "knowledge": get_knowledge
}