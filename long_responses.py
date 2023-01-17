import random


def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sorry I was unable to understand that",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response
