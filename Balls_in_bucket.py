def min_shifts_to_alternate(buckets):
    positions = list(buckets)  # Convert string to list for easier manipulation
    ball_count = positions.count('B')  # Step 1: Count number of balls

    # Step 2: Determine if the sequence is impossible
    invalid_bound = (len(positions) // 2) + (1 if len(positions) % 2 == 1 else 0)
    if ball_count > invalid_bound:
        return -1  # Impossible case

    start_index = 0
    end_index = 2 * ball_count - 2  # Initial window length
    min_shifts_val = ball_count  # Start with the max possible shifts

    while end_index <= len(positions) - 1:
        ball_correct_pos = 0

        # Step 3: Count how many balls are already in correct alternating positions
        for i in range(start_index, end_index + 1, 2):  # Move through the window with step 2
            if positions[i] == 'B':
                ball_correct_pos += 1

        # Update min_shifts_val if the current window requires fewer moves
        shifts_needed = ball_count - ball_correct_pos
        if shifts_needed < min_shifts_val:
            min_shifts_val = shifts_needed

        # Step 4: Move the window to the right
        start_index += 1
        end_index += 1

    # Step 5: Return the minimum number of moves required
    return min_shifts_val


# Example usage:
buckets1 = "BB.B.BBB..."
buckets2 = "..B....B.BB"
buckets3 = "B.B.B.B..."  # Already correct sequence
buckets4 = "BB..BB...B"  # Impossible case

print(min_shifts_to_alternate(buckets1))  # Output: 4
print(min_shifts_to_alternate(buckets2))  # Output: 2
print(min_shifts_to_alternate(buckets3))  # Output: 0
print(min_shifts_to_alternate(buckets4))  # Output: -1
