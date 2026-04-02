def calculate_stats(numbers: list[int]) -> dict:
    """A simple function to test Ruff linting and Pyright types."""
    if not numbers:
        return {"mean": 0, "total": 0}
    total = sum(numbers)
    mean = total / len(numbers)

    return {
        "mean": mean,
        "total": total,
    }


if __name__ == "__main__":
    # Test Ruff formatting: extra spaces and messy lists
    data = [10, 20, 30, 40, 50]

    results = calculate_stats(data)

    print(f"Total: {results['total']}")
    print(f"Mean: {results.get('mean')}")

    print("This is a test that the pylsp is working")

# comment
