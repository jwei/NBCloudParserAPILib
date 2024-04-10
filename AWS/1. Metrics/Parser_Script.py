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
            'techName': 'Amazon AWS',
            'paramType': 'SDN',
            'params': ['*']
        }
    )
    return response


def RetrieveData(params):    
    START_TIME = datetime.now(timezone.utc) - timedelta(hours=300)
    END_TIME = datetime.now(timezone.utc) - timedelta(days=3)
    MAX_DATA_POINTS = 20
    ID = "a0"
    PERIOD = 300
    STAT = "Sum"
    NAME_SPACE = "AWS/ApplicationELB"
    METRIC_NAME = "RequestCount"
    NAME = "LoadBalancer"
    
    result = ParserAPIlib.GetAWSMetrics(
        retrieve_data_params=params,
        api_param={
            'StartTime': START_TIME,
            'EndTime': END_TIME,
            'MaxDatapoints': MAX_DATA_POINTS,
            'MetricDataQueries':[
                {
                    'Id': ID,
                    'MetricStat': {
                        'Period': PERIOD,
                        'Stat': STAT,
                        'Metric': {
                            'Namespace':NAME_SPACE,
                            'MetricName':METRIC_NAME,
                            'Dimensions':[
                                {
                                    'Name': NAME,
                                    'Value': '$'
                                }
                            ]
                        }
                    }
                }
            ]
        }
    )

    return result



    