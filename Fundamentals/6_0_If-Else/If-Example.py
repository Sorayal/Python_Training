harvard = "linguistics, physics, programming, fine arts"
stanford = "biology, classics, geophysics, music"

arts = "linguistics, fine arts, classics, music"
sciences = "physics, programming, biology, geophysics"

major = "biology"
if major in harvard:
    if major in arts:
        print("This is an arts program at Harvard")
    if major in sciences:
        print("This is a sciences program at Harvard")
if major in stanford:
    if major in arts:
        print("This is an arts program at Stanford")
    if major in sciences:
        print("This is a sciences program at Stanford")

# it goes through the collection to look which university first, then it goes through the
# the collections of arts and sciences
