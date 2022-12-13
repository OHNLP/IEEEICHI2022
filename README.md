# IEEE ICHI 2022

Homepage for IEEE ICHI 2022 (https://ohnlp.github.io/IEEEICHI2022/, or https://ichi2022.institute4hi.org/).

This website is built upon Python `flask` and `frozen-flask` packages for managing the source codes and generating the static version. 

For development, run:

```bash
python server.py
```

For update the static version, run:

```bash
python server.py build
```

The updated static version will be saved into `docs` folder.

Then, you could push the updates to GitHub to update the public site.