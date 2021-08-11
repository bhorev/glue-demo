# Flow

* Setup
    * git clone https://github.com/bhorev/glue-demo.git
    * sed -i "s/uniqueid/<YOUR-LOGIN>/g" glue-demo/setup.sh
    * chmod +x glue-demo/setup.sh
    * ./glue-demo/setup.sh
* Create demo database (please call it "demo")
* Crawl source bucket and create table in Glue catalog
* Change partition name to "week"
* Configure and run Glue job (with bookmarks)
* Crawl destination bucket out folder (not the whole bucket)
* Athena query
* QuickSight dashboard
* Add a folder in source bucket and run the job (with bookmarks)
