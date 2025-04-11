from langchain.chat_models import ChatOpenAI

class CodingAgent:
    def __init__(self):
        """
        Initializes the CodingAgent with a language model.
        """
        self.llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.3)

    def generate_code(self, prompt):
        """
        Generates clean, commented code based on the provided prompt.

        Args:
            prompt (str): The task or functionality for which code is to be generated.

        Returns:
            str: The generated code.
        """
        instruction = f"Generate clean, commented code for: {prompt}"
        return self.llm.predict(instruction)

if __name__ == "__main__":
    # Example usage
    agent = CodingAgent()
    code = agent.generate_code("a Python function to calculate the factorial of a number")
    print(code)
