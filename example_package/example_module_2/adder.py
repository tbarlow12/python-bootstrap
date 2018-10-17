class Adder:
    '''
    This is an example class with static methods to add various values
    '''

    @staticmethod
    def sum(n, m):
        '''
        This is a PythonDoc. If you document your code in this format,
        it will be easily picked up by Sphinx when you generate documentation.
        This method will return the value of `n` + `m`
        :param n: First number to be added
        :param m: Second number to be added
        :return: n + m
        '''
        return n + m

    @staticmethod
    def plus_three(n):
        '''
        This is a PythonDoc. If you document your code in this format,
        it will be easily picked up by Sphinx when you generate documentation.
        This method will return the value of `n` + 3
        :param n: The number to be multiplied by 3
        :return: n + 3
        '''
        return n + 3
