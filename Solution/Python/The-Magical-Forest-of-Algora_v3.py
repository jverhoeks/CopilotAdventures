import azure.cognitiveservices.speech as speechsdk

# Create an instance of a speech config with specified subscription key and service region.
# Replace with your own subscription key and service region (e.g., "westus").
speech_key, service_region = "93d5cd53cba1458d8e7cb6cbaa00b273", "westeurope.api.cognitive.microsoft.com"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)


# Define the dance moves for each character
lox_moves = ['Twirl', 'Leap', 'Spin', 'Twirl', 'Leap']
drako_moves = ['Spin', 'Twirl', 'Leap', 'Leap', 'Spin']

# Define the effects of different combinations of dance moves
dance_moves = {
    ('Twirl', 'Twirl'): 'Fireflies light up the forest',
    ('Leap', 'Spin'): 'Gentle rain starts falling',
    ('Spin', 'Leap'): 'A rainbow appears in the sky',
    # Add more combinations of dance moves and their effects
}

# Initialize the state of the forest
forest_state = 'Normal'


def get_number_from_speech() -> int:
    # Create a speech recognizer
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

    # Start continuous recognition
    result = speech_recognizer.recognize_once()

    # Check if speech recognition is successful
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        # Get the recognized speech as text
        recognized_text = result.text

        # Convert the recognized text to an integer
        try:
            number = int(recognized_text)
            return number
        except ValueError:
            print("Invalid input. Please speak a number.")
            return get_number_from_speech()
    else:
        print("Speech recognition failed. Please try again.")
        return get_number_from_speech()

# Perform the dance sequence
for sequence in range(15):
    # Determine the dance move for each character
    
    # print the content of lox_moves
    for i, move in enumerate(lox_moves, 1):
        print(f'{i}. {move}')
    lox_move = get_number_from_speech()
    for i, move in enumerate(drako_moves, 1):
        print(f'{i}. {move}')
    drako_move = get_number_from_speech()
    
    # Rest of the code...
    if lox_move == '0' or drako_move == '0':
        print("Exiting the program...")
        exit()
    # Convert the input to integers
    lox_move = int(lox_move)
    drako_move = int(drako_move)

    # Check if the input is within the valid range
    if lox_move < 1 or lox_move > 5 or drako_move < 1 or drako_move > 5:
        print("Invalid dance move number. Please select a number between 1 and 5.")
        exit()

    # Get the actual dance moves based on the input
    lox_move = lox_moves[lox_move - 1]
    drako_move = drako_moves[drako_move - 1]
    lox_move = lox_moves[sequence]
    drako_move = drako_moves[sequence]

    # Determine the effect of the dance moves
    if (lox_move, drako_move) in dance_moves:
        effect = dance_moves[(lox_move, drako_move)]
        # Update the state of the forest based on the effect
        if effect == 'Fireflies light up the forest':
            forest_state = 'Enchanted'
        elif effect == 'Gentle rain starts falling':
            forest_state = 'Calm'
        elif effect == 'A rainbow appears in the sky':
            forest_state = 'Magical'
        # Add more conditions to update the forest state for other effects

    # Display the state of the forest after each sequence
    print(f'State of the forest after sequence {sequence+1}: {forest_state}')