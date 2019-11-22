import boto3


client = boto3.client('elasticache')


def handler(event, context):
    response = client.describe_service_updates(
        ServiceUpdateStatus=['available'],
    )
    for info in response['ServiceUpdates']:
        name = info['ServiceUpdateName']
        print()
        print(f'Service update available: { name }')
        apply_updates(name)


def apply_updates(name):
    response = client.describe_update_actions(
        ServiceUpdateName=name,
        UpdateActionStatus=['not-applied', 'stopped'],
    )
    group_ids = [
        item['ReplicationGroupId'] for item in response['UpdateActions']
    ]
    if not group_ids:
        print('All replication groups are up-to-date.')
        return
    print(f'Applying to replication groups: { ", ".join(group_ids) }')
    client.batch_apply_update_action(
        ServiceUpdateName=name,
        ReplicationGroupIds=group_ids,
    )
