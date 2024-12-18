def flirtatiousChatbotFunction(user_message):
    flirtatious_responses = [
        "Well, hello there, you've caught my attention 😉",
        "Are you trying to make me blush? 😏",
        "Is it hot in here, or is it just you? 😘",
        "I’m not saying I’m falling for you, but you’ve definitely got my attention 😌",
        "Careful, or you might make me fall for you... 🥰"
    ]
    
    # Here, you could implement logic to trigger flirtatious responses based on keywords or context
    if "hi" in user_message.lower() or "hello" in user_message.lower():
        return random.choice(flirtatious_responses)
    elif "how are you" in user_message.lower():
        return "I’m better now that you’re talking to me 😘"
    else:
        return "I could keep talking with you all day, but I might start falling for you 💕"
