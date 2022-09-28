#! usr/bin env python3

import boto3

ec2 = boto3.client('ec2')

test_response = ec2.describe_vpcs()
vpcId = response.get('Vpcs', [{}]) [0].get('VpcId', '')

#Query for security group id
response = create_securtity_group(GroupName= 'DP_Security_group', Description='DP_test_sg' VPCId=vpcId

security_group_id = test_response['GroupId']
test_data = ec2.authorize_security_group_ingress(Ip_Permissions=[
            {'IpProtocol': 'tcp', 'FromPort': 80', 'ToPort': 80, 'IpRanges':[{CidrIp': '0.0.0.0/0'}]},
            {'IpProtocol': 'tcp', 'FromPort': 22', 'ToPort': 22, 'IpRanges':[{CidrIp': '0.0.0.0/0'}]}
            ])
print('Ingress Succesfully set %s' % test_data)

#Describe security group
#respone = ec2.describe_sercurity_group(GroupIds=[security_group_id])
print(security_group id)
