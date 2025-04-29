from dataclasses import dataclass

@dataclass
class AzureResource:
    subscriptionId: str
    name: str
    type: str
    rgName: str
    location: str
    applicationName: str
    environment: str
    rgApplicationName: str
    rgEnvironment: str


