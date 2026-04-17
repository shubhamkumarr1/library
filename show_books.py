from utils import books, issue_books

def show():
    print(f"\nTotal Books Available: {len(books)}")
    print(f"Total Books Issued: {len(issue_books)}")
    
    if len(books) == 0:
        print("No books available in the library.")
    else:
        print("List of Available Books:")
        for book in books:
            print(f"- {book}")
