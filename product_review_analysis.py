def capitalize_words(reviews):
    keywords = ["good", "excellent", "bad", "poor", "average"]

    for review in reviews:
        for keyword in keywords:
            review = review.replace(keyword, keyword.upper())
        print(review)


def tally(reviews):
    positive_words = [
        "good",
        "excellent",
        "great",
        "awesome",
        "fantastic",
        "superb",
        "amazing",
    ]
    negative_words = [
        "bad",
        "poor",
        "terrible",
        "horrible",
        "awful",
        "disappointing",
        "subpar",
    ]

    positive_count = 0
    negative_count = 0

    for review in reviews:
        lower_case_review = review.lower()

        for word in positive_words:
            positive_count += lower_case_review.count(word)

        for word in negative_words:
            negative_count += lower_case_review.count(word)

    return positive_count, negative_count


def review_summary(reviews):
    for review in reviews:
        if len(review) >= 30:
            new_review = review[:31]

            print(new_review, end="...")


reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it.",
]


positive_count, negative_count = tally(reviews)
capitalize_words(reviews)
print("\n")
review_summary(reviews)

# I had trouble with this one. Think I figured it out for the most part, but I cant get the two print statements meshed.
# I dont know if you have to combine functions or something but maybe you can provide some notes or insight about that.
# So far I am able to get th 1st task and 2nd task to work correctly but not combined and printed together.
# Also I have the counter running but only as a return because that is what the prompt asked. So it doesnt print. Let me know if thats wrong and I can modify it.
