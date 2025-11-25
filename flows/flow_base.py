from LLM.LLM import example_llm

# This should be abstract
class _base_flow: 
    def run(date, data, ticker=None):
        pass
