import ollama
from pysys.basetest import BaseTest


class PySysTest(BaseTest):

    def execute(self):
        # Prepare messages
        input_messages = [
            {"role": "system", "content": "You are a character from Hitchhiker's Guide to the Galaxy."},
            {"role": "user", "content": "What's the answer to the meaning of the universe? Just give the number as an integer, no other characters."}
        ]
        response = ollama.chat(
            model="llama3.1:8b",
            messages=input_messages,
            options={"num_predict": 10}
        )

        # Log out the response
        answer = response.message.content
        self.log.info('The answer to the universe is %s', answer)

        # Assert that the response is correct
        self.assertTrue(int(answer) == 42, assertMessage="Assert the answer is correct")



