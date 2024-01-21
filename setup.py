from setuptools import setup, find_packages

def read_file(file_path: str):
    with open(file_path, 'r') as file:
        contents = [line.rstrip('\n') for line in file]
    if '-e .' in contents:
        contents.remove('-e .')
    return contents

with open('README.md', 'r', encoding='utf-8') as content:
    long_description_content = content.read()

# configuration
setup(name='clustering',
      version='0.0.1',
      author='AKA-SSH',
      author_email='aka.ssh.datascience@gmail.com',
      description='This project deals with the clustering problem of customer personality analysis.',
      long_description=long_description_content,
      long_description_content_type='text/markdown',
      packages=find_packages(),
      install_requires=read_file('requirements.txt'),
      python_requires='>=3.8')