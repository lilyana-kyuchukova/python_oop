from project.movie import Movie
from unittest import TestCase, main


class TestMovie(TestCase):
    def setUp(self):
        self.movie = Movie("Terminator", 1982, 8.8)
        self.other = Movie("Barbie", 2023, 7.6)

    def test_init(self):
        self.assertEqual(self.movie.name, "Terminator")
        self.assertEqual(self.movie.year, 1982)
        self.assertEqual(self.movie.rating, 8.8)
        self.assertEqual(self.movie.actors, [])

    def test_name_raise_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.movie = Movie("", 1234, 4.4)

        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

    def test_year_raise_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.movie = Movie("ABC", 1234, 4.5)

        self.assertEqual("Year is not valid!", str(ve.exception))

    def test_add_actor_new_entry(self):
        self.movie.add_actor("Arnold")

        self.assertEqual(self.movie.actors, ["Arnold"])

    def test_add_actor_already_in_the_list(self):
        name = "Arnold"
        self.movie.add_actor(name)
        result = self.movie.add_actor(name)

        self.assertEqual(f"{name} is already added in the list of actors!", result)

    def test__gt__movie_is_better_than_other(self):
        result = self.movie.__gt__(self.other)
        self.assertEqual(f'"{self.movie.name}" is better than "{self.other.name}"', result)

    def test__gt__other_is_better_than_movie(self):
        self.other.rating = 9.8
        result = self.movie.__gt__(self.other)
        self.assertEqual(f'"{self.other.name}" is better than "{self.movie.name}"', result)

    def test__repr__(self):
        self.movie.add_actor("Arnold")
        expected = f"Name: {self.movie.name}\n" \
                    f"Year of Release: {self.movie.year}\n" \
                    f"Rating: {self.movie.rating:.2f}\n" \
                    f"Cast: {', '.join(self.movie.actors)}"

        result = str(self.movie)

        self.assertEqual(expected, result)