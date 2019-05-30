import utils20


def radiance_conversion(con_name, con_value):
    if con_name == 'Level':
        return utils20.levels[str(con_value)]
    elif con_name == 'Wounds':
        return utils20.wounds[con_value]


if __name__ == '__main__':
    print("Converter.py")
