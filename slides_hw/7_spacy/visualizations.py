import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter

try:
    from wordcloud import WordCloud
except ImportError:
    WordCloud = None


def freq_df(tokens, normalize=False):
    """
    tokens: list[str]
    normalize: if True, adds 'prop' column (proportion)
    returns: pd.DataFrame with columns ['token','freq'] (+ 'prop' if normalize)
    """
    c = Counter(tokens)
    df = pd.DataFrame(c.items(), columns=["token", "freq"]).sort_values("freq", ascending=False)
    if normalize and len(tokens) > 0:
        df["prop"] = df["freq"] / df["freq"].sum()
    return df.reset_index(drop=True)

def pie(tokens, k=8, title="Pie: Top Categories", autopct="%1.1f%%"):
    """
    tokens: list[str] (e.g., POS tags, languages, whatever categories)
    k: how many slices to show before grouping the rest into 'Other'
    """
    df = freq_df(tokens, normalize=True)
    if df.empty:
        print("No data.")
        return df

    top = df.head(k).copy()
    if len(df) > k:
        other_prop = df["prop"][k:].sum()
        other_row = pd.DataFrame([{"token": "Other", "freq": df["freq"][k:].sum(), "prop": other_prop}])
        plot_df = pd.concat([top, other_row], ignore_index=True)
    else:
        plot_df = top

    plt.figure()
    plt.pie(plot_df["prop"], labels=plot_df["token"], autopct=autopct)
    plt.title(title)
    plt.tight_layout()
    plt.show()
    return plot_df
  
def line(tokens, title="Line: Rank vs Frequency", logy=False, marker="o"):
    """
    tokens: list[str]
    logy: True to use log scale on y (often helpful for Zipf-like curves)
    """
    df = freq_df(tokens)
    if df.empty:
        print("No data.")
        return df

    df["rank"] = range(1, len(df) + 1)

    plt.figure()
    plt.plot(df["rank"], df["freq"], marker=marker)
    plt.xlabel("Rank (1 = most frequent)")
    plt.ylabel("Frequency")
    if logy:
        plt.yscale("log")
        plt.ylabel("Frequency (log)")
    plt.title(title)
    plt.tight_layout()
    plt.show()
    return df[["token", "freq", "rank"]]

def scatter(tokens, title="Scatter: Length vs Frequency", logy=False):
    """
    tokens: list[str]
    Plots each unique token once, at (length, frequency).
    """
    df = freq_df(tokens)
    if df.empty:
        print("No data.")
        return df

    df["length"] = df["token"].str.len()

    plt.figure()
    plt.scatter(df["length"], df["freq"])
    plt.xlabel("Token length")
    plt.ylabel("Frequency")
    if logy:
        plt.yscale("log")
        plt.ylabel("Frequency (log)")
    plt.title(title)
    plt.tight_layout()
    plt.show()
    return df[["token", "length", "freq"]].sort_values(["length", "freq"], ascending=[True, False]).reset_index(drop=True)

def wordcloud(tokens, title="Word Cloud", width=800, height=400, background_color="white"):
    """
    tokens: list[str]
    Shows a word cloud based on frequency. Requires 'wordcloud' package.
    """
    if WordCloud is None:
        print("WordCloud not installed. Run: pip install wordcloud")
        return None

    df = freq_df(tokens)
    if df.empty:
        print("No data.")
        return df

    freqs = dict(zip(df["token"], df["freq"]))
    wc = WordCloud(width=width, height=height, background_color=background_color)
    wc = wc.generate_from_frequencies(freqs)

    plt.figure()
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.title(title)
    plt.tight_layout()
    plt.show()
    return df

__all__ = ["freq_df", "pie", "line", "scatter", "wordcloud"]
