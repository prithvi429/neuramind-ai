from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

class WritingAgent:
    def __init__(self):
        """
        Initializes the WritingAgent with a language model.
        """
        self.llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

    def generate_content(self, prompt):
        """
        Generates creative content based on the provided prompt.

        Args:
            prompt (str): The topic or input for content generation.

        Returns:
            str: The generated content.
        """
        template = PromptTemplate.from_template("Write a creative blog paragraph about: {topic}")
        chain = template | self.llm
        return chain.invoke({"topic": prompt})

if __name__ == "__main__":
    # Example usage
    agent = WritingAgent()
    content = agent.generate_content("Write a short story about AI.")
    print(content)