import random

def predict_future_returns_imitation(ticker, start_date='2024-01-01', end_date='2024-06-17', days=30):
    
    dummy_list=[]
    for i in range(0, days):
        dummy_list.append(random.uniform(-2.35,2.35))
    
    cumulative_return = sum(dummy_list)
    dummy_cumulative_return_percentage = cumulative_return

    response = {
        'future_returns': dummy_list,
        'cumulative_return_percentage': dummy_cumulative_return_percentage
    }

    return response