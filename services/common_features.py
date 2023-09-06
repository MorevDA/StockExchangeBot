def get_message_max_len_in_dict(string_list: list, len_msg=4096) -> list:
    """Функция для формирования сообщений максимальной длинны сообщения(4096 символов)."""
    result = []
    string = ''
    x = string_list[-1]
    for stock in string_list:
        text = '\n'.join([f'{key} {value}' for key, value in stock.items()]) + '\n\n'
        if len(string) + len(text) <= len_msg and stock != x:
            string += text
        elif len(string) + len(text) <= len_msg and stock == x:
            string += text
            result.append(string)
        else:
            result.append(string)
            string = text
    return result


def get_message_max_len_in_list(string_list: list, len_msg=4096) -> list:
    """Функция для формирования сообщений максимальной длинны сообщения(4096 символов)."""
    result = []
    string = ''
    last_elem = string_list[-1]
    for elem in string_list:
        if len(string) + len(elem) <= len_msg and elem != last_elem:
            string += elem
        elif len(string) + len(elem) <= 4906 and elem == last_elem:
            string += elem
            result.append(string)
        else:
            result.append(string)
            string = elem
    return result


