from txtai.embeddings import Embeddings

data = ["US tops 5 million confirmed virus cases",
        "Canada's last fully intact ice shelf has suddenly collapsed, forming a Manhattan-sized iceberg",
        "Beijing mobilises invasion craft along coast as Taiwan tensions escalate",
        "The National Park Service warns against sacrificing slower friends in a bear attack",
        "Maine man wins $1M from $25 lottery ticket",
        "Make huge profits without work, earn up to $100,000 a day"]

# Create embeddings model, backed by sentence-transformers & transformers
embeddings = Embeddings({"path": "sentence-transformers/nli-mpnet-base-v2"})
embeddings.index(((x, text, None) for x, text in enumerate(data)))

print("%-20s %s" % ("Query", "Best Match"))
print("-" * 50)

for query in ("feel good story", "climate change", "public health story",
              "war", "wildlife", "asia", "lucky", "dishonest junk"):
    # Get index of best section that best matches query
    uid = embeddings.search(query, 1)[0][0]

    print("%-20s %s" % (query, data[uid]))