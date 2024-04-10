# Todo - implementation in globalpython
#   add new .py to new global python file:
#       * global_python_scripts/netbrain/techspec/cloud_data_retrieve/parser_api_lib.py (new)
#       * global_python_scripts/netbrain/techspec/cloud_data_retrieve/nb_azure_API_library.py (existing)

# tech_spec.py

import json

class NBGCPParserAPILib: 

# solution 1
    def getApiNbData(self, retrieve_data_params, metric_type):
        if metric_type["metrics"] == "loadbalancing.googleapis.com/https/total_latencies": 
            return retrieve_data_params['params']['nbProperties']['forwardingRules'][0].split("/")[-1]
        elif metric_type["metrics"] == "loadbalancing.googleapis.com/https/backend_rule_hits": 
            return retrieve_data_params['params']['backendRule']['name']

    def getGCPMetrics(self, retrieve_data_params, metric_type, api_param): # , extra_param):
        if metric_type["metrics"] == "loadbalancing.googleapis.com/https/total_latencies": 
            api_param['filter']['resource.labels.forwarding_rule_name'] = self.getApiNbData(retrieve_data_params, metric_type)
        elif metric_type["metrics"] == "loadbalancing.googleapis.com/https/backend_rule_hits": 
            api_param['filter']['resource.labels.backend_rule_name'] = self.getApiNbData(retrieve_data_params, metric_type)

        # Get Live Data
        data = NBGCPAPILibrary.GetMonitorMetrics(
            api_server_id=retrieve_data_params['apiServerId'],
            proj_id=retrieve_data_params['projId'],
            url_params=api_param
        )
        return json.dumps(data, indent=4, default=str)

# # solution 2     

#     def buildMetricsParam(self, retrieve_data_params, metric_type, api_param):
#         nb_node = retrieve_data_params['nb_node']

#         if nb_node['nbPathSchema'] == "GCP.xxx.Loadbalancer":
#             if metric_type == "loadbalancing.googleapis.com/https/total_latencies":
#                 api_param['filter']['resource.labels.forwarding_rule_name'] = nb_node['nbProperties']['forwardingRules'][0].split("/")[-1]


#     def getGCPMetrics(self, retrieve_data_params, metric_type, api_param): # , extra_param):
#         self.buildMetricsParam(retrieve_data_params, metric_type, api_param)
        
#         # Get Live Data
#         data = NBGCPAPILibrary.GetMonitorMetrics(
#             api_server_id=retrieve_data_params['apiServerId'],
#             proj_id=retrieve_data_params['projId'],
#             url_params=api_param
#         )
#         return json.dumps(data, indent=4, default=str) 