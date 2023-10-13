from setuptools import setup


setup(
    version="2023.3.1",
    python_requires=">=3.9",  # also update classifiers
    # Meta data
    name="inmanta",
    description="Inmanta deployment tool",
    author="Inmanta",
    author_email="code@inmanta.com",
    url="https://github.com/inmanta/inmanta",
    license="Apache Software License 2",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Telecommunications Industry",
        "Operating System :: POSIX :: Linux",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="orchestrator orchestration configurationmanagement",
    project_urls={
        "Bug Tracker": "https://github.com/inmanta/inmanta-core/issues",
        "Documentation": "https://docs.inmanta.com/community/latest/",
    },
    install_requires=[
        "inmanta-core>=5.0.0.dev",
        "inmanta-ui>=2.0.0.dev",
    ],
    # explicitly declare packages so setuptools does not attempt auto discovery
    packages=[],
)
