# Cost Optimization Setup
This tool was designed to export information from your organization to BigQuery to identify opportunities for cost optimization.

## Prerequisites
### Environment
This tool is designed to be executed in the Cloud Shell.

### Permissions
This tool requires the following permissions:
- Billing Account Administrator Role [to enable billing data export](https://cloud.google.com/billing/docs/how-to/export-data-bigquery#required_permissions).
- BigQuery User role for the Cloud project that contains the BigQuery dataset [that will be used to store the Cloud Billing data](https://cloud.google.com/billing/docs/how-to/export-data-bigquery#required_permissions).
- Cloud Asset Viewer (roles/cloudasset.viewer), which grants [read-only access to cloud asset metadata](https://cloud.google.com/asset-inventory/docs/access-control#roles) at the organization level.

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
The script uses the following environment variables:
- `BILLING_ACCOUNT_ID` - The billing account ID.
- `ORGANIZATION_ID` - The organization ID used to export assets information.
- `BIGQUERY_PROJECT_ID` - The project ID for the project that contains BigQuery and will contain the exported data.
- `BIGQUERY_DATASET` - The dataset name for the dataset in the project matching

You can set these enviroment variables in-line.  Here is an example:
```
$ BILLING_ACCOUNT_ID=123456789 ./cost-optimization-setup
```

You can set these environment variables prior to running the command.  Here is an example:
```
$ export BILLING_ACCOUNT_ID=123456789
$ ./cost-optimization-setup
```

You can also set the environment variables in a file called `settings.sh`.  A `settings.sh.sample` has been provided for convenience. 
