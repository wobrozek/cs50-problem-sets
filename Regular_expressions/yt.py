import re

"""
Suppose that you’d like to extract the URLs of YouTube videos that are embedded in pages
 (e.g., https://www.youtube.com/embed/xvFZjo5PgG0),
converting them back to shorter, shareable youtu.be URLs (e.g., https://youtu.be/xvFZjo5PgG0)
 where they can be watched on YouTube itself.
"""

def parse(link):
    tab=re.search(r'''(.+)https?://(www\.)?youtube\.com/embed/(.+)"''' ,link)
    if tab == None:
        return tab
    return f"https://youtu.be/{tab.group(3)}"

def main():
    print(parse('<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>'))


if __name__=="__main__":
    main()