import csv
import logging
from resourcegraph import run_azure_rg_query_for_resources
from data_class import AzureResource
from setup_logging import setup_logging

def convert_list_csv(resources: list[AzureResource], filename: str = "azure_resources.csv"):
	"""
	This function converts a list of AzureResource objects into a CSV file. Each object in the list is written as a row in the CSV file, with the attributes of the AzureResource class as columns.


	Parameters:
	resources (list[AzureResource]):
	A list of AzureResource objects to be written to the CSV file.


	filename (str, optional):
	The name of the output CSV file. Defaults to "azure_resources.csv"
	"""
	logger = logging.getLogger(__name__)  # Get the logger for this module
	with open(filename, mode="w", newline="", encoding="utf-8") as f:
		writer = csv.writer(f)
		writer.writerow([field.name for field in AzureResource.__dataclass_fields__.values()])
		for r in resources:
			writer.writerow([
				r.subscriptionId, r.name, r.type, r.rgName, r.location,
				r.applicationName, r.environment, r.rgApplicationName, r.rgEnvironment
			])
	logger.info(f"Complete resource list written to {filename}....")

def main():
	"""
	To test the script
	:return:
	"""
	setup_logging()  # Initialize logging
	logger = logging.getLogger(__name__)  # Get the logger for this module
	all_resources = run_azure_rg_query_for_resources()
	convert_list_csv(all_resources, "azure_resources.csv")


if __name__ == "__main__":
	main()