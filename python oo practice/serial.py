# serial.py

class SerialGenerator:
    """Machine to create unique incrementing serial numbers."""
    
    def __init__(self, start=0):
        """Initialize the generator with the start number."""
        self.start = self.next = start
    
    def generate(self):
        """Generate the next serial number."""
        current = self.next
        self.next += 1
        return current
    
    def reset(self):
        """Reset the generator to the original start number."""
        self.next = self.start
    
    def __repr__(self):
        """Representation of the generator."""
        return f"<SerialGenerator start={self.start} next={self.next}>"
