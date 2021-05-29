import boto3
ddb = boto3.client("dynamodb")

def handler(event, context):
    try:
        data = ddb.put_item(
            TableName="ChineseAnimal",
            Item={
                'BirthYear': {
                    'N': "2010"
                },
                'Animal': {
                    'S': "Pig"
                }
            }
        )
    except BaseException as e:
        print(e)
        raise(e)
    
    return {"message": "Successfully executed"}
