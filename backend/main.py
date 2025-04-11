from fastapi import FastAPI
from agent_manager import AgentManager

app = FastAPI()
agent_manager = AgentManager()

@app.get("/task/{task_type}")
def handle(task_type: str, q: str):
    """
    API endpoint to handle tasks by delegating them to the appropriate agent.

    Args:
        task_type (str): The type of task to handle (e.g., 'write', 'code', 'image').
        q (str): The input query or prompt for the task.

    Returns:
        dict: The result of the task handled by the agent.
    """
    return {"result": agent_manager.handle_task(task_type, q)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
