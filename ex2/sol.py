from typing import Callable

'''
    lastcall is a decorator that returns a version of
    the function that remembers it's last input.
    if the function is invoked with the same arguments consecutively
    it prints an appropriate message otherwise it just returns the output.

'''

def lastcall(f: Callable):

    def wrraped(*args, last: list = [], **kwargs):

        # arguments that were'nt specefied as key-word arguments
        locs = {arg : None for arg in f.__code__.co_varnames if arg not in kwargs.keys()}
        # relevant for functions that expect exact number of arguments aside from the key-word arguments
        if 'args' not in locs:

            if len(locs) != len(args):  raise TypeError('argument count doesnt match')
            for i, arg in enumerate(locs.keys()):   locs[arg] = args[i]
            args = ()
            kwargs.update(locs)

        # checking if last call was the same
        if len(last) != 0:
            if (last[0] == args and last[1] == kwargs) or last[0] == kwargs:
                print('I already told u the answere is', last[2], 'u dope')
                return

        # invoking
        res = f(*args, **kwargs)

        # updating memory
        last.clear()
        last.append(args)
        last.append(kwargs)
        last.append(res)

        return res

    return wrraped