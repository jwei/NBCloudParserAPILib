# No-code - Webserver Generate this code as Parser Script

'''
Begin Declare Input Parameters
 [
    {"name": "$intf_name"}
 ]
End Declare

For sample
[
    {"name": "$param1"},
    {"name": "$param2"}
]
'''

import json
import datetime

def BuildParameters(context, device_name, params):
    intf_name = params['intf_name']

    response = GetDeviceProperties(context, device_name, {'techName': 'Amazon AWS', 'paramType': 'SDN', 'params': ['*']})
    dev = response['params']

    res_intf = GetInterfaceProperties(context, device_name, intf_name, {'techName': 'Amazon AWS', 'paramType': 'SDN', 'params': ['*']})
    dev.update(res_intf['params'])
    return response

def RetrieveData(params):
    FUNC_NAME = "describe_transit_gateway_route_tables",
    KEY1 = "connectionId",
    KEY2 = "virtualInterfaceId"

    result = ParserAPIlib.getAWSSingleAPIdata(
        retrieve_data_params=params,
        api_param={
                    "func_name": FUNC_NAME,
                    KEY1: '$VALUE1',
                    KEY1: '$VALUE2'
                  }
    )

    return result