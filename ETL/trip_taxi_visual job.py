import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.gluetypes import *
from awsglue import DynamicFrame

def _find_null_fields(ctx, schema, path, output, nullStringSet, nullIntegerSet, frame):
    if isinstance(schema, StructType):
        for field in schema:
            new_path = path + "." if path != "" else path
            output = _find_null_fields(ctx, field.dataType, new_path + field.name, output, nullStringSet, nullIntegerSet, frame)
    elif isinstance(schema, ArrayType):
        if isinstance(schema.elementType, StructType):
            output = _find_null_fields(ctx, schema.elementType, path, output, nullStringSet, nullIntegerSet, frame)
    elif isinstance(schema, NullType):
        output.append(path)
    else:
        x, distinct_set = frame.toDF(), set()
        for i in x.select(path).distinct().collect():
            distinct_ = i[path.split('.')[-1]]
            if isinstance(distinct_, list):
                distinct_set |= set([item.strip() if isinstance(item, str) else item for item in distinct_])
            elif isinstance(distinct_, str) :
                distinct_set.add(distinct_.strip())
            else:
                distinct_set.add(distinct_)
        if isinstance(schema, StringType):
            if distinct_set.issubset(nullStringSet):
                output.append(path)
        elif isinstance(schema, IntegerType) or isinstance(schema, LongType) or isinstance(schema, DoubleType):
            if distinct_set.issubset(nullIntegerSet):
                output.append(path)
    return output

def drop_nulls(glueContext, frame, nullStringSet, nullIntegerSet, transformation_ctx) -> DynamicFrame:
    nullColumns = _find_null_fields(frame.glue_ctx, frame.schema(), "", [], nullStringSet, nullIntegerSet, frame)
    return DropFields.apply(frame=frame, paths=nullColumns, transformation_ctx=transformation_ctx)

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node Amazon S3
AmazonS3_node1726782071020 = glueContext.create_dynamic_frame.from_catalog(database="triptaxis", table_name="proyect_taxi", transformation_ctx="AmazonS3_node1726782071020")

# Script generated for node Change Schema
ChangeSchema_node1726782086467 = ApplyMapping.apply(frame=AmazonS3_node1726782071020, mappings=[("vendorid", "int", "vendorid", "int"), ("tpep_pickup_datetime", "timestamp", "tpep_pickup_datetime", "timestamp"), ("tpep_dropoff_datetime", "timestamp", "tpep_dropoff_datetime", "timestamp"), ("trip_distance", "double", "trip_distance", "double"), ("pulocationid", "int", "pulocationid", "int"), ("dolocationid", "int", "dolocationid", "int"), ("payment_type", "long", "payment_type", "long"), ("fare_amount", "double", "fare_amount", "double")], transformation_ctx="ChangeSchema_node1726782086467")

# Script generated for node Drop Null Fields
DropNullFields_node1726782176035 = drop_nulls(glueContext, frame=ChangeSchema_node1726782086467, nullStringSet={"null"}, nullIntegerSet={}, transformation_ctx="DropNullFields_node1726782176035")

# Script generated for node Amazon Redshift
AmazonRedshift_node1726782190251 = glueContext.write_dynamic_frame.from_options(frame=DropNullFields_node1726782176035, connection_type="redshift", connection_options={"redshiftTmpDir": "s3://aws-glue-assets-084828606692-us-east-1/temporary/", "useConnectionProperties": "true", "dbtable": "public.trip_taxis_01", "connectionName": "Redshift connection", "preactions": "CREATE TABLE IF NOT EXISTS public.trip_taxis_01 (vendorid INTEGER, tpep_pickup_datetime TIMESTAMP, tpep_dropoff_datetime TIMESTAMP, trip_distance DOUBLE PRECISION, pulocationid INTEGER, dolocationid INTEGER, payment_type BIGINT, fare_amount DOUBLE PRECISION);"}, transformation_ctx="AmazonRedshift_node1726782190251")

job.commit()