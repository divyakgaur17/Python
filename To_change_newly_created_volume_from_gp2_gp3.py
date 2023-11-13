import boto3

def extract_volume_id(volume_arn):
    volume_id = volume_arn.split('/')[-1]
    return volume_id

def lambda_handler(event, context):
    
    volume_arn = event['resources'][0]
    volume_id = extract_volume_id(volume_arn)
    
    ec2_client = boto3.client('ec2')
    
    response = ec2_client.describe_volumes(
        VolumeIds=[volume_id]
    )
    volume_type = response['Volumes'][0]['VolumeType']
    if "gp2" in volume_type:
        print(f"You Have Old Volume Type: {volume_type}.\n Changing to gp3!!!")
        response = ec2_client.modify_volume(
            VolumeId=volume_id,
            VolumeType='gp3'
        )
    else:
        print(f"You already have Latest VolumeType: {volume_type}.")