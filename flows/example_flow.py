from flows.flow_base import _base_flow
from LLM.LLM import example_llm

class example_flow(_base_flow): 
    def run(date, data, ticker=None):
        llm = example_llm()
        prompt = f"Given the data for {date} and ticker {ticker}, analyze the following headlines: {data['headlines']}"

        return llm.work(prompt)