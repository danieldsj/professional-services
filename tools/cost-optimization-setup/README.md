# Cost Optimization Setup
This tool was designed to export information from your organization to BigQuery to identify opportunities for cost optimization.

## Prerequisites
This tool is designed to be executed in the Cloud Shell.

## Usage
### Basic
Do the following:
1. Clone the professional services repository 
```
git clone https://github.com/danieldsj/professional-services.git
```
2. Change directory to the cost optimization setup directory:
```
cd professional-services/tools/cost-optimization-setup
```
3. Run the cost optimization setup command:
```
./cost-optimization-setup
```
### Advanced
If you would not like to be prompted interactively, set the following environment variables:
- `BILLING_ACCOUNT_ID` - The billing account ID.
- `ORGANIZATION_ID` - The organization ID used to export assets information.
- `BIGQUERY_PROJECT_ID` - The project ID for the project that contains BigQuery and will contain the exported data.
- `BIGQUERY_DATASET` - The dataset name for the dataset in the project matching

You can set these enviroment variables in-line.  Here is an example:
```
$ BILLING_ACCOUNT_ID=123456789 ./cost-optimization-setup
```

You can set these environment variables in advance or running the command.  Here is an example:
```
$ export BILLING_ACCOUNT_ID=123456789
$ ./cost-optimization-setup
```

You can also set the environment variables in a file called `settings.sh`.  A `settings.sh.sample` has been provided for convenience. 
