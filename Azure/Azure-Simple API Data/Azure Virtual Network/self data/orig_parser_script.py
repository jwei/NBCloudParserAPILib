'''
Begin Declare Input Parameters
[
]
End Declare
'''
 
def BuildParameters(context, device_name, params):
    response = GetDeviceProperties(
        context,
        device_name,
        {'techName': 'Microsoft Azure', 'paramType': 'SDN', 'params': ['*']}
    )
    return response
 
 
def RetrieveData(params):   
    # Note that the VNet Router (Virtual Network Distributed Router) is generated from Azure Virtual Network.
    # The purpose is to represent vnet's networking entity.
    # The VNet's resource URI is saved in the "vNetId" data field of the VNet Router.
    nb_vnet_router = params['params']
    vnet_id = nb_vnet_router['vNetId']
    
    # get vnet
    vnet = NBAzureAPILibrary.GetResourceDataByAPI(
        api_server_id=params['apiServerId'],
        azure_resource_uri=vnet_id
    )

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