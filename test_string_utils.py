from string_utils import StringUtils

utils = StringUtils()


# 1. capitalize — делает первую букву заглавной
def test_capitalize_positive():
    assert utils.capitalize("skypro") == "Skypro"


def test_capitalize_negative():
    assert utils.capitalize("") == ""


# 2. trim — удаляет пробелы в начале
def test_trim_positive():
    assert utils.trim("   skypro") == "skypro"


def test_trim_negative():
    assert utils.trim("") == ""


# 3. to_list — превращает строку в список
def test_to_list_positive():
    assert utils.to_list("a,b,c") == ["a", "b", "c"]


def test_to_list_negative():
    assert utils.to_list("") == []


# 4. contains — проверяет, есть ли символ в строке
def test_contains_positive():
    assert utils.contains("SkyPro", "S") is True


def test_contains_negative():
    assert utils.contains("SkyPro", "U") is False


# 5. delete_symbol — удаляет символ из строки
def test_delete_symbol_positive():
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"


def test_delete_symbol_negative():
    assert utils.delete_symbol("SkyPro", "z") == "SkyPro"


# 6. starts_with — проверяет, начинается ли строка с символа
def test_starts_with_positive():
    assert utils.starts_with("SkyPro", "S") is True


def test_starts_with_negative():
    assert utils.starts_with("SkyPro", "P") is False


# 7. end_with — проверяет, заканчивается ли строка на символ
def test_end_with_positive():
    assert utils.end_with("SkyPro", "o") is True


def test_end_with_negative():
    assert utils.end_with("SkyPro", "y") is False


# 8. is_empty — проверяет, пустая ли строка
def test_is_empty_positive():
    assert utils.is_empty("") is True


def test_is_empty_negative():
    assert utils.is_empty("SkyPro") is False


# 9. list_to_string — соединяет элементы списка в строку
def test_list_to_string_positive():
    assert utils.list_to_string(["a", "b", "c"]) == "a, b, c"


def test_list_to_string_negative():
    assert utils.list_to_string([]) == ""
