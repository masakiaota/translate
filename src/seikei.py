import re


def text_to_url(text):
    ret = re.sub(r"-\n", "", text)
    ret = re.sub(r"- ", "", text)
    ret = re.sub(r"\n", "%20", ret)
    ret = re.sub("\. ", ".%0A%0A", ret)
    ret = re.sub(" ", "%20", ret)

    return "https://translate.google.co.jp/?hl=ja#en/ja/"+ret


if __name__ == "__main__":
    sentence = """Recent years have witnessed a growing interest in the use
for sparse representations for signals. Using an overcom-
plete dictionary matrix D ∈ IRn×K that contains K atoms,
{d }K , as its columns, it is assumed that a signal y ∈ IRn j j=1
can be represented as a sparse linear combination of these atoms."""
    # print("original sentence")
    # print(sentence)

    print("shaped sentence")
    print()
    print(text_to_url(sentence))
