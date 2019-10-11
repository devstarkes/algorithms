def rectangles_count(points):
    y_count = {}
    rectangles_count = 0

    for x, y in points:
        for x_inner, y_inner in points:
            if x == x_inner and y_inner > y:
                key = '{0}_{1}'.format(y, y_inner)

                rectangles_count += y_count.setdefault(key, 0)
                y_count[key] += 1

    print(rectangles_count)


if __name__ == "__main__":
    points = [(1, 0), (1, 4), (4, 0), (4, 4), (3, 0), (3, 4), (8, 0), (8, 1), (0, 1), (0, 0)]
    rectangles_count(points)
