import re
'''
Utility functions for preprocessing inputs in the MCP tool.
'''

def preprocess_rsi_input(input) -> int:
    '''
    Preprocess the RSI input value to ensure it is an integer.
    '''
    if isinstance(input, str):
        # Extract digits from the string
        match = re.search(r'\d+', input)
        if match:
            return int(match.group())
        else:
            raise ValueError(f"No integer found in input: {input}")
    elif isinstance(input, int):
        return input
    