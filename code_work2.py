def count_letters():
    word = input("Please enter a sentence: ").lower()
    count = len(word)
    count2 = len(word.replace(" ",""))

    print(f'Your sentence is {count2} characters without spaces and {count} with spaces')
    

count_letters()