def initialize(full_name):
    '''
    Return the person's initials.
    '''
    name_parts = full_name.split(" ")
    initial_list = [name[0]+"." for name in name_parts]

    output = ""
    for initial in initial_list:
        output = output + initial

    return(output)
