from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
    'sqlparse>=0.1.8'
]

test_requirements = [
    'pytest',
]


package_name = 'pgdiff'


setup(
    name=package_name,
    version='0.2',
    url='https://github.com/Onapsis/pgdiff',
    description="A fork of PgDiffPy from https://github.com/Dancer3809/PgDiffPy",
    long_description=readme,
    author="Onapsis",
    author_email='info@onapsis.com',
    packages=find_packages(include=['pgdiff*']),
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    entry_points={
        'console_scripts': [
            'pgdiff = pgdiff.PgDiff:main',
        ]
    }
)