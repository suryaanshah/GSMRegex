#!/bin/bash

# Algo
"""
1. search the website and show suggestions
2. if not found
    prompt user to search again
3. if found
    ask user to select
4. display model info if any 
5. displa model info in regex
"""

content=$(curl -L google.com)

