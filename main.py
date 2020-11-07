from LFSR import LFSR

# choose primitive polynomial for maximum period,
# max-period = (2**m)-1, where m is degree

# LSFR.generate() takes 2 args,
# intial states of registers [0 or 1]
# required length of random bits, default = 256

# example 1
lfsr1 = LFSR("7 6 0")                   # exponents of polynomial

prng1 = lfsr1.generate("1100101", 84)
random_seq_1 = ''.join(prng1)
print("Random sequence 1", random_seq_1)

prng2 = lfsr1.generate("1100101", 256)
random_seq_2 = ''.join(prng2)
print("Random sequence 2", random_seq_2)

# example 2
lfsr2 = LFSR("8 6 5 4 0")
prng3 = lfsr2.generate("11001001", 128)
random_seq_3 = ''.join(prng3)
print("Random sequence 3", random_seq_3)
