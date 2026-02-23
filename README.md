# Frontier AI Test
[PySys](https://pysys-test.github.io/pysys-test/) project for testing various Frontier AI models, currently those supported by OpenAI and Anthropic.

## Project Structure
The broad project layout is as defined below;
```
frontier-ai-test/
├── README.md
├── pysysproject.xml       # pysys project file
├── src
│   └── utils
│       └── docker.py      # utils for running docker as tool
└── test
    ├── models
    │   ├── anthropic      # tests using anthropic models e.g. claude-opus
    │   └── openai         # tests using openai models e.g. chatGPT
    └── utils
        └── docker         # tests for the docker tools
```
