'''
Utility functions for preprocessing outputs in the MCP tool for the AI agent.
'''

import json
from toon import encode

def json_output(output):
    '''
    This function converts the output to a JSON string with a content type declaration.
    '''
    return json.dumps({
        "content_type": "application/json",
        "content": output
    }, indent=2)

def toon_output(output):
    '''
    This function convert the output in toon format optimizes LLM token consumption
    '''
    return encode(output)