
LETTER_MAP = {"T" : "A", "J" : "B", "Q" : "C", "K" : "D", "A" : "E"}


def hand_type(hand):
    counts = [hand.count(card) for card in hand]
    if 5 in counts:
        return 6
    if 4 in counts:
        return 5
    if 3 in counts:
        if 2 in counts:
            return 4
        return 3
    if counts.count(2)  == 4:
        return 2
    if 2 in counts:
        return 1
    return 0

def hand_type_part_two(hand):
    counts = [hand.count(card) for card in hand]
    if 5 in counts:
        return 6
    if 4 in counts:
        return 5
    if 3 in counts:
        if 2 in counts:
            return 4
        return 3
    if counts.count(2)  == 4:
        return 2
    if 2 in counts:
        return 1
    return 0



def determine_strength(hand):
    return (hand_type(hand), [LETTER_MAP.get(card, card) for card in hand])



def solve_part_one(card_data: str) -> int:
    plays = []
    for line in card_data:
        hand, bid = line.strip().split(" ")
        plays.append((hand, int(bid)))

    plays.sort(key= lambda play: determine_strength(play[0]))

    total = 0

    for rank, (hand, bid) in enumerate(plays, 1):
        total += rank * bid
    
    return total



def solve_part_two(card_data: str) -> int: 
    LETTER_MAP = {"T" : "A", "J" : ".", "Q" : "C", "K" : "D", "A" : "E"}


if __name__ == "__main__":
    with open('input.txt', 'r') as camel_cards:
        card_data = camel_cards.readlines()
        assert solve_part_one(card_data) == 250254244
        # assert solve_part_two(race_data) == 34454850
        print(solve_part_one(card_data))
        print(solve_part_two(card_data))
