# Kata Break-out rooms

## Iteration 1
We would like to make groups of people to organise them into different random work teams.

Write a function that takes the list of attendees, the size of the rooms (number of people per room) and the number of rounds.

The function will organise the rooms minimizing the number of repetitions per round.

The result of the function is a list of lists containing rooms with participants.

## Iteration 2

The function will be deterministic, in case the same number of rounds, the same participants and room size are given again, the result will be the same. This will serve as a history.

## Example

### input:

- Number of rounds: 2
- Participants: Ada, Mary, Sara, Angela, Rita, Marta, Cristina, Nina, Josefa, Noe, Carolina, Yazmina, Adassa, Carmen, Juani, Sonia, Monica, Nuria, Carla, Jessi, Emilia.
- Room size: 2

### Output 1st round

Juani - Monica,
Carmen - Sara,
Nina - Noe,
Nuria - Carolina,
Josefa - Emilia,
Cristina - Carla,
Jessi - Mary,
Angela - Yazmina,
Marta - Ada,
Sonia - Adassa y Rita

### Output 2nd round

Angela - Carmen,
Mary - Ada,
Rita - Jessi,
Josefa - Monica,
Adassa - Carla,
Nuria - Cristina,
Noe - Carolina,
Juani - Yazmina,
Marta - Sara,
Emilia - Sonia, y Nina

**Reference Kata:** 
https://github.com/lean-mind/break-out-rooms-kata/blob/main/README.md