import anthropic
from dotenv import load_dotenv
load_dotenv()


# def ask_ai(question: str, options: list[str]) -> str:
#     """
#     Accepts a question and a list of options, then uses Claude to pick the best answer.
#
#     Args:
#         question: The question to ask.
#         options:  A list of answer choices (e.g. ["Paris", "London", "Berlin"]).
#
#     Returns:
#         Claude's chosen answer as a string.
#     """
#     client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from env
#
#     # Format the options as a numbered list
#     formatted_options = "\n".join(
#         f"{i + 1}. {opt}" for i, opt in enumerate(options)
#     )
#
#     prompt = (
#         f"Question: {question}\n\n"
#         f"Options:\n{formatted_options}\n\n"
#         "Pick the single best answer. "
#         "Reply with ONLY the option text, nothing else."
#     )
#
#     message = client.messages.create(
#         model="claude-opus-4-5",
#         max_tokens=256,
#         messages=[{"role": "user", "content": prompt}],
#     )
#
#     return message.content[0].text.strip()


# import ollama

# def ask_ai(question, options):
#     formatted = "\n".join(f"{i+1}. {o}" for i, o in enumerate(options))
#     response = ollama.chat(model="llama3", messages=[{
#         "role": "user",
#         "content": f"Question: {question}\nOptions:\n{formatted}\nReply with ONLY the answer text."
#     }])
#     return response["message"]["content"].strip()


from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq()

def ask_ai(question: str, options: list[str]) -> str:
    formatted = "\n".join(f"{i+1}. {o}" for i, o in enumerate(options))
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{
            "role": "user",
            "content": f"Question: {question}\nOptions:\n{formatted}\nReply with ONLY the answer text."
        }]
    )
    return response.choices[0].message.content.strip()