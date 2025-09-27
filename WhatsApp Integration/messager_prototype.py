import pywhatkit as kit

def get_response(user_message):
    user_message = user_message.lower()
    
    ai_responses = {
    "vaccination schedules": "National Immunization Schedule (2018)\n\nAt Birth:\n- BCG: At birth, till 1 year.\n- Hepatitis B (Birth dose): Within 24 hours of birth.\n- OPV-0: Within the first 15 days.\n\nAt 6, 10, & 14 Weeks:\n- OPV 1, 2 & 3\n- Pentavalent 1, 2 & 3\n- Fractional IPV\n- Rotavirus & PCV (if applicable)\n\nAt 9 Months:\n- Measles / Rubella (1st dose)\n- Japanese Encephalitis (if applicable)\n- Vitamin A (1st dose)\n\nNote: This is a general guide. Please consult your pediatrician for the exact schedule."
}
    
    for key in ai_responses:
        if key in user_message:
            return ai_responses[key]
    return "Sorry, I didn't understand that. Can you rephrase?"

recipient_number = "+919994539696"

while True:
    user_message = input("User: ")
    if user_message.lower() == "exit":
        break
    else:
        reply = get_response(user_message)
        kit.sendwhatmsg_instantly(recipient_number, reply)
        print(f"Bot: {reply}")