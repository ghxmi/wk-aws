def lambda_handler(event, context):
	name = event.get('name', 'Guest')  # Default to 'Guest' if no name is provided
	return {
		'statusCode': 200,
		'body': f'Hello, {name}!'  # Personalized greeting
	}



import json

def lambda_s3(event, context):
	print("Received event:", json.dumps(event, indent=2))

	for record in event.get('Records', []):
		bucket_name = record['s3']['bucket']['name']
		file_key = record['s3']['object']['key']
		print(f"File {file_key} was uploaded to {bucket_name}")

	return {
		"statusCode": 200,
		"body": json.dumps({"message": "S3 event processed successfully!"})
	}