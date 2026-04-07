EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time in minutes.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(n_layers):
    """Calculate preparation time based on number of layers.
    :param n_layers: int - number of layers in the lasagna.
    :return: int - preparation time in minutes.
    """
    return PREPARATION_TIME * n_layers

def elapsed_time_in_minutes(n_layers, elapsed_bake_time):
    """Calculate total elapsed time in minutes.
    :param n_layers: int - number of layers in the lasagna.
    :param elapsed_bake_time: int - time already in the oven.
    :return: int - total elapsed time in minutes.
    """
    return preparation_time_in_minutes(n_layers)+elapsed_bake_time