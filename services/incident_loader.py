import json

from models.incident import Incident


def load_incident():

    with open("data/incident.json", "r") as file:

        data = json.load(file)

    return Incident(
        shortdescription=data["shortdescription"],
        number=data["number"],
        application=data["application"],
        priority=data["priority"],
        impact=data["impact"],
        cpu=data["cpu"],
        change=data["change"]
    )