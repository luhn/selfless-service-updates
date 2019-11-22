import boto3


client = boto3.Client('elasticache')


def handler(event, context):
    response = client.describe_service_updates(
        ServiceUpdateStatus=['available'],
    )
    for info in response['ServiceUpdates']:
        apply_updates(info['ServiceUpdateName'])


def apply_updates(name):
    response = client.describe_update_actions(
        ServiceUpdateName=name,
        UpdateActionStatus=['not-applied', 'stopped'],
    )
    group_ids = [
        item['ReplicationGroupId'] for item in response['UpdateActions']
    ]
    client.batch_apply_update_action(
        ServiceUpdateName=name,
        ReplicationGroupIds=group_ids,
    )
