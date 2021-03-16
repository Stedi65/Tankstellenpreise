class AppException(Exception):
    def __init__(self, error=None, message=None):
        self.error = error
        self.message = message

    def __str__(self):
        output = []
        if self.error:
            output.append(f"Fehlermeldung: {self.error}")
        if self.message:
            output.append(f"Message: {self.message}")
        return ", ".join(output)

