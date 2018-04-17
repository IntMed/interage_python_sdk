from setuptools import setup, find_packages
from io import open


with open('README.md', encoding='utf-8') as f:
    long_description = f.read()


setup(
  name = "interage_python_sdk",
  packages = find_packages(),
  version = "0.4.1",
  description = "SDK oficialmente mantido pela IntMed Software para auxiliar no desenvolvimento de aplicações em Python integradas ao serviço de interações medicamentosas do sistema Interage",
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = "IntMed Software",
  author_email = "contato@intmed.com.br",
  url = "https://github.com/IntMed/interage_python_sdk",
  download_url = "https://github.com/IntMed/interage_python_sdk/archive/0.4.1.tar.gz",
  keywords = "interage intmed api python sdk interage-python-sdk health",
  classifiers=[ 
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Internet :: WWW/HTTP',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
