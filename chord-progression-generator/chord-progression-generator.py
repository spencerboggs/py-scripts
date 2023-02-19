import random

array = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
print("Enter q to quit")

while True:
    extraNotes = ["maj7", "min7", "7", "min7b5", "dim7", "6", "6/9", "min6", "9", "maj9", "min9"]
    finalChords = []
    def random_extra_notes():
        chord = extraNotes[random.randint(0, len(extraNotes) - 1)]
        return chord

    finalChords = []
    number = input("Enter the number of chords (default: 4):")
    if (number.isnumeric()):
        number = int(number)
    elif (number == 'q'):
        break;
    else:
        number = 4

    i = 0;
    selected = []
    while (i < number):
        selected = array[random.randint(0, len(array) - 1)]
        combinedChords = selected + random_extra_notes()
        finalChords.append(combinedChords)
        i = i + 1

    print("")
    print("Selected strings (" + str(number) + "):\n", *finalChords)
    print("")
