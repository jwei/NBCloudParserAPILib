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
import json
import datetime

def BuildParameters(context, device_name, params):
    response = GetDeviceProperties(
        context,
        device_name,
        {
            'techName': 'Google Cloud',
            'paramType': 'SDN',
            'params': ['*']
        }
    )
    return response


def RetrieveData(params):
    FUNC_NAME = "describe_transit_gateway_route_tables"
    FILTER_KEYS = ["transit-gateway-id"]
    CUSTOMIZED_FUNC_MAPPING = {}
    result = ParserAPIlib.getAWSSingleAPIdata(
        retrieve_data_params=params,
        api_param={
                    "func_name": FUNC_NAME,
                    "filter_keys": FILTER_KEYS,
                    "customized_func_mapping": CUSTOMIZED_FUNC_MAPPING
                  }  
    )

    return result



    