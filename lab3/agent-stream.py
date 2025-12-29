from bedrock_agentcore.runtime import BedrockAgentCoreApp
from strands import Agent

app = BedrockAgentCoreApp()
agent = Agent()

@app.entrypoint
def invoke(payload):
    """
    Accepts Anthropic-style multimodal messages
    and forwards them to the Strands agent
    """

    # Option A — formato Anthropic messages[]
    if "messages" in payload:
        user_input = payload["messages"]
    else:
        # fallback legacy format
        user_input = payload.get("prompt", "")

    result = agent(user_input)

    return {"result": result.message}

if __name__ == "__main__":
    app.run()
