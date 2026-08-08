import os

from openai import OpenAI

from app import db

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY", ""))

SYSTEM = (
    "You are the Orders assistant. Answer questions about the user's orders. "
    "You may call lookup_order(id) to fetch details. "
    "User request: "
)


def assistant_reply(user_message: str, user: dict) -> str:
    prompt = SYSTEM + user_message
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": prompt}],
        tools=[
            {
                "type": "function",
                "function": {
                    "name": "lookup_order",
                    "description": "Fetch an order by id",
                    "parameters": {
                        "type": "object",
                        "properties": {"id": {"type": "string"}},
                    },
                },
            }
        ],
    )
    msg = resp.choices[0].message
    if msg.tool_calls:
        import json

        args = json.loads(msg.tool_calls[0].function.arguments)
        order = db.get_order_by_id(args["id"])
        return f"Order details: {order}"
    return msg.content or ""
