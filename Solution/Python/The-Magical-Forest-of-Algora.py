import random
import time

# Define the dance moves for each character
lox_moves = ['Twirl', 'Leap', 'Spin']
drako_moves = ['Jump', 'Slide', 'Flip']
luna_moves = ['Swirl', 'Glide', 'Twist']
orion_moves = ['Shake', 'Bounce', 'Roll']
vega_moves = ['Slide', 'Twist', 'Turn']

# Define the effects of different combinations of dance moves
dance_moves = {
    ('Twirl', 'Jump', 'Swirl', 'Shake', 'Slide'): 'Fireflies light up the forest',
    ('Leap', 'Slide', 'Glide', 'Bounce', 'Twist'): 'Gentle rain starts falling',
    ('Spin', 'Flip', 'Twist', 'Roll', 'Turn'): 'A rainbow appears in the sky',
    # Add more combinations of dance moves and their effects
}

# Initialize the state of the forest
forest_state = 'Normal'
random.seed(time.time())

# Perform the dance sequence
for sequence in range(125):

    # Determine the dance move for each character
    lox_move = random.choice(lox_moves)
    drako_move = random.choice(drako_moves)
    luna_move = random.choice(luna_moves)
    orion_move = random.choice(orion_moves)
    vega_move = random.choice(vega_moves)


    # Determine the effect of the dance moves
    if (lox_move, drako_move, luna_move, orion_move, vega_move) in dance_moves:
        effect = dance_moves[(lox_move, drako_move, luna_move, orion_move, vega_move)]
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
    time.sleep(0.5)