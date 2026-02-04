import os
import sys
import boto3
from dotenv import load_dotenv
from strands import Agent
from strands import session
from strands.session import FileSessionManager, session_manager
from strands.models import BedrockModel
from strands_tools import (
    file_read,
    editor,
    shell,
    think
)

load_dotenv()

# Bedrockを利用するための認証情報を取得
session=boto3.Session(
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name=os.getenv('AWS_REGION_NAME')
)

# Strands Agentが会話履歴を保存するためのSessionを定義
session_manager = FileSessionManager(
    session_id="default",
    storage_dir="./sessions"
)

# 適宜モデルを設定
Bedrock_models = {
    "sonnet": BedrockModel(
        model_id="jp.anthropic.claude-sonnet-4-5-20250929-v1:0",
        boto_session=session
    ),
    "opus": BedrockModel(
        model_id="global.anthropic.claude-opus-4-5-20251101-v1:0",
        boto_session=session
    ),
    "haiku": BedrockModel(
        model_id="jp.anthropic.claude-4-5-haiku-20251001-v1:0",
        boto_session=session
    )
}

# Agentの定義
agent = Agent(
    session=session_manager,
    model=BedrockModel(
        client=session.client("bedrock-runtime"),
        model_id=Bedrock_models["sonnet"]
    ),
    tools=[
        file_read, 
        # editor, # remove comment if you allow agent to edit your files
        shell, 
        think
    ],
    system_prompt=(
        "You are an excellent dewvelop assistant that runs localy"
        "Please avoid excessive assumptions and strive to provide minimal and appropriate answers"
    )
)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        agent.run(sys.argv[1])
    else:
        agent.run("help")
