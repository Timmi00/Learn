def show_messages(messages: list):
    while messages:
        message: str = messages.pop()
        print(message)
        sent_msgs.append(message)


msgs: list = ['dsds dsd ws', '21212 1212ws', 'a1sd']
sent_msgs: list = []
show_messages(msgs[:])
print(msgs, sent_msgs)
