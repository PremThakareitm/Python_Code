
class LibraryItem:
    def __init__(self, title, item_id, num_copies):
        self.title = title
        self.item_id = item_id
        self.num_copies = num_copies
        self.checked_out_copies = 0

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Item ID: {self.item_id}")
        print(f"Total Copies: {self.num_copies}")
        print(f"Copies Checked Out: {self.checked_out_copies}")

    def check_out(self):
        if self.checked_out_copies < self.num_copies:
            self.checked_out_copies += 1
            print(f"{self.title} checked out successfully.")
        else:
            print(f"Sorry, all copies of {self.title} are currently checked out.")

    def check_in(self):
        if self.checked_out_copies > 0:
            self.checked_out_copies -= 1
            print(f"{self.title} checked in successfully.")
        else:
            print(f"All copies of {self.title} are already checked in.")


class Book(LibraryItem):
    def __init__(self, title, item_id, num_copies, author):
        super().__init__(title, item_id, num_copies)
        self.author = author

    def display_info(self):
        super().display_info()
        print(f"Author: {self.author}")


class DVD(LibraryItem):
    def __init__(self, title, item_id, num_copies, director):
        super().__init__(title, item_id, num_copies)
        self.director = director

    def display_info(self):
        super().display_info()
        print(f"Director: {self.director}")


class Journal(LibraryItem):
    def __init__(self, title, item_id, num_copies, issue_number):
        super().__init__(title, item_id, num_copies)
        self.issue_number = issue_number

    def display_info(self):
        super().display_info()
        print(f"Issue Number: {self.issue_number}")


# Example Usage:
book1 = Book("The Great Gatsby", "B001", 5, "F. Scott Fitzgerald")
dvd1 = DVD("Inception", "D001", 3, "Christopher Nolan")
journal1 = Journal("Scientific American", "J001", 10, 225)

book1.display_info()
book1.check_out()
book1.check_out()

dvd1.display_info()
dvd1.check_out()

journal1.display_info()
journal1.check_in()
