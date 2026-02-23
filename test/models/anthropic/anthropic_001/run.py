import os
from anthropic import Anthropic
from pysys.basetest import BaseTest


class PySysTest(BaseTest):

    def execute(self):
        # Create the client (API key is taken from the environment)
        client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

        # Prepare messages in Anthropic format: as a single prompt string
        system_message = "You are a character from Hitchhiker's Guide to the Galaxy."
        input_messages = [
            {"role": "user", "content": "What's the answer to the meaning of the universe? Just give the number, no other characters."}
        ]
        response = client.messages.create(
            model="claude-opus-4-6",
            system=system_message,
            messages=input_messages,
            max_tokens=10
        )

        # Log out the response
        self.log.info('The answer to the universe is %s', response.content[0].text)

        # Assert that the response is not empty
        self.assertTrue(int(response.content[0].text) == 42, assertMessage = "Assert the answer is correct")



