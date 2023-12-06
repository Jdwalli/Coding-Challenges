
separator = '|'
def calculate_card_points(card):
    winning_values, elf_values = card.split(": ")[1].split(separator)
    winning_values = [int(n) for n in winning_values.split()]
    elf_values = [int(n) for n in elf_values.split()]
    matches = 0

    for value in elf_values:
        if value in winning_values:
            matches += 1

    return 2 ** (matches - 1) if matches > 0 else 0

def calculate_additional_cards(card):
    card_number = int(card.split(": ")[0][4:])
    winning_values, elf_values = card.split(": ")[1].split(separator)
    winning_values = [int(n) for n in winning_values.split()]
    elf_values = [int(n) for n in elf_values.split()]
    matches = 0
    cards_won = []

    
    for value in elf_values:
        if value in winning_values:
            matches += 1

    print(f"Matches: {matches}")
    print(f"Card Number: {card_number}")
    for i in range(card_number, card_number + matches + 1):
        cards_won.append(i)
        

    print(cards_won, end='\n')
    return cards_won

def solve_part_one(scratchcard_data):
    score = 0
    for card in scratchcard_data:
        score += calculate_card_points(card)
     
    return score


def solve_part_two(scratchcard_data): 
    additional_cards_won = []
    for card in scratchcard_data:
        additional_cards_won.extend(calculate_additional_cards(card))
    
    print(additional_cards_won)

    return sum(additional_cards_won)




if __name__ == "__main__":
    with open('input.txt', 'r') as scratchcards:
        scratchcard_data = scratchcards.readlines()
        # print(solve_part_one(scratchcard_data))
        print(solve_part_two(scratchcard_data))