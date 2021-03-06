# Flow

* **Storage Setup**
    * `git clone https://github.com/bhorev/glue-demo.git`
    * Replace _YOUR-LOGIN_: `sed -i "s/uniqueid/YOUR-LOGIN/g" glue-demo/setup.sh`
    * Zip is in current directory. Note zip name is referenced from setup.sh
    * `chmod +x glue-demo/setup.sh`
    * `./glue-demo/setup.sh`
* **Glue Data Catalog Setup (source)**
   * Create demo database (please call it "demo")
   * Crawl source bucket and create table in Glue catalog
   * Change partition name to "week"
* **ETL Batch Job Setup**
   * Configure Glue job
       * Fix _glue_source_table_ in job script from hyphens to underscores
   * Make sure IAM role has permissions on both source and destination buckets
   * Run Glue job (with bookmarks)
   * Crawl destination bucket out folder (not the whole bucket)
* **Running (repeatable)**
   * Athena query
       * Note: Before you run your first query, you need to set up a query result location in Amazon S3
   * QuickSight dashboard
   * Add a folder in source bucket and re-run the job (with bookmarks), and in Athena - load partitions

## Misc. Commands
* Run job: `aws glue start-job-run --job-name myjob --arguments {\"--job-bookmark-option\":\"job-bookmark-enable\"}`
* Reset job bookmark: `aws glue reset-job-bookmark --job-name myjob`

See also: https://github.com/aws-samples/aws-glue-samples
