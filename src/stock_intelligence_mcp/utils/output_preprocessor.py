'''
Utility functions for preprocessing outputs in the MCP tool for the AI agent.
'''

import json

def json_output(output):
    '''
    This function converts the output to a JSON string with a content type declaration.
    '''
    return json.dumps({
        "content_type": "application/json",
        "content": output
    }, indent=2)
    