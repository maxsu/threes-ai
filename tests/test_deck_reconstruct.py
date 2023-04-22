from threes_ai.deck_reconstruct import DeckReconstructor

# We can generate boart/tileset pairs from OCR.ocr

def test_simple_sequence():

    boards = []
    tilesets = []
    deck = DeckReconstructor(boards[0])

    # simple test sequence

    for tileset in tilesets:
        deck.update(tileset[0])
        print(deck)
