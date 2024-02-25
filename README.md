## Introduction

Python package to implement different GPT-Testing algorithms, currently (v0.0.1) has implemented the MELD algorithm detailed at: https://www.microsoft.com/en-us/research/uploads/prod/2023/03/GPT-4_medical_benchmarks.pdf


## Setup
to setup venv and install packages:

1) To setup venv, in the root of the project run
```
python3 -m venv venv
```

2) Ensure venv is activated (windows)
```
.venv\Scripts\activate
```

3) Create a .env file in the root directory and place the openai API key inside e.g.:
```
OPENAI_API_KEY = "<key_value_here>"
```


4) To install packages
```
python3 -m pip install .
```



## Usage

Once installed the gpt_tester package can be run from the /test/ directory
The example code shows how to run the MELD algorithm over a set of examples
    D, loaded from example.py


