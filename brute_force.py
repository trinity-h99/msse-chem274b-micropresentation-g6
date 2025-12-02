"""
Brute-force string search algorithm for pattern matching.
"""


def brute_force_search(text: str, pattern: str) -> int:
    """
    Simple brute-force string search for timing comparison with TST.
    Returns the starting index of the first match, or -1 if not found.
    
    Args:
        text: The text to search in
        pattern: The pattern to search for
        
    Returns:
        Starting index of the first match, or -1 if not found
    """
    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):
        ok = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                ok = False
                break
        if ok:
            return i
    return -1

