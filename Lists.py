'''4.
What are the lengths of the following lists? Fill in the variable lengths with your predictions. (Try to make a prediction for each list without just calling len() on it.)'''
a = [1, 2, 3]
b = [1, [2, 3]]
c = []
d = [1, 2, 3][1:]

# Put your predictions in the list below. Lengths should contain 4 numbers, the
# first being the length of a, the second being the length of b and so on.
lengths = [3,2,0,2]

# Check your answer
q4.check()

'''5. 🌶️
We're using lists to record people who attended our party and what order they arrived in. For example, the following list represents a party with 7 guests, in which Adela showed up first and Ford was the last to arrive:

party_attendees = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
A guest is considered 'fashionably late' if they arrived after at least half of the party's guests. However, they must not be the very last guest (that's taking it too far). In the above example, Mona and Gilbert are the only guests who were fashionably late.

Complete the function below which takes a list of party attendees as well as a person, and tells us whether that person is fashionably late.'''

def fashionably_late(arrivals, name):
    order = arrivals.index(name) #metodo index
    return order >= len(arrivals) / 2 and order != len(arrivals) - 1
# Check your answer
q5.check()
