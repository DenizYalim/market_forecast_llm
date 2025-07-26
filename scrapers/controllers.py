
""" Runs scrapers of all sites. Returns String[] that has headlines

Keyword arguments: Currently nothing. 
argument -- description
Return: return_description
"""
def scrape_all():
    pass


""" gpt is asked if based on headlines should an instrument sold, bold or hold.

Keyword arguments:
headlines : string[] -- list of headlines
enstrument : string  -- an enstrument name/ticket

Return: response : String  -- the response of the llm, callerLLM will analyze this and make calls
* Maybe we can also ask if its not worth at all to send to the callerLLM, to save tokens.
"""
def consult_llm():
    pass

""" Response from consulterLLM will be reviewd by caller to make endpoint calls to the binance wrapper.

Keyword arguments:
response : String  -- Analyze from response

Return: return_description
"""
def caller_llm():
    pass