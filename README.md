# azure-pull-all-resource-details
Python automation to pull all resource data and convert it as a csv

# Features

* Extracts details of Azure resources.
* Converts the resource data into a CSV file for easy analysis.
* Supports automation workflows using GitHub Actions.

# Prerequisites
* 
* Python 3.11 or higher.
* Required Python packages (install using poetry install).
* Azure credentials for accessing resource details.

# Installation

* Clone the repository:

`
git clone https://github.com/githubofkrishnadhas/azure-pull-all-resource-details.git
`

* `cd azure-pull-all-resource-details`

* Install dependencies:

```bash
poetry install
```

## Usage

```python
    poetry run python convert_csv.py
```


# Dependabot Configuration

Automates dependency updates for Python packages with the following settings:

* Updates scheduled monthly.
* Pull requests assigned to githubofkrishnadhas.
* Target branch: main.
