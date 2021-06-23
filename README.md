# Kata Break-out rooms

## Iteration 1
We would like to make groups of people to organise them into different random work teams.

Write a function that takes the list of attendees, the size of the rooms (number of people per room) and the number of rounds.

The function will organise the rooms minimizing the number of repetitions per round.

The result of the function is a list of lists. 

Each inner list contains strings that represent every room. 

Every string contains the names of the participants in that room.

### ToDo List

[ ] Generate random combinations

[ ] Consider more than one round

[ ] Combinations should not have the same participants in different rounds

### To implement

For each round
      1. Randomly draw 1 person from the list of participants.
      2. Add this person to the room.
      3. Check if the person is not in another room with the same people.
      4. Remove this person from the participant list to assign

## Iteration 2

Coming soon... 🥁

## Example

### Input:

- Number of rounds: 2
- Participants: Ada, Mary, Sara, Angela, Rita, Marta, Cristina, Nina, Josefa, Noe, Carolina, Yazmina, Adassa, Carmen, Juani, Sonia, Monica, Nuria, Carla, Jessi, Emilia.
- Room size: 2

### Example of the method signature in Python

def break_out_rooms(rounds, participants, room_size)

### Example of a method call

break_out_rooms(2, 
["Ada", "Mary", "Sara", "Angela", "Rita", "Marta", "Cristina", "Nina", "Josefa", "Noe", "Carolina", "Yazmina", "Adassa",
 "Carmen", "Juani", "Sonia", "Monica", "Nuria", "Carla", "Jessi", "Emilia"],
2);


### Output 1st round
"Juani, Monica", "Carmen, Sara", "Nina, Noe", "Nuria, Carolina", "Josefa, Emilia", "Cristina, Carla", "Jessi, Mary", "Angela, Yazmina", "Marta, Ada", "Sonia, Adassa, Rita"

### Output 2nd round 

"Angela, Carmen", "Mary, Ada", "Rita, Jessi", "Josefa, Monica", "Adassa, Carla", "Nuria, Cristina", "Noe, Carolina", "Juani, Yazmina", "Marta, Sara", "Emilia, Sonia, Nina"

**Reference Kata:** 
https://github.com/lean-mind/break-out-rooms-kata/blob/main/README.md