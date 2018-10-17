class Multiplier:
    '''
    This is an example class with static methods to multiply by various values
    '''

    @staticmethod
    def times_two(n):
        '''
        This is a PythonDoc. If you document your code in this format,
        it will be easily picked up by Sphinx when you generate documentation.
        This method will return the value of `n` multiplied by 2
        :param n: The number to be multiplied by 2
        :return: n * 2
        '''
        return n * 2

    @staticmethod
    def times_three(n):
        '''
        This is a PythonDoc. If you document your code in this format,
        it will be easily picked up by Sphinx when you generate documentation.
        This method will return the value of `n` multiplied by 3
        :param n: The number to be multiplied by 3
        :return: n * 3
        '''
        return n * 3
