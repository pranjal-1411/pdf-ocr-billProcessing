import json

def lambda_handler(event, context):
    # TODO implement
    # print(event)
    name = event['currentIntent']['slots']['Name']
    return {
        'statusCode': 200,
        'body': json.dumps({  
    "dialogAction": {
        "type": "Close",
        "fulfillmentState": "Fulfilled",
        "message": {
            "contentType": "PlainText",
            "content": "Fuck you bitch"
        }
    }
}
            )
    }
