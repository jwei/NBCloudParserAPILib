# No-code - Webserver Generate this code as Parser Script

'''
Begin Declare Input Parameters
[
]
End Declare

For sample
[
    {"name": "$param1"},
    {"name": "$param2"}
]
'''


def BuildParameters(context, device_name, params):
    response = GetDeviceProperties(
        context,
        device_name,
        {
            'techName': 'Microsoft Azure',
            'paramType': 'SDN',
            'params': ['*']
        }
    )
    return response


def RetrieveData(params):       
    DATA_TYPE = "vnet_peerings"

    result = NBAzureParserAPIlib.GetResourceData(  # Cloud Parser Lib Built-in
        retrieve_data_params=params,        
        api_param={
            "dataType": DATA_TYPE
        }
    )

    return result



    