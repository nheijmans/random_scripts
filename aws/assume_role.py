def get_temp_keys(acc):
    assume_acc  = "the_other_acc_to_assume_role (arn)"
    assume_role = "the_role_to_assume (name)"
    rootacc="arn:aws:iam::{0}/{1}".format(assume_acc, assume_role)
    stsclient = boto3.client('sts')
    assumed_role_obj = stsclient.assume_role(RoleArn=rootacc,RoleSessionName="temp_role")
    credentials = assumed_role_obj['Credentials']

    return credentials
