from setuptools import setup, find_packages

setup(
    name="giccinema",
    version="0.1.0",
    description="GIC Cinemas Booking System",
    author="Khaled Md Tuhidul Hossain",
    packages=find_packages(),
    install_requires=[],
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "giccinema=giccinema.main:main",
        ],
    },
)