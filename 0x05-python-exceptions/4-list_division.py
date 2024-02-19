#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            division = 0
            if isinstance(my_list_1[i], (int, float)) and isinstance(my_list_2[i], (int, float)) and my_list_2[i] != 0:
                division = my_list_1[i] / my_list_2[i]
            elif not isinstance(my_list_1[i], (int, float)):
                print("wrong type")
            elif my_list_2[i] == 0:
                print("division by 0")
            result.append(division)
        except IndexError:
            print("out of range")
            result.append(0)
        finally:
            pass
    return result


if __name__ == "__main__":
    pass
