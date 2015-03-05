import fresh_tomatoes
import media

back_to_the_future = media.Movie("Back to the Future",
                        "About a young man that travels back in time to change his future.",
                        "http://upload.wikimedia.org/wikipedia/en/d/d2/Back_to_the_Future.jpg",
                        "https://www.youtube.com/watch?v=qvsgGtivCgs")

the_karate_kid = media.Movie("The Karate Kid",
                        "About a young man that learns to defend himself by learning karate.",
                        "http://vignette1.wikia.nocookie.net/vswikia/images/a/a0/TheKarateKid84.jpg/revision/latest?cb=20140713174203",
                        "https://www.youtube.com/watch?v=n7JhKCQnEqQ")

into_the_wild = media.Movie("Into the Wild",
                        "Using rock music to learn",
                        "http://upload.wikimedia.org/wikipedia/en/8/8a/Into-the-wild.jpg",
                        "https://www.youtube.com/watch?v=2LAuzT_x8Ek")

the_karate_kid_two = media.Movie("The Karate Kid 2",
                        "The sequal to The Karate Kid, where Daniel expands his learning of karate.",
                        "http://upload.wikimedia.org/wikipedia/en/d/d5/Karate_kid_ver2.jpg",
                        "https://www.youtube.com/watch?v=ksWefA8f7_g")

battle_la = media.Movie("Battle:LA",
                        "A rat is a chef in Paris",
                        "http://upload.wikimedia.org/wikipedia/en/2/29/Battle_Los_Angeles_Poster.jpg",
                        "https://www.youtube.com/watch?v=ORb3zC8z94w")

super_eight = media.Movie("Super 8",
                        "Going back in time to meet authors",
                        "http://upload.wikimedia.org/wikipedia/en/7/74/Super_8_Poster.jpg",
                        "https://www.youtube.com/watch?v=vpzUCA5i6zY")

movies = [back_to_the_future, the_karate_kid, into_the_wild, the_karate_kid_two, battle_la, super_eight]
fresh_tomatoes.open_movies_page(movies)
