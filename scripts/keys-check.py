import boto3
from botocore.exceptions import ClientError, NoCredentialsError

def test_aws_keys(access_key, secret_key, region="us-west-3"):
    try:
        client = boto3.client(
            "sts",
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region
        )
        response = client.get_caller_identity()
        print("Valid AWS keys. User ARN:", response['Arn'])
        return True
    except NoCredentialsError:
        print("No credentials provided.")
        return False
    except ClientError as e:
        print("Invalid AWS keys:", e)
        return False

# Example usage
access_key = "<AWS_ACCESS_KEY>"
secret_key = "<AWS_SECRET_KEY>"
test_aws_keys(access_key, secret_key)