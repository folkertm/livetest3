try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

    
setup(name='livetest3',
      version='0.1.0',
      description='Test against a live site with an API like Paste WebTest',
      long_description=long_description,
      long_description_content_type='text/markdown',
      classifiers=[
          "Development Status :: Beta",
          "Environment :: Web Environment",
          "Framework :: Paste",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Software Development :: Testing"
      ],
      keywords='http integration wsgi test unit tests testing web functional',
      author='Folkert Meeuw',
      author_email='folkert.meeuw@googlemail.com',
      url='http://github.com/folkertm/livetest3',
      license='',
      packages=find_packages(exclude=['ez_setup', 'tests']),
      include_package_data=True,
      install_requires=['WebTest>=1.2'],
      tests_require=['nose>=1.7.3'],
      test_suite='nose.collector',
      zip_safe=False)
