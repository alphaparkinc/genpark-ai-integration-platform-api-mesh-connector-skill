class AiIntegrationPlatformApiMeshConnectorClient:
    def connect_systems(self, source_system, target_system='hubspot', data_schema=None):
        data_schema = data_schema or {}
        mapping = [
            {'source_field': 'email', 'target_field': 'contact.email', 'transform': 'lowercase'},
            {'source_field': 'company', 'target_field': 'company.name', 'transform': 'titlecase'},
            {'source_field': 'arr', 'target_field': 'deal.amount_usd', 'transform': 'currency_parse'}
        ]
        return {
            'connection_id': 'conn-' + source_system[:4] + '-' + target_system[:4] + '-7821',
            'status': 'ACTIVE',
            'field_mappings': mapping,
            'sync_frequency': 'real_time',
            'records_synced_last_24h': 4821
        }
