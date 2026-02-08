# strands-coding-agent

Strands Agents を使って、Amazon Bedrock 上のモデルに対話プロンプトを投げる最小構成のサンプルです（`app.py`）。

## セットアップ

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

`.env`で以下を設定してください。

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_REGION_NAME`

## 使い方

```bash
python app.py "help"
python app.py "こんにちは。できることを教えて"
```

セッションは `./sessions` に保存されます。

## オプション
app.pyの内容を修正することで以下のような変更が可能です。
* モデルの切り替え
* セッション（会話履歴）をS3に保存
* システムプロンプトの修正
* エージェントが使用できるtoolの追加
