import boto3

def dynamodb():
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    table = dynamodb.Table('users')
    response = table.get_item(
        Key={
            'username': 'janedoe',
            'last_name': 'Doe'
        }
    )
    item = response['Item']
    print(item)
    return item


def func(x):
    print x
    return x + 1

def test_func():
    assert func(3) == 4

def test_aws():
    assert dynamodb() != None

