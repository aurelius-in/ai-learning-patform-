from setuptools import setup, find_packages

setup(
    name="ai_learning_platform",
    version="0.1.0",
    description="An AI-driven learning platform with adaptive paths and personalized assessments.",
    author="Your Name",
    author_email="you@example.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "fastapi",
        "uvicorn",
        "pydantic",
        "scikit-learn",
        "pandas",
        "numpy",
        "joblib",
        "torch",
        "jinja2"
    ],
    entry_points={
        "console_scripts": [
            "train-model=src.models.train:train_model",
            "run-inference=src.models.predict:predict"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires='>=3.8',
)