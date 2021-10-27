import boto3

rds = boto3.client('rds',
                    region_name = 'us-east-2',
                    aws_access_key_id='',
                    aws_secret_access_key='',
)

response = rds.stop_db_instance(DBInstanceIdentifier='test-db-instance')
