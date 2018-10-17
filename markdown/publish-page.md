After Sphinx generates the `docs/` directory structure, to publish the pages manually, move up to the root directory and run:

```bash
~/python-bootstrap/docs (my-branch) $ cd ..
~/python-bootstrap (my-branch) $ make sphinx && make ghpages
~/python-bootstrap (gh-pages) $ git push origin gh-pages
```

**Important to note**: In the GitHub repo settings, you must specify that the GitHub pages are being published from the `gh-pages` branch