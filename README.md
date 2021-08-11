#Workshop Flow

1. Setup
  1. git clone https://github.com/bhorev/glue-demo.git
  1. sed -i "s/uniqueid/<YOUR-LOGIN>/g" glue-demo/setup.sh
  1. chmod +x glue-demo/setup.sh
  1. ./glue-demo/setup.sh
1. Create demo database (please call it demo)
1. Crawl source bucket and create table in Glue catalog
1. Change partition name to week
1. Configure and run Glue job (with bookmarks)
1. Crawl destination bucket out folder (not the whole bucket)
1. Athena query
1. QuickSight dashboard
1. Add a folder in source bucket and run the job (with bookmarks)
