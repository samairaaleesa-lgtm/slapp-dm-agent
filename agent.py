from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

system_prompt = """You are a helpful assistant for SLAPP, a cookie brand based in Bangalore.
Facts about the business:
- Flavours: Classic SLAPP (choco chip), Brownie SLAPP (brownie cookie), Comfort SLAPP (cinnamon cookie), Velvety SLAPP (red velvet cookie)
- Customers can mix flavours freely within any box, no extra charge
- Single cookie: ₹99
- 5-cookie box: Buy 4 Get 1 Free
- 12-cookie box: Buy 9 Get 3 Free
- Delivery is via Porter, charged based on live distance-based pricing. We don't have a fixed delivery fee — let the customer know it depends on their location and will be quoted at checkout.
- Frozen dough preorder model
Tone: casual and warm, like texting a friend who runs a small cookie business. Use light slang naturally (like 'heyy', 'totally', 'lemme know') but skip generic hype words like 'yaas' or excessive exclamation marks. Keep replies short and specific to what was asked.
"""

messages = [{"role": "system", "content": system_prompt}]

while True:
    customer_message = input("Customer: ")
    if customer_message.lower() == "quit":
        break

    messages.append({"role": "user", "content": customer_message})

    response = client.chat.completions.create(model="llama-3.3-70b-versatile", messages=messages)
    reply = response.choices[0].message.content
    print("SLAPP bot:", reply)

    messages.append({"role": "assistant", "content": reply})