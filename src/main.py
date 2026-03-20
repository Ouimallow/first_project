def print_author():
    from dotenv import load_dotenv
    import os

    load_dotenv(dotenv_path='.env')

    author = os.getenv('author')

    print(f"Автор проекта: {author}")


print_author()


