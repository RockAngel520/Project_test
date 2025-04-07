import masks


def mask_account_card(card_or_account_number: str) -> str:
    """Функция, которая определяет карта это или номер и возвращает маску"""
    if "Счет" in card_or_account_number:
        mask_account_number = f"Счет " + masks.get_mask_account(card_or_account_number)
        return mask_account_number
    else:
        card_name_and_numder = card_or_account_number.split()
        card_name_and_numder[-1] = masks.get_mask_card_number(card_name_and_numder[-1])
        mask_account_number = " ".join(card_name_and_numder)
        return mask_account_number
