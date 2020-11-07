# LFSR
Linear Feedback Shift Register imitation for pseudo random bits generation

LFSRs are used to generate pseudo random bits. A single LFSR is easy to crack if the attacker knows 
* degree (m)
* 2<sup>m</sup>-1 bits
* ciphertext

It's recommended to use combination of multiple LFSRs to make it hard to crack.
The file `LFSR.py` contains class for generating the (pseudo) random sequence, and the file `main.py` contains the examples of implementation.

[Learn more about LFSR](https://en.wikipedia.org/wiki/Linear-feedback_shift_register)
