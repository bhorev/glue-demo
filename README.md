# Flow

* **Storage Setup**
    * git clone https://github.com/bhorev/glue-demo.git
    * sed -i "s/uniqueid/<YOUR-LOGIN>/g" glue-demo/setup.sh
    * Rename zip referenced from setup.sh (if needed)
    * chmod +x glue-demo/setup.sh
    * ./glue-demo/setup.sh
* **Glue Catalog Setup (source)**
   * Create demo database (please call it "demo")
   * Crawl source bucket and create table in Glue catalog
   * Change partition name to "week"
* **ETL Batch Job Setup**
   * Configure and run Glue job (with bookmarks)
   * Crawl destination bucket out folder (not the whole bucket)
* **Running (repeatable)**
   * Athena query
   * QuickSight dashboard
   * Add a folder in source bucket and re-run the job (with bookmarks)
