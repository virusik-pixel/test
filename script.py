from itertools import chain, permutations, product

suit = input().strip()
rank = input().strip()

suits = {'буби': 'бубен', 'пики': 'пик', 'трефы': 'треф', 'черви': 'червей'}
ranks = ['10', '2', '3', '4', '5', '6', '7', '8', '9', 'валет', 'дама', 'король', 'туз']

ranks.remove(rank)

deck = product(ranks, suits.values())

triplets = permutations(deck, 3)

triplets = [triplet for triplet in triplets if suits[suit] in chain.from_iterable(triplet)]

sorted_combinations = sorted(triplets)
for combination in sorted_combinations[:10]:
    print(', '.join(f'{rank} {suit}' for rank, suit in combination))