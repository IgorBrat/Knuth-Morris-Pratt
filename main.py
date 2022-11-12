from typing import List


def calculate_steps(pattern: str) -> List[int]:
    pat_len = len(pattern)
    steps = [0] * pat_len
    current_max_len = 0
    i = 1
    while i < pat_len:
        if pattern[i] == pattern[current_max_len]:
            current_max_len += 1
            steps[i] = current_max_len
            i += 1
        else:
            if current_max_len != 0:
                current_max_len = steps[current_max_len - 1]
            else:
                steps[i] = current_max_len
                i += 1
    return steps


def main():
    string = input("Input string: ")
    pattern = input("Input pattern: ")
    steps = calculate_steps(pattern)
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
            pat_idx = steps[pat_idx - 1]
        else:
            str_idx += 1
        if pat_idx == pat_len:
            res.append((str_idx - pat_len, str_idx - 1))
            pat_idx = steps[pat_idx - 1]
    print(res)


if __name__ == '__main__':
    main()
