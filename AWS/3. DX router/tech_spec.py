# Todo - implementation in globalpython
#   add new .py to new global python file:
#       * global_python_scripts/netbrain/techspec/cloud_data_retrieve/parser_api_lib.py (new)
#       * global_python_scripts/netbrain/techspec/cloud_data_retrieve/nb_azure_API_library.py (existing)

# tech_spec.py

import json

class ParserAPILib:   

    def buildMetricsParam(self, nb_node, api_param):        
        nb_node['func_param'] = api_param
        if nb_node['nbPathSchema'] == "AWS.xxx.Loadbalancer":
            _id = NBAWSAPILibrary.GetResourceIDFromDataModel(nb_node)
            api_param['MetricDataQueries']['MetricStat']['Metric']['Dimensions']['Value'] = _id


    def GetAWSMetrics(self, retrieve_data_params, api_param): # , extra_param):
        nb_node = retrieve_data_params['params']
        self.buildMetricsParam(nb_node, api_param)
        # Get Live Data
        res = NBAWSAPILibrary.GetCloudWatchMetrics(nb_node)
        return json.dumps(res, indent=4, default=str)


    def getAWSSingleAPIdata(self, retrieve_data_params, api_param): # , extra_param):
        nb_node = retrieve_data_params['params']        
        NBAWSAPILibrary.GetResourceData(
                param=nb_node, 
                func_name=api_param['func_name'], 
                filter_keys=api_param['filter_keys'], 
                customized_func_mapping=api_param['customized_func_mapping']
        )   
        return json.dumps(res, indent=4, default=str)


    # DX router
    def getAWSSingleAPIdata(params):
        nb_vif = params['params']
        vif_id = NBAWSAPILibrary.GetResourceIDFromDataModel(nb_vif)
        connection_id = nb_vif['connectionId']

        data = NBAWSAPILibrary.GetResourceData(
                    param=nb_vif,
                    func_name='describe_virtual_interfaces',
                    connectionId=connection_id,
                    virtualInterfaceId=vif_id
        )
        return json.dumps(data, indent=4, default=str)