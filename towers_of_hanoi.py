def towers_of_hanoi(N: int, x: str, y: str, z: str) -> None:
    """moving N towers from x to y using z"""
    if N >= 1:  # only postive numbers of towers
        # first move N-1 tiles from tower x to z using y
        towers_of_hanoi(N - 1, x, z, y)

        # print for last n-1th tile
        print(f"move from {x} to {y}")

        # Now all remaing n-1 tiles  are in tower z
        # move n-1 from tower z to y using x
        towers_of_hanoi(N - 1, z, y, x)


if __name__ == "__main__":
    N = 2  # numbers of tiles
    x, y, z = "Tower1", "Tower2", "Tower3"
    towers_of_hanoi(N, x, y, z)
