import logging
from azure.identity import DefaultAzureCredential
import azure.mgmt.resourcegraph as arg
from azure.mgmt.resourcegraph.models import QueryRequest
from setup_logging import setup_logging
from dotenv import load_dotenv
from data_class import AzureResource

def run_azure_rg_query_for_resources():
    """
    Run a resource graph query to get all the resources in azure
    """
    logger = logging.getLogger(__name__)
    credential = DefaultAzureCredential()
    # Create Azure Resource Graph client and set options
    arg_client = arg.ResourceGraphClient(credential)
    all_resources = []

    query = f"""
        resources
        | extend applicationName = tostring(tags['ApplicationName'])
        | extend environment = tostring(tags['Environment'])
        | join kind=leftouter (
            resourcecontainers
            | where type == 'microsoft.resources/subscriptions/resourcegroups'
            | extend rgApplicationName = tostring(tags['ApplicationName'])
            | extend rgEnvironment = tostring(tags['Environment'])
            | project subscriptionId, resourceGroup, rgApplicationName, rgEnvironment
        ) on subscriptionId, resourceGroup
        | project-rename rgName = resourceGroup
        | project
            subscriptionId,
            name,
            type,
            rgName,
            location,
            applicationName,
            environment,
            rgApplicationName,
            rgEnvironment
    """

    logger.info(f"query is {query}")
    skip_token = None
    page_size = 100  # number of records per page

    while True:
        logger.info(f"Executing query with skip_token: {skip_token}")
        request = QueryRequest(
            query=query,
            options={
                "top": page_size,
                "skipToken": skip_token
            }
        )

        response = arg_client.resources(request)

        all_resources.extend(response.data)
        logger.info(f"Fetched {len(response.data)} resources from Azure....")

        # Check for the next skip token to determine if there are more records
        skip_token = response.skip_token
        if not skip_token:
            logger.info("No more pages to fetch. Ending loop.")
            break  # No more pages, so we can exit the loop

    logger.info(f"Total resources fetched: {len(all_resources)}")
    # return all_resources
    structured_resources = [AzureResource(**dict(resource)) for resource in all_resources]
    return structured_resources


def main():
    """
    To test the script
    :return:
    """
    load_dotenv()
    setup_logging()  # Initialize logging
    logger = logging.getLogger(__name__)  # Get the logger for this module

    logger.info("ARG query being prepared......")
    run_azure_rg_query_for_resources()
    logger.info("ARG query Completed......")


if __name__ == "__main__":
    main()

