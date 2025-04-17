from datetime import datetime

print("Type 'exit' to end")
with open('chat_log.txt', 'a', encoding='utf-8') as log_file:
    while True:
        message = input("You: ")
        
        if message.lower() == 'exit':
            print("Chat saved to chat_log.txt")
            break
            
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
        log_entry = f"[{timestamp}] {message}\n"
        log_file.write(log_entry)
