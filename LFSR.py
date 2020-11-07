class LFSR():
    """
    Class that implements 'basic' Linear Feedback Shift Register (LFSR) for the generation of pseudo random numbers
    """

    def __init__(self, fb_poly):
        self.fb_poly = fb_poly
        exponents = fb_poly.split()
        self.degree = int(exponents[0])
        indices = ["0"]*(self.degree+1)
        for i in exponents:
            indices[int(i)] = '1'
        indices = indices[::-1][1:]
        self.p_states = [i for i in range(self.degree) if indices[i] == "1"]

    def __calculate_feedback(self, state):
        xor_elements = [state[i] for i in self.p_states]
        result = 0
        for i in xor_elements:
            result = result ^ int(i)
        return str(result)

    def generate(self, initial, count=256):
        if len(initial) != self.degree:
            raise Exception("Incorrect number of initial states, should be {}".format(self.degree))

        seq = initial
        output_bit = seq[-1]
        for _ in range(count):
            yield output_bit
            seq = self.__calculate_feedback(seq) + seq[:-1]
            output_bit = seq[-1]
