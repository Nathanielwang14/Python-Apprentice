"""
Use the words in the list to create a story. 

Use indexing to get words from the list, then 
append them to the story

"""

words = ['Once', '👦', 'upon', '🐕', 'park', 'met', 'with', 'a', 'the', 
    'time', 'to', 'who', '🐈', '👧', 'and', 'went', 'had', 'play', '⚽.', 'they']

story = []

print(list(set("Once upon a time a 👦 with a 🐕 met a 👧 who had a 🐈 and they went to the park to play with a ⚽.".split())))

# Create a story using the words in the list

# Display the story to the user
print(' '.join(story))