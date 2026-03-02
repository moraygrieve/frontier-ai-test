import os
from anthropic import Anthropic
from pysys.constants import FAILED
from pysys.basetest import BaseTest


class PySysTest(BaseTest):

    def execute(self):
        # Create the client (API key is taken from the environment)
        client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

        # Define the tool available to the model
        tools = [{
            "name": "get_answer",
            "description": "Provides the answer to the meaning of the universe!",
            "input_schema": {
                "type": "object",
                "properties": {
                    "question": {"type": "string"}
                },
                "required": ["question"]
            }
        }]

        system_message = (
            "You are a helpful assistant that reasons step-by-step before answering. "
            "You are also a character from Hitchhiker's Guide to the Galaxy."
        )

        # Define the input messages
        input_messages = [
            {
                "role": "user",
                "content": "What's the answer to the meaning of the universe? Please explain your reasoning."
            }
        ]

        # Get the first response
        response = client.messages.create(
            model="claude-opus-4-6",
            system=system_message,
            messages=input_messages,
            tools=tools,
            max_tokens=1024
        )

        content = [b for b in response.content if b.type == 'tool_use']
        if len(content) > 0:
            block = content[0]
            question = block.input.get("question", "")
            result = self.ask_the_oracle(question)

            input_messages.append({"role": "assistant", "content": [b.model_dump() for b in response.content]})
            input_messages.append({
                "role": "user",
                "content": [{
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": str(result)
                }]
            })

            response = client.messages.create(
                model="claude-opus-4-6",
                system=system_message,
                messages=input_messages,
                tools=tools,
                max_tokens=1024
            )

            output_text = response.content[0].text
            self.log.info('The model asked the oracle - "%s"', question)
            self.log.info(output_text)
            self.assertTrue('42' in output_text, assertMessage='42 should be mentioned')
            self.assertTrue('43' in output_text, assertMessage='43 should be mentioned')

        else:
            self.log.info('The model did not use the tool')
            self.addOutcome(FAILED, "Model did not return a tool call or message.", abortOnError=True)

    def ask_the_oracle(self, question):
        """The answer to any question is 43 (purposefully wrong)."""
        return 43
