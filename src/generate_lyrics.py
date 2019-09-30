from textgenrnn import textgenrnn


def main():
    textgen = textgenrnn("data/textgenrnn_weights_4epochs.hdf5")
    lyrics = textgen.generate(n=50, return_as_list=True)
    for row in lyrics:
        print(row)


if __name__ == "__main__":
    main()
