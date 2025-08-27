from stlitepack import pack, setup_github_pages

pack(
    "single_page_with_reqs.py",
    requirements=["plotly", "pandas", "numpy", "matplotlib"],
    run_preview_server=True,
)

setup_github_pages(mode="gh-actions")
