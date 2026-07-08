from services.knowledge_service import get_knowledge
from services.tool_service import (
    get_cpu_metrics,
    get_recent_changes
)

def build_context(incident):

    knowledge = get_knowledge(incident)

    metrics = get_cpu_metrics()

    changes = get_recent_changes()

    

    return {
        "knowledge": knowledge,
        "metrics": metrics,
        "changes": changes
    }