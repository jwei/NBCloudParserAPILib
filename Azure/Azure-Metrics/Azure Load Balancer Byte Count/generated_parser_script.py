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
    START_TIME = datetime.now(timezone.utc) - timedelta(hours=4)
    END_TIME = datetime.now(timezone.utc)
    METRIC_NAME = "ByteCount"
        
    result = NBAzureParserAPIlib.GetMetrics(  # Cloud Parser Lib Built-in
        retrieve_data_params=params,        
        api_param={
            "metricnames": METRIC_NAME,
            "timespan": START_TIME + '/' + END_TIME
        }
    )

    return result



    