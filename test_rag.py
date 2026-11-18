
from rag import ask_question

question = "What is the main objective of this research paper?"

answer, sources = ask_question(question)

print("\nAI ANSWER:")
print(answer)

print("\nSOURCE CITATIONS:")

for source in sources:
    print(f"File: {source['file']}, Page: {source['page']}")
