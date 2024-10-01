from datetime import date

from django.shortcuts import render

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Yahya",
        "date": date(2024, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": """
          Hiking through the mountains was one of the most breathtaking experiences of my life. 
          The vast landscapes, the cool breeze, and the peaceful surroundings created a serene atmosphere.
          As I reached the summit, I couldn't believe the view in front of me – a perfect panorama of valleys and peaks.
          But what I didn’t expect was the sudden storm that rolled in, making the descent far more challenging than anticipated.

          I encountered slippery rocks, strong winds, and limited visibility, but these difficulties only added to the adventure.
          By the time I made it back to safety, I realized how unprepared I had been, but the thrill of the journey outweighed the challenges.

          This experience taught me the importance of preparation in hiking, but it also reinforced why I love nature so much – it's unpredictable, awe-inspiring, and always humbling.
        """,
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Yahya",
        "date": date(2024, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          There’s something both exhilarating and frustrating about programming. Yesterday, I spent hours tracking down a single error in my code.
          It was a simple bug that caused the entire application to break, and finding it felt like searching for a needle in a haystack.

          Debugging can be tedious, but once you find that mistake and the code finally works, it's like solving a complex puzzle.
          The satisfaction of watching everything run smoothly after hours of troubleshooting is unmatched. 

          Through this process, I’ve learned the importance of patience, persistence, and paying attention to detail – all critical skills for any programmer.
          Plus, the journey of problem-solving in programming is what makes it so rewarding in the end.
        """,
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Yahya",
        "date": date(2024, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Walking through the woods is always a magical experience. The rustling of leaves, the chirping of birds, and the gentle breeze through the trees create a perfect atmosphere for reflection.
          It’s in nature where I find most of my inspiration – away from the noise of everyday life, everything seems to fall into place.

          On my latest walk, I noticed how the forest changes with each season. The vibrant greens of summer were starting to fade, replaced by hints of autumn’s orange and yellow.
          There’s a certain beauty in watching nature’s cycle unfold, reminding me of the importance of growth, change, and balance.

          These quiet moments in the woods provide a sense of clarity and peace, making me appreciate the world around us even more.
        """,
    },
]


def get_date(post):
    return post["date"]


# Create your views here.


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {"posts": latest_posts})


def posts(request):
    return render(request, "blog/all-posts.html", {"all_posts": all_posts})


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post["slug"] == slug)
    return render(request, "blog/post-detail.html", {"post": identified_post})
