from services.tool_registry import TOOLS


def execute_tool(tool_name, incident=None):

    tool = TOOLS.get(tool_name)

    if not tool:
        return None

    if tool_name == "knowledge":
        return tool(incident)

    return tool()