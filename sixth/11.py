def playCard(cards):
    if not cards or len(cards) < 5:
        return None
    card_values = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}
    joker_count = cards.count('大王') + cards.count('小王')
    numeric_cards = []
    for card in cards:
        if card in card_values:
            numeric_cards.append(card_values[card])
    if not numeric_cards:
        return None
    numeric_cards.sort()
    unique_cards = []
    for card in numeric_cards:
        if card not in unique_cards:
            unique_cards.append(card)
    gaps = 0
    for i in range(len(unique_cards) - 1):
        gaps += unique_cards[i+1] - unique_cards[i] - 1
    if gaps <= joker_count:
        return True
    else:
        return False
if __name__ == "__main__":
    poker_hand = ['A', '2', '3', '10', 'J', 'Q', 'K', '大王', '小王']
    result = playCard(poker_hand)
    if result:
        print("找到了一个顺子组合")
    else:
        print("没有找到顺子组合")
    test_cases = {
        "4,5,6,7,8": ['4','5','6','7','8'],
        "5,5,7,8,9": ['5','5','7','8','9'],
    }
    for name, hand in test_cases.items():
        if playCard(hand):
            print(f"测试 '{name}': 是顺子")
        else:
            print(f"测试 '{name}': 不是顺子")
