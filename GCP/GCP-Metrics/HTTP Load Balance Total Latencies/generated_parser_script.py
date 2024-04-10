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
            'techName': 'Google Cloud',
            'paramType': 'SDN',
            'params': ['*']
        }
    )
    return response


def RetrieveData(params):    
    START_TIME = datetime.now(timezone.utc) - timedelta(hours=300)
    END_TIME = datetime.now(timezone.utc) - timedelta(days=3)
    
    resource_info = NBGCPParserAPIlib.GetResourceInfoFromDataModel(params)  # Cloud Parser Lib Built-in

    result = NBGCPParserAPIlib.GetMetrics(  # Cloud Parser Lib Built-in
        retrieve_data_params=resource_info,
        metric_type={"metrics": "loadbalancing.googleapis.com/https/total_latencies"}, 
        api_param={
                    "filter": {
                        "metric.type": "loadbalancing.googleapis.com/https/total_latencies",                        
                        "resource.labels.forwarding_rule_name": "$"
                    },
                    # interval is "5 days ago to 3 days ago"
                    "interval.startTime": START_TIME,
                    "interval.endTime": END_TIME
                }   
    )

    return result



    