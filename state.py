import enum


# Enum class to maintain the state of knight
class State(enum.Enum):
    Live = "LIVE"
    Dead = "DEAD"
    DROWNED = "DROWNED"
