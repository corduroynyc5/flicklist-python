import webapp2
import random

class Index(webapp2.RequestHandler):

    def getRandomMovie(self):

        # TODO: make a list with at least 5 movie titles
        movieList = ["The Big Lebowski", "Airplane!", "Superbad", "Anchorman", "Caddyshack"]

        # TODO: randomly choose one of the movies, and return it        
        return random.choice(movieList)

    def get(self):
        # choose a movie by invoking our new function
        movie = self.getRandomMovie()

        # build the response string
        content = "<h1>Movie of the Day</h1>"
        content += "<p>" + movie + "</p>"

        # TODO: pick a different random movie, and display it under
        # the heading "<h1>Tommorrow's Movie</h1>"
        tomorrowMovie =self.getRandomMovie()
        # build the response string
        content += "<h1>Tommorrow's Movie</h1>"
        content += "<p>" + tomorrowMovie + "</p>"


        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
