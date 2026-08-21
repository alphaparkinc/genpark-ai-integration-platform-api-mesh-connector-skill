from client import AiIntegrationPlatformApiMeshConnectorClient

def main():
    client = AiIntegrationPlatformApiMeshConnectorClient()
    res = client.connect_systems('salesforce', 'hubspot')
    print('Connection: ' + res['connection_id'] + ' | Status: ' + res['status'])
    print('Sync: ' + res['sync_frequency'] + ' | Records/24h: ' + str(res['records_synced_last_24h']))
    print('Field Mappings:')
    for m in res['field_mappings']:
        print('  ' + m['source_field'] + ' -> ' + m['target_field'] + ' [' + m['transform'] + ']')

if __name__ == '__main__':
    main()
