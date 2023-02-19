import random

printedArray = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G",
                "G#", "A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]
array = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G",
         "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
print("Enter q to quit")
input("Press enter to start")
while True:
    extraNotes = ["maj7", "min7", "7", "min7b5",
                  "dim7", "6", "6/9", "min6", "maj9", "min9"]
    finalChords = []
    randomValue = random.randint(0, (len(array)/2) - 1)

    def random_extra_notes():
        chord = extraNotes[random.randint(0, len(extraNotes) - 1)]
        return chord

    finalChords = []

    flatOrNot = random.randint(0, 1)
    if (flatOrNot == 0):
        randomSelectValue = randomValue + 12
    elif (flatOrNot == 1):
        randomSelectValue = randomValue
    printSelected = []
    printSelected = printedArray[randomSelectValue]
    selected = []
    selected = array[randomValue]
    randomExtra = random_extra_notes()
    combinedChords = printSelected + randomExtra
    note1 = selected
    noteb2 = array[randomValue + 1]
    note2 = array[randomValue + 2]
    noteb3 = array[randomValue + 3]
    note3 = array[randomValue + 4]
    note4 = array[randomValue + 5]
    noteb5 = array[randomValue + 6]
    note5 = array[randomValue + 7]
    noteb6 = array[randomValue + 8]
    note6 = array[randomValue + 9]
    noteb7 = array[randomValue + 10]
    note7 = array[randomValue + 11]
    if (randomExtra == extraNotes[0]):
        correctAnswer = note1 + " " + note3 + " " + note5 + " " + note7
        # print(correctAnswer)
    elif (randomExtra == extraNotes[1]):
        correctAnswer = note1 + " " + noteb3 + " " + note5 + " " + noteb7
        # print(correctAnswer)
    elif (randomExtra == extraNotes[2]):
        correctAnswer = note1 + " " + note3 + " " + note5 + " " + noteb7
        # print(correctAnswer)
    elif (randomExtra == extraNotes[3]):
        correctAnswer = note1 + " " + noteb3 + " " + noteb5 + " " + noteb7
        # print(correctAnswer)
    elif (randomExtra == extraNotes[4]):
        correctAnswer = note1 + " " + noteb3 + " " + noteb5 + " " + note6
        # print(correctAnswer)
    elif (randomExtra == extraNotes[5]):
        correctAnswer = note1 + " " + note3 + " " + note5 + " " + note6
        # print(correctAnswer)
    elif (randomExtra == extraNotes[6]):
        correctAnswer = note1 + " " + note3 + " " + note5 + " " + note6 + " " + note2
        # print(correctAnswer)
    elif (randomExtra == extraNotes[7]):
        correctAnswer = note1 + " " + noteb3 + " " + note5 + " " + note6
        # print(correctAnswer)
    elif (randomExtra == extraNotes[8]):
        correctAnswer = note1 + " " + note3 + " " + note5 + " " + note7 + " " + note2
        # print(correctAnswer)
    elif (randomExtra == extraNotes[9]):
        correctAnswer = note1 + " " + noteb3 + " " + note5 + " " + noteb7 + " " + note2
        # print(correctAnswer)

    print("")
    print(combinedChords)
    print("Input the notes of the chord")
    print("seperate the notes with spaces")
    print("")
    Answer = input("")
    Answer = Answer.replace("Ab", "G#")
    Answer = Answer.replace("Bb", "A#")
    Answer = Answer.replace("Db", "C#")
    Answer = Answer.replace("Eb", "D#")
    Answer = Answer.replace("Gb", "F#")
    while (Answer != correctAnswer) and (Answer != ""):
        print("Wrong. Try again (" + combinedChords + "): ")
        Answer = input("")
    if (Answer == correctAnswer):
        print("Correct!")
    elif (Answer == ""):
        print("Chord skipped! Correct answer:")
        print(correctAnswer)
    print("")
