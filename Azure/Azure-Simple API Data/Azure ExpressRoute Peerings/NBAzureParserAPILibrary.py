import json
from NBAzureAPILibrary import *

class NBAzureParserAPILib: 

    def GetMetrics(self, retrieve_data_params, api_param):
        # Get Live Data
        data = NBAzureAPILibrary.GetMonitorMetrics(
            api_server_id=retrieve_data_params['apiServerId'],
            azure_resource_uri=retrieve_data_params['params']['id'],
            params=api_param
        )
        return json.dumps(data, indent=4, default=str)