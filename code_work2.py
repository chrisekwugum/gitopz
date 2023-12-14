def count_letters():
    word = input("Please enter a sentence: ").lower()
    count = len(word)
    count2 = len(word.replace(" ",""))
    count3 = len(word.split())

    print(f'Your sentence has a total of {count3 } words, {count2} characters without spaces and {count} with spaces.')
    

count_letters()