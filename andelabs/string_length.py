def string_length(x):

    if type(x) == str:

        return [len(x)]

    elif type(x) == list:

        j = []
        for i in x:

            if type(i) == str:

                j.append(len(i))

            else:

                return "Invalid input. Provide a list of strings"

        return j

    else:

        return "Invalid data type. Add a string or a list of strings"