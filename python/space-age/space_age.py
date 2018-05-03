"""

   - Earth: orbital period 365.25 Earth days, or 31557600 seconds
   - Mercury: orbital period 0.2408467 Earth years
   - Venus: orbital period 0.61519726 Earth years
   - Mars: orbital period 1.8808158 Earth years
   - Jupiter: orbital period 11.862615 Earth years
   - Saturn: orbital period 29.447498 Earth years
   - Uranus: orbital period 84.016846 Earth years
   - Neptune: orbital period 164.79132 Earth years


"""

earth_year = 31557600
mercury_year = earth_year * 0.2408467
venus_year = earth_year * 0.61519726
mars_year = earth_year * 1.8808158
jupiter_year = earth_year * 11.862615
saturn_year = earth_year * 29.447498
uranus_year = earth_year * 84.016846
neptune_year = earth_year * 164.79132


class SpaceAge(object):
    def __init__(self, seconds):
        self.seconds = seconds

# So long for DRY :(
# I can't think of anything better without changing the test specification

    def on_earth(self):
        return round(self.seconds / earth_year, 2)

    def on_mercury(self):
        return round(self.seconds / mercury_year, 2)

    def on_venus(self):
        return round(self.seconds / venus_year, 2)

    def on_mars(self):
        return round(self.seconds / mars_year, 2)

    def on_jupiter(self):
        return round(self.seconds / jupiter_year, 2)

    def on_saturn(self):
        return round(self.seconds / saturn_year, 2)

    def on_uranus(self):
        return round(self.seconds / uranus_year, 2)

    def on_neptune(self):
        return round(self.seconds / neptune_year, 2)
