with open("Mail Merge Project Start/Input/Names/invited_names.txt") as file:
    names = file.readlines()
    new_names = []
    for x in names:
        format_name = x.strip()
        new_names.append(format_name)
    print(new_names)

with open("Mail Merge Project Start/Input/Letters/starting_letter.txt") as file:
    letters = file.read()
    for x in new_names:
        new_letter = letters.replace("[name]", x)
        with open(f"Mail Merge Project Start/Output/ReadyToSend/letter_for_{x}.txt", mode="w") as file:
            file.write(new_letter)

