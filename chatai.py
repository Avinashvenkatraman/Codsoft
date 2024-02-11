class AIChatbot:
    def __init__(self):
        self.name = ""
        self.help_needed = False
        self.about_user = ""
        self.hobbies = ""
        self.age = ""
        
    def ask_name(self):
        self.name = input("Hello! What's your name? ")
        
    def ask_help_needed(self):
        response = input(f"Nice to meet you, {self.name}! Can I help you with something? (yes/no) ")
        if response.lower() == "yes":
            self.help_needed = True
            self.ask_age()
        elif response.lower() in ("no", "sorry", "nope", "later"):
            print("Okay, maybe next time! Have a great day!")
            exit()
        else:
            self.help_needed = False
            
    def ask_age(self):
        self.age = input("What is your age? ")
        
    def ask_about_user(self):
        if self.help_needed:
            self.about_user = input("Sure! Could you tell me a little bit about yourself? ")
        else:
            print("Alright, just let me know if there's anything else I can assist you with.")
            
    def ask_hobbies(self):
        if self.help_needed:
            self.hobbies = input("Great! What are your hobbies? ")
        else:
            print("Alright, just let me know if there's anything else I can assist you with.")
            
    def chat(self):
        self.ask_name()
        self.ask_help_needed()
        if not self.help_needed:
            return
        
        self.ask_about_user()
        if self.about_user.lower() == "no":
            print("Okay, maybe next time! Have a great day!")
            exit()
        
        self.ask_hobbies()
        if self.hobbies.lower() == "no":
            print("Okay, maybe next time! Have a great day!")
            exit()
        
        print("\nThanks for chatting with me! Here's what I know about you:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Help Needed: {'Yes' if self.help_needed else 'No'}")
        if self.help_needed:
            print(f"About User: {self.about_user}")
            print(f"Hobbies: {self.hobbies}")

# Create an instance of the AIChatbot and start chatting
chatbot = AIChatbot()
chatbot.chat()
