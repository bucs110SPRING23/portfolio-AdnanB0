from stringutility import StringUtility


def main():
    # create a list of StringUtility objects to use for testing
    test_strings = [
        "interesting",
        "aardvark",
        "aaa",
        "aeiouAEIOU",
        "a b c d e f g h i j k l m n o p q r s t u v w x y z",
        "",
    ]
    su = []
    for i in test_strings:
        su.append(StringUtility(i))

    print("=========== Testing __str__ method... ===========")
    expected_results = [
        "interesting",
        "aardvark",
        "aaa",
        "aeiouAEIOU",
        "a b c d e f g h i j k l m n o p q r s t u v w x y z",
        "",
    ]
    i = 0
    for s in su:
        result = str(s)
        print(f"{s}, got: {result}, expected: {expected_results[i]}")
        assert result == expected_results[i]
        i += 1
    print("=========== ...__str__ method passed ===========")

    print("=========== Testing vowels method... ===========")
    expected_results = ["4", "3", "3", "many", "many", "0"]
    i = 0
    for s in su:
        result = s.vowels()
        print(f"{s}, got: {result}, expected: {expected_results[i]}")
        assert result == expected_results[i]
        i += 1
        print("=========== ...vowels method passed ===========")

    print("=========== Testing bothEnds method... ===========")
    expected_results = ["inng", "aark", "aaaa", "aeOU", "a  z", ""]
    i = 0
    for s in su:
        result = s.bothEnds()
        print(f"{s}, got: {result}, expected: {expected_results[i]}")
        assert result == expected_results[i]
        i += 1
        print("=========== ...bothEnds method passed ===========")

    print("=========== Testing fixStart method... ===========")
    expected_results = [
        "interest*ng",
        "a*rdv*rk",
        "a**",
        "aeiouAEIOU",
        "a b c d e f g h i j k l m n o p q r s t u v w x y z",
        "",
    ]
    i = 0
    for s in su:
        result = s.fixStart()
        print(f"{s}, got: {result}, expected: {expected_results[i]}")
        assert result == expected_results[i]
        i += 1
    print("=========== ...fixStart method passed ===========")

    print("=========== Testing asciiSum method... ===========")
    expected_results = [1196, 844, 291, 902, 3647, 0]
    i = 0
    for s in su:
        result = s.asciiSum()
        print(f"{s}, got: {result}, expected: {expected_results[i]}")
        assert result == expected_results[i]
        i += 1
    print("=========== ...asciiSum method passed ===========")

    print("=========== Testing cipher method... ===========")
    expected_results = [
        "tyepcpdetyr",
        "iizldizs",
        "ddd",
        "kosyeKOSYE",
        "z a b c d e f g h i j k l m n o p q r s t u v w x y",
        "",
    ]
    i = 0
    for s in su:
        result = s.cipher()
        print(f"{s}, got: {result}, expected: {expected_results[i]}")
        assert result == expected_results[i]
        i += 1
    print("=========== ...cipher method passed ===========")

    print("=========== Testing __str__ method (again)... ===========")
    expected_results = [
        "interesting",
        "aardvark",
        "aaa",
        "aeiouAEIOU",
        "a b c d e f g h i j k l m n o p q r s t u v w x y z",
        "",
    ]
    i = 0
    for s in su:
        result = str(s)
        print(f"{s}, got: {result}, expected: {expected_results[i]}")
        assert result == expected_results[i]
        i += 1
    print("=========== ...__str__ method passed (again) ===========")

    print("=========== Tests Complete! ===========")


main()
