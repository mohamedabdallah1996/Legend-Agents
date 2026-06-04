class LegendNameNotFound(Exception):
    """Exception raised when a Legend's name is not found."""

    def __init__(self, legend_id: str):
        self.message = f"Legend name for {legend_id} not found."
        super().__init__(self.message)

class LegendStyleNotFound(Exception):
    """Exception raised when a Legend's style is not found."""

    def __init__(self, legend_id: str):
        self.message = f"Legend style for {legend_id} not found."
        super().__init__(self.message)

class LegendPerspectiveNotFound(Exception):
    """Exception raised when a Legend's perspective is not found."""

    def __init__(self, legend_id: str):
        self.message = f"Legend perspective for {legend_id} not found."
        super().__init__(self.message)


