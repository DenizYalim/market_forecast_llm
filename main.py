from datetime import datetime, timedelta

def flow(cur_date, data, ticker=None):
    """
    Keyword arguments:
    arguments -- cur_date:str, data:dict, ticker:str = None,
    Return: response:json
    """
    pass


def get_data(date:str, ticker=None):
    """returns data for a given date and ticker

    Keyword arguments:
    argument -- date:str, ticker:str = None
    Return: data:json
    """

    return {"headlines": ["Apple releases new product", "Market hits all-time high"]}

def backtest(start_date:str, end_date:str, ticker=None):
    start_date_dt = datetime.strptime(start_date, "%Y-%m-%d")
    end_date_dt = datetime.strptime(end_date, "%Y-%m-%d")

    current_date = start_date_dt

    results = []

    while current_date <= end_date_dt:
        date_str = current_date.strftime("%Y-%m-%d")
        data = get_data(date_str, ticker)

        results.append(flow(date_str, data, ticker))

        current_date += timedelta(days=1)
    
    return results

if __name__ == "__main__":
    print("Hello, World!")
