#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
import os
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.transforms import *
from awsglue.dynamicframe import DynamicFrame
glueContext = GlueContext(SparkContext.getOrCreate())


# In[2]:


glue_source_database = "demo"
glue_source_table = "xhorev_out"
datasource1 = glueContext.create_dynamic_frame.from_catalog(database = glue_source_database, table_name = glue_source_table, transformation_ctx = "datasource1")


# In[3]:


datasource1.count()
datasource1.printSchema()


# In[4]:


df = datasource1.toDF()
df.createOrReplaceTempView("docs")
sqlDF = glueContext.sql("SELECT severity, count(severity) FROM docs GROUP BY severity")
sqlDF.show()


# In[5]:


datasource0 = glueContext.create_dynamic_frame.from_options(connection_type="parquet", connection_options={ "paths": ["s3://xhorev-glue-120821-dst/out"]})


# In[6]:


datasource0.count()


# In[7]:


df0 = datasource0.toDF()
df0.createOrReplaceTempView("docs0")
sqlDF0 = glueContext.sql("SELECT severity, count(severity) FROM docs0 GROUP BY severity")
sqlDF0.show()


# In[ ]:




