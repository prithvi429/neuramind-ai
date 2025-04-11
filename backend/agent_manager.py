# Agent Manager: Handles the coordination between different agents.

from agents.writing_agent import WritingAgent
from agents.coding_agent import CodingAgent
from agents.finance_agent import FinanceAgent
from agents.mapping_agent import MappingAgent
from agents.image_agent import ImageAgent
from agents.voice_agent import VoiceAgent

class AgentManager:
    def __init__(self):
        self.writing = WritingAgent()
        self.coding = CodingAgent()
        self.finance = FinanceAgent()
        self.mapping = MappingAgent()
        self.image = ImageAgent()
        self.voice = VoiceAgent()

    def handle_task(self, task_type, user_input):
        """
        Handles tasks by delegating them to the appropriate agent.

        Args:
            task_type (str): The type of task to handle (e.g., 'write', 'code', 'finance', 'map', 'image', 'voice').
            user_input (str): The input data for the task.

        Returns:
            str: The response from the agent.
        """
        if task_type == "write":
            return self.writing.generate_content(user_input)
        elif task_type == "code":
            return self.coding.generate_code(user_input)
        elif task_type == "finance":
            return self.finance.analyze_data(user_input)
        elif task_type == "map":
            return self.mapping.provide_route(user_input)
        elif task_type == "image":
            return self.image.generate_image(user_input)
        elif task_type == "voice":
            return self.voice.transcribe_and_respond(user_input)
        else:
            return "❌ Unknown task type."

if __name__ == "__main__":
    manager = AgentManager()
    print(manager.handle_task("write", "how AI is changing education"))
    print(manager.handle_task("code", "a simple to-do app in React"))
    print(manager.handle_task("image", "a futuristic city at night"))
