def can_trust_message(message):
    alpha = set("abcdefghijklmnopqrstuvwxyz")
    messageLetter = set(message.replace(" ", ""))
    return alpha.issubset(messageLetter)
    


message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

print(can_trust_message(message1))
print(can_trust_message(message2))