#!/bin/bash
export JSON_EXAMPLES=te_jsons_examples
export SRC_BUCKET_NAME=uniqueid-glue-120821-src
export DST_BUCKET_NAME=uniqueid-glue-120821-dst

unzip $JSON_EXAMPLES.zip
mv $JSON_EXAMPLES 32
unzip $JSON_EXAMPLES.zip
mv $JSON_EXAMPLES 33

aws s3 mb s3://$SRC_BUCKET_NAME
aws s3 sync ./ s3://$SRC_BUCKET_NAME/ --exclude "*" --include "*.te_json"

aws s3 mb s3://$DST_BUCKET_NAME
aws s3api put-object --bucket $DST_BUCKET_NAME --key temp/
aws s3api put-object --bucket $DST_BUCKET_NAME --key out/

sed -i "s/SRC_BKT/$SRC_BUCKET_NAME/g" glue-demo/demo-job.py
sed -i "s/DST_BKT/$DST_BUCKET_NAME/g" glue-demo/demo-job.py
aws s3 cp glue-demo/demo-job.py s3://$DST_BUCKET_NAME/demo-job.py
