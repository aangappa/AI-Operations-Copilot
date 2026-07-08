from dataclasses import dataclass

@dataclass
class Incident:
    shortdescription: str
    number: str
    application: str
    priority: str
    impact: str
    cpu: str
    change: str