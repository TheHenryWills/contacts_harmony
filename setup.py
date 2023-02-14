import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()
    
project_urls = {
  'Documentation ': 'https://contacts-harmony.readthedocs.io/',
  'Source Code': 'https://github.com/TheHenryWills/contacts_harmony/'
}

setuptools.setup(
    name="contacts_harmony",
    version="0.0.1",
    author="Henry Wills",
    author_email="henry@debutwith.com",
    description="A Python library to normalize and validate email addresses and phone numbers entered into web forms.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url="https://github.com/TheHenryWills/contacts_harmony/tree/main/contacts_harmony",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "contacts_harmony"},
    packages = setuptools.find_packages(where="contacts_harmony"),
    python_requires='>=3.6',
    project_urls = project_urls
)
