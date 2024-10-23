from pygame.math import Vector2


def set_window_proportion(vector) -> list:
    from game import Game

    if type(vector) == list:      pass
    if type(vector) == tuple:     vec = list(vector)
    elif type(vector) == Vector2: vec = list(vector.xy)
    else:                         raise "Аргумент-вектор имеет неподходящий тип."

    return list(map(
        lambda x: x[0] / x[1], list(zip(vector, Game().window_proportion))
    ))
