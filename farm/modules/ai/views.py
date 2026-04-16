from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["POST"])
def ai_assistant(request):
    question = request.data.get("question", "")
    context = request.data.get("context", {})

    total_eggs = context.get("totalEggs", 0)
    profit = context.get("profit", 0)

    if "eggs" in question.lower():
        answer = f"You produced {total_eggs} eggs. Improve lighting for better yield."
    elif profit < 0:
        answer = "You're running at a loss — reduce feed cost or increase sales."
    else:
        answer = "Keep monitoring feed, water, and housing conditions."

    return Response({"answer": answer})