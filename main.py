import string
import random

from config import BOT_CONFIG


class User:

    def __init__(self, name):
        self.name = name
        self.posts = list()
        self.liked_posts = list()

    def count_of_posts(self):
        return len(self.posts)

    def __repr__(self):
        return self.name


class Post:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.liked_by = list()
        self.author.posts.append(self)

    def liked(self):
        return len(self.liked_by)

    def __repr__(self):
        return '{} - {}'.format(self.title, self.author)


class Bot:

    def __init__(self):
        self.max_likes_per_user = BOT_CONFIG.get('max_likes_per_user', 0)
        self.max_posts_per_user = BOT_CONFIG.get('max_posts_per_user', 0)
        self.max_number_of_users = BOT_CONFIG.get('number_of_users', 0)
        self.users = list()
        self.posts = list()


    def _create_random_user(self):
        user = User(name='User{}'.format(len(self.users)))
        self.users.append(user)
        return user

    def _create_random_post(self, user):
        chars = string.printable
        title = ''.join(random.choice(chars) for x in range(10))
        post = Post(title, user)
        self.posts.append(post)
        return post

    def _like_post(self, post, user):
        try:
            post.liked_by.append(user)
            user.liked_posts.append(post)
        except:
            return 1
        return 0

    def _dislike_post(self, post, user):
        try:
            post.liked_by.remove(user)
            user.liked_posts.remove(post)
        except:
            return 1
        return 0

    def simulate_activity(self):
        count_of_users = random.randint(1, self.max_number_of_users)
        for i in range(count_of_users):
            user = self._create_random_user()
            number_of_posts = random.randint(1, self.max_posts_per_user)
            for j in range(number_of_posts):
                self._create_random_post(user)

        [self._like_post(random.choice(self.posts), random.choice(self.users))
         for i in range(0, self.max_number_of_users*2)]
        [self._dislike_post(random.choice(self.posts), random.choice(self.users))
         for i in range(0, self.max_number_of_users*2)]
