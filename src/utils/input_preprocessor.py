
'''
Utility functions for preprocessing inputs in the MCP tool.
'''

import re

def preprocess_rsi_input(input) -> int:
    '''
    Preprocess the RSI input value to ensure it is an integer.
    '''
    try:
        if isinstance(input, str):
           # Extract digits from the string
            match = re.search(r'\d+', input)
            if match:
                return int(match.group())
        elif isinstance(input, int):
            return input
            
        print("Input is not an integer. Set input to default value 14...")
        
        return 14
        
    except ValueError as e:
        print(f"ValueError: {e}")
    except Exception as e:
        print(f"A non ValueError occured: {e}")
