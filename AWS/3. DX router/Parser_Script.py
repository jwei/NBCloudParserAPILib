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
    FUNC_NAME = "describe_virtual_interfaces"
    FILTER_KEYS = []
    CUSTOMIZED_FUNC_MAPPING = {}

    DATA_TYPE = "virtual_interface"

    result = ParserAPIlib.getAWSAggregatedAPIdata(
        retrieve_data_params=params,
        api_param={
                    "func_name": FUNC_NAME,
                    "filter_keys": FILTER_KEYS,
                    "customized_func_mapping": CUSTOMIZED_FUNC_MAPPING
                    "dataType": DATA_TYPE
                  }
    )

    return result