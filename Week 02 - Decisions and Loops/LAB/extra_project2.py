# Higher or Lower Game

account_a_name = "Tech Channel"
account_a_followers = 550  # in millions

account_b_name = "Music Artist"
account_b_followers = 320  # in millions

print("Welcome to Higher or Lower!")
print("-" * 30)


while True:
    print(f"\nCompare A: {account_a_name}")
    print(f"Against B: {account_b_name}")
    

    guess = input("Who has more followers? Type 'A' or 'B' (or 'quit' to exit): ").strip().lower()
    
    if guess == "quit":
        print("Thanks for playing!")
        break
        

    if account_a_followers > account_b_followers:
        correct_answer = "a"
    else:
        correct_answer = "b"
        
    if guess == correct_answer:
        print("✅ Correct!")
    elif guess in ["a", "b"]:
        print("❌ Wrong!")
    else:
        print("⚠️ Invalid input. Please type 'A', 'B', or 'quit'.")