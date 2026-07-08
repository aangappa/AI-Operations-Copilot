def choose_tools(incident):

    title = incident.shortdescription.lower()

    tools = []

    if "sap" in title:
        tools.extend([
            "cpu",
            "changes",
            "knowledge"
        ])

    elif "vpn" in title:
        tools.append("knowledge")

    else:
        tools.append("knowledge")

    return tools