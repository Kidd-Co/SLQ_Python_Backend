import boto3

rds = boto3.client('rds',
                    region_name = 'us-east-2',
                    aws_access_key_id='AKIA5K3OVVSU7PIF27WW',
                    aws_secret_access_key='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',
)

response = rds.start_db_instance(DBInstanceIdentifier='test-db-instance')
