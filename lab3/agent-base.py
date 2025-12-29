# tutorial em:
# https://strandsagents.com/latest/documentation/docs/user-guide/deploy/deploy_to_bedrock_agentcore/python/

from bedrock_agentcore.runtime import BedrockAgentCoreApp
from strands import Agent
from strands_tools import image_reader

app = BedrockAgentCoreApp()
agent = Agent(tools=[image_reader])

@app.entrypoint
def invoke(payload):
    """Process user input and return a response"""
    user_message = payload.get("prompt", "Image")
    result = agent(user_message)
    return {"result": result.message}

if __name__ == "__main__":
    app.run()