#!/usr/bin/python

import boto3

def main():
    profile = 'yourprofilename'
    session = boto3.session.Session(profile_name=profile)
    client = session.client('ec2', region_name='us-east-1')
    ec2_regions = [region['RegionName'] for region in client.describe_regions()['Regions']]
    
    for region in ec2_regions:
        conn = session.resource('ec2', region_name=region)
        instances = conn.instances.filter()
        for instance in instances:
            if instance.state['Name'] == 'running':
                print (instance.id, instance.public_ip_address, instance.instance_type, region)
    return

main()
