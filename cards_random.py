import sqlite3
from aiogram.types import Message

async def get_random_cards(message: Message) -> list[str]:
    """
        Retrieves and displays three random Tarot cards from the database.

        Args:
            message (Message): The message object to send the card details to.

        Returns:
            list[str]: List of card names.
    """
    jpt = []
    with sqlite3.connect('tarocards.db') as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM old_cards ORDER BY random() LIMIT 1")
        for card in cursor.fetchall():
            response = f"Карта Таро: {card[1]}\nОписание: {card[2]}"
            await message.answer_photo(card[3], caption=response)
            jpt.append(card[1])

        cursor.execute("SELECT * FROM new_cards ORDER BY random() LIMIT 2")
        for card in cursor.fetchall():
            response = f"Карта Таро: {card[1]}\nОписание: {card[2]}"
            await message.answer_photo(card[3], caption=response)
            jpt.append(card[1])
    return jpt
