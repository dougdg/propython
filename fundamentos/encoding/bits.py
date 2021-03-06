#!/usr/bin/env python

'''
The `bin` function returns a binary representation of an integer::

    >>> bin(0)
    '0'
    >>> bin(1)
    '1'
    >>> bin(10)
    '1010'
    >>> bin(int('ff',16))
    '11111111'
    >>> bin(int('aaaa',16))
    '1010101010101010'

The binary result may be padded with 0s to a specified length::

    >>> bin(10,8)
    '00001010'
    >>> bin(int('ff',16),16)
    '0000000011111111'
    
Bits may be separated at word boundaries. The default word length is 8::    
        
    >>> bin(int('ff',16),16, ':')
    '00000000:11111111'
    >>> bin(int('ff',16), 12, ' ')
    '0000 11111111'
    >>> bin(int('aaaa',16),32,' ')
    '00000000 00000000 10101010 10101010'

A different word length may be specified::

    >>> bin(10,8,':',4)
    '0000:1010'
    >>> bin(int('ff',16), 12, sep=' ', word_len=4)
    '0000 1111 1111'

The one-liner also works, within it's limitations::

    >>> bin1(0)
    '0'
    >>> bin1(2**8-1)
    '11111111'
    >>> bin1(2**8)
    '100000000'
    >>> bin1(2**64-1) == '1'*64
    True
    
    
'''

def bin1(n):
    ''' bin(n) -> n as string of bits
    
    One-liner with limitations: max width is 64, leading zeros removed. 
    '''
    return ''.join(reversed([str((n>>i)&1) for i in range(64)])).lstrip('0') or '0'

def bin(n, width=0, sep='', word_len=8):
    ''' bin(n) -> n as string of bits
    
    Result may be optionally zero-padded to a certain width, 
    and separated in words of specified length.
    '''
    if n == 0:
        return '0'
    bits = []
    while n:
        bits.insert(0, str(n&1))
        n >>= 1
    if len(bits) < width:
        bits[:0] = ['0']*(width-len(bits))
    if sep:
        for i in xrange(len(bits)-word_len,0,-word_len):
            bits.insert(i, sep)    
    return ''.join(bits)    

if __name__ == '__main__':
    import doctest
    doctest.testmod()

