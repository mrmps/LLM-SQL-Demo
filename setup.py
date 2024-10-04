from setuptools import setup, find_packages

setup(
    name='llmsql',
    version='0.1',
    description='LLM SQL Demo',
    packages=find_packages(),
    install_requires=[
        'openai>=1.51.0',  # Update the version here
        'jiter>=0.5.0',
        'anthropic>=0.34.2',
        'pydantic>=2.9.2',
        'tqdm>=4.66.5',
        'huggingface-hub>=0.25.1',
        'tokenizers>=0.20.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Adjust based on your project's Python version
)
