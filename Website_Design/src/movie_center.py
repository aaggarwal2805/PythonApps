import fresh_tomatoes
import website
pink = website.Movie("Pink",
                     "https://bollymusicnfilmreviewz.files.wordpress.com/2016/09/pink-2016-hindi-full-movie-watch-online-free.jpg",
                     "https://www.youtube.com/watch?v=AL2TShb6fFs",
                     "https://www.imdb.com/title/tt5571734/",
                     "When three young women are implicated in a crime, a retired lawyer steps forward to help them clear their names.")


drishyam = website.Movie("Dridhyam",
                         "http://t1.gstatic.com/images?q=tbn:ANd9GcTkMKFMrv9gfroA4CC9c9C_d8I1NrhiGgVhYGL7xMWO5oylqi4_",
                         "https://www.youtube.com/watch?v=AuuX2j14NBg",
                         "https://www.imdb.com/title/tt4430212/",
                         "Desperate measures are taken by a man who tries to save his family from the dark side of the law, after they commit an unexpected crime.")


omkara = website.Movie("Omkara",
                       "https://in.bmscdn.com/iedb/movies/images/website/poster/large/omkara-et00002995-25-07-2018-05-47-54.jpg",
                       "https://www.youtube.com/watch?v=Hp697cTAIMU",
                       "https://www.imdb.com/title/tt0488414/",
                       "A politically-minded enforcer's misguided trust in his lieutenant leads him to suspect his wife of infidelity in this adaptation of Shakespeare's 'Othello'.")



judwa_2 = website.Movie("Judwa 2",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/9/91/Judwaa_2_Poster.jpg/220px-Judwaa_2_Poster.jpg",
                        "https://www.youtube.com/watch?v=DDwbjWCgxVM",
                        "https://www.imdb.com/title/tt5456546/",
                        "Twin brothers Raja and Prem are separated at birth after their father exposes a kingpin and his racket. They eventually come together to battle a smuggling ring and save their family from certain doom.")

movies = [pink, drishyam, omkara, judwa_2]
fresh_tomatoes.open_movies_page(movies)
