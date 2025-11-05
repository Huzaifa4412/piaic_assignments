def main():
    mood = input(
        "How are you feeling today? (happy, sad, tired, angry, excited, bored): "
    ).lower()

    # Check mood and respond with a message
    if mood == "happy":
        print("That's great! Keep smiling and share your happiness with others 😊")
    elif mood == "sad":
        print(
            "It's okay to feel sad sometimes. Remember, tough times don't last but tough people do 💪"
        )
    elif mood == "tired":
        print("You’ve been working hard. Take a break, rest, and come back stronger 😴")
    elif mood == "angry":
        print("Take a deep breath. Stay calm and focus on what you can control 🧘‍♀️")
    elif mood == "excited":
        print("Awesome! Use that energy to do something amazing today ⚡")
    elif mood == "bored":
        print(
            "Try learning something new or go for a walk — it might refresh your mind 🌿"
        )
    else:
        print(
            "Hmm, I’m not sure what that mood means, but I hope you have a wonderful day! 🌞"
        )


if __name__ == "__main__":
    main()
