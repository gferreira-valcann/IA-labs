import os
import base64

from bedrock_agentcore.runtime import BedrockAgentCoreApp
from strands import Agent
from strands_tools import image_reader

SAVE_DIR = "/home/gabriel-valcann/strands/lab3/imgs"
os.makedirs(SAVE_DIR, exist_ok=True)

app = BedrockAgentCoreApp()
agent = Agent(tools=[image_reader])

def save_images(images_json):
    saved_paths = []

    if not images_json:
        return saved_paths

    for img in images_json:
        filename = img.get("filename", "image.png")
        data_b64 = img.get("data")

        if not data_b64:
            continue

        path = os.path.join(SAVE_DIR, filename)

        with open(path, "wb") as f:
            f.write(base64.b64decode(data_b64))

        saved_paths.append(path)

    return saved_paths


@app.entrypoint
def invoke(payload):
    prompt = payload.get("prompt", "")
    images = payload.get("images", [])
    image_paths = save_images(images)

    full_message = f"{prompt}\n imagens:\n" + "\n".join(image_paths)
    result = agent(full_message)

    return {
        "result": result.message,
        "saved_images": image_paths
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
