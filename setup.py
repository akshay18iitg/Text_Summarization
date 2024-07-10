import setuptools

with open("README.md",'r',encoding='utf-8') as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = 'Text-Summarizer'
AUTHOR_USER_NAME = 'Akshay'
SRC_REPO = 'Text_Summarization'
AUTHOR_EMAIL = 'akshayhitendrashah@gmail.com'

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    description="A samlll python package for NLP app",
    long_description=long_description,
    long_description_content='text/markdown',
    url=f'https://github.com/akshay18iitg/Text_Summarization',
    project_urls={
        "Bug Tracker": f"https://github.com/akshay18iitg/Text_Summarization/issues",
    },
        package_dir={"":"src"},
        packages=setuptools.find_packages(where='src')
)