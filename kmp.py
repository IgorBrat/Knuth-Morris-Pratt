from typing import List
import time


def get_lps_array(pattern: str) -> List[int]:
    """
    Method to build lps (the longest proper prefix which is also a suffix at the current position) array for pattern
    :param pattern: substring we are searching in string
    :return: lps array
    :time complexity: O(m)
    """
    pat_len = len(pattern)
    lps = [0] * pat_len
    current_max_len = 0
    i = 1
    while i < pat_len:
        if pattern[i] == pattern[current_max_len]:
            current_max_len += 1
            lps[i] = current_max_len
            i += 1
        else:
            if current_max_len != 0:
                current_max_len = lps[current_max_len - 1]
            else:
                lps[i] = current_max_len
                i += 1
    return lps


def kmp(string: str, pattern: str):
    """
    Knuth Morris Pratt algorithm - finds position of pattern in string
    :param string: given string
    :param pattern: substring we are searching in string
    :return: array with tuples (start_position, end_position) of pattern in string
    :time complexity: O(n), plus time complexity of get_lps_array() method
    """
    start = time.time()
    lps = get_lps_array(pattern)
    res = []
    str_len = len(string)
    pat_len = len(pattern)
    str_idx = 0
    pat_idx = 0
    while str_idx < str_len:
        if string[str_idx] == pattern[pat_idx]:
            str_idx += 1
            pat_idx += 1
        elif pat_idx > 0:
            pat_idx = lps[pat_idx - 1]
        else:
            str_idx += 1
        if pat_idx == pat_len:
            res.append((str_idx - pat_len, str_idx - 1))
            pat_idx = lps[pat_idx - 1]
    end = time.time()
    print(f"Time taken: {(end-start)*10**3:.05f}ms")
    return res
