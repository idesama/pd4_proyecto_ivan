class ClockService:

    def set_time(self, time_str):
        """Set the current time of the clock."""
        self.current_time = time_str

    def get_time(self):
        """Get the current time of the clock."""
        return self.current_time