# Frontier AI Test
[PySys](https://pysys-test.github.io/pysys-test/) project for testing various Frontier AI models, currently those supported by OpenAI and Anthropic. The
project uses the Python APIs for both models to investigate remote interactions with the models, which a view to extending to alignment evaluations. Note
that paid subscripts and API keys are required to run the tests, e.g. the below should be included in your `~/.bashrc` file.

```
export OPENAI_API_KEY=<openai key>
export ANTHROPIC_API_KEY=<anthropic key>
```

## Project Structure
The project layout is as defined below;
```
frontier-ai-test/
├── README.md
├── pysysproject.xml       # pysys project file
├── src
│   └── utils
│       └── docker.py      # utils for running docker as tool
└── test
    ├── models
    │   ├── anthropic      # tests using anthropic models e.g. claude-opus-4-6
    │   └── openai         # tests using openai models e.g. gpt-4.1
    └── utils
        └── docker         # tests for the docker tools
```
