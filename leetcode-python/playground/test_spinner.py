from time import sleep



if __name__ == "__main__":
    s = "|/-\\"
    chars = "abcdef"
    print("Loading....", end="", flush=True)

    for i in range(20):
        print(f"\b{s[i % len(s)]}", end="", flush=True)
        print(f"\b{chars[i % len(s)]}", end="", flush=True)
        sleep(0.5)