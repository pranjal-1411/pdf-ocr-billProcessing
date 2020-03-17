
import os 
from dotenv import load_dotenv
load_dotenv()
from attachment_processor.attachment_helper import processAttachment 
import boto3

botName = os.getenv('BOT_NAME')
botAlias = os.getenv('BOT_ALIAS')
intentName = os.getenv('INTENT_NAME')

def receiveMessage( message ):
    
    #json format of message to be followed 
    ''' {
            # {
        #     sender:{
        #         id:
        #         name:
        #     }
        #     message:{
        #         text:" "
        #         attachment:{
        #             type: "image/file"
        #             url: // for downlaoding    
        #         }
        #     }
        # }
    } 
    '''
    
    sender_id = message['sender']['id']
    response = None
    if message.get('attachment'):
        downloadUrl = message['attachment']['url']
        fileType = message['attachment']['type']
        data = processAttachment( downloadUrl, fileType  )
        response = sendSlotValuesToLex( data , sender_id , intentName ) 
    
    elif message.get('text'):
        response = sendTextToLex( message['text'],sender_id )
        
def sendTextToLex( message , sender_id  ):
    
    #request and response syntax
    '''  {
            # response = client.post_text(
            #     botName='string',
            #     botAlias='string',
            #     userId='string',
            #     sessionAttributes={
            #         'string': 'string'
            #     },
            #     requestAttributes={
            #         'string': 'string'
            #     },
            #     inputText='string'
            # )
        }
    '''
    #response syntax   
    '''      {
                'intentName': 'string',
                'slots': {
                    'string': 'string'
                },
                'sessionAttributes': {
                    'string': 'string'
                },
                'message': 'string',
                'sentimentResponse': {
                    'sentimentLabel': 'string',
                    'sentimentScore': 'string'
                },
                'messageFormat': 'PlainText'|'CustomPayload'|'SSML'|'Composite',
                'dialogState': 'ElicitIntent'|'ConfirmIntent'|'ElicitSlot'|'Fulfilled'|'ReadyForFulfillment'|'Failed',
                'slotToElicit': 'string',
                'responseCard': {
                    'version': 'string',
                    'contentType': 'application/vnd.amazonaws.card.generic',
                    'genericAttachments': [
                        {
                            'title': 'string',
                            'subTitle': 'string',
                            'attachmentLinkUrl': 'string',
                            'imageUrl': 'string',
                            'buttons': [
                                {
                                    'text': 'string',
                                    'value': 'string'
                                },
                            ]
                        },
                    ]
                },
                'sessionId': 'string'
            }
    '''
    client = boto3.client('lex-runtime')
    response = client.post_text(
        botName= botName ,
        botAlias= botAlias,
        userId=sender_id,
        sessionAttributes={},
        requestAttributes={},
        inputText=message
    )
    return response

def sendSlotValuesToLex( data , sender_id ):
    
    slotValue = { 'receipt':'success' }
    
    if data.get('amount'): slotValue['amount']=data['amount']['value']
    if data.get('category'): slotValue['category'] = data['category']
    if data.get('date') : slotValue['date'] = data['date']
    
    client = boto3.client('lex-runtime')
    
    get_session_response = { 'recentIntentSummaryView':[] }
    try:
        get_session_response = client.get_session(
        botName= botName ,
        botAlias= botAlias ,
        userId= sender_id 
        #checkpointLabelFilter='string'
        )
        temp = []
        for recentIntent in get_session_response['recentIntentSummaryView']:
            if recentIntent['intentName']!=intentName: 
                temp.append(recentIntent)
            else:
                for key,value in recentIntent['slots'].items():
                    if value is not None:  slotValue[key] = value
                
        get_session_response['recentIntentSummaryView'] = temp     
    except Exception as e:
        print(e)
         
    client = boto3.client('lex-runtime')
    response = client.put_session(
        botName=botName,
        botAlias=botAlias,
        userId= sender_id ,
        sessionAttributes={},
        dialogAction={
            'type': 'Delegate',
            'intentName': intentName ,
            'slots': slotValue
        },
        recentIntentSummaryView= get_session_response.get('recentIntentSummaryView') 
    ) 
    print(response)
    
    
    
    
     
if __name__ == "__main__":
    #sendSlotValuesToLex({'category':'Food'},'1234567')    

   
    
    