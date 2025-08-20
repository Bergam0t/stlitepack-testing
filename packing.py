from stlitepack import pack, setup_github_pages

pack("single_page_with_reqs.py", "requirements.txt")

setup_github_pages(mode="gh-pages")
