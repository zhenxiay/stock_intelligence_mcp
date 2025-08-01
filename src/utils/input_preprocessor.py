def preprocess_rsi_input(input) -> int:
    '''
    Preprocess the RSI input value to ensure it is an integer.
    '''
    if isinstance(input, str):
        # Extract digits from the string
        import re
        match = re.search(r'\d+', input)
        if match:
            return int(match.group())
        else:
            raise ValueError(f"No integer found in input: {input}")
    elif isinstance(input, int):
        return input
    else:
        raise TypeError(f"Expected a string or integer, got {type(input)} instead.")