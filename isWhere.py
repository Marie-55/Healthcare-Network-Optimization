from shapely.geometry import Point, Polygon


def is_Where(coordinates):
    # Define the polygons for west, center, and east
    east_polygon = Polygon(
        [
            (3.2165888258747373, 36.82087159167379),
            (3.397885470054746, 36.790697444931894),
            (3.386675450680201, 36.723194033981216),
            (3.2021232999180427, 36.65120807141844),
            (3.1112549258081117, 36.5691460533812),
            (3.0575754036219394, 36.58385048435072),
            (3.0957832870563777, 36.75455989135196),
            (3.216766083230624, 36.8201556300146),
        ]
    )

    center_polygon = Polygon(
        [
            (3.0956765218824955, 36.75488741747553),
            (3.0576145909291483, 36.583756353878954),
            (2.9323505379221615, 36.58885777131795),
            (3.0104635997143134, 36.82534311336808),
            (3.0816373301463784, 36.79715065542128),
            (3.0954901361618283, 36.754196275466015),
        ]
    )

    west_polygon = Polygon(
        [
            (3.0104084607573043, 36.82534051669904),
            (2.9322797292120697, 36.588826587703),
            (2.79868506642174, 36.652680406509816),
            (2.8063690203871374, 36.70148051737267),
            (2.8381965086880427, 36.76517895118609),
            (2.894150263641137, 36.80782839664124),
            (3.0109099297139608, 36.82567992055678),
        ]
    )

    lat, lon = coordinates
    point = Point(lon, lat)
    
    if west_polygon.touches(point) or point.within(west_polygon):
        return "West"
    elif center_polygon.touches(point) or point.within(center_polygon):
      return "Center"
    elif east_polygon.touches(point) or point.within(east_polygon):
        return "East"
    else:
        return "ERROR"
