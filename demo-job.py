import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
#from awsglue.transforms import Relationalize

# Begin variables to customize with your information
glue_source_database = "demo"
glue_source_table = "SRC_BKT"
glue_temp_storage = "s3://DST_BKT/temp"
glue_repartitioned_parquet_output_s3_path = "s3://DST_BKT/out"
dfc_root_table_name = "root" #default value is "roottable"
# End variables to customize with your information

# Initialize
#glueContext = GlueContext(spark.sparkContext)
glueContext = GlueContext(SparkContext.getOrCreate())
## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Transformation - relationalize (and orc)
datasource0 = glueContext.create_dynamic_frame.from_catalog(database = glue_source_database, table_name = glue_source_table, transformation_ctx = "datasource0")
dfc = Relationalize.apply(frame = datasource0, staging_path = glue_temp_storage, name = dfc_root_table_name, transformation_ctx = "dfc")
mydata = dfc.select(dfc_root_table_name)

# Repartition and to parquet
dailyData = mydata.repartition(1)
parquetoutput = glueContext.write_dynamic_frame.from_options(frame = dailyData, connection_type = "s3", connection_options = {"path": glue_repartitioned_parquet_output_s3_path}, format = "parquet", transformation_ctx = "parquetoutput")

# Close
job.commit()
