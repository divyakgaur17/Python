import boto3

def lambda_handler(event, context):
    
    ec2_client = boto3.client('ec2')
    response = ec2_client.describe_volumes()

    gp2_volumes = [volume for volume in response['Volumes'] if volume['VolumeType'] == 'gp2']

    for volume in gp2_volumes:
        print(f"Volume ID: {volume['VolumeId']}")
        print(f"Volume Type: {volume['VolumeType']}")
        print(f"Size: {volume['Size']} GB")
        print(f"Availability Zone: {volume['AvailabilityZone']}")
        print("------------------------------")