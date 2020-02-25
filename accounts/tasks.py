import boto3
from botocore.exceptions import ClientError


def send_with_second_api(sender, receiver, message):
	region = "eu-west-1"
	originationNumber = "+1 201-591-1480"
	# The registered keyword associated with the originating short code.
	registeredKeyword = "keyword_123633862529"

	destinationNumber = receiver

	# The content of the SMS message.
	message = message

	# The Amazon Pinpoint project/application ID to use when you send this message.
	# Make sure that the SMS channel is enabled for the project or application
	# that you choose.
	applicationId = "e88bfe9f5cd84aed85d0bcf16b7be707"

	# The type of SMS message that you want to send. If you plan to send
	# time-sensitive content, specify TRANSACTIONAL. If you plan to send
	# marketing-related content, specify PROMOTIONAL.
	messageType = "TRANSACTIONAL"


	senderId = 'VehMail'
	client = boto3.client('pinpoint',
		aws_access_key_id='AKIAI72AYUZZSVZRFSNQ',
		aws_secret_access_key='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',
		region_name=region)
	print('about sending sms')
	try:
	    response = client.send_messages(
	        ApplicationId=applicationId,
	        MessageRequest={
	            'Addresses': {
	                destinationNumber: {
	                    'ChannelType': 'SMS'
	                }
	            },
	            'MessageConfiguration': {
	                'SMSMessage': {
	                    'Body': message,
	                    'MessageType': messageType,
	                    'SenderId': senderId
	                }
	            }
	        }
	    )

	except ClientError as e:
	    print(e.response['Error']['Message'])
	    print(e)
	    return False
	else:
	    print("Message sent! Message ID: "
	            + response['MessageResponse']['Result'][destinationNumber]['MessageId'])
	    return True



def send_sms(sender, receiver, message):
	region = "eu-west-1"
	originationNumber = "+1 201-591-1480"
	# The registered keyword associated with the originating short code.
	registeredKeyword = "keyword_123633862529"

	destinationNumber = receiver

	# The content of the SMS message.
	message = message

	# The Amazon Pinpoint project/application ID to use when you send this message.
	# Make sure that the SMS channel is enabled for the project or application
	# that you choose.
	applicationId = "e88bfe9f5cd84aed85d0bcf16b7be707"

	# The type of SMS message that you want to send. If you plan to send
	# time-sensitive content, specify TRANSACTIONAL. If you plan to send
	# marketing-related content, specify PROMOTIONAL.
	messageType = "TRANSACTIONAL"


	senderId = 'VehMail'
	client = boto3.client('pinpoint',
		aws_access_key_id='AKIAI72AYUZZSVZRFSNQ',
		aws_secret_access_key='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',
		region_name=region)
	print('about sending sms')
	try:
	    response = client.send_messages(
	        ApplicationId=applicationId,
	        MessageRequest={
	            'Addresses': {
	                destinationNumber: {
	                    'ChannelType': 'SMS'
	                }
	            },
	            'MessageConfiguration': {
	                'SMSMessage': {
	                    'Body': message,
	                    'MessageType': messageType,
	                    'SenderId': senderId
	                }
	            }
	        }
	    )

	except ClientError as e:
	    print(e.response['Error']['Message'])
	    print(e)
	    return send_with_second_api(sender, receiver, message)
	else:
	    print("Message sent! Message ID: "
	            + response['MessageResponse']['Result'][destinationNumber]['MessageId'])
	    return True

