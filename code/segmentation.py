import nltk
nltk.download('punkt')

# This function segments sentences and saves them to Text file sentence by sentence per line
def content2txt(output_filepath, text=None, input_filepath=None):
    if input_filepath == None and text != None:
        # Segment the text into sentences
        sentences = nltk.sent_tokenize(text)

        # Save each sentence as one line in a new file
        with open(output_filepath, "w", encoding='utf-8') as file:
            for sentence in sentences:
                file.write(sentence+'\n')
            print("Sentences have been successfully saved")
    elif text == None and input_filepath != None:
        # Open the file and get the text
        with open(input_filepath, 'r', encoding='UTF-8') as file:
            text = file.read()
        # Segment the text into sentences    
        sentences = nltk.sent_tokenize(text)

        # Save each sentence as one line in a new file
        with open(output_filepath, "w", encoding='utf-8') as file:
            for sentence in sentences:
                file.write(sentence+'\n')
            print("Sentences have been successfully saved")
    else:
        print("Please provide one of the following keyword arguments: text or input_filepath")
    pass