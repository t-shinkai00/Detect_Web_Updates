import boto3

def readS3():
  # バケット名,オブジェクト名
  BUCKET_NAME = 'old-elem-labwiki'
  OBJECT_KEY_NAME = 'old_elem.txt'

  s3 = boto3.resource('s3')

  bucket = s3.Bucket(BUCKET_NAME)
  obj = bucket.Object(OBJECT_KEY_NAME)

  response = obj.get()
  body = response['Body'].read()

  return body.decode('utf-8')