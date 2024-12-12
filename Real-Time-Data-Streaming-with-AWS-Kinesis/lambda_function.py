import base64
import json

import boto3
import datetime

def lambda_handler(event, context):
    # Receive a batch of events from kinesis and add to dynamodb
    try:
        dynamo_db = boto3.resource('dynamodb')
        table = dynamo_db.Table('customer-data')

        for record in event["Records"]:
            decoded_data = base64.b64decode(record["kinesis"]["data"]).decode("utf-8")
            print(decoded_data)
            print(json.loads(decoded_data))
            decoded_data_dic = json.loads(decoded_data)
            with table.batch_writer() as batch_writer:
                batch_writer.put_item(Item=decoded_data_dic)
    except Exception as e:
        print(str(e))
