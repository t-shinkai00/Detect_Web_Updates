import boto3

# バケット名,オブジェクト名
BUCKET_NAME = 'old-elem-labwiki'
OBJECT_KEY_NAME = 'old_elem.txt'
s3 = boto3.resource('s3')

bucket = s3.Bucket(BUCKET_NAME)
obj = bucket.Object(OBJECT_KEY_NAME)

def readS3():
  response = obj.get()
  body = response['Body'].read()
  return body.decode('utf-8')

def writeS3(input):
  data=input.encode("utf-8")
  obj.put(Body=bytearray(data))  # データを書き込む

# print(readS3())
# writeS3("hello world")
# print(readS3())