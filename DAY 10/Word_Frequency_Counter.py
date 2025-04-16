import string

def word_counter(input_file='story.txt', output_file='frequency.txt'):
    word_dictionary = {}
    
    with open(input_file, 'r') as file:
        for line in file:

            line = line.translate(str.maketrans('', '', string.punctuation))
            words = line.lower().split()
            
            for word in words:
                if word in word_dictionary:
                    word_dictionary[word] += 1
                else:
                    word_dictionary[word] = 1
    
    with open(output_file, 'w') as result_file:
        for word, count in word_dictionary.items():
            result_file.write(f'{word}: {count}\n')

word_counter()
