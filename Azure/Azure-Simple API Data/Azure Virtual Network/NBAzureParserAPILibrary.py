import json
from NBAzureAPILibrary import *

class NBAzureParserAPILib: 

    # return resource nbPathSchema
    def GetResourceType(self, retrieve_data_params):
        nb_node = retrieve_data_params['params']
        return nb_node['nbPathSchema']

    def GetResourceData(self, retrieve_data_params, api_param):

        schema = self.GetResourceType(retrieve_data_params)        

        if schema == "Azure.Subscription.children.ResourceGroup.children.VirtualNetwork.children.VirtualNetworkDistributedRouter":
            if not api_param or "dataType" not in api_param:
                return self.GetVNet(retrieve_data_params)
            elif api_param["dataType"] == "vnet_peerings":
                return self.GetVNetPeerings(retrieve_data_params)
        elif schema == "Azure.Subscription.children.ResourceGroup.children.LoadBalancer"
            if ...

    # Region: APIs for Virtual Network
    def GetVNet(self, retrieve_data_params):
        nb_vnet_router = retrieve_data_params['params']
        vnet_id = nb_vnet_router['vNetId']
        
        # get vnet
        vnet = NBAzureAPILibrary.GetResourceDataByAPI(
            api_server_id=params['apiServerId'],
            azure_resource_uri=vnet_id
        )

        return json.dumps(vnet, indent=4)

    def GetVNetPeerings(self, retrieve_data_params):
        vnet = json.load(self.GetVNet(retrieve_data_params))

        # get vnet peerings
        result = []
        peerings = vnet['virtualNetworkPeerings'] 
        for peering_id in peerings:
            info = NBAzureAPILibrary.GetResourceDataByAPI(
                api_server_id=params['apiServerId'],
                azure_resource_uri=peering_id
            )
            result.append(info)

        return json.dumps(result, indent=4)        
    # End Region