import string

class WordCount():
    def __init__(self) -> None:
        self.sentence = []
        self.word_count_dict = {}
        self.words_in_sentence = []
        s = input("Enter the sentence/paragraph here:\t")
        if s != "":
            self.sentence =self.prepareString(s)
            self.calculateWordsInSentence(self.sentence)
            self.wordCount()
        else:
            print("please input correctly")
            self.__init__()

    def prepareString(self,str):
        #function to prepare the entered sentence like removing punctuation,making it case insensitive to do word counting
        str = str
        new_str = str.translate(str.maketrans('','',string.punctuation))
        new_str = new_str.casefold()
        new_str = new_str.split(" ")
        return new_str
    
    def calculateWordsInSentence(self,str):
        #calculating unique words from entered sentence 
        for word in self.sentence:
            if word not in self.words_in_sentence:
                self.words_in_sentence.append(word)
            else:
                pass

    def wordCount(self):
        #function to calculate frequency of each word presented in sentence/paragraph
        for words in self.words_in_sentence:
            count = self.sentence.count(words)
            self.word_count_dict[words] = count

    def printTotalWords(self):
        #function to print total number of unique words
        print("--------------------------------------------------\n")
        print("Total unique words in paragraph:\t",len(self.words_in_sentence))

    def printWordsWithCounting(self):
        #function to print each word's frequency
        print("Frequency of each words:\n")
        print("--------------------------------------------------\n")
        for i in self.word_count_dict:
            print(i,":",self.word_count_dict.get(i),"\n")

wc = WordCount()
wc.printWordsWithCounting()
wc.printTotalWords()