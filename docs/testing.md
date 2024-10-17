## Testing

To run the tests after installation, use `pytest` or `coverage run --omit="*/tests/*,*/test_*.py" -m pytest` and `coverage report` to see the coverage report. 

### Coverage report:
<details><summary>Click to expand:</summary>

  ```

  =========================================== test session starts ============================================
platform win32 -- Python 3.12.5, pytest-8.3.3, pluggy-1.5.0      
rootdir: C:\Users\Bence\Documents\rsa\helsinki-algorithms-project
configfile: pyproject.toml
collected 8 items

tests\test_encoding.py ....                                                                           [ 50%]
tests\test_erathosthenes.py .                                                                         [ 62%]
tests\test_primality.py ...                                                                           [100%]

============================================ 8 passed in 2.05s =============================================
PS C:\Users\Bence\Documents\rsa\helsinki-algorithms-project> coverage report
Name                                          Stmts   Miss  Cover
-----------------------------------------------------------------
__init__.py                                       0      0   100%
helsinki_algorithms_project\__init__.py           0      0   100%
helsinki_algorithms_project\encoding.py          22      1    95%
helsinki_algorithms_project\erathostenes.py      16      1    94%
helsinki_algorithms_project\primality.py         37      2    95%
-----------------------------------------------------------------
TOTAL                                            75      4    95%

```
</details>

### What has been tested and how?
- Testing the implementation of `Sieve of Erathostenes`:
  - Test primality of numbers from -10 to 10000.
  - Check if `sieve_of_erathostenes(n)` a list of correct prime numbers up to `n` value
    - If the list includes all prime numbers, and does not include any composite numbers, the test is successful.
- Test factorization step of the Miller-Rabin primality test:
  - Run the `factorize()` function for a list of values, then check if the output (`k` and `m`) is the expected value or not.
- Test primality:
  - Test primality of numbers from -10 to 11587 using Miller-Rabin primality test.
  - If for all numbers, the function correctly decides if it's a prime number or not, the test is successful.
- Test `check_primality()` only accepts integer values for ALL parameters.
  - This is needed, because with float or other values, miscalculations might happen. 
- Tests for encoding messages:
  - In all of the below cases, we use previously set modulus, public- and private exponents. We encode a test string, then decode it, and compare the decoded message with the original.
  - If we get back the original message, the test passes.
    - Encoding with public key, decoding with private key
    - Encoding with private key, decoding with public key
    - Encoding with sender's private key and the reciever's public key. Decoding with the reciever's private key and the sender's public key.
    - Ensure an exception is raised, if the message is too long for the key to encode.
