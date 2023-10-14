
## SQL Complex Query
The purpose of this project is to execute a complex SQL query of data stored in Azure Databricks. The following steps are taken:
1. `extract.py` - extracts a dataset from a URL and creates a file path within the repo
2. `transform_load.py` - transforms and loads the dataset into Databricks SQL warehouse
3. `query.py` - performs a complex query on the data

In order to establish a connection to Databricks, the repo stores the necessary Databricks secrets, including ACCESS_TOKEN, HTTP_PATH, and SERVER_HOSTNAME

The following is the complex query that is performed:

![Alt text](query(2).png)



Below is a log of the successful tests


