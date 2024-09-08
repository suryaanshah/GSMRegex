# GSMRegex
This scrapes GSMArena and similar sites to search for phones and/or models and also returns the regex format of the models if prompted.

Limitation:
- It can only generate specific regex for now.
- Too many requests can make the website inaccessible.


## How to use

### Install dependencies

```
pip install requests beautifulsoup4

```

### Run using:
```
python gsmregex.py [-h] [--url URL] [--model MODEL]
```
options:
```
  -h, --help     show this help message and exit
  --url URL      GSMArena phone model URL to extract models from
  --model MODEL  Phone model name to search on GSMArena and extract models from
```

Example usage: 

![gsmregex](https://github.com/user-attachments/assets/53f4456e-965d-4ba5-9fc6-89236c3033ba)
