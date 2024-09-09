def run_tests(check_password_strength, get_strength_rating):
    # Test cases: (password, min_length, require_special, expected_score_range)
    test_cases = [
        ("short", 8, True, range(0, 21)),  # Too short, no numbers or special chars
        ("longerpassword", 8, False, range(41, 61)),  # Longer but no numbers or special chars
        ("ALLUPPERCASE123", 8, False, range(61, 81)),  # All uppercase with numbers
        ("alllowercase123", 8, False, range(61, 81)),  # All lowercase with numbers
        ("MixedCase123", 8, False, range(81, 101)),  # Mixed case with numbers
        ("MixedCase123!", 8, True, range(81, 101)),  # Mixed case with numbers and special char
        ("Super$trong1", 12, True, range(81, 101)),  # Strong password, but shorter than min_length
        ("Weak", 4, False, range(21, 41)),  # Meets custom min_length, but weak
        ("C0mpl3x!P@ssw0rd", 8, True, range(81, 101)),  # Very strong password
        ("", 8, True, range(0, 1)),  # Empty password
        ("NoSpecialChars123", 8, True, range(0, 1)),  # No special chars when required
        ("!@#$%^&*()", 8, True, range(21, 41)),  # Only special characters
        ("12345678", 8, False, range(21, 41)),  # Only numbers
        ("abcdefghijklmnopqrstuvwxyz", 8, False, range(41, 61)),  # Very long, but only lowercase
    ]

    for i, (password, min_length, require_special, expected_range) in enumerate(test_cases, 1):
        score = check_password_strength(password, min_length, require_special)
        rating = get_strength_rating(score)
        result = "PASS" if score in expected_range else "FAIL"
        print(f"Test {i}: Password: '{password}', Score: {score}, Rating: {rating} - {result}")
        if result == "FAIL":
            print(f"  Expected score in range {expected_range}, got {score}")

# Run the tests
run_tests(check_password_strength, get_strength_rating)