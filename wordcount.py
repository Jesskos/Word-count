# put your code here.
# open file
# remove whitespace
# separate by each space
# empty dictionary
# .iteritems/.items iterate through each word of file
# one function that prints out each occurence of the word in the file
# close file

def word_count(file_name):

    word_file = open(file_name)
    word_count = {}

    for line in word_file:
        line = line.rstrip()
        words = line.split(' ')

        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
            

    for word, number in word_count.iteritems():
        print "{} {}".format(word, number)


word_count("test.txt")