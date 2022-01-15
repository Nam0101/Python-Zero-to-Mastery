def do_stuff(num=0):
    try:
        if num:
            return int(num)+5
        else:
            return 0
    except ValueError as err:
        return err
