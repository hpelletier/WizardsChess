import speech_recognition as sr
from subprocess import call


def listen():
    call(["amixer", "set", "Capture", "70"])
    call(["arecord", '-f', 'dat', '-c', '1', '-D', 'hw:0,0', '-d', '5', '-V', 'mono', 'test.wav'])
    r = sr.Recognizer(language = "en-US", key = "AIzaSyB5HMzhJDY9iKLLku6_gQRGleTmFgiq4Ec")
    
    with sr.WavFile("test.wav") as source:              # use "test.wav" as the audio source
        audio = r.record(source)                        # extract audio data from the file
    try:
        return r.recognize(audio)
    except:
        return None

def recognize():

    r = sr.Recognizer()

    wav = listen()
    res = []
    with sr.WavFile("test.wav") as source:              # use "test.wav" as the audio source
        audio = r.record(source)                        # extract audio data from the file

    try:
        l = r.recognize(audio,True)
    except LookupError:
        return ''
    # generate a list of possible transcriptions
    # print("Possible transcriptions:")
    try:
        for prediction in l:
            text = str(prediction["text"])
            res.append(text)
        return res
    except LookupError:                                 # speech is unintelligible
        return None

def translate(dictionary):
    sentence = ""


    res = recognize()

    for r in res:
        found = True
        sentence = r
        words = r.split()
        #print words
        for w in words:
            if w.lower() not in dictionary:
                found = False
                break
        if found:
            #print sentence
            return sentence
    return None

def interpret():

    pawn = ['pawn', 'han', 'pon', 'porn', 'pork']
    king = ['king']
    knight = ['knight', 'night', 'nite', 'kite']
    rook = ['rook', 'hook', 'cook', 'look']
    queen = ['queen', 'ween', 'keen']
    bishop = ['bishop']

    pieces = [pawn, king, knight, rook, queen, bishop]
    

    one = ['1', 'one', 'won', 'on', 'win']
    two = ['2', 'to', 'two', 'too', '22']
    three = ['3', 'three', 'tree', 'free', 're', 'ree']
    four = ['4', 'four', 'for', 'fore']
    five = ['5', 'five', 'hive', 'ive', 'chive']
    six = ['6', 'sex', 'six', 'sick']
    seven = ['7', 'seven', 'heaven', 'evan']
    eight = ['8', 'eight', 'ate', 'hate']


    numbers = [one, two, three, four, five, six, seven, eight]


    a = ['a', 'ay', 'ey', 'hey', 'hay']
    b = ['b', 'be', 'bee', 'pee', 'p']
    c = ['c', 'see', 'sea', 'cee']
    d = ['d', 'de', 'dee', 'deet']
    e = ['e', 'ep', 'ee', 'eep', 'he', 'hee']
    f = ['f', 'ass', 'ef', 'eff']
    g = ['g', 'gee', 'jee', 'je', 'chee', 'chi', 'qi']
    h = ['h', 'aitch', 'achive']

    letters = [a, b, c, d, e, f, g, h]
    
    dictionary = pawn + king + knight + rook + queen + bishop + one + two + three + four + five + six + seven + eight + a + b + c + d + e + f + g + h

    sentence = translate(dictionary)

    if sentence == None:
        return None
    else:
        phrase = sentence.split()

        if len(phrase) != 4:
            return None
        else:
            #print "THIS IS ORIGINAL PHRASE" + str(phrase)
            for i in range(len(phrase)):
                if i == 0:
                    for piece in pieces:
                        if phrase[i].lower() in piece:
                            phrase[i] = piece[0]
                if i == 1 or i == 3:
                    for num in numbers:
                        if phrase[i].lower() in num:
                            phrase[i] = num[0]
                if i == 2:
                    for letter in letters:
                        if phrase[i].lower() in letter:
                            phrase[i] = letter[0]
          
            print phrase

            phraseEdit = [phrase[0], phrase[1], phrase[2]+phrase[3]]
            print phraseEdit

            # phrase[2] += phrase[3]
            # phrase.remove(phrase[3])

            final = ' '.join(phraseEdit)
            
            return final

    

